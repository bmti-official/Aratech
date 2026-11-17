# Aratech

가설 검증, 조사 아카이브, 대형 기획을 한 양식으로 쌓는 작업 사이트와 에이전트 작업 공간.

- 사이트: `site/` (GitHub Pages로 자동 배포)
- 사이트 데이터: `site/data/*.json` — 에이전트는 이 파일만 고친다
- 에이전트 규칙: [`AGENTS.md`](AGENTS.md)
- 단계별 지시문: [`prompts/`](prompts/README.md)
- 데이터 형식: [`docs/schema.md`](docs/schema.md)

## 작업 흐름

1. 에이전트가 브랜치에서 `site/data/` 또는 `work/`를 고치고 PR을 연다.
2. PR마다 `check-data` 검사가 자동으로 돈다 (등급, 날짜, 개인정보 패턴).
3. 새 Claude 대화로 검수한다 (`prompts/05-review.md`).
4. 사업 총괄·멘토가 PR을 승인(Merge)하면 몇 분 뒤 사이트에 반영된다.

## 내 컴퓨터에서 미리 보기

`index.html`을 더블클릭으로 열면 데이터 파일을 못 읽는다. 저장소 폴더에서:

```bash
python3 -m http.server 8000 -d site
```

그다음 브라우저에서 http://localhost:8000 을 연다.

## 검사와 계산

```bash
python3 scripts/check_data.py
python3 scripts/calc.py
```

## 공개 범위

이 저장소가 공개(public)이면 `AGENTS.md`, `prompts/`, `work/`까지 누구나 볼 수 있다.
수익 숫자 전체, 독점 전략, 인터뷰 원본, 전체 회의록은 저장소에 넣지 않고 권한을 제한한 구글 독스에 둔다.
