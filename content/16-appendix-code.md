---
title: 부록 A — Unity C# 공통 뼈대 코드
nav: 부록 A. 공통 뼈대 코드
eyebrow: 부록
summary: 2~10장의 구현 스케치가 공통으로 기대는 부품(게임 시계, 욕구, 사건 버스, 판단 예산, 저장)을 한곳에 모았다. 각 장의 코드는 이 부품들이 있다고 가정한다.
goals: 실존감
---

## 이 부록의 원칙

- **엔진과 무관한 부분은 순수 C#**으로 씁니다. 테스트하기 쉽고, 나중에 다른 엔진으로 옮기기도 쉽습니다.
- **Unity에 기대는 부분**(MonoBehaviour, ScriptableObject, Time, Vector)은 파일 맨 위에 `// [Unity 의존]`이라고 표시했습니다.
- 데이터(성격, 일정, 대사, 사건)는 **코드 밖**에 둡니다. Unity에서는 ScriptableObject가 가장 손쉽고, 작가가 많이 쓸 데이터(대사)는 CSV·JSON이 편합니다.

## 추천 폴더 구조

```
Assets/
  Scripts/
    Core/        GameClock, EventBus, ThinkScheduler, SaveSystem   (대부분 순수 C#)
    Npc/         Npc, NeedSet, Personality, MemorySlots, SocialState
    Brain/       UtilityAction, Behavior Tree 노드, GOAP, Schedule
    World/       NpcLodManager, Catchup, Chronicle, TownRating
    Dialogue/    DialogueRule, DialoguePicker, Template
    AI/          (선택) LLM 클라이언트, Guard(출력 검사)
  Data/
    Personalities/   *.asset  (ScriptableObject)
    Schedules/       *.asset
    Dialogue/        *.csv
```

## 게임 시계

```csharp
// 게임 시간을 실제 시간과 분리한다. 하루가 바뀌는 순간 이벤트를 쏜다. [Unity 의존: MonoBehaviour, Time]
using UnityEngine;

public class GameClock : MonoBehaviour
{
    public static GameClock I { get; private set; }
    public float RealSecondsPerGameMinute = 0.7f;     // 스타듀처럼 빠르게, 또는 동숲처럼 1:1(=60)
    public int Day { get; private set; }
    public int MinuteOfDay { get; private set; } = 6 * 60;
    public static int NowSecondOfDay => I.MinuteOfDay * 60;

    public event System.Action<int> OnMinute;         // 분이 바뀔 때
    public event System.Action<int> OnNewDay;         // 날이 바뀔 때 (회고·일정 다시 고르기에 사용)

    float acc;
    void Awake() => I = this;

    void Update()
    {
        acc += Time.deltaTime;
        while (acc >= RealSecondsPerGameMinute)
        {
            acc -= RealSecondsPerGameMinute;
            MinuteOfDay++;
            if (MinuteOfDay >= 24 * 60) { MinuteOfDay = 0; Day++; OnNewDay?.Invoke(Day); }
            OnMinute?.Invoke(MinuteOfDay);
        }
    }
}
```

## 욕구 묶음

```csharp
// 욕구 이름 → 0~1 값. 시간이 지나면 줄어든다. (순수 C#)
using System.Collections.Generic;

[System.Serializable]
public class NeedSet
{
    readonly Dictionary<string, float> values = new();
    readonly Dictionary<string, float> decayPerHour = new();

    public void Define(string need, float start, float decay) { values[need] = start; decayPerHour[need] = decay; }
    public float Get(string need) => values.TryGetValue(need, out var v) ? v : 1f;
    public void Add(string need, float delta) => values[need] = System.Math.Clamp(Get(need) + delta, 0f, 1f);

    public void Decay(float gameHours)
    {
        foreach (var k in new List<string>(values.Keys)) Add(k, -decayPerHour[k] * gameHours);
    }

    // 낮을수록 급함. 곡선은 UtilityAction 쪽에서 바꾼다
    public float Urgency(string need) => 1f - Get(need);

    public float Lowest()
    {
        float m = 1f;
        foreach (var v in values.Values) if (v < m) m = v;
        return m;
    }
}
```

## 사건 버스

```csharp
// 시스템끼리 직접 참조하지 않고 사건으로 통신한다. 사건은 연대기(8장)에도 그대로 기록된다. (순수 C#)
using System;
using System.Collections.Generic;

public record GameEvent(string Type, string Actor, string Target, int Intensity, string CauseId = null);

public static class EventBus
{
    static readonly Dictionary<string, List<Action<GameEvent>>> handlers = new();

    public static void On(string type, Action<GameEvent> h)
    {
        if (!handlers.TryGetValue(type, out var list)) handlers[type] = list = new List<Action<GameEvent>>();
        list.Add(h);
    }

    public static void Emit(GameEvent e)
    {
        Chronicle.Instance.Add(e);                              // 모든 사건은 기록된다
        if (handlers.TryGetValue(e.Type, out var list))
            foreach (var h in list.ToArray()) h(e);
        if (handlers.TryGetValue("*", out var all))
            foreach (var h in all.ToArray()) h(e);
    }
}
// 예: EventBus.On("gift", e => npcs[e.Target].Memory.Remember(e));   선물을 받은 NPC가 기억한다
//     EventBus.On("insult", e => social.AddFeel(e.Target, e.Actor, Network.Friendship, -5));
```

