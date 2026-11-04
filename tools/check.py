#!/usr/bin/env python3
"""빌드된 사이트(docs/)를 점검한다.

1. 내부 링크: 가리키는 파일과 소제목(#앵커)이 실제로 있는가
2. 외부 링크: 응답 코드 (--external 옵션을 줄 때만, 시간이 걸림)
3. 출처 없는 주장:
   - 모든 페이지에 "출처" 소제목이 있고 링크가 하나 이상 있는가
   - "사례" 구역의 문단·목록 항목에 신뢰도 태그가 붙어 있는가
     (자기 자신, 위쪽 목록 항목, 바로 위 소제목 중 하나에 태그가 있으면 통과)
   - 신뢰도 태그가 붙은 주장 근처(같은 항목, 위 항목, 소제목)에 링크나 소스 파일 경로가 있는가

사용법:  python3 tools/check.py [--external]
필요 패키지:  pip install beautifulsoup4 lxml
"""
import subprocess
import sys
import urllib.parse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from bs4 import BeautifulSoup

DOCS = Path(__file__).resolve().parent.parent / "docs"
TRUST_CLASSES = {"trust-official", "trust-analysis", "trust-guess", "trust-unknown"}


def load():
    pages = {}
    for f in sorted(DOCS.glob("*.html")):
        pages[f.name] = BeautifulSoup(f.read_text(encoding="utf-8"), "lxml")
    return pages


def article(soup):
    return soup.select_one("main article")


def has_trust(el):
    return any(TRUST_CLASSES & set(s.get("class", [])) for s in el.select(".tag.trust"))


def own_text_trust(el):
    """하위 목록을 빼고 이 요소 자신의 내용에 신뢰도 태그가 있는가"""
    clone = BeautifulSoup(str(el), "lxml")
    for sub in clone.select("ul, ol"):
        sub.decompose()
    return has_trust(clone)


def has_source_near(el):
    """링크(a[href^=http]) 또는 소스 파일 경로(code)가 근처에 있는가"""
    node = el
    for _ in range(4):
        if node is None:
            break
        if node.select('a[href^="http"]') or any("/" in c.get_text() or "." in c.get_text() for c in node.select("code")):
            return True
        node = node.find_parent(["li", "section"])
    return False


def region_source(el):
    """소제목(h3) 바로 아래의 '근거 줄'(신뢰도 태그 + 링크가 있는 문단)이 구역 전체의 출처가 되는 경우"""
    h3 = el.find_previous("h3")
    if h3 is None or h3.find_parent("section") is not el.find_parent("section"):
        return False
    sib = h3
    for _ in range(3):   # 소제목 바로 아래 세 덩어리 안에 근거 줄이 있어야 한다
        sib = sib.find_next_sibling()
        if sib is None or sib.name in ("h2", "h3"):
            return False
        if sib.name == "p" and has_trust(sib) and (sib.select('a[href^="http"]') or sib.select("code")):
            return True
        if sib.name in ("ul", "ol"):
            return False
    return False


def check_internal(pages):
    problems = []
    for name, soup in pages.items():
        for a in soup.select("a[href]"):
            href = a["href"]
            if href.startswith(("http://", "https://", "mailto:")):
                continue
            path, _, frag = href.partition("#")
            target = path or name
            if target not in pages:
                problems.append(f"{name}: 없는 페이지 → {href}")
                continue
            if frag:
                frag = urllib.parse.unquote(frag)
                if not pages[target].find(id=frag):
                    problems.append(f"{name}: 없는 소제목 → {href}")
    return problems


