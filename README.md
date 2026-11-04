# LIFE SIMUL LAB

살아있는 NPC와 세계를 만드는 설계 가이드. 실제 게임의 디컴파일 소스·게임 데이터·개발자 발표와 논문에서
"살아있다는 느낌"을 만드는 기법을 뽑아, **AI 없이 / AI 사용 / 섞어 쓰기** 세 갈래로 정리했습니다.

- 사이트: `docs/` 폴더 (GitHub Pages)
- 원고: `content/*.md`
- 빌드: `tools/build.py`, 점검: `tools/check.py`

## 고치는 법

```bash
pip install markdown pygments
python3 tools/build.py        # content/ → docs/
python3 tools/check.py        # 링크·출처 점검 (외부 링크까지: --external)
```

`docs/`는 빌드 결과물이므로 직접 고치지 말고 `content/`를 고친 뒤 다시 빌드하세요.

### 원고 안의 약속

| 쓰는 법 | 결과 |
|---|---|
| `[공식]` `[분석]` `[추정]` `[확인 못 함]` | 신뢰도 태그 (색으로 구분, 필터 가능) |
| `{소속감}` `{개연성}` `{관계}` `{실존감}` | 목표 태그 |
| ```` ```mermaid ```` | 다이어그램 |
| ```` ```csharp ```` | 문법 강조된 코드 |
| `!!! note "제목"` | 알림 상자 |
| 앞머리 `goals:` | 페이지 맨 위 목표 태그 |

## GitHub Pages 켜기

저장소 **Settings → Pages → Build and deployment**에서 Source를 **Deploy from a branch**, Branch를 `main` / `/docs`로 고르면
`https://<아이디>.github.io/LIFE_SIMUL_LAB/`에 배포됩니다.
