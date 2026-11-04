---
title: 참고문헌
nav: 15. 참고문헌
eyebrow: 15장
summary: 이 가이드에서 인용한 모든 자료를 종류별로 모았다. 각 항목 앞의 태그는 그 자료를 근거로 쓸 때의 신뢰도다.
goals: 소속감, 개연성, 관계, 실존감
---

## 디컴파일 소스·게임 데이터

- [분석] ACreTeam, **ac-decomp** — 동물의 숲 GameCube 북미판(GAFE01) 디컴파일. 이 가이드는 커밋 `e4926f7`(2026-11-03) 기준으로 확인했습니다. <https://github.com/ACreTeam/ac-decomp>
    - 주요 파일: `include/m_npc.h`, `include/m_npc_personal_id.h`, `include/m_npc_walk.h`, `include/m_font.h`, `include/m_field_make.h`, `include/m_name_table.h`, `src/game/m_npc.c`, `src/game/m_npc_schedule.c`, `src/game/m_npc_walk.c`, `src/game/m_cockroach.c`, `src/game/m_field_assessment.c`, `src/game/m_random_field_ovl.c`, `src/game/m_field_make.c`, `src/game/m_kankyo.c`, `src/actor/ac_set_npc_manager.c`, `src/actor/ac_quest_talk_greeting.c`, `src/actor/ac_quest_talk_normal_init.c`, `src/actor/ac_quest_talk_init.c`, `src/actor/npc/ac_npc_act_greeting.c_inc`, `src/actor/npc/ac_npc_action.c_inc`
- [분석] zeldaret/af — 동물의 숲 N64판 디컴파일(진행 중) <https://github.com/zeldaret/af>
- [분석] Stardew Valley Wiki, Modding:Schedule data <https://stardewvalleywiki.com/Modding:Schedule_data>
- [분석] Stardew Valley Wiki, Modding:Dialogue <https://stardewvalleywiki.com/Modding:Dialogue>
- [분석] Stardew Valley Wiki, Modding:Event data <https://stardewvalleywiki.com/Modding:Event_data>
- [분석] Stardew Valley Wiki, Friendship / Gifts / Community Center <https://stardewvalleywiki.com/Friendship>, <https://stardewvalleywiki.com/Gifts>, <https://stardewvalleywiki.com/Community_Center>
- [분석] RimWorld Wiki: Mood, Mental break, Opinion, Social, AI Storytellers <https://rimworldwiki.com/wiki/Mood>, <https://rimworldwiki.com/wiki/Mental_break>, <https://rimworldwiki.com/wiki/Opinion>, <https://rimworldwiki.com/wiki/Social>, <https://rimworldwiki.com/wiki/AI_Storytellers>
- [분석] Dwarf Fortress Wiki: Personality facet, Memory, Need, World generation, Legends <https://dwarffortresswiki.org/index.php/DF2014:Personality_facet>, <https://dwarffortresswiki.org/index.php/DF2014:Memory_(thought)>, <https://dwarffortresswiki.org/index.php/DF2014:Need>, <https://dwarffortresswiki.org/index.php/DF2014:World_generation>, <https://dwarffortresswiki.org/index.php/DF2014:Legends>
- [분석] Nookipedia: Villager, Catchphrase, Environment rating <https://nookipedia.com/wiki/Villager>, <https://nookipedia.com/wiki/Catchphrase>, <https://nookipedia.com/wiki/Island_evaluation>
- [분석] Caves of Qud Wiki, Sultan history <https://wiki.cavesofqud.com/wiki/Sultan_history>
- [분석] Nintendo Everything, 모여봐요 이사 데이터마이닝(Ninji) 보도 <https://nintendoeverything.com/animal-crossing-new-horizons-datamine-provides-details-about-how-villagers-move-out/>
- [분석] Paavo, "What was Radiant AI, anyway?" (2025) — 오블리비언 게임 데이터와 당시 자료를 정리한 분석 <https://blog.paavo.me/radiant-ai>

## 분석 글

