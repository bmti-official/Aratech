# 조사·비교 아카이브 포스트

세 단계로 나눠서 각 에이전트에 보낸다.

## 1) Antigravity — 자료 수집

```
AGENTS.md를 따라 줘. "{{조사 대상}}"({{유형: 경쟁사 / 유사 모델 / 벤치마크 / 시장 동향}})에 대한
공개 자료를 모아 work/archive/{{영문-슬러그}}/sources.md에 정리해 줘.
- 항목: 대상, 사업 형태, 고객, 수익 모델, 가격대, 핵심 자산(모방이 어려운 것), 규모 지표
- 사실마다 출처(링크), 등급(A/B/C), 확인일
- 원문 복사 금지, 요약만. 못 찾은 항목은 "미확인"
- 우리 사업 계획은 검색어에 넣지 않는다
브랜치 archive/{{영문-슬러그}}로 커밋만 하고 PR은 아직 열지 마.
```

## 2) Codex — 비교표 데이터

```
AGENTS.md를 따라 줘. 브랜치 archive/{{영문-슬러그}}의 work/archive/{{영문-슬러그}}/sources.md를 읽고
docs/schema.md의 posts 형식에 맞춰 compare(비교표)와 sources 배열만 만들어
work/archive/{{영문-슬러그}}/post.json으로 저장해 줘. 빈 칸은 "미확인"으로 표시하고, 새 값을 만들지 마.
필요하면 비교 그래프를 같은 폴더에 PNG로.
```

## 3) Claude — 포스트 완성

```
아래 비교표와 출처로 조사 아카이브 포스트를 완성해 줘. (post.json, sources.md 붙여 넣기)
- 상위 항목은 원문 링크를 열어 사실이 맞는지 확인하고, 확인 못 한 것은 표시
- 한 줄 결론: 우리에게 의미하는 바
- facts(사실, 등급 포함)와 interpretation(해석)을 나눠서
- implications: 적용할 점과 적용하지 않을 점, 최대 3개
- tags: 사업 형태, 지역, 연결된 가설 사이클
docs/schema.md 형식의 posts 항목 하나(JSON)로 출력. id는 P + 3자리.
```

완성된 JSON을 `site/data/posts.json`의 `posts` 배열에 추가해 PR → 05 검수 → 06 승인.
