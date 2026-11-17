#!/usr/bin/env python3
"""PR 변경 내용을 코드 대신 한국어 문장으로 요약한다.

사용: python3 scripts/summarize_pr.py origin/main > summary.md
- site/data/*.json은 항목 단위로 "무엇이 추가·변경·삭제됐는지" 문장으로 쓴다
- 그 밖의 파일은 "어떤 종류의 파일이 바뀌었는지"만 쓴다
- 데이터 검사 결과와 승인 판단 안내, 새 대화 검수용 문구를 붙인다
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = sys.argv[1] if len(sys.argv) > 1 else "origin/main"

FILE_KIND = [
    ("site/data/", "사이트 데이터"),
    ("site/", "사이트 화면(디자인)"),
    ("AGENTS.md", "에이전트 규칙"),
    ("prompts/", "지시문 템플릿"),
    ("scripts/", "검사·계산 프로그램"),
    (".github/", "자동 작업 설정"),
    ("work/", "중간 자료 (사이트에 안 나감)"),
    ("docs/", "안내 문서"),
    ("README.md", "안내 문서"),
]
CALC_NAMES = {"N": "대상 시장 인원", "P": "교육 가격", "M": "목표 판매 인원", "c": "전환율",
              "CAC": "1명 확보 비용", "VC": "1명당 변동비", "FC": "고정비", "k": "1인당 구매 횟수"}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True).stdout


def base_json(path):
    out = subprocess.run(["git", "show", f"{BASE}:{path}"], cwd=ROOT, capture_output=True, text=True)
    return json.loads(out.stdout) if out.returncode == 0 else None


def head_json(path):
    p = ROOT / path
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def g(x):
    return f"등급 {x}" if x else "등급 미확인"


def money(v, unit):
    if v is None:
        return "미정"
    return f"{v:,}{unit}" if isinstance(v, (int, float)) else f"{v}{unit}"


def by_key(items, key):
    return {str(i.get(key)): i for i in items or []}


def diff_list(old, new, key):
    o, n = by_key(old, key), by_key(new, key)
    added = [n[k] for k in n if k not in o]
    removed = [o[k] for k in o if k not in n]
    changed = [(o[k], n[k]) for k in n if k in o and o[k] != n[k]]
    return added, removed, changed


def field_changes(a, b, skip=()):
    out = []
    for k in sorted(set(a) | set(b)):
        if k in skip or a.get(k) == b.get(k):
            continue
        out.append(f"{k}: {a.get(k) if a.get(k) is not None else '없음'} → {b.get(k) if b.get(k) is not None else '없음'}")
    return out


def summarize_meetings(o, n):
    lines = []
    ev_key = lambda e: f"{e.get('date')}|{e.get('title')}"
    oe = {ev_key(e): e for e in o.get("events", [])}
    ne = {ev_key(e): e for e in n.get("events", [])}
    for k, e in ne.items():
        if k not in oe:
            lines.append(f"📅 일정 추가: **{e.get('title')}** ({e.get('date') or '날짜 미정'})")
    for k, e in oe.items():
        if k not in ne:
            lines.append(f"🗑️ 일정 삭제: {e.get('title')} ({e.get('date') or '날짜 미정'})")
    if o.get("weekly_summary") != n.get("weekly_summary"):
        lines.append(f"📝 이번 주 회의 요약 변경: “{n.get('weekly_summary') or '비움'}”")
    a, r, c = diff_list(o.get("meetings"), n.get("meetings"), "date")
    for m in a:
        lines.append(f"🗣️ 회의 기록 추가: {m.get('date')} {m.get('title', '회의')} — “{m.get('summary') or '요약 없음'}”"
                     f" (결정 {len(m.get('decisions', []))}개, 할 일 {len(m.get('actions', []))}개)")
    for m in r:
        lines.append(f"🗑️ 회의 기록 삭제: {m.get('date')}")
    for a_, b_ in c:
        lines.append(f"✏️ 회의 기록 수정: {b_.get('date')} {b_.get('title', '회의')}")
    return lines


def summarize_sources(o, n):
    lines = []
    a, r, c = diff_list(o.get("items"), n.get("items"), "id")
    for s in a:
        lines.append(f"📎 근거 추가: **{s.get('title')}** ({g(s.get('grade'))}, 출처: {s.get('source')}, 확인일 {s.get('checked') or '없음'})")
    for s in r:
        lines.append(f"🗑️ 근거 삭제: {s.get('title')}")
    for x, y in c:
        lines.append(f"✏️ 근거 수정: {y.get('title')} — " + "; ".join(field_changes(x, y, skip=("id",))))
    return lines


def summarize_calc(o, n):
    lines = []
    if o.get("status") != n.get("status"):
        lines.append(f"⚠️ 수익 계산 상태: {o.get('status')} → **{n.get('status')}**")
    oi, ni = by_key(o.get("inputs"), "key"), by_key(n.get("inputs"), "key")
    for k, y in ni.items():
        x = oi.get(k, {})
        if x.get("value") != y.get("value") or x.get("grade") != y.get("grade"):
            unit = y.get("unit", "")
            lines.append(f"🔢 {k} {CALC_NAMES.get(k, '')}: {money(x.get('value'), unit)} → **{money(y.get('value'), unit)}** ({g(y.get('grade'))})")
    if o.get("recommendations") != n.get("recommendations"):
        lines.append("💡 가격·인원 추천안(A/B/C) 문구 또는 값 변경")
    return lines


def summarize_hypothesis(o, n):
    lines = []
    for ch in field_changes(o.get("cycle", {}), n.get("cycle", {})):
        lines.append(f"🔄 사이클 정보 — {ch}")
    oc, nc = by_key(o.get("card"), "key"), by_key(n.get("card"), "key")
    for k, y in nc.items():
        x = oc.get(k, {})
        if x.get("value") != y.get("value") or x.get("grade") != y.get("grade"):
            lines.append(f"🧪 가설 카드 ‘{k}’: {x.get('value') or '미정'} → **{y.get('value') or '미정'}** ({g(y.get('grade'))})")
    if o.get("verdict") != n.get("verdict"):
        lines.append(f"⚖️ 판정: {o.get('verdict') or '대기'} → **{n.get('verdict') or '대기'}**")
    for name, label in (("start_conditions", "시작 조건"), ("next_steps", "다음 단계")):
        ol, nl = by_key(o.get(name), "text"), by_key(n.get(name), "text")
        for t, y in nl.items():
            if t not in ol:
                lines.append(f"➕ {label} 추가: {t}")
            elif ol[t].get("done") != y.get("done"):
                lines.append(f"{'✅' if y.get('done') else '↩️'} {label} {'완료' if y.get('done') else '완료 취소'}: {t}")
        for t in ol:
            if t not in nl:
                lines.append(f"🗑️ {label} 삭제: {t}")
    for t in n.get("timing", []):
        old = next((x for x in o.get("timing", []) if x.get("code") == t.get("code")), {})
        if old.get("value") != t.get("value"):
            lines.append(f"📈 타이밍 점수 {t.get('code')} {t.get('name')}: {old.get('value') or '미측정'} → {t.get('value') or '미측정'}")
    for h in n.get("history", [])[len(o.get("history", [])):]:
        lines.append(f"🏁 사이클 판정 기록 추가: 사이클 {h.get('cycle')} — {h.get('verdict')} ({h.get('signal')}) · 배운 점: {h.get('learned')}")
    return lines


def summarize_posts(o, n):
    lines = []
    a, r, c = diff_list(o.get("posts"), n.get("posts"), "id")
    for p in a:
        lines.append(f"📰 조사 포스트 추가: **{p.get('title')}** ({p.get('type')}) — 결론: “{p.get('conclusion')}” · 출처 {len(p.get('sources', []))}개")
    for p in r:
        lines.append(f"🗑️ 조사 포스트 삭제: {p.get('title')}")
    for x, y in c:
        lines.append(f"✏️ 조사 포스트 수정: {y.get('title')}")
    return lines


def summarize_plan(o, n):
    lines = []
    op, np_ = by_key(o.get("packs"), "id"), by_key(n.get("packs"), "id")
    for k, y in np_.items():
        if op.get(k, {}).get("status") != y.get("status"):
            lines.append(f"🧭 질문 팩 {k} 상태: {op.get(k, {}).get('status')} → **{y.get('status')}**")
    for cnc in n.get("conclusions", [])[len(o.get("conclusions", [])):]:
        lines.append(f"🏛️ 대형 기획 결론 공개: “{cnc.get('conclusion')}” (질문: {cnc.get('question')})")
    return lines


SUMMARIZERS = {
    "meetings.json": ("캘린더·회의", summarize_meetings),
    "sources.json": ("근거 자료", summarize_sources),
    "calc.json": ("수익 계산", summarize_calc),
    "hypothesis.json": ("가설 검증", summarize_hypothesis),
    "posts.json": ("조사 아카이브", summarize_posts),
    "plan.json": ("대형 기획", summarize_plan),
}
NEEDS_REVIEW = {"posts.json", "plan.json", "calc.json"}


def main():
    changed = [f for f in git("diff", "--name-only", f"{BASE}...HEAD").split("\n") if f]
    if not changed:
        changed = [f for f in git("diff", "--name-only", BASE).split("\n") if f]

    out = ["## 📋 변경 요약 (자동 작성)", ""]
    need_review = False
    data_lines = []
    for f in changed:
        name = Path(f).name
        if f.startswith("site/data/") and name in SUMMARIZERS:
            label, fn = SUMMARIZERS[name]
            o, n = base_json(f) or {}, head_json(f) or {}
            lines = fn(o, n) if n else ["🗑️ 파일 삭제"]
            if not lines:
                lines = ["내용 변화 없음 (줄바꿈·형식만 정리)"]
            data_lines.append(f"**{label}** 화면")
            data_lines += [f"- {x}" for x in lines]
            data_lines.append("")
            if name in NEEDS_REVIEW and lines and lines[0] != "내용 변화 없음 (줄바꿈·형식만 정리)":
                need_review = True
            if name == "hypothesis.json" and any(("판정" in x or "가설 카드" in x) for x in lines):
                need_review = True
    if data_lines:
        out.append("### 사이트에 보이는 변화")
        out += data_lines
    else:
        out += ["### 사이트에 보이는 변화", "- 없음 (화면 데이터는 그대로)", ""]

    others = {}
    for f in changed:
        if f.startswith("site/data/"):
            continue
        kind = next((k for p, k in FILE_KIND if f.startswith(p)), "기타 파일")
        others.setdefault(kind, []).append(f)
    if others:
        out.append("### 그 밖에 바뀐 파일")
        for k, fs in others.items():
            out.append(f"- {k}: " + ", ".join(f"`{x}`" for x in fs))
            if k in ("사이트 화면(디자인)", "자동 작업 설정", "검사·계산 프로그램", "에이전트 규칙"):
                need_review = True
        out.append("")

    chk = subprocess.run([sys.executable, str(ROOT / "scripts" / "check_data.py")], capture_output=True, text=True)
    result = chk.stdout.strip().split("\n")[-1] if chk.stdout.strip() else "실행 실패"
    out.append("### 자동 검사")
    out.append(f"- {'✅' if chk.returncode == 0 else '❌'} {result}")
    detail = [x for x in chk.stdout.split("\n") if x.startswith("[")]
    if detail:
        out.append("<details><summary>검사 상세</summary>\n")
        out += [f"- {x}" for x in detail]
        out.append("\n</details>")
    out.append("")

    out.append("### 승인하는 사람이 할 일")
    if chk.returncode != 0:
        out.append("- ❌ 검사 오류가 있어 **Merge하지 마세요.** 댓글로 \"검사 오류 고쳐 주세요\"라고 남기면 됩니다.")
    elif need_review:
        out.append("- 🔍 **새 Claude 대화 검수가 필요한 변경**입니다. 아래 '검수용 문구'를 펼쳐 복사 → 새 대화에 붙여 넣기 → \"검수 통과\"가 나오면 Merge")
    else:
        out.append("- 👍 **간단한 변경**입니다. 위 요약이 의도와 맞으면 바로 Merge해도 됩니다.")
    out.append("- 맞지 않으면 Merge하지 말고, 아래 댓글 칸에 고칠 점을 한국어로 적어 주세요.")
    out.append("")

    review = "\n".join(x for x in out if not x.startswith("<details") and x != "\n</details>")
    out.append("<details><summary>검수용 문구 (새 Claude 대화에 그대로 붙여 넣기)</summary>\n")
    out.append("```")
    out.append("너는 검수자야. 아래 변경을 Aratech 지침서 기준으로 점검해 줘. 고쳐 쓰지 말고 문제만 찾아.")
    out.append("점검: 개인정보(실명·연락처·환자 정보), 등급 없는 숫자, 지어낸 값, 공개 범위(수익 전체·독점 전략),")
    out.append("실존 인물 발언 날조, 조작 표현(불안 조장·허위 희소성·가짜 후기), 사실과 해석 혼동.")
    out.append("문제마다 위치/문제/고칠 방향을 쓰고, 없으면 \"검수 통과\"와 근거 한 줄.")
    out.append("")
    out.append(review.replace("```", "'''"))
    out.append("```")
    out.append("\n</details>")
    print("\n".join(out))


if __name__ == "__main__":
    main()
