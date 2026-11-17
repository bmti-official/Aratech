# 프롬프트 템플릿

사람은 이 파일들을 직접 붙여 넣지 않는다. **메인 에이전트**(Claude Code 세션)에게 무엇을 할지 말하면, 메인이 `{{ }}`를 채워 Gemini나 Claude 서브에이전트에게 맡기거나 직접 쓴다. 누가 무엇을 하는지는 `AGENTS.md` §4.
규칙은 저장소의 `AGENTS.md`를 따른다. 무엇을 PR로 올리고 무엇을 바로 올리는지는 `AGENTS.md` §3.

## 가설 검증 (7일 사이클)

| 순서 | 파일 | 누가 | 결과물 | 올리는 방법 |
|---|---|---|---|---|
| 1 | `01-hypothesis-card.md` | 메인 | `hypothesis.json` 가설 카드 | 확정 시 PR |
| 2 | `02-evidence.md` | Gemini | `work/evidence/` → 메인이 `sources.json` 반영 | 바로 |
| 3 | `03-calc.md` | 메인 | `work/calc/` → 메인이 `calc.json` 반영 | 바로 (P·M 확정은 PR) |
| 4 | `04-synthesis.md` | 메인 | 사이트 데이터 반영 | 카드 변경은 PR, 나머지 바로 |
| 5 | `05-review.md` | 새 검수 서브에이전트 | 검수 의견 | PR 건과 포스트에 필수 |
| 6 | `06-approval.md` | 사람 | PR 승인(merge) | — |

검수에서 문제가 나오면 메인이 4단계로 돌아간다.

## 그 밖의 작업

| 파일 | 용도 |
|---|---|
| `archive-post.md` | 조사·비교 아카이브 포스트 (Gemini → 메인 → 검수 → 바로 올림) |
| `meeting.md` | 주간 회의 요약 반영 (바로 올림) |
| `verdict.md` | 7일차 판정과 회고 (PR) |
| `bigplan/1-question.md` → `3-lens.md` → `4-rebuttal.md` → `5-synthesis.md` | 대형 기획 3개 관점 분석. 틸은 Claude, 게이츠·저커버그는 Gemini가 따로. 결론은 PR |
