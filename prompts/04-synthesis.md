# 04 글·도식 종합 — Claude

```
사이클 {{번호}}의 재료를 사이트 데이터로 종합해 줘.

[재료] (파일 내용을 붙여 넣거나 저장소를 열어서)
- 가설 카드 초안: {{01 결과}}
- 근거: site/data/sources.json, work/evidence/cycle{{번호}}.md
- 계산: work/calc/cycle{{번호}}.md

[해 줄 것]
1. hypothesis.json 갱신: card 각 칸의 value와 grade, next_steps, start_conditions의 done
2. 근거와 가설 카드가 서로 맞는지 점검 (예: 반증 기준이 계산 결과와 모순되지 않는지)
3. 사실과 해석을 나눠서, 사람이 판단할 때 볼 요약 5줄
4. 사업 총괄이 정해야 할 것 3가지

[규칙]
- 사이트에 나가는 것은 site/data/ 뿐. 익명 통계와 검수 가능한 결론만
- 등급이 없는 숫자는 쓰지 않는다. C는 C로 표시
- 이름 대신 역할

[출력]
변경할 JSON 전체 + 요약. 저장소에서 작업 중이면 브랜치 cycle{{번호}}/synthesis로 PR.
```
