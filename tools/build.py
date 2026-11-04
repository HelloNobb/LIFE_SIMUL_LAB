#!/usr/bin/env python3
"""LIFE SIMUL LAB 정적 사이트 빌더.

content/*.md  →  docs/*.html  (GitHub Pages는 docs/ 폴더를 배포)

사용법:  python3 tools/build.py
필요 패키지:  pip install markdown pygments

Markdown 안에서 쓰는 약속:
  신뢰도 태그   [공식] [분석] [추정] [확인 못 함]
  목표 태그     {소속감} {개연성} {관계} {실존감}
  다이어그램    ```mermaid ... ```   (브라우저에서 Mermaid로 그림)
  코드          ```csharp ... ```    (빌드할 때 Pygments로 색칠)
  알림 상자     !!! note "제목"  /  !!! warning "제목"
"""
import html
import json
import re
import shutil
import sys
from pathlib import Path

import markdown
from pygments.formatters import HtmlFormatter

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
OUT = ROOT / "docs"
ASSETS_SRC = ROOT / "assets"

SITE_TITLE = "LIFE SIMUL LAB"
SITE_DESC = "살아있는 NPC와 세계를 만드는 설계 가이드"

TRUST = {
    "공식": ("official", "개발자 발표·공식 문서·GDC·논문"),
    "분석": ("analysis", "데이터마이닝·디컴파일·게임 데이터·검증된 위키 수치"),
    "추정": ("guess", "플레이 관찰·커뮤니티 추측·2차 보도"),
    "확인 못 함": ("unknown", "찾아봤지만 믿을 만한 출처가 없음"),
}
GOALS = {
    "소속감": ("belong", "내가 이 공동체의 일원이라는 느낌"),
    "개연성": ("plaus", "사건이 '그럴 만했다'고 납득되는 것"),
    "관계": ("relation", "관계가 쌓이고 변하는 것"),
    "실존감": ("alive", "NPC가 실제로 사는 사람처럼 느껴지는 것"),
}

TRUST_RE = re.compile(r"\[(공식|분석|추정|확인 못 함)\]")
GOAL_RE = re.compile(r"\{(소속감|개연성|관계|실존감)\}")
MERMAID_RE = re.compile(r"^```mermaid\n(.*?)\n```", re.S | re.M)


def slugify(value, separator="-"):
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[^\w\s가-힣-]", "", value).strip().lower()
    return re.sub(r"[\s]+", separator, value)


def parse_front_matter(text):
    meta = {}
    if text.startswith("---\n"):
        end = text.index("\n---\n", 4)
        for line in text[4:end].splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        text = text[end + 5:]
    return meta, text


def trust_span(m):
    label = m.group(1)
    cls, tip = TRUST[label]
    return f'<span class="tag trust trust-{cls}" data-tag="{cls}" title="{tip}">{label}</span>'


def goal_span(m):
    label = m.group(1)
    cls, tip = GOALS[label]
    return f'<span class="tag goal goal-{cls}" data-tag="{cls}" title="{tip}">{label}</span>'


def replace_tags_outside_code(body):
    """<pre>, <code> 안은 건드리지 않고 태그만 바꾼다."""
    parts = re.split(r"(<pre[\s\S]*?</pre>|<code>[\s\S]*?</code>)", body)
    for i in range(0, len(parts), 2):
        parts[i] = TRUST_RE.sub(trust_span, parts[i])
        parts[i] = GOAL_RE.sub(goal_span, parts[i])
        parts[i] = re.sub(r"<li>\[ \] ", '<li class="task"><input type="checkbox" class="task-box" aria-label="확인"> ', parts[i])
    return "".join(parts)


def wrap_sections(body):
    """h2 단위로 <section>을 둘러 필터·검색에 쓴다."""
    chunks = re.split(r"(?=<h2[ >])", body)
    out = []
    for c in chunks:
        if c.startswith("<h2"):
            out.append(f'<section class="sec">{c}</section>')
        else:
            out.append(c)
    return "".join(out)


