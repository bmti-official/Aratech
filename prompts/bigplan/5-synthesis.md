# 대형 기획 5 종합 — Claude / 6 사람 결정

## 5 종합

```
work/bigplan/{{날짜}}/의 question, evidence, lens-3개, rebuttal-3개를 종합해 줘.

[한 페이지 요약]
- 결론 3줄
- 렌즈 간 합의
- 렌즈 간 충돌과 각 쪽 근거
- 핵심 숫자 (등급 포함, C는 C로)
- 사업 총괄이 정할 결정 3가지 (각각 선택지 2~3개와 trade-off)

[부록]
렌즈별 분석 원문, 교차 반박, 근거 목록(출처와 등급)

전체는 제한 문서(구글 독스)에 붙여 넣을 마크다운으로.
그리고 사이트용으로 plan.json conclusions에 넣을 항목 하나를 따로:
question, conclusion(한 줄), decisions(사람이 정한 뒤 채움), restricted_url(빈 값)
```

## 6 사람 결정

1. 제한 문서에서 한 페이지 요약을 읽고 결정 3가지와 공개 범위를 정한다.
2. 정한 결정과 구글 독스 링크를 Claude에게 주고 `plan.json`의 `conclusions`를 채워 PR을 받는다.
3. 05 검수 → 06 승인. 사이트에는 결론 한 줄과 링크만 나간다.
