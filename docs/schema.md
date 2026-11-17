# 데이터 파일 형식 (`site/data/`)

모든 파일 공통: 맨 위에 `"updated": "YYYY-MM-DD"`. 날짜는 모두 `YYYY-MM-DD`. 등급은 `"A" | "B" | "C" | null`.
변경 후에는 `python3 scripts/check_data.py`로 검사한다.

## hypothesis.json

```jsonc
{
  "updated": "2026-11-17",
  "cycle": {
    "no": 1,                       // 사이클 번호
    "title": "물리치료사 AI 임상 비서 교육",
    "status": "시작 전",           // 시작 전 | 진행 중 | 판정 완료
    "start_date": null,            // 시작일 (YYYY-MM-DD)
    "current_day": 0,              // 0~7
    "ladder_stage": 1              // 검증 사다리 1(인터뷰) 2(랜딩) 3(소규모 비교)
  },
  "card": [                        // 가설 카드 칸. value가 null이면 placeholder가 흐리게 보임
    { "key": "가설 한 줄", "value": "…", "grade": "C" },
    { "key": "반증 기준", "value": null, "placeholder": "K%p 미만이면 기각 · 숫자 미정" }
  ],
  "verdict": null,                 // null | 유지 | 수정 | 중단
  "start_conditions": [ { "text": "…", "done": false } ],
  "next_steps":       [ { "text": "…", "done": false } ],
  "timing": [ { "code": "M", "name": "동기·결핍", "meaning": "…", "signals": "…", "value": null } ],
  "history": [                     // 판정이 끝난 사이클
    {
      "cycle": 1, "title": "…", "period": "2026-12-01 ~ 2026-12-07",
      "verdict": "수정",            // 유지 | 수정 | 중단
      "threshold": "+5%p",         // 반증 기준
      "measured": "+2%p (C, n=40)",// 실측치, 등급과 표본 수
      "signal": "판단 불가",        // 지지 신호 | 반대 신호 | 판단 불가
      "learned": "…"
    }
  ]
}
```

## sources.json

```jsonc
{
  "updated": "…",
  "items": [
    {
      "id": "S007",               // S + 3자리, 중복 금지
      "title": "국내 물리치료사 면허 등록 인원",
      "used_in": "수익 계산 N",    // 어디에 쓰이는 근거인지
      "grade": "A",
      "source": "보건복지부 통계 (기관명 · 자료명)",
      "url": "https://…",         // 없으면 null
      "checked": "2026-11-20"     // 확인일. 90일이 지나면 재확인 필요 표시
    }
  ]
}
```

## calc.json

```jsonc
{
  "updated": "…",
  "status": "example",            // example(예시 값) | draft(실제 값, 승인 전) | approved
  "status_note": "…",
  "inputs": [
    { "key": "N", "name": "대상 시장 인원", "unit": "명", "value": null, "step": 100, "grade": null, "note": "미확인 · …", "source_id": "S007" },
    { "key": "P", "name": "교육 가격", "unit": "원", "value": 290000, "step": 10000, "grade": "C", "recommend": true }
    // key는 N, P, M, c(%), CAC, VC, FC, k 로 고정
  ],
  "recommendations": {
    "P": { "title": "…", "sub": "…", "options": [
      { "id": "A", "lens": "틸 관점", "value": 390000, "why": "…", "risk": "이 값이 틀렸을 때의 손실", "grade": "C" }
      // A 틸, B 게이츠, C 절충. 정확히 3개
    ]},
    "M": { … }
  }
}
```

공개 범위 주의: `status`가 `approved`인 수익 숫자 전체는 제한 문서에 두는 것이 원칙이다. 사이트에 올릴지 사업 총괄에게 먼저 묻는다.

## meetings.json

```jsonc
{
  "updated": "…",
  "events": [
    { "date": "2026-11-17", "title": "지침서 확정", "badge": "지", "color": "blue" },
    { "date": null, "title": "가설 사이클 시작일", "note": "미정 · …", "badge": "!", "color": "warn" }
    // color: blue | pink | green | yellow | peach | cream | warn
  ],
  "weekly_summary": null,         // 그 주 회의를 합친 요약 한두 문장 (홈에 표시)
  "meetings": [
    {
      "date": "2026-11-24", "time": "10:00", "title": "정기 회의",
      "roles": ["사업 총괄", "멘토", "기록 담당"],   // 이름 금지, 역할만
      "cycle": 1,
      "summary": "한 줄 요약",
      "decisions": ["…"],
      "actions": [ { "task": "…", "owner_role": "사업 총괄", "due": "2026-11-28", "status": "진행" } ],  // 완료 | 진행 | 지연
      "changes": ["일정·숫자 변경"],
      "open_questions": ["…"],
      "full_minutes_url": "https://docs.google.com/…"   // 권한을 제한한 구글 독스 링크
    }
  ]
}
```

## posts.json

```jsonc
{
  "updated": "…",
  "posts": [
    {
      "id": "P001",
      "title": "…",
      "type": "경쟁사",            // 경쟁사 | 유사 모델 | 벤치마크 | 시장 동향
      "conclusion": "우리에게 의미하는 바 한 줄",
      "compare": [                 // 비교표. 열 이름은 자유, 아래 순서 권장
        { "대상": "…", "사업 형태": "…", "고객": "…", "수익 모델": "…", "가격대": "…", "핵심 자산": "…", "규모 지표": "…", "출처 등급": "B" }
      ],
      "facts": [ { "text": "출처로 확인된 사실", "grade": "A" } ],
      "interpretation": ["에이전트의 해석"],
      "implications": ["적용할 점 / 적용하지 않을 점"],   // 최대 3개
      "sources": [ { "title": "…", "url": "https://…", "grade": "B", "checked": "2026-11-20" } ],
      "tags": ["교육", "국내", "사이클1"],
      "approved_at": "2026-11-25"
    }
  ]
}
```

## plan.json

```jsonc
{
  "updated": "…",
  "packs": [ { "id": "A", "title": "…", "status": "대기", "blocker": "입력값 필요" } ],
  "conclusions": [
    {
      "date": "2026-12-10",
      "question": "질문 한 줄",
      "conclusion": "검수한 결론 한 줄",
      "decisions": ["사람이 정한 결정 1", "결정 2", "결정 3"],
      "restricted_url": "https://docs.google.com/…"   // 전체 분석 (제한 문서)
    }
  ]
}
```