def strip_html(s):
    s = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def load_pages():
    pages = []
    for path in sorted(CONTENT.glob("*.md")):
        meta, text = parse_front_matter(path.read_text(encoding="utf-8"))
        slug = path.stem
        out_name = "index.html" if slug == "00-index" else f"{slug}.html"
        pages.append({"src": path, "meta": meta, "text": text, "slug": slug, "out": out_name})
    return pages


def render_markdown(text):
    mermaids = []

    def keep_mermaid(m):
        mermaids.append(m.group(1))
        return f"\n<div class=\"mermaid-wrap\" markdown=\"0\"><pre class=\"mermaid\" data-src=\"{len(mermaids)-1}\">MERMAID{len(mermaids)-1}</pre></div>\n"

    text = MERMAID_RE.sub(keep_mermaid, text)
    md = markdown.Markdown(
        extensions=["fenced_code", "codehilite", "tables", "toc", "attr_list", "md_in_html", "admonition", "sane_lists"],
        extension_configs={
            "codehilite": {"css_class": "hl", "guess_lang": False},
            "toc": {"slugify": slugify, "toc_depth": "2-3", "permalink": "#", "permalink_title": "이 소제목 링크"},
        },
    )
    body = md.convert(text)
    for i, src in enumerate(mermaids):
        body = body.replace(f"MERMAID{i}", html.escape(src))
    return body, md.toc_tokens


def toc_html(tokens):
    if not tokens:
        return ""
    items = []
    for t in tokens:
        sub = "".join(f'<li><a href="#{c["id"]}">{c["name"]}</a></li>' for c in t.get("children", []))
        items.append(f'<li><a href="#{t["id"]}">{t["name"]}</a>' + (f"<ul>{sub}</ul>" if sub else "") + "</li>")
    return "<ul>" + "".join(items) + "</ul>"


def nav_html(pages, current):
    links = []
    for p in pages:
        label = p["meta"].get("nav", p["meta"].get("title", p["slug"]))
        cls = ' class="active" aria-current="page"' if p is current else ""
        links.append(f'<li><a href="{p["out"]}"{cls}>{html.escape(label)}</a></li>')
    tag_cls = ' class="active" aria-current="page"' if current == "tags" else ""
    links.append(f'<li class="nav-sep"><a href="tags.html"{tag_cls}>태그 모아보기</a></li>')
    return "<ul>" + "".join(links) + "</ul>"


def filter_bar():
    goals = "".join(
        f'<button type="button" class="chip goal goal-{c}" data-filter="{c}" aria-pressed="false" title="{t}">{k}</button>'
        for k, (c, t) in GOALS.items()
    )
    trust = "".join(
        f'<button type="button" class="chip trust trust-{c}" data-filter="{c}" aria-pressed="false" title="{t}">{k}</button>'
        for k, (c, t) in TRUST.items()
    )
    return (
        '<div class="filter-bar" role="group" aria-label="태그 필터">'
        '<span class="filter-label">태그 필터</span>'
        f'<span class="chips">{goals}</span><span class="chips">{trust}</span>'
        '<button type="button" class="chip clear" data-filter-clear>해제</button>'
        '<span class="filter-hint" aria-live="polite"></span></div>'
    )


def toc_parts(toc):
    if not toc:
        return {"toc_block": "", "toc_mobile": ""}
    return {"toc_block": f'<p class="toc-title">이 페이지</p>{toc}',
            "toc_mobile": f'<details class="toc-mobile"><summary>이 페이지 목차</summary>{toc}</details>'}


def header_tags(meta):
    goals = [g.strip() for g in meta.get("goals", "").split(",") if g.strip()]
    spans = "".join(goal_span(re.match(r"(.*)", g)) for g in goals if g in GOALS)
    return f'<div class="page-goals"><span class="lbl">기여하는 목표</span>{spans}</div>' if spans else ""


