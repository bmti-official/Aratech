# 프롬프트 템플릿

`{{ }}` 부분만 채워서 해당 에이전트에 붙여 넣는다. 모든 템플릿은 저장소의 `AGENTS.md`를 따른다는 전제로 쓰였다.
Claude는 claude.ai의 **Aratech 프로젝트**(지침서 PDF를 프로젝트 지식에 올려 둔 곳)에서 쓴다.

## 가설 검증 (7일 사이클)

| 순서 | 파일 | 에이전트 | 결과물 |
|---|---|---|---|
| 1 | `01-hypothesis-card.md` | Claude | `hypothesis.json` 가설 카드 |
| 2 | `02-evidence.md` | Antigravity | `sources.json` 근거 |
| 3 | `03-calc.md` | Codex | `calc.json`, `work/calc/` |
| 4 | `04-synthesis.md` | Claude | 사이트 데이터 반영 PR |
| 5 | `05-review.md` | **새** Claude 대화 | 검수 의견 |
| 6 | `06-approval.md` | 사람 | PR 승인(merge) |

검수에서 문제가 나오면 4단계로 돌아간다.

## 그 밖의 작업

| 파일 | 용도 |
|---|---|
| `archive-scheduled.md` | **예약 작업**이 매주 월·목 오전 6:15에 읽는 조사 아카이브 자동 수집 지시 |
| `archive-post.md` | 조사·비교 아카이브 포스트를 사람이 직접 요청할 때 (Antigravity → Codex → Claude) |
| `meeting.md` | 주간 회의 요약 반영 |
| `verdict.md` | 7일차 판정과 회고 |
| `bigplan/1-question.md` → `3-lens.md` → `4-rebuttal.md` → `5-synthesis.md` | 대형 기획 3개 관점 분석 (근거 팩은 1에 안내) |