def check_claims(pages):
    problems = []
    stats = defaultdict(int)
    for name, soup in pages.items():
        if name == "tags.html":
            continue
        is_refs = name.startswith("15-references")
        art = article(soup)
        heads = [h.get_text(" ", strip=True).replace("#", "").strip() for h in art.select("h2")]
        if not is_refs and not any(h.startswith("출처") for h in heads):
            problems.append(f"{name}: '출처' 소제목이 없음")
        else:
            src = [s for s in art.select("section.sec") if s.find("h2") and s.find("h2").get_text().startswith("출처")]
            if src and not src[0].select('a[href^="http"], a[href$=".html"]'):
                problems.append(f"{name}: '출처' 구역에 링크가 없음")

        for sec in art.select("section.sec"):
            h2 = sec.find("h2").get_text(" ", strip=True)
            if "사례" not in h2:
                continue
            for el in sec.select("li, p"):
                if el.find_parent(["div"], class_=["admonition", "card", "hl"]) or el.find_parent("table"):
                    continue
                text = el.get_text(" ", strip=True)
                if len(text) < 25 or text.startswith("배울 점") or text.startswith("**배울 점"):
                    continue
                if el.find_parent("li") is None and el.name == "li" and el.select("ul, ol") and not own_text_trust(el):
                    pass
                stats["checked"] += 1
                ok = own_text_trust(el)
                parent = el.find_parent("li")
                while not ok and parent is not None:
                    ok = own_text_trust(parent)
                    parent = parent.find_parent("li")
                if not ok:
                    prev_h = el.find_previous(["h3", "h2"])
                    ok = prev_h is not None and has_trust(prev_h)
                if not ok:
                    ok = region_source(el)
                if not ok:
                    lead = text[:15]
                    if lead.startswith(("배울 점", "교훈", "장점", "약점")):
                        continue
                    problems.append(f"{name} › {h2}: 신뢰도 태그 없음 → \"{text[:70]}…\"")
                else:
                    stats["tagged"] += 1

        for tag in art.select(".tag.trust"):
            if "trust-unknown" in tag.get("class", []):
                continue
            holder = tag.find_parent(["li", "p", "td", "dd", "h3"])
            if holder is None:
                continue
            if holder.find_parent("table") or holder.find_parent(class_="card") or holder.find_parent(class_="admonition"):
                continue
            stats["trust_tags"] += 1
            if "trust-guess" in tag.get("class", []) and "이 가이드" in holder.get_text():
                continue   # 이 가이드 자신의 판단이라고 밝힌 [추정]
            if not has_source_near(holder) and not region_source(holder):
                # 같은 소제목 구역 안에 링크가 있으면 통과 (구역 첫머리에 출처를 모아 둔 경우)
                sec = holder.find_parent("section")
                h3 = holder.find_previous("h3")
                region_ok = False
                if h3 is not None and h3.find_parent("section") is sec:
                    sib = h3
                    for _ in range(40):
                        sib = sib.find_next_sibling()
                        if sib is None or sib.name in ("h2", "h3"):
                            break
                        if sib.select('a[href^="http"]') or sib.select("code"):
                            region_ok = True
                            break
                if not region_ok:
                    problems.append(f"{name}: 출처 링크가 근처에 없음 → \"{holder.get_text(' ', strip=True)[:70]}…\"")
    return problems, stats


def fetch_status(url):
    try:
        out = subprocess.run(
            ["curl", "-s", "-o", "/dev/null", "-L", "-m", "30", "-A", "Mozilla/5.0 (LIFE_SIMUL_LAB link check)", "-w", "%{http_code}", url],
            capture_output=True, text=True, timeout=40,
        )
        return url, out.stdout.strip() or "000"
    except Exception:
        return url, "ERR"


def check_external(pages):
    urls = sorted({a["href"].split("#")[0] for s in pages.values() for a in s.select('a[href^="http"]')})
    urls = [u for u in urls if "github.com/HelloNobb" not in u]
    with ThreadPoolExecutor(max_workers=8) as ex:
        results = list(ex.map(fetch_status, urls))
    bad = [(u, c) for u, c in results if not c.startswith(("2", "3"))]
    return urls, bad


def main():
    pages = load()
    print(f"페이지 {len(pages)}개")

    internal = check_internal(pages)
    print(f"\n[내부 링크] 문제 {len(internal)}개")
    for p in internal:
        print("  -", p)

    claims, stats = check_claims(pages)
    print(f"\n[출처·태그] 사례 문장 {stats['checked']}개 점검, 신뢰도 태그 {stats['trust_tags']}개 점검, 문제 {len(claims)}개")
    for p in claims:
        print("  -", p)

    if "--external" in sys.argv:
        urls, bad = check_external(pages)
        print(f"\n[외부 링크] {len(urls)}개 중 응답 이상 {len(bad)}개")
        for u, c in bad:
            print(f"  - {c} {u}")

    return 1 if internal else 0


if __name__ == "__main__":
    sys.exit(main())
