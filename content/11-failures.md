---
title: 실패 사례에서 배우기
nav: 11. 실패 사례
eyebrow: 11장
summary: 시뮬레이션이 너무 자유로우면 게임을 망가뜨리고, 너무 숨겨져 있으면 아무도 모른다. 오블리비언의 래디언트 AI, 심즈의 "너무 똑똑한" 자율 행동, 보이지 않는 시뮬레이션의 사례에서 공통 교훈을 뽑는다.
goals: 개연성, 실존감
---

## 한눈에 보기

실패는 크게 세 종류입니다.

1. **너무 자유로움**: NPC가 목표를 이루려고 게임이 원하지 않는 방법을 고른다. (오블리비언)
2. **너무 잘함**: 자율 행동이 플레이어보다 잘해서 플레이어가 할 일이 없다. (심즈 초기 버전)
3. **보이지 않음**: 시뮬레이션은 돌아가지만 플레이어가 모른다. (울티마 온라인·바이오쇼크의 생태계, 동숲 GC의 주민 관계값)

## 오블리비언의 래디언트 AI — 약속과 결과 {개연성} {실존감}

### 무엇을 약속했나 [공식]

E3 2005 데모에서 토드 하워드는 래디언트 AI가 NPC에게 24시간 일정을 주고, 스크립트 없이 **일반적인 목표만 주면 방법은 NPC가 스스로 찾는다**고 소개했습니다. "필요하면 먹고, 음식을 어떻게 구할지는 그들에게 달렸다. 훔칠 수도, 살 수도, 기를 수도 있다." 당시 홍보 문구는 NPC가 개인 특성에 따라 어디서 먹을지, 누구와 말할지, 무엇을 말할지 정하고, 잠자고, 교회에 가고, 물건을 훔치기까지 한다고 설명했습니다. ([Paavo의 자료 정리](https://blog.paavo.me/radiant-ai)에 재수록된 데모 발언과 홍보 문구)

### 무슨 일이 있었나 [공식]

개발자 에밀 파글리아룰로는 출시 전 포럼에서 "AI가 너무 영리하고 집요해서 퀘스트를 망쳐 놓는 일이 있어 일부 행동을 의식적으로 줄였다"고 썼고, 예를 들었습니다. 암흑 형제단 퀘스트에서 만나야 하는 약 거래상이 테스트 중에 플레이어가 도착하기 전에 죽어 있었는데, **약에 중독된 NPC들이 약이 떨어지자 거래상을 죽이고 약을 구하고 있었다**는 것입니다. 다른 개발자는 기능을 없앤 것은 아니고 "상황별로" NPC를 조정해 원하는 행동을 얻었다고 답했습니다. ([Paavo](https://blog.paavo.me/radiant-ai)에 인용된 당시 개발자 포럼 발언, 재게시본 기준)

### 실제로 출시된 것 [분석]

Paavo의 분석에 따르면 출시판 NPC에게는 심즈나 드워프 포트리스 같은 **욕구가 없고**, 일정·조건이 붙은 **AI 패키지**를 차례로 실행합니다. NPC는 공격성·자신감·활동성·책임감 수치를 가지고, 책임감이 낮으면 목표를 이루려고 범죄를 저지릅니다. 그는 래디언트 AI를 특정한 시스템이라기보다 오블리비언의 새 AI 기능 전체를 부르는 우산 같은 이름으로 봅니다. ([Paavo](https://blog.paavo.me/radiant-ai))

### 교훈

- **목표 + 자유로운 수단 = 퀘스트 파괴**: 핵심 NPC(퀘스트 대상)는 자율 행동의 피해자·가해자가 되지 않게 보호 목록을 두세요.
- **수단을 고르는 규칙에 "게임 규칙 보호" 조건을 넣으세요**: GOAP라면 "퀘스트 NPC를 해치는 행동"의 비용을 무한대로 두는 식입니다([2장](02-brain.html)).
- **데모용 연출과 시스템을 구분하세요**: 개발자 스스로 E3 데모의 서점 장면과 대사는 데모용으로 만든 것이라고 밝혔습니다. [공식] ([Paavo](https://blog.paavo.me/radiant-ai))
- **잘 돌아가면 아무도 모른다**: 베데스다 쪽에서는 래디언트 AI를 개선할수록 플레이어가 덜 알아챈다는 발언도 나왔습니다. [추정: 인터뷰 보도] ([FRVR 보도](https://frvr.com/blog/news/elder-scrolls-designer-explains-that-radiant-ai-is-an-enormous-investment-for-bethesda-but-every-improvement-actually-makes-it-less-noticeable-to-players/))

## 심즈 — 자율 행동이 너무 잘했다 {실존감}

윌 라이트는 초기 버전의 자율 행동이 너무 잘해서 "플레이어가 무엇을 하든 심을 자동으로 두는 것보다 못했다"고 말했습니다. [공식] ([PC Gamer](https://www.pcgamer.com/games/the-sims/will-wright-says-the-original-sims-ai-was-actually-too-good-almost-anything-the-player-did-was-worse-than-the-sims-running-on-autopilot))

**교훈**: 시뮬레이션의 목표는 최적의 행동이 아니라 **플레이어가 개입할 이유**를 남기는 것입니다. 자율 행동은 "그럭저럭 살지만 플레이어가 도우면 확실히 나아지는" 수준이 좋습니다.

## 보이지 않는 시뮬레이션 {개연성}

- **울티마 온라인과 바이오쇼크의 생태계**: Tynan Sylvester는 두 게임의 생태계 시뮬레이션이 플레이어의 머릿속 모델로 옮겨지지 않아 "잡음으로 전락"했다고 평가합니다. [공식] ([The Simulation Dream](https://www.gamedeveloper.com/design/the-simulation-dream))
- **동숲 GC의 주민 관계값**: 주민마다 다른 주민에 대한 관계값이 있고 인사할 때마다 바뀌지만, 이 값을 읽어 행동을 바꾸는 코드는 소스에서 찾지 못했습니다. 플레이어가 실제로 보는 것은 관계값이 아니라 옮겨 다니는 말버릇과 옷입니다. [분석] ([6장](06-relationship.html))
- **너무 많은 정보**: Tynan은 림월드가 정착민 수를 12명 정도로 제한해 플레이어가 각 인물을 기억할 수 있게 했고, 드워프는 200명까지 늘어 개인에게 애착을 갖기 어렵다고 비교합니다. 그는 "모든 세부를 채우면 아포페니아가 일어날 여지가 없고, 사람들은 인지적 수고를 싫어한다"고 말합니다. [공식] ([RPS 인터뷰](https://www.rockpapershotgun.com/how-rimworld-generates-great-stories))

**교훈**: 시스템을 추가하기 전에 "이 결과를 플레이어가 어디서, 어떻게 보게 되는가"를 먼저 정하세요. 답이 없으면 만들지 않는 편이 낫습니다.

## 절차 생성의 한계를 인정한 사례 [공식]

- **Wildermyth**: 개발자들은 무작위 챕터 구조와 절차적 악당을 시도했지만 기획 단계를 넘지 못했다고 밝혔습니다. ([인터뷰](https://turnbasedlovers.com/10-turns-interview/with-wildermyth-developer)) 대신 손으로 쓴 이야기와 절차 생성 이야기를 번갈아 쌓는 방식을 택했고, 공식 위키는 분기가 많은 이벤트가 시스템상 다루기 어려워 대부분의 이야기가 선택 하나를 중심으로 돈다고 적었습니다. ([Wildermyth Wiki](https://www.wildermyth.com/wiki/Event_Types))

**교훈**: 모든 것을 절차적으로 만들 필요는 없습니다. **뼈대는 손으로, 살은 절차로**가 현실적인 경우가 많습니다.

## LLM NPC의 실패 양상 {실존감}

- **Generative Agents의 한계(논문)** [공식] ([Park 외 2023](https://arxiv.org/abs/2304.03442))
    - 관련 기억을 못 찾거나 일부만 찾음(선거 이야기를 들었는데도 모른다고 답함).
    - 기억에 없는 내용을 덧붙임(완전히 지어내지는 않지만 과장). 다른 에이전트를 아느냐는 답 453개 중 6개(1.3%)가 지어낸 답.
    - 지나치게 격식 있고 협조적인 말투(언어 모델의 지시 학습 영향).
    - 25명이 이틀을 지내는 데 토큰 비용으로 수천 달러, 실행에 여러 날.
- **인조이 Smart Zoi의 체감 차이**: 크래프톤은 기능이 아직 개발 중이며 더 확장할 계획이라고 밝혔고 [공식] ([크래프톤 공지](https://playinzoi.com/en/news/8419)), 일부 플레이어는 "생각 말풍선 외에 행동 차이를 못 느꼈다"고 썼습니다. [추정] ([Steam 토론](https://steamcommunity.com/app/2456740/discussions/0/836123794066162014/))

**교훈**: LLM이 만든 "속마음"이 행동으로 이어지지 않으면 [1장](01-intro.html)의 원칙과 반대로 **말과 행동이 어긋나는 것**이 보입니다. LLM 출력은 행동 시스템의 결정과 같은 원본에서 나오게 하세요([2장 섞어 쓰기](02-brain.html)).

## 실패를 막는 체크리스트

| 위험 | 막는 방법 |
|---|---|
| 자율 행동이 퀘스트·핵심 NPC를 망침 | 보호 목록, 퀘스트 중 자율 행동 범위 제한, 계획 비용에 금지 조건 |
| 자율 행동이 너무 잘함 | 의도적 비효율, 플레이어만 할 수 있는 개입 남기기 |
| 시뮬레이션이 안 보임 | 각 시스템마다 "보이는 결과" 최소 1개 정하기 |
| 정보가 너무 많음 | 인원 제한, 요약 UI, 중요한 것만 알림 |
| 원인이 안 보임 | 이유 하나 골라 보여주기([8장](08-events.html)) |
| LLM이 사실과 다른 말을 함 | 사실 묶음 밖의 고유명사·숫자·약속 거르기, 대체 대사 |
| LLM 속마음과 행동이 어긋남 | 결정은 규칙이, 표현만 LLM이 |

## 출처

- Paavo, "What was Radiant AI, anyway?" (2025) — <https://blog.paavo.me/radiant-ai>
- FRVR, 래디언트 AI 관련 발언 보도 — <https://frvr.com/blog/news/elder-scrolls-designer-explains-that-radiant-ai-is-an-enormous-investment-for-bethesda-but-every-improvement-actually-makes-it-less-noticeable-to-players/>
- PC Gamer, 윌 라이트 심즈 자율 행동 발언 — <https://www.pcgamer.com/games/the-sims/will-wright-says-the-original-sims-ai-was-actually-too-good-almost-anything-the-player-did-was-worse-than-the-sims-running-on-autopilot>
- Tynan Sylvester, "The Simulation Dream" — <https://www.gamedeveloper.com/design/the-simulation-dream>
- Rock Paper Shotgun, "How RimWorld Generates Great Stories" — <https://www.rockpapershotgun.com/how-rimworld-generates-great-stories>
- Turn Based Lovers, Wildermyth 개발자 인터뷰 — <https://turnbasedlovers.com/10-turns-interview/with-wildermyth-developer>
- Wildermyth Wiki, Event Types — <https://www.wildermyth.com/wiki/Event_Types>
- Park 외 2023 — <https://arxiv.org/abs/2304.03442>
- 크래프톤, Smart Zoi 공지 — <https://playinzoi.com/en/news/8419>
- Steam 토론 — <https://steamcommunity.com/app/2456740/discussions/0/836123794066162014/>
- ACreTeam, ac-decomp — <https://github.com/ACreTeam/ac-decomp>