- [분석] 동숲 최적화 분석 0편 "놀동숲이 32MB 안에 들어갔다고?" <https://nobbs-it-study.tistory.com/entry/%EA%B2%8C%EC%9E%84%EB%B6%84%EC%84%9D-%EB%86%80%EB%8F%99%EC%88%B2%EC%9D%B4-32MB-%EC%95%88%EC%97%90-%EB%93%A4%EC%96%B4%EA%B0%94%EB%8B%A4%EA%B3%A0>
- [분석] 동숲 최적화 분석 1편 "놀동숲의 마을은 36 Byte다" <https://nobbs-it-study.tistory.com/entry/%EA%B2%8C%EC%9E%84%EB%B6%84%EC%84%9D-%EB%86%80%EB%8F%99%EC%88%B2%EC%9D%98-%EB%A7%88%EC%9D%84%EC%9D%80-36-Byte%EB%8B%A4-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B6%84%EC%84%9D-1%ED%8E%B8>
- [분석] 동숲 최적화 분석 2편 "동숲 주민을 어떻게 살아있게 만들었나" — 이 가이드에서 주장 13개를 소스와 다시 대조함 <https://nobbs-it-study.tistory.com/entry/%EA%B2%8C%EC%9E%84-%EB%B6%84%EC%84%9D-%EB%8F%99%EC%88%B2-%EC%A3%BC%EB%AF%BC%EC%9D%84-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%82%B4%EC%95%84%EC%9E%88%EA%B2%8C-%EB%A7%8C%EB%93%A4%EC%97%88%EB%82%98-%EC%B5%9C%EC%A0%81%ED%99%94-%EB%B6%84%EC%84%9D-2%ED%8E%B8>

## 개발자 발표·글·공식 자료

- [공식] Kenneth D. Forbus & Will Wright, "Some notes on programming objects in The Sims" (2001) <https://qrg.northwestern.edu/papers/Files/Programming_Objects_in_The_Sims.pdf>
- [공식] Richard Evans, "Modeling Individual Personalities in The Sims 3" (GDC) <https://gdcvault.com/play/1012294/Modeling-Individual-Personalities-in-The>
- [공식] Tynan Sylvester, "The Simulation Dream" (Game Developer, 2013) <https://www.gamedeveloper.com/design/the-simulation-dream>
- [공식] Tynan Sylvester, "RimWorld: Contrarian, Ridiculous, and Impossible Game Design Methods" (GDC 2017) <https://gdcvault.com/play/1024232/-RimWorld-Contrarian-Ridiculous-and>
- [공식] Rock Paper Shotgun, "How RimWorld Generates Great Stories" (2016, Tynan Sylvester 인터뷰) <https://www.rockpapershotgun.com/how-rimworld-generates-great-stories>
- [공식] Jeff Orkin, "Three States and a Plan: The A.I. of F.E.A.R." (GDC 2006) <https://pages.cs.wisc.edu/~dyer/cs540/handouts/gdc2006_orkin_jeff_fear.pdf>
- [공식] Dave Mark & Kevin Dill, "Improving AI Decision Modeling Through Utility Theory" (GDC 2010) <https://gdcvault.com/play/1012410/Improving-AI-Decision-Modeling-Through>
- [공식] Elan Ruskin, "AI-driven Dynamic Dialog through Fuzzy Pattern Matching" (GDC 2012) <https://gdcvault.com/play/1015317/AI-driven-Dynamic-Dialog-through> / Emily Short의 요약 <https://emshort.blog/2012/03/16/gdc-2012-talk-on-dynamic-dialogue/>
- [공식] Jason Grinblat, "Procedurally Generating History in Caves of Qud" (GDC) <https://gdcvault.com/play/1024990/Procedurally-Generating-History-in-Caves>
- [공식] Nate Austin, "Getting Players Emotionally Invested in Procedural Characters in Wildermyth" (GDC 2022) <https://gdcvault.com/play/1027614/Independent-Games-Summit-Session-Getting>
- [공식] Wildermyth Wiki (개발사 운영), Event Types <https://www.wildermyth.com/wiki/Event_Types>
- [공식] Petr Smrcek, "Supporting Thousands of NPCs in Kingdom Come: Deliverance" (GDC 2026) <https://gdcvault.com/play/1035718/Supporting-Thousands-of-NPCs-in>
- [공식] Paradox, CK3 개발 일지 31·58·104 (원문 접속 제한으로 검색 인용 기준 확인) <https://forum.paradoxplaza.com/forum/developer-diary/ck3-dev-diary-31-a-stressful-situation.1399764/>, <https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-58-stre-ss-tching-the-traits.1472092>, <https://forum.paradoxplaza.com/forum/threads/ck3-dev-diary-104-ai-ai-ai.1539411/>
- [공식] 크래프톤, CES 2025 CPC 발표 <https://www.businesswire.com/news/home/20250108628507/en/KRAFTON-Showcases-AI-Model-CPC-Built-with-NVIDIA-ACE-at-CES-2025>
- [공식] 크래프톤, inZOI Smart Zoi 공지 <https://playinzoi.com/en/news/8419>
- [공식] NVIDIA, inZOI·NARAKA ACE 발표 <https://www.nvidia.com/en-gb/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month>
- [공식] PC Gamer, 윌 라이트 심즈 자율 행동 발언 <https://www.pcgamer.com/games/the-sims/will-wright-says-the-original-sims-ai-was-actually-too-good-almost-anything-the-player-did-was-worse-than-the-sims-running-on-autopilot>
- [공식] Game Developer, 네메시스 시스템 특허 보도 <https://www.gamedeveloper.com/business/-i-shadow-of-war-i-publisher-warner-bros-has-patented-the-series-nemesis-system>
- [공식] Turn Based Lovers, Wildermyth 개발자 인터뷰 <https://turnbasedlovers.com/10-turns-interview/with-wildermyth-developer>

