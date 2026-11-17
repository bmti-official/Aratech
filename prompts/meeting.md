# 주간 회의 요약 반영

## 회의 전 (Claude)

```
{{날짜}} {{시간}} 정기 회의 카드를 만들어 줘.
meetings.json의 meetings에 들어갈 항목으로, summary·decisions는 비워 두고
지난 회의의 actions를 가져와 status(완료/진행/지연)를 점검할 수 있게 넣어 줘.
안건 초안: {{안건}}
```

## 녹음 요약 (Gemini 앱, 활동 기록 끔)

- 팀 내부 회의만. 파일은 100MB 이하로 변환하거나 1시간씩 나눠 올린다.
- 요약 결과는 개인 메모로만 쓰고 저장소에 올리지 않는다.

## 회의 직후 (Claude)

```
아래 녹음 요약과 내가 대조한 메모로 회의 기록을 만들어 줘.
[녹음 요약] {{붙여 넣기}}
[사람 메모] {{붙여 넣기}}

1. 전체 회의록: 주제별 목차, 이름은 역할로. → 내가 제한된 구글 독스에 붙여 넣을 것
2. meetings.json 항목: summary(한 줄), decisions, actions(task·owner_role·due·status),
   changes(일정·숫자 변경), open_questions, full_minutes_url은 {{구글 독스 링크}}
3. 이번 주 회의를 합친 weekly_summary 한두 문장
사이트용 JSON에는 실명·개인정보·수익 숫자 전체를 넣지 마.
```

이후 PR → 05 검수 → 06 승인.