## 판단 예산 (시간 나누기)

NPC가 많으면 모든 NPC가 매 프레임 판단하지 않도록 **한 프레임에 판단할 수를 제한**합니다. 동숲의 "7초에 한 칸"([9장](09-world.html))과 같은 생각입니다.

```csharp
// 등록된 NPC들을 돌아가며 한 프레임에 N명만 판단시킨다. [Unity 의존: MonoBehaviour]
using System.Collections.Generic;
using UnityEngine;

public interface IThinker { void Think(); bool IsNearPlayer { get; } }

public class ThinkScheduler : MonoBehaviour
{
    public int ThinksPerFrameNear = 8;     // 플레이어 근처 NPC
    public int ThinksPerFrameFar = 2;      // 화면 밖 NPC (AI LOD)
    readonly List<IThinker> near = new(), far = new();
    int iNear, iFar;

    public void Register(IThinker t) => (t.IsNearPlayer ? near : far).Add(t);

    void Update()
    {
        Rebucket();
        Run(near, ref iNear, ThinksPerFrameNear);
        Run(far, ref iFar, ThinksPerFrameFar);
    }

    static void Run(List<IThinker> list, ref int index, int budget)
    {
        for (int n = 0; n < budget && list.Count > 0; n++)
        {
            index %= list.Count;
            list[index++].Think();
        }
    }

    void Rebucket()
    {
        for (int i = near.Count - 1; i >= 0; i--) if (!near[i].IsNearPlayer) { far.Add(near[i]); near.RemoveAt(i); }
        for (int i = far.Count - 1; i >= 0; i--) if (far[i].IsNearPlayer) { near.Add(far[i]); far.RemoveAt(i); }
    }
}
```

## 저장과 재현

```csharp
// 저장할 것: 무작위 시드, 마지막 시각들, 기억·관계·연대기, (LLM을 쓴다면) 생성된 문장. (순수 C#)
[System.Serializable]
public class SaveData
{
    public int Seed;                         // 같은 시드 + 같은 입력 = 같은 결과
    public long LastPlayedUnix;              // 9장: 마지막 시각 계산
    public long LastHomeVisitUnix;
    public int Roaches;
    public System.Collections.Generic.List<NpcSave> Npcs = new();
    public System.Collections.Generic.List<GameEvent> Chronicle = new();
    public System.Collections.Generic.Dictionary<string, string> GeneratedLines = new();   // LLM 출력 캐시: 로드 때 다시 생성하지 않는다
}

public static class Rng
{
    static System.Random r;
    public static void Init(int seed) => r = new System.Random(seed);
    public static int Next(int max) => r.Next(max);
    public static double Value() => r.NextDouble();
}
// 주의: UnityEngine.Random과 System.Random을 섞어 쓰면 재현성이 깨진다. 시뮬레이션에는 한쪽만 쓰자.
```

## 디버그 화면

[2장](02-brain.html)에서 말했듯 Utility나 기억 검색은 **점수가 보여야** 조율할 수 있습니다. 선택한 NPC의 다음 정보를 화면에 띄우세요.

- 현재 일정 블록과 상태(1층·2층·3층)
- 행동 후보별 점수와 고른 행동
- 욕구 값, 기분과 그 원인(생각 목록)
- 기억 칸, 관계 수치(속마음·공개 관계)
- 최근 사건 기록 10개

```csharp
// 간단한 IMGUI 디버그 창 [Unity 의존: OnGUI]
void OnGUI()
{
    if (selected == null) return;
    GUILayout.BeginArea(new Rect(10, 10, 360, 600), GUI.skin.box);
    GUILayout.Label($"{selected.Name}  [{selected.Personality.name}]  일정: {selected.CurrentBlock}");
    foreach (var (action, score) in selected.LastScores) GUILayout.Label($"{score:0.00}  {action}");
    GUILayout.Label("욕구: " + string.Join(", ", selected.Needs.Debug()));
    GUILayout.Label("기억: " + string.Join(" / ", selected.Memory.Debug()));
    GUILayout.EndArea();
}
```

## 출처

- 이 부록의 구조는 앞 장들의 사례에서 공통 부분을 뽑은 것입니다: 시간 나누기와 화면 밖 간략화는 동물의 숲 GC([ac-decomp](https://github.com/ACreTeam/ac-decomp) `src/actor/ac_set_npc_manager.c`), 점수 디버그의 필요성은 Utility 자료([Game AI Pro 1권 9장](https://www.gameaipro.com/GameAIPro/GameAIPro_Chapter09_An_Introduction_to_Utility_Theory.pdf)), 사건 기록은 [8장](08-events.html)의 사례에서 왔습니다.
