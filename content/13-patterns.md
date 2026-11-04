---
title: 설계 패턴 카탈로그
nav: 13. 패턴 카드
eyebrow: 13장
summary: 앞 장들의 기법을 "패턴 카드" 30장으로 다시 정리했다. 기획할 때 문제에서 출발해 카드를 고르고, 자세한 설명과 코드는 각 카드의 출처 장으로 넘어가면 된다.
goals: 소속감, 개연성, 관계, 실존감
---

## 카드 읽는 법

각 카드는 같은 형식입니다: **이름 / 해결하는 문제 / 핵심 아이디어 / 쓰인 게임 / AI 필요 여부 / 구현 난이도(1~5) / 함께 쓰면 좋은 패턴 / 주의점 / 출처**.

- 구현 난이도는 Unity 2D 프로젝트에서 1인 개발자가 처음 구현할 때를 기준으로 한 이 가이드의 판단입니다. [추정]
- "쓰인 게임" 칸의 신뢰도 태그는 그 게임이 실제로 그렇게 동작한다는 근거의 종류입니다.
- 위의 **태그 필터**로 목표별 카드만 볼 수 있습니다.

### 문제에서 카드 찾기

| 이런 문제가 있다면 | 먼저 볼 카드 |
|---|---|
| NPC가 기계 같다 | 일정 블록 + 욕구 끼어들기, 성격 열쇠 표, 오랜만 인사 |
| NPC들이 다 똑같다 | 성격 열쇠 표, 배열 중복 가중치, 유행 전파 |
| 사건이 무작위로 느껴진다 | 이유 하나 고르기, 기한부 생각, 원인 기록 |
| 관계가 얕다 | 속마음/공개 관계 분리, 칸 제한 기억, 유행 전파 |
| 내가 마을 사람 같지 않다 | 가꾸면 커지는 공동체, 유행 전파, 마지막 시각 계산 |
| NPC가 너무 많아 무겁다 | AI LOD 좌표 산책, 마지막 시각 계산 |
| LLM을 넣고 싶은데 불안하다 | 규칙이 고르고 LLM이 말한다, 사실 묶음 가드레일 |