LAYOUT = """<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · {site}</title>
<meta name="description" content="{desc}">
<script>try{{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/pygments.css">
</head>
<body>
<a class="skip" href="#main">본문으로 건너뛰기</a>
<header class="topbar">
  <button type="button" class="icon-btn" id="nav-toggle" aria-label="목차 열기" aria-expanded="false" aria-controls="sidebar">☰</button>
  <a class="brand" href="index.html">{site}</a>
  <div class="search">
    <input type="search" id="search-input" placeholder="검색  (단축키 /)" aria-label="사이트 검색" autocomplete="off">
    <div id="search-results" class="search-results" role="listbox" hidden></div>
  </div>
  <button type="button" class="icon-btn" id="theme-toggle" aria-label="다크 모드 전환">◐</button>
</header>
<div class="layout">
  <nav class="sidebar" id="sidebar" aria-label="전체 목차">{nav}</nav>
  <main id="main" class="content">
    <article>
      <header class="page-head">
        <p class="eyebrow">{eyebrow}</p>
        <h1>{title}</h1>
        {summary}
        {goals}
      </header>
      {filter}
      {toc_mobile}
      {body}
      <nav class="pager" aria-label="이전·다음">{pager}</nav>
    </article>
  </main>
  <aside class="toc" aria-label="이 페이지 목차">{toc_block}</aside>
</div>
<footer class="site-foot">신뢰도: <span class="tag trust trust-official">공식</span> <span class="tag trust trust-analysis">분석</span> <span class="tag trust trust-guess">추정</span> <span class="tag trust trust-unknown">확인 못 함</span> · 소스: <a href="https://github.com/HelloNobb/LIFE_SIMUL_LAB">GitHub</a></footer>
<script src="assets/search-index.js"></script>
<script src="assets/app.js"></script>
<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10.9.1/dist/mermaid.esm.min.mjs';
window.__mermaid = mermaid;
window.dispatchEvent(new Event('mermaid-ready'));
</script>
</body>
</html>
"""


