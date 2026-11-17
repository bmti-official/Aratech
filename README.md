# Aratech

가설 검증, 조사 아카이브, 대형 기획을 한 양식으로 쌓는 작업 사이트와 에이전트 작업 공간.

- 사이트: `site/` (GitHub Pages로 자동 배포)
- 사이트 데이터: `site/data/*.json` — 에이전트는 이 파일만 고친다
- 에이전트 규칙: [`AGENTS.md`](AGENTS.md)
- 단계별 지시문: [`prompts/`](prompts/README.md)
- 데이터 형식: [`docs/schema.md`](docs/schema.md)
- 처음 설정: [`docs/setup-guide.md`](docs/setup-guide.md)

## 작업 흐름

사람은 메인 에이전트(Claude Code 세션)와만 대화한다. 메인이 서브에이전트(근거·계산·렌즈·검수)를 띄워 일을 나눈다.

1. **대부분의 변경**(근거, 일정, 회의 요약, 체크 표시, `work/`)은 메인이 검사(`check_data.py` 오류 0건) 후 `main`에 바로 올린다. 몇 분 뒤 사이트에 반영된다.
2. **사업 핵심 변경**(가설 카드 확정, 판정, 가격·인원 확정, 대형 기획 결론, 규칙 변경)만 검수 서브에이전트를 거쳐 PR로 올라온다. 사업 총괄·멘토가 승인(Merge)해야 반영된다.
3. 검사(`check-data`)는 PR과 `main` push 때마다 자동으로 돈다. 오류가 있으면 사이트 배포가 멈춘다.

자세한 기준: [`AGENTS.md` §3](AGENTS.md)

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
