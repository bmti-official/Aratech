# 03 계산·그래프 — 계산 서브에이전트

```
이 저장소의 AGENTS.md를 먼저 읽고 따라 줘.

[작업]
site/data/sources.json의 근거를 바탕으로 calc.json 입력값을 정하고 계산해 줘.

[입력값 규칙]
- N: sources.json에 A/B 근거가 있으면 그 값을 넣고 source_id를 단다. 없으면 null 유지
- P, M: 사업 총괄이 고른 값 {{P=  , M=  }} (비어 있으면 recommendations의 C안 유지)
- c, CAC, VC, FC, k: 측정 전이면 grade "C" 유지
- 근거 없는 숫자를 새로 만들지 않는다

[계산]
python3 scripts/calc.py 실행. 결과(R, Reach, BEP, LTV, LTV/CAC, c ±50% 3개 시나리오)를
work/calc/cycle{{번호}}.md에 표로 저장한다. LTV/CAC 3배는 업계 경험칙(B) 점검선으로만 표시한다.

[그래프가 필요하면]
work/calc/ 아래에 PNG로 저장. 사이트에는 넣지 않는다 (사이트 그래프는 데이터에서 자동으로 그림).

[끝나면]
바꿀 calc.json 입력값을 work/calc/cycle{{번호}}.md 맨 위에 적고 메인에게 보고한다. 커밋·push하지 않는다.
calc.json의 status는 사람이 PR로 승인하기 전까지 "example" 또는 "draft".
```