def build():
    pages = load_pages()
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for f in ASSETS_SRC.iterdir():
        shutil.copy(f, OUT / "assets" / f.name)
    light = HtmlFormatter(style="friendly").get_style_defs(".hl")
    dark = HtmlFormatter(style="github-dark").get_style_defs(".hl")
    dark_scoped = "\n".join(
        (":root[data-theme=dark] " + line) if line.startswith(".hl") else line for line in dark.splitlines()
    )
    dark_auto = "\n".join(
        ("  :root:not([data-theme=light]) " + line) if line.startswith(".hl") else line for line in dark.splitlines()
    )
    (OUT / "assets" / "pygments.css").write_text(
        light + "\n" + dark_scoped + "\n@media (prefers-color-scheme: dark) {\n" + dark_auto + "\n}\n", encoding="utf-8"
    )
    (OUT / ".nojekyll").write_text("")

    index = []
    claims = []
    rendered = []
    for p in pages:
        body, toc = render_markdown(p["text"])
        body = wrap_sections(replace_tags_outside_code(body))
        rendered.append((p, body, toc))

    for i, (p, body, toc) in enumerate(rendered):
        meta = p["meta"]
        title = meta.get("title", p["slug"])
        prev_p = rendered[i - 1][0] if i > 0 else None
        next_p = rendered[i + 1][0] if i + 1 < len(rendered) else None
        pager = ""
        if prev_p:
            pager += f'<a class="prev" href="{prev_p["out"]}">← {html.escape(prev_p["meta"].get("nav", ""))}</a>'
        if next_p:
            pager += f'<a class="next" href="{next_p["out"]}">{html.escape(next_p["meta"].get("nav", ""))} →</a>'
        summary = f'<p class="summary">{replace_tags_outside_code(html.escape(meta["summary"]))}</p>' if meta.get("summary") else ""
        page_html = LAYOUT.format(
            title=html.escape(title), site=SITE_TITLE, desc=html.escape(meta.get("summary", SITE_DESC)),
            nav=nav_html(pages, p), eyebrow=html.escape(meta.get("eyebrow", "")), summary=summary,
            goals=header_tags(meta), filter=filter_bar(), body=body, pager=pager, **toc_parts(toc_html(toc)),
        )
        (OUT / p["out"]).write_text(page_html, encoding="utf-8")

        # 검색 색인: 소제목(h2) 단위
        for sec in re.findall(r'<section class="sec">([\s\S]*?)</section>', body):
            m = re.search(r'<h2 id="([^"]+)">([\s\S]*?)</h2>', sec)
            if not m:
                continue
            head = strip_html(re.sub(r'<a class="headerlink"[\s\S]*?</a>', "", m.group(2)))
            plain = re.sub(r'<a class="headerlink"[\s\S]*?</a>|<pre[\s\S]*?</pre>', " ", sec)
            index.append({"u": f'{p["out"]}#{m.group(1)}', "p": title, "h": head, "t": strip_html(plain)[:4000]})
            # 태그 모아보기: 태그가 붙은 문단·목록 항목·표 행
            for card in re.findall(r'<div class="card"[^>]*>([\s\S]*?)</div>', sec):
                tags = sorted(set(re.findall(r'data-tag="([a-z]+)"', card)))
                name = re.search(r"<h3[^>]*>([\s\S]*?)</h3>", card)
                summary = re.search(r"<dt>핵심 아이디어</dt><dd>([\s\S]*?)</dd>", card)
                if tags and name:
                    claims.append({"u": f'{p["out"]}#{m.group(1)}', "p": title, "h": head, "tags": tags,
                                   "html": f"<strong>{strip_html(name.group(1))}</strong> — " + (summary.group(1) if summary else "")})
            for kind, el in re.findall(r"<(li|p|tr)(?: [^>]*)?>([\s\S]*?)</(?:li|p|tr)>", re.sub(r'<div class="card"[\s\S]*?</dl>\s*</div>', "", sec)):
                tags = sorted(set(re.findall(r'data-tag="([a-z]+)"', el)))
                if not tags or el.lstrip().startswith("<ul") or "<li>" in el:
                    continue
                if kind == "tr":   # 표의 한 줄: 칸을 구분해서 보여 준다
                    cells = [c.strip() for c in re.findall(r"<t[dh][^>]*>([\s\S]*?)</t[dh]>", el)]
                    el = ' <span class="sep">·</span> '.join(cells)
                claims.append({"u": f'{p["out"]}#{m.group(1)}', "p": title, "h": head, "tags": tags, "html": el.strip()})
        index.append({"u": p["out"], "p": title, "h": title, "t": strip_html(meta.get("summary", ""))})

    # 태그 모아보기 페이지
    rows = "".join(
        f'<li class="claim" data-tags="{" ".join(c["tags"])}"><a class="claim-src" href="{c["u"]}">{html.escape(c["p"])} › {html.escape(c["h"])}</a><div class="claim-body">{c["html"]}</div></li>'
        for c in claims
    )
    tags_body = (
        '<p>사이트 전체에서 태그가 붙은 문장을 한곳에 모았습니다. 위 필터에서 태그를 고르면 그 태그가 붙은 문장만 남습니다. '
        '예를 들어 <span class="tag trust trust-guess">추정</span>만 골라 보면, 아직 근거가 약한 주장만 한눈에 볼 수 있습니다.</p>'
        f'<p class="claim-count">전체 {len(claims)}개</p><ul class="claims">{rows}</ul>'
    )
    tags_html = LAYOUT.format(
        title="태그 모아보기", site=SITE_TITLE, desc="태그별로 모아 본 주장 목록", nav=nav_html(pages, "tags"),
        eyebrow="도구", summary='<p class="summary">목표 태그와 신뢰도 태그로 전체 내용을 걸러 봅니다.</p>', goals="",
        filter=filter_bar(), body=tags_body, pager="", **toc_parts(""),
    )
    (OUT / "tags.html").write_text(tags_html, encoding="utf-8")

    (OUT / "assets" / "search-index.js").write_text(
        "window.SEARCH_INDEX=" + json.dumps(index, ensure_ascii=False) + ";", encoding="utf-8"
    )
    print(f"built {len(pages)} pages, {len(index)} index entries, {len(claims)} tagged claims → {OUT}")


if __name__ == "__main__":
    sys.exit(build())