## Game AI Pro (무료 공개 장)

- [공식] Champandard & Dunstan, "The Behavior Tree Starter Kit" (1권 6장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter06_The_Behavior_Tree_Starter_Kit.pdf>
- [공식] David "Rez" Graham, "An Introduction to Utility Theory" (1권 9장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter09_An_Introduction_to_Utility_Theory.pdf>
- [공식] "Building Utility Decisions into Your Existing Behavior Tree" (1권 10장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter10_Building_Utility_Decisions_into_Your_Existing_Behavior_Tree.pdf>
- [공식] Troy Humphreys, "Exploring HTN Planners through Example" (1권 12장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter12_Exploring_HTN_Planners_through_Example.pdf>
- [공식] Phil Carlisle, "A Simple and Practical Social Dynamics System" (1권 35장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter35_A_Simple_and_Practical_Social_Dynamics_System.pdf>
- [공식] Michael Mateas & Josh McCoy, "An Architecture for Character-Rich Social Simulation" (1권 43장) <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter43_An_Architecture_for_Character-Rich_Social_Simulation.pdf>
- [공식] Jeff Orkin, "Combat Dialogue in FEAR: The Illusion of Communication" (2권 2장) <https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter02_Combat_Dialogue_in_FEAR_The_Illusion_of_Communication.pdf>
- [공식] Kevin Dill, "Dual-Utility Reasoning" (2권 3장) <https://www.gameaipro.com/GameAIPro2/GameAIPro2_Chapter03_Dual-Utility_Reasoning.pdf>
- [공식] "Overcoming Pitfalls in Behavior Tree Design" (3권 9장) <https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter09_Overcoming_Pitfalls_in_Behavior_Tree_Design.pdf>
- [공식] "A Character Decision-Making System for FINAL FANTASY XV" (3권 11장) <https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter11_A_Character_Decision-Making_System_for_FINAL_FANTASY_XV_by_Combining_Behavior_Trees_and_State_Machines.pdf>
- [공식] Mike Lewis, "Choosing Effective Utility-Based Considerations" (3권 13장) <https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter13_Choosing_Effective_Utility-Based_Considerations.pdf>
- [공식] "Behavior Decision System: Dragon Age Inquisition's Utility Scoring Architecture" (3권 31장) <https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter31_Behavior_Decision_System_Dragon_Age_Inquisition%E2%80%99s_Utility_Scoring_Architecture.pdf>
- [공식] Hendrik Skubch, "Ambient Interactions: Improving Believability by Leveraging Rule-Based AI" (3권 35장) <https://www.gameaipro.com/GameAIPro3/GameAIPro3_Chapter35_Ambient_Interactions_Improving_Believability_by_Leveraging_Rule-Based_AI.pdf>

## 논문·연구

- [공식] Park 외, "Generative Agents: Interactive Simulacra of Human Behavior" (UIST 2023) <https://arxiv.org/abs/2304.03442>
- [공식] joonspk-research/generative_agents — 위 논문의 공식 코드(커밋 `fe05a71`) <https://github.com/joonspk-research/generative_agents>
- [공식] Park 외, "Generative Agent Simulations of 1,000 People" (2024) <https://arxiv.org/abs/2411.10109>
- [공식] Altera, "Project Sid: Many-agent simulations toward AI civilization" (2024) <https://arxiv.org/abs/2411.00114>
- [공식] Vezhnevets 외, Concordia (Google DeepMind) <https://arxiv.org/abs/2312.03664>, <https://github.com/google-deepmind/concordia>
- [공식] a16z-infra, AI Town (커밋 `8e05997`) <https://github.com/a16z-infra/ai-town>
- [공식] Gallotta 외, "Large Language Models and Games: A Survey and Roadmap" (2024) <https://arxiv.org/abs/2402.18659>
- [공식] Michael Mateas & Andrew Stern, "Structuring Content in the Façade Interactive Drama Architecture" (AIIDE 2005) <https://cdn.aaai.org/AIIDE/2005/AIIDE05-016.pdf>
- [공식] McCoy 외, "Comme il Faut: A System for Authoring Playable Social Models" (AIIDE 2011) <https://ojs.aaai.org/index.php/AIIDE/article/view/12454>
- [공식] McCoy 외, "Prom Week: Social Physics as Gameplay" (FDG 2011) <https://doi.org/10.1145/2159365.2159425>
- [공식] Richard Evans & Emily Short, "Versu — A Simulationist Storytelling System" (IEEE TCIAIG 2014) <https://www.cs.uky.edu/~sgware/reading/papers/evans2014versu.pdf>
- [공식] James Ryan, *Curating Simulated Storyworlds* (UCSC 박사논문, 2018) <https://escholarship.org/uc/item/1340j5h2> / Emily Short의 장별 리뷰 <https://emshort.blog/2019/05/21/curating-simulated-storyworlds-james-ryan/>
- [공식] Jason Grinblat & C. Brian Bucklew, "Subverting Historical Cause & Effect: Generation of Mythic Biographies in Caves of Qud" (FDG 2017) <https://doi.org/10.1145/3102071.3110574>
- [공식] Tanya X. Short & Tarn Adams (편), *Procedural Storytelling in Game Design* (Routledge, 2019) <https://www.routledge.com/Procedural-Storytelling-in-Game-Design-1st-Edition/Short-Adams/p/book/9781138595309>

## 커뮤니티 자료 (신뢰도 낮음)

- [추정] Steam 토론, "What is Smart Zoi really doing (as of the current patch)?" <https://steamcommunity.com/app/2456740/discussions/0/836123794066162014/>
- [추정] Fextralife inZOI Wiki, Smart Zoi Mode <https://inzoi.wiki.fextralife.com/Smart_Zoi_Mode>
- [추정] GoNintendo, CEDEC 2020 모동숲 주민 제작 과정 요약(2차 보도) <https://gonintendo.com/stories/368235-nintendo-details-their-process-for-creating-unique-villagers-in-a>
- [추정] FRVR, 래디언트 AI 관련 발언 보도 <https://frvr.com/blog/news/elder-scrolls-designer-explains-that-radiant-ai-is-an-enormous-investment-for-bethesda-but-every-improvement-actually-makes-it-less-noticeable-to-players/>

## 확인하지 못한 것

- [확인 못 함] 인조이 Smart Zoi에서 언어 모델이 행동을 직접 고르는지, 기존 행동 시스템의 가중치만 바꾸는지
- [확인 못 함] 인조이 CPC 언어 모델의 크기(보도마다 다름)
- [확인 못 함] 섀도우 오브 모르도르 네메시스 시스템의 구조에 대한 개발사 발표 자료
- [확인 못 함] 킹덤 컴 2 GDC 발표의 본문 내용(소개문만 확인)
- [확인 못 함] 놀러오세요·튀어나와요의 이사·친밀도 내부 수치(디컴파일·데이터마이닝 근거 없음)
- [확인 못 함] 동숲 GC의 주민 사이 관계값(`animal_relations`)을 읽어서 행동을 바꾸는 코드(쓰는 곳만 찾음)
- [확인 못 함] 위키독스 461274 페이지(사이트의 봇 확인으로 접속하지 못함)
