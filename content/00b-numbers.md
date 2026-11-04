---
title: 수치 레퍼런스 — 실제 게임 값과 시작값
nav: ★ 수치 레퍼런스
eyebrow: 바로 가져다 쓰기
summary: 이 가이드에서 확인한 실제 게임 수치를 한 장에 모았다. 각 줄에 "내 게임에서 처음 넣어 볼 값"을 같이 적었다.
goals: 실존감, 관계, 개연성, 소속감
---

## 쓰는 법

- **실제 값** 칸은 게임 소스·데이터·공식 자료로 확인한 값입니다. 태그는 근거의 종류입니다.
- **시작값** 칸은 [실전 페이지](00a-practice.html)의 주민 8명 예제(친밀도 0~100, 게임 1시간 = 현실 1분)에 맞춘 이 가이드의 제안입니다. [추정]
- 표의 근거 링크는 맨 아래 출처에 모았습니다. 소스 파일 이름은 [ac-decomp](https://github.com/ACreTeam/ac-decomp) 기준입니다.

## 일정과 욕구

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 성격별 시간표 수 | 동숲 GC: 성격 6종에 1장씩 | [분석] `m_npc_schedule.c` | 성격 3종에 1장씩 |
| 먹보(lazy) 하루 | 잠 22~08, 바깥 9~12·14~19:30 | [분석] `m_npc_schedule.c` | 그대로 |
| 무뚝뚝(cranky) 하루 | 잠 5~10, 바깥 11~15·16~22·23~4 | [분석] `m_npc_schedule.c` | 그대로 |
| 일정 고르는 법 | 스타듀: 키(계절_날짜, 날짜_하트, rain…)를 정해진 순서로 맞춰 첫 일치 | [분석] Schedule data | 인물이 적으면 이 방식 |
| 비 오는 날 다른 일정 | 스타듀 `rain2`: 비 오는 날 50% | [분석] Schedule data | 50% |
| 심즈 욕구 | 에너지·편안함·허기·위생·방광·방·사교·재미·기분 | [공식] Forbus & Wright | 3개(배고픔·에너지·사교)로 시작 |
| 광고 값 예 | 심즈 변기: 방광 0~70 / 어항 먹이: 장난기 따라 재미 1~11 | [공식] Forbus & Wright | 채우는 양 30~60 |
| 욕구 감소 | (공개 자료로 확인 못 함) | [확인 못 함] | 배고픔 −6/h, 에너지 −4/h, 사교 −5/h |
| 끼어들기 기준 | (공개 자료로 확인 못 함) | [확인 못 함] | 욕구 15 미만 |
| 판단 주기 | (공개 자료로 확인 못 함) | [확인 못 함] | 1~2초 |

## 성격

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 연속 대화 짜증 시작 / 거부 | 동숲 GC: 친절함·먹보 12/15, 아이돌·운동광 10/13, 무뚝뚝·성숙함 9/12 | [분석] `m_npc.c` | 무난 12/15, 까칠 9/12 |
| 짜증 회복 타이머 | 아이돌 3000, 친절함·먹보·운동광 4000, 무뚝뚝·성숙함 5000 (프레임) | [분석] `m_npc.c` | 까칠할수록 길게 |
| 산책 목적지 가중치 | 무뚝뚝 {신사×3, 혼자×7}, 성숙함(01:30까지) {신사×7, 혼자×3} | [분석] `m_npc_walk.c` | 배열 중복으로 표현 |
| 정신 붕괴 기준 이동 | 림월드 강철 의지 −18%, 신경과민 +8% | [분석] RimWorld 위키 | 성격별 ±10~20% |
| 모욕 확률 | 림월드 거친 성격: 모욕·무시 ×2.3 | [분석] RimWorld 위키 | 다툼 확률 ×2 |
| 성격 수치 | 드워프 포트리스 측면 0~100, 40~60은 "보통" | [분석] DF 위키 | 극단값만 문장으로 보여 주기 |

## 관계

| 항목 | 실제 값 | 근거 | 시작값 (0~100) |
|---|---|---|---|
| 하트 크기 | 스타듀 1하트 = 250점, 최대 10하트(배우자 14) | [분석] Friendship | 10점 = 1하트 |
| 하루 대화 | 스타듀 +20 | [분석] Friendship | +1 |
| 선물 | 스타듀 최애 +80, 좋아함 +45, 보통 +20, 싫어함 −20 | [분석] Gifts | +3 / +2 / +1 / −1 |
| 생일 선물 | 스타듀 ×8, 겨울 축제 ×5 | [분석] Gifts | ×4 |
| 선물 제한 | 스타듀 하루 1개, 주 2개 | [분석] Gifts | 그대로 |
| 감소 | 스타듀 배우자 −20/일, 꽃다발 후 −10/일, 그 외 −2/일 (문턱에서 멈춤) | [분석] Friendship | −0.1/일, 80 이상 멈춤 |
| 목격된 나쁜 행동 | 스타듀 쓰레기통 뒤지기 −25 | [분석] Friendship | −3 |
| 연애 잠금 | 스타듀 결혼 후보는 8하트에서 멈추고 꽃다발로 해제 | [분석] Friendship | 80에서 멈춤 + 고백 사건 |
| 친밀도 범위 | 동숲 GC 0~127, 처음 1 / 모여봐요 0~255 | [분석] `m_npc.c` / 데이터마이닝 보도 | 0~100, 처음 0 |
| 편지 | 동숲 GC 편지 +3, 이상한 편지 추가 −5, 선물 동봉 추가 +3 | [분석] `m_npc.c` | 그대로 |
| 주민끼리 관계 | 동숲 GC 0~255, 처음 128, 인사 반응으로 ±8/−4 | [분석] `ac_npc_act_greeting.c_inc` | 그대로 |
| 주먹다짐 | 림월드 모욕 1회 4%, 무시 1회 0.5% | [분석] RimWorld 위키 | 말다툼 사건 4% |

## 기억과 대사

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 플레이어 기억 칸 | 동숲 GC 7칸 | [분석] `m_npc.h` | 7칸 |
| 잊는 순서 | 외부인 → 편지 없음 → 친밀도 낮음 → 오래됨 | [분석] `m_npc.c` | 그대로 |
| 오랜만 인사 | 동숲 GC 1일 / 14일 / 60일 (현실 날짜) | [분석] `ac_quest_talk_greeting.c` | 현실 기준 그대로, 게임 날짜면 1·7·28일 |
| 드워프 기억 | 단기 8칸, 장기 8칸, 1년 버티면 장기로 | [분석] DF 위키 | 사건 기억 8칸 |
| 기억 검색 (논문) | 최근성·중요도·관련성 각 0~1, 가중치 1·1·1, 시간당 감소 0.995 | [공식] Park 외 2023 | 그대로 |
| 기억 검색 (공식 코드) | 가중치 0.5·3·2, 감소 0.99 | [공식] generative_agents 코드 | 관련성을 중시하려면 이쪽 |
| 회고 시작 | 중요도 합 150 (하루 2~3번) / AI Town: 최근 100개 합 500 | [공식] 논문, AI Town 코드 | 하루 1번(밤)으로 단순화 |
| 대사 주제 확률 | 동숲 GC 평소 40 / 날씨·시간 30 / 물건 주기 10 / 가구 10 / 물건 사기 10 | [분석] `ac_quest_talk_normal_init.c` | 그대로 |
| 날씨 대사 수 | 동숲 GC 성격별 날씨마다 5문장 중 무작위 | [분석] `ac_quest_talk_normal_init.c` | 3~5문장 |
| 인사 대사 수 | 동숲 GC 상황별 성격마다 3문장 중 무작위 | [분석] `ac_quest_talk_greeting.c` | 3문장 |
| 대사 고르는 법 | Valve: 조건이 가장 많이 맞는 규칙 | [공식] Ruskin GDC 2012 | 그대로 + 쿨다운 24게임시간 |

## 주민끼리, 사건, 시간

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 인사 반응 확률 | 동숲 GC 말다툼 20, 말버릇 따라 하기 10, 그만하라 10, 우산 10, 옷 따라 입기 10, 새 옷 5, 무늬 옷 10, 원래대로 5, 없음 20 (%) | [분석] `ac_npc_act_greeting.c_inc` | 그대로, 잦으면 따라 하기 5% |
| 화면 밖 이동 | 동숲 GC 7초에 한 칸 | [분석] `ac_set_npc_manager.c` | 5~10초에 한 칸 |
| 동시에 산책하는 주민 | 동숲 GC 주민 수 ÷ 3 | [분석] `m_npc_walk.h` | 그대로 |
| 한 구역 최대 인원 | 동숲 GC 3명 이상이면 들어가지 않음 | [분석] `ac_set_npc_manager.c` | 그대로 |
| 목적지 체류 | 동숲 GC 108,000프레임(60fps 기준 30분) | [분석] `ac_set_npc_manager.c` | 게임 30분~1시간 |
| 기분 움직임 | 림월드 시간당 +12 / −8 | [분석] RimWorld 위키 | 그대로 |
| 사건 위험 기준 | 림월드 35 / 20 / 5 % | [분석] RimWorld 위키 | 35 / 20 |
| 붕괴 후 회복 | 림월드 카타르시스 +40, 2.5일 | [분석] RimWorld 위키 | +20, 1일 |
| 스토리텔러 | 림월드 카산드라: 위협 → 휴식 → 더 큰 위협 | [분석] RimWorld 위키 | 생활 시뮬은 작은 사건 위주 |
| 비운 동안 흔적 | 동숲 GC 바퀴벌레: 6일 유예, 최대 10 | [분석] `m_cockroach.c` | 3일부터 잡초, 7일부터 소식 |

## 마을과 공동체

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 주민 수 | 동숲 GC 최소 5, 최대 15 | [분석] `m_npc.h` | 8명 시작, 최대 10 |
| 새 주민 조건 | 정원 미만, 하루 1명, 이 마을 플레이어가 주민 전원과 대화했을 것 | [분석] `m_npc.c` | 그대로 |
| 새 주민 확률 | 마을 등급 0~6 → 40·50·60·70·80·90·100% | [분석] `m_npc.c` | 그대로 |
| 새 주민 성격 | 지금 가장 적은 성격 | [분석] `m_npc.c` | 그대로 |
| 주민이 떠나는 조건 | 15명 꽉 참 + 마지막 변화 후 10일 | [분석] `m_npc.c` | 정원 + 14일 |
| 떠날 주민 | 기억이 가장 적은 주민 → 편지 적은 → 같은 성격 많은 | [분석] `m_npc.c` | 그대로, 또는 플레이어에게 허락받기(모여봐요) |
| 구역 평가 | 나무 12~14 완벽, 9~11·15~17 좋음, 잡초 3개 이상 0점 | [분석] `m_field_assessment.c` | 구역 크기에 맞게 나무 수 조정 |
| 마을 점수 | 완벽 수 + 좋음 수 ÷ 2, 쓰레기 5개 이상이면 0 | [분석] `m_field_assessment.c` | 그대로 |
| 등급 문턱 | 점수 0 / 2 / 4 / 7 / 12 / 16 초과마다 한 단계 | [분석] `m_field_assessment.c` | 8구역이면 0 / 1 / 2 / 3 / 5 / 6 |
| 최고 등급 보상 | 15일 연속이면 금도끼 | [분석] `m_field_assessment.h` | 연속 일수 보상 |
| 말버릇 길이 | 10글자 이하 | [분석] Nookipedia | 그대로 |

## LLM 관련

| 항목 | 실제 값 | 근거 | 시작값 |
|---|---|---|---|
| 연구 규모 비용 | 25명 × 이틀에 토큰 비용 수천 달러, 실행 여러 날 (gpt-3.5-turbo) | [공식] Park 외 2023 | 하루 호출 수를 먼저 계산 |
| 지어낸 답 비율 | 다른 에이전트를 아느냐는 답 453개 중 1.3% | [공식] Park 외 2023 | 출력 검사 필수 |
| 중요도 파싱 실패 시 | AI Town: 5로 둠 | [공식] AI Town 코드 | 모든 출력에 기본값 |
| 응답 제한 시간 | (공개 자료로 확인 못 함) | [확인 못 함] | 대화 1.5초, 일기는 밤에 일괄 |

## 출처

- ACreTeam, ac-decomp — <https://github.com/ACreTeam/ac-decomp>
- Stardew Valley Wiki: Schedule data, Friendship, Gifts — <https://stardewvalleywiki.com/Modding:Schedule_data>, <https://stardewvalleywiki.com/Friendship>, <https://stardewvalleywiki.com/Gifts>
- RimWorld Wiki: Mood, Mental break, Opinion — <https://rimworldwiki.com/wiki/Mood>, <https://rimworldwiki.com/wiki/Mental_break>, <https://rimworldwiki.com/wiki/Opinion>
- Dwarf Fortress Wiki: Personality facet, Memory — <https://dwarffortresswiki.org/index.php/DF2014:Personality_facet>, <https://dwarffortresswiki.org/index.php/DF2014:Memory_(thought)>
- Forbus & Wright 2001 — <https://qrg.northwestern.edu/papers/Files/Programming_Objects_in_The_Sims.pdf>
- Nintendo Everything, 모여봐요 데이터마이닝 보도 — <https://nintendoeverything.com/animal-crossing-new-horizons-datamine-provides-details-about-how-villagers-move-out/>
- Nookipedia, Catchphrase — <https://nookipedia.com/wiki/Catchphrase>
- Park 외 2023 — <https://arxiv.org/abs/2304.03442> / 공식 코드 <https://github.com/joonspk-research/generative_agents>
- a16z-infra/ai-town — <https://github.com/a16z-infra/ai-town>
- Elan Ruskin, GDC 2012 — <https://gdcvault.com/play/1015317/AI-driven-Dynamic-Dialog-through>