## 행동 선택
<div class="card" markdown="0">
<h3>층 나눈 상태 기계</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>상태가 늘면 상태 기계의 화살표가 얽힌다</dd><dt>핵심 아이디어</dt><dd>'무엇을 할 시간인가(일정)' → '무엇을 할까(생각)' → '어떻게 움직일까(행동)'로 층을 나눠 각 층을 단순하게 유지한다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC [분석], F.E.A.R.(3개 상태 + 계획기) [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>일정 블록 + 욕구 끼어들기, Utility</dd><dt>주의점</dt><dd>위층이 아래층의 진행 상태를 알아야 할 때 신호 규칙을 미리 정할 것</dd><dt>출처</dt><dd><a href="02-brain.html#상태-기계-fsm">2장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>배열 중복 가중치</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>확률 숫자는 기획자가 읽고 고치기 어렵다</dd><dt>핵심 아이디어</dt><dd>후보 배열에 같은 값을 여러 번 넣어 가중치를 표현한다. {신사, 신사, 신사, 혼자×7}</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC 산책 목적지 [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>성격 열쇠 표</dd><dt>주의점</dt><dd>후보가 많아지면 배열이 길어짐. 그때는 (값, 가중치) 표로 바꿀 것</dd><dt>출처</dt><dd><a href="02-brain.html#utility-ai">2장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>반응 곡선 Utility + 관성</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>참/거짓 조건으로는 '얼마나 급한가'를 비교할 수 없다</dd><dt>핵심 아이디어</dt><dd>욕구를 곡선으로 0~1 점수로 바꿔 곱하고, 하던 행동에 작은 보너스를 줘서 결정이 깜빡이지 않게 한다</dd><dt>쓰인 게임</dt><dd>심즈 [공식], Dave Mark·Kevin Dill GDC 2010 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>스마트 오브젝트 광고, 일정 블록</dd><dt>주의점</dt><dd>점수 디버그 화면 없이는 조율이 불가능에 가까움</dd><dt>출처</dt><dd><a href="02-brain.html#utility-ai">2장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>스마트 오브젝트 광고</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>NPC 쪽에 모든 행동을 넣으면 물건이 늘 때마다 NPC 코드를 고쳐야 한다</dd><dt>핵심 아이디어</dt><dd>오브젝트가 '나는 어떤 욕구를 얼마나 채운다'를 광고하고 실행 절차도 들고 있다. 성격에 따라 광고 값이 바뀌고 거리에 따라 약해진다</dd><dt>쓰인 게임</dt><dd>심즈 1 (변기: 방광 0~70, 어항: 장난기 따라 재미 1~11) [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>반응 곡선 Utility</dd><dt>주의점</dt><dd>모든 NPC가 모든 오브젝트를 매번 평가하면 비쌈: 근처만, 몇 초에 한 번</dd><dt>출처</dt><dd><a href="02-brain.html#스마트-오브젝트">2장</a></dd></dl>
</div>

## 일상
<div class="card" markdown="0">
<h3>일정 블록 + 욕구 끼어들기</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>시간표만 있으면 기계 같고, 욕구만 있으면 생활 리듬이 없다</dd><dt>핵심 아이디어</dt><dd>시간표가 '지금 허용된 행동 후보'를 정하고, 그 안에서 욕구 점수로 고른다. 욕구가 임계값 아래로 떨어지면 일정을 무시한다</dd><dt>쓰인 게임</dt><dd>스타듀(일정) + 심즈(욕구)의 혼합 [추정]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>층 나눈 상태 기계, 반응 곡선 Utility</dd><dt>주의점</dt><dd>끼어들기가 잦으면 일정이 무의미해짐: 임계값을 낮게</dd><dt>출처</dt><dd><a href="03-routine.html">3장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>조건 키 일정</h3>
<dl><dt>목표</dt><dd>{실존감} {관계}</dd><dt>해결하는 문제</dt><dd>NPC가 계절·요일·날씨·관계에 따라 다른 하루를 보내야 한다</dd><dt>핵심 아이디어</dt><dd>'spring_Mon', '11_6', 'rain' 같은 키를 정해진 순서로 맞춰 보고 첫 일치를 쓴다. GOTO로 재사용</dd><dt>쓰인 게임</dt><dd>스타듀 밸리 [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>성격 열쇠 표</dd><dt>주의점</dt><dd>키 순서 규칙을 문서로 남기지 않으면 작가가 헷갈림</dd><dt>출처</dt><dd><a href="03-routine.html">3장</a></dd></dl>
</div>

## 성격
<div class="card" markdown="0">
<h3>성격 열쇠 표</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>적은 데이터로 확실히 다른 NPC들을 만들어야 한다</dd><dt>핵심 아이디어</dt><dd>성격 값 하나가 일정, 선택 가중치, 임계값, 대사 구간, 인사 동작을 동시에 정한다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC (성격 1바이트) [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>배열 중복 가중치, 빈칸 대사 틀</dd><dt>주의점</dt><dd>같은 성격끼리는 비슷함: 기억·말버릇·옷 같은 '살면서 바뀌는 값'으로 개인차를</dd><dt>출처</dt><dd><a href="04-personality.html">4장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>성격 위반 스트레스</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>플레이어가 캐릭터의 성격을 무시하고 최적 행동만 한다</dd><dt>핵심 아이디어</dt><dd>성격에 어긋나는 선택에 스트레스를 매기고, 쌓이면 성격에 맞는 붕괴 사건이 일어난다</dd><dt>쓰인 게임</dt><dd>크루세이더 킹즈 3 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>이유 하나 고르기, 기한부 생각</dd><dt>주의점</dt><dd>벌만 있으면 짜증남: 스트레스를 푸는 행동도 같이</dd><dt>출처</dt><dd><a href="04-personality.html">4장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>성격 다양성 보정</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>무작위로 NPC를 뽑으면 한 성격으로 쏠릴 수 있다</dd><dt>핵심 아이디어</dt><dd>새 NPC를 뽑을 때 지금 가장 적은 성격(동점이면 적은 성별)에서 고른다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC 새 주민 [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>성격 열쇠 표</dd><dt>주의점</dt><dd>플레이어가 원하는 NPC를 고르는 게임이면 맞지 않음</dd><dt>출처</dt><dd><a href="09-world.html">9장</a></dd></dl>
</div>

## 기억
<div class="card" markdown="0">
<h3>칸 제한 기억 + 잊는 순서</h3>
<dl><dt>목표</dt><dd>{관계}</dd><dt>해결하는 문제</dt><dd>기억을 무한히 쌓으면 저장량과 검색 비용이 커진다</dd><dt>핵심 아이디어</dt><dd>사람·사건별 기억을 N칸으로 제한하고, 꽉 차면 '관계의 가치'가 낮은 기억부터 지운다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC (7칸: 외부인·편지 없음·낮은 친밀도·오래됨 순) [분석], 드워프 포트리스(단기 8·장기 8, 약한 것부터) [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>오랜만 인사, 인연 약한 쪽이 떠남</dd><dt>주의점</dt><dd>잊은 기억을 NPC가 말하면 버그처럼 보임: 대사는 항상 현재 칸에서</dd><dt>출처</dt><dd><a href="05-memory.html">5장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>오랜만 인사</h3>
<dl><dt>목표</dt><dd>{관계} {실존감}</dd><dt>해결하는 문제</dt><dd>NPC가 나를 알아보는 느낌을 싸게 만들고 싶다</dd><dt>핵심 아이디어</dt><dd>사람별 마지막 대화 시각을 저장하고 경과 시간(1일/14일/60일)으로 인사를 가른다. 몇 달 지났는지 대사에 넣는다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>칸 제한 기억, 빈칸 대사 틀</dd><dt>주의점</dt><dd>현실 시계를 쓰면 시간대·시계 조작 처리 필요</dd><dt>출처</dt><dd><a href="05-memory.html">5장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>기한부 생각</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>기분이 왜 이런지 플레이어가 알 수 없다</dd><dt>핵심 아이디어</dt><dd>사건이 '효과 + 남은 시간'을 가진 생각을 남기고, 생각의 합이 기분이 된다. 목록을 그대로 보여 준다</dd><dt>쓰인 게임</dt><dd>림월드 [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>이유 하나 고르기, 긴장 곡선 스토리텔러</dd><dt>주의점</dt><dd>같은 생각이 무한히 쌓이지 않게 종류별 상한</dd><dt>출처</dt><dd><a href="05-memory.html">5장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>기억 스트림 검색 점수</h3>
<dl><dt>목표</dt><dd>{관계} {실존감}</dd><dt>해결하는 문제</dt><dd>기억이 너무 많아 다 쓸 수 없다</dd><dt>핵심 아이디어</dt><dd>최근성·중요도·관련성을 각각 0~1로 정규화해 가중합하고 상위만 쓴다. 꺼내 본 기억은 다시 최근이 된다</dd><dt>쓰인 게임</dt><dd>Generative Agents [공식] (논문: 가중치 1·1·1, 감소 0.995 / 코드: 0.5·3·2, 0.99), AI Town [공식]</dd><dt>AI 필요 여부</dt><dd>선택 (관련성을 태그로 하면 불필요)</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>회고 요약, 사실 묶음 가드레일</dd><dt>주의점</dt><dd>논문과 공식 코드의 값이 다름: 어느 쪽을 쓸지 정할 것</dd><dt>출처</dt><dd><a href="05-memory.html">5장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>회고 요약</h3>
<dl><dt>목표</dt><dd>{관계}</dd><dt>해결하는 문제</dt><dd>관찰만 쌓이면 '이 사람은 어떤 사람인가' 같은 판단을 못 한다</dd><dt>핵심 아이디어</dt><dd>중요도 합이 임계값(150)을 넘으면 최근 기억으로 질문을 만들고, 근거를 인용한 통찰을 다시 기억에 넣는다</dd><dt>쓰인 게임</dt><dd>Generative Agents [공식]</dd><dt>AI 필요 여부</dt><dd>필요</dd><dt>구현 난이도</dt><dd>●●●●○ (4/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>기억 스트림 검색 점수</dd><dt>주의점</dt><dd>통찰이 사실과 다를 수 있음: 게임 규칙에는 쓰지 말고 표시·대사용으로</dd><dt>출처</dt><dd><a href="05-memory.html">5장</a></dd></dl>
</div>

## 관계
<div class="card" markdown="0">
<h3>속마음/공개 관계 분리</h3>
<dl><dt>목표</dt><dd>{관계} {개연성}</dd><dt>해결하는 문제</dt><dd>관계 수치 하나로는 '사귀지만 마음이 식은' 상태를 표현할 수 없다</dd><dt>핵심 아이디어</dt><dd>인물 사이의 한쪽 방향 수치(연애·우정·존중)와 모두가 아는 관계(친구·연인·적, 참/거짓)를 나누고, 관계는 사회적 교환으로만 바뀐다</dd><dt>쓰인 게임</dt><dd>Prom Week / Comme il Faut [공식], 스타듀 꽃다발(8하트에서 멈춤) [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●●○ (4/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>기한부 생각, 가장 구체적인 규칙 대사</dd><dt>주의점</dt><dd>교환 규칙 작성량이 많음</dd><dt>출처</dt><dd><a href="06-relationship.html">6장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>유행 전파</h3>
<dl><dt>목표</dt><dd>{소속감} {관계}</dd><dt>해결하는 문제</dt><dd>NPC끼리의 관계가 눈에 보이지 않는다</dd><dt>핵심 아이디어</dt><dd>NPC가 만나면 확률표로 말버릇·옷을 옮긴다. 플레이어와 친한 쪽이 주도하고, 플레이어가 아는 NPC 쪽으로 퍼진다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC [분석], 모여봐요(대화 목격으로 말버릇 옮김) [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>빈칸 대사 틀, 성격 열쇠 표</dd><dt>주의점</dt><dd>관계 수치만 바꾸고 보이는 결과가 없으면 무의미</dd><dt>출처</dt><dd><a href="06-relationship.html">6장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>인연 약한 쪽이 떠남</h3>
<dl><dt>목표</dt><dd>{관계} {소속감}</dd><dt>해결하는 문제</dt><dd>NPC가 바뀌어야 하지만 플레이어가 아끼는 NPC를 잃게 하고 싶지 않다</dd><dt>핵심 아이디어</dt><dd>떠날 NPC를 고를 때 플레이어와의 기억·편지가 적은 쪽, 같은 성격이 많은 쪽을 우선한다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>칸 제한 기억, 성격 다양성 보정</dd><dt>주의점</dt><dd>모여봐요처럼 플레이어에게 허락받는 방식도 고려</dd><dt>출처</dt><dd><a href="06-relationship.html">6장</a></dd></dl>
</div>

## 대화
<div class="card" markdown="0">
<h3>빈칸 대사 틀 + 대사 속 명령</h3>
<dl><dt>목표</dt><dd>{실존감} {관계}</dd><dt>해결하는 문제</dt><dd>인물마다 대사를 따로 쓰면 작성량이 폭발한다</dd><dt>핵심 아이디어</dt><dd>대사 틀은 공용으로, 이름·말버릇·물건은 빈칸으로. 표정·친밀도 변화 같은 명령을 대사 데이터 안에 넣어 작가가 코드 없이 관계를 설계한다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC 제어 코드 [분석], 스타듀 $h·$d [분석], Prom Week %greeting% [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>가장 구체적인 규칙 대사, 유행 전파</dd><dt>주의점</dt><dd>빈칸에 들어갈 값이 없을 때의 대체 문구를 꼭 정할 것</dd><dt>출처</dt><dd><a href="07-dialogue.html">7장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>가장 구체적인 규칙 대사</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>상황에 맞는 대사를 많이 쓰고 싶은데 if 문이 감당이 안 된다</dd><dt>핵심 아이디어</dt><dd>세계의 사실과 규칙의 조건을 맞춰 보고, 조건이 가장 많이 맞는 규칙의 대사를 쓴다. 덜 구체적인 규칙은 대체용</dd><dt>쓰인 게임</dt><dd>Valve (레프트 4 데드 2 등) [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>빈칸 대사 틀</dd><dt>주의점</dt><dd>규칙이 수백 개를 넘으면 '왜 이 대사가 골라졌나' 디버그 도구 필수</dd><dt>출처</dt><dd><a href="07-dialogue.html">7장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>말하는 AI, 보여주는 AI</h3>
<dl><dt>목표</dt><dd>{실존감} {개연성}</dd><dt>해결하는 문제</dt><dd>AI가 똑똑하게 행동해도 플레이어가 모른다</dd><dt>핵심 아이디어</dt><dd>AI가 내린 결정을 NPC끼리의 짧은 대화로 알린다. 'AI가 말하지 않았다면 일어나지 않은 것'</dd><dt>쓰인 게임</dt><dd>F.E.A.R. 분대 대화 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>이유 하나 고르기</dd><dt>주의점</dt><dd>말이 너무 많으면 소음이 됨</dd><dt>출처</dt><dd><a href="07-dialogue.html">7장</a></dd></dl>
</div>

## 사건
<div class="card" markdown="0">
<h3>이유 하나 고르기</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>사건이 무작위로 느껴진다</dd><dt>핵심 아이디어</dt><dd>사건에 영향을 준 원인들 중 하나를 강도에 비례해 골라 '○○ 때문에'라고 보여 준다</dd><dt>쓰인 게임</dt><dd>림월드 정신 붕괴 이유 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>기한부 생각, 원인 기록</dd><dt>주의점</dt><dd>원인 목록이 플레이어에게도 보여야 납득됨</dd><dt>출처</dt><dd><a href="08-events.html">8장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>긴장 곡선 스토리텔러</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>사건의 크기와 간격이 들쭉날쭉하다</dd><dt>핵심 아이디어</dt><dd>재산·인원·최근 피해로 위협 점수를 계산하고, 위협 → 휴식 → 조금 더 큰 위협의 순환으로 사건을 보낸다</dd><dt>쓰인 게임</dt><dd>림월드 카산드라 [분석], Façade 드라마 관리자 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>이유 하나 고르기, 원인 기록</dd><dt>주의점</dt><dd>곡선이 너무 규칙적이면 플레이어가 예측함: 약간의 무작위를</dd><dt>출처</dt><dd><a href="08-events.html">8장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>원인 기록 (연대기)</h3>
<dl><dt>목표</dt><dd>{개연성} {소속감}</dd><dt>해결하는 문제</dt><dd>사건이 다음 사건과 연결되지 않고, 나중에 이야기할 거리가 없다</dd><dt>핵심 아이디어</dt><dd>모든 사건을 {언제, 무엇, 누가, 누구에게, 원인}으로 기록하고 이벤트 조건·대사·소식에서 다시 쓴다</dd><dt>쓰인 게임</dt><dd>드워프 포트리스 전설 모드 [분석], Prom Week 사회적 사실 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>시뮬레이션 + 선별, 사실 묶음 가드레일</dd><dt>주의점</dt><dd>기록이 커지면 오래된 사소한 사건은 요약·삭제</dd><dt>출처</dt><dd><a href="08-events.html">8장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>시뮬레이션 + 선별</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>시뮬레이션 결과가 너무 많아 재미있는 것이 묻힌다</dd><dt>핵심 아이디어</dt><dd>많이 시뮬레이션하고, 흥미로운 사건만 골라 보여 준다. 결과가 플레이어가 아는 인물 쪽으로 흐르게 한다</dd><dt>쓰인 게임</dt><dd>Talk of the Town [공식], 동물의 숲 유행·이사 규칙 [분석]</dd><dt>AI 필요 여부</dt><dd>선택</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>원인 기록, 유행 전파</dd><dt>주의점</dt><dd>'흥미로움'의 기준을 정하는 것이 가장 어려움</dd><dt>출처</dt><dd><a href="01-intro.html">1장</a></dd></dl>
</div>

## 세계
<div class="card" markdown="0">
<h3>사건 먼저, 이유 나중</h3>
<dl><dt>목표</dt><dd>{개연성}</dd><dt>해결하는 문제</dt><dd>역사 시뮬레이션은 비싸다</dd><dt>핵심 아이디어</dt><dd>사건을 먼저 무작위로 뽑고, 나중에 그럴듯한 이유를 붙여 서술한다</dd><dt>쓰인 게임</dt><dd>Caves of Qud [공식]</dd><dt>AI 필요 여부</dt><dd>선택 (서술에 LLM 가능)</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>원인 기록</dd><dt>주의점</dt><dd>사건끼리 실제로 상호작용하지는 않음</dd><dt>출처</dt><dd><a href="09-world.html">9장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>AI LOD 좌표 산책</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>NPC가 많으면 모두를 정밀하게 시뮬레이션할 수 없다</dd><dt>핵심 아이디어</dt><dd>플레이어 근처만 진짜 캐릭터, 화면 밖은 좌표와 목적지만 몇 초에 한 칸씩. 가까워지면 화면 가장자리에서 걸어 들어오게 생성</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC (7초에 한 칸) [분석], 킹덤 컴 2 [공식]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>마지막 시각 계산</dd><dt>주의점</dt><dd>화면 밖 상태와 화면 안 상태가 어긋나지 않게(위치·소지품)</dd><dt>출처</dt><dd><a href="09-world.html">9장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>마지막 시각 계산</h3>
<dl><dt>목표</dt><dd>{실존감} {소속감}</dd><dt>해결하는 문제</dt><dd>게임을 끈 동안의 시간을 시뮬레이션할 수 없다</dd><dt>핵심 아이디어</dt><dd>마지막 시각만 저장하고 다시 켤 때 경과 시간으로 결과를 한 번에 계산해 흔적(바퀴벌레, 편지, 성장)으로 보여 준다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC 바퀴벌레(6일, 최대 10) [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●○○○○ (1/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>오랜만 인사, AI LOD</dd><dt>주의점</dt><dd>벌처럼 느껴지면 복귀를 망설이게 됨</dd><dt>출처</dt><dd><a href="09-world.html">9장</a></dd></dl>
</div>

## 소속감
<div class="card" markdown="0">
<h3>가꾸면 커지는 공동체</h3>
<dl><dt>목표</dt><dd>{소속감}</dd><dt>해결하는 문제</dt><dd>기여가 보상 아이템으로만 끝난다</dd><dt>핵심 아이디어</dt><dd>공동체 상태(마을 평가)가 공동체의 성장(새 주민 확률, 가게 영업일)으로 이어지게 하고, 그 원인을 말해 준다</dd><dt>쓰인 게임</dt><dd>동물의 숲 GC 마을 평가 → 입주 확률 40~100% [분석], 스타듀 마을회관 [분석]</dd><dt>AI 필요 여부</dt><dd>없음</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>유행 전파, 정기 행사</dd><dt>주의점</dt><dd>평가 기준을 알려 주지 않으면 운에 맡기는 느낌</dd><dt>출처</dt><dd><a href="10-belonging.html">10장</a></dd></dl>
</div>

## AI 결합
<div class="card" markdown="0">
<h3>규칙이 고르고 LLM이 말한다</h3>
<dl><dt>목표</dt><dd>{실존감}</dd><dt>해결하는 문제</dt><dd>LLM에게 결정을 맡기면 일관성·재현성·비용 문제가 생긴다</dd><dt>핵심 아이디어</dt><dd>행동·사건·관계 변화는 규칙 시스템이 정하고, LLM은 그 결정과 이유를 문장(속마음, 대사, 일기, 소식)으로만 바꾼다</dd><dt>쓰인 게임</dt><dd>이 가이드의 구현 스케치 / 인조이 발표 내용과 비슷한 방향 [추정]</dd><dt>AI 필요 여부</dt><dd>필요 (표현만)</dd><dt>구현 난이도</dt><dd>●●●○○ (3/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>사실 묶음 가드레일, 반응 곡선 Utility</dd><dt>주의점</dt><dd>LLM이 만든 문장이 결정과 어긋나지 않게 이유 점수를 같이 넘길 것</dd><dt>출처</dt><dd><a href="02-brain.html#섞어-쓰기">2장</a></dd></dl>
</div>
<div class="card" markdown="0">
<h3>사실 묶음 가드레일</h3>
<dl><dt>목표</dt><dd>{관계}</dd><dt>해결하는 문제</dt><dd>LLM이 세계에 없는 것을 말하거나 약속한다</dd><dt>핵심 아이디어</dt><dd>필요한 사실만 묶어 주고 '이 사실만 사용'을 지시한 뒤, 출력에 묶음 밖의 고유명사·숫자·약속이 있으면 버리고 미리 쓴 대사로 바꾼다</dd><dt>쓰인 게임</dt><dd>AI Town (중요도 파싱 실패 시 5) [공식]</dd><dt>AI 필요 여부</dt><dd>필요</dd><dt>구현 난이도</dt><dd>●●○○○ (2/5)</dd><dt>함께 쓰면 좋은 패턴</dt><dd>규칙이 고르고 LLM이 말한다, 빈칸 대사 틀</dd><dt>주의점</dt><dd>검사가 너무 엄격하면 거의 다 버려짐: 대체 대사 품질이 중요</dd><dt>출처</dt><dd><a href="07-dialogue.html">7장</a></dd></dl>
</div>

## 출처

각 카드의 근거와 원문 링크는 카드의 "출처" 칸에 적힌 장에 있습니다. 주요 원자료는 다음과 같습니다.

- ACreTeam, ac-decomp — <https://github.com/ACreTeam/ac-decomp>
- Forbus & Wright, "Some notes on programming objects in The Sims" (2001) — <https://qrg.northwestern.edu/papers/Files/Programming_Objects_in_The_Sims.pdf>
- Stardew Valley Wiki, Modding:Schedule data — <https://stardewvalleywiki.com/Modding:Schedule_data>
- RimWorld Wiki, Mood — <https://rimworldwiki.com/wiki/Mood>
- Park 외, "Generative Agents" — <https://arxiv.org/abs/2304.03442>
- Mateas & McCoy, Game AI Pro 1권 43장 — <https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter43_An_Architecture_for_Character-Rich_Social_Simulation.pdf>
- Elan Ruskin, GDC 2012 — <https://gdcvault.com/play/1015317/AI-driven-Dynamic-Dialog-through>
- 전체 목록 — [15장](15-references.html)
