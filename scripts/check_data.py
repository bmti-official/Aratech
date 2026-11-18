#!/usr/bin/env python3
"""site/data/*.json 검사. 오류가 있으면 종료 코드 1.

검사 항목
- JSON 형식, 필수 키
- 근거 등급은 A/B/C/null
- 날짜 형식 YYYY-MM-DD, 확인일 90일 경과 경고
- 개인정보로 보이는 문자열 (이메일, 전화번호, 주민번호 형태)
- 포스트 시사점 최대 3개, 추천안은 정확히 3개
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "site" / "data"
GRADES = {"A", "B", "C", None}
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
PII = [
    ("이메일", re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")),
    ("전화번호", re.compile(r"(?<!\d)01[016789][-\s]?\d{3,4}[-\s]?\d{4}(?!\d)")),
    ("주민번호 형태", re.compile(r"(?<!\d)\d{6}-[1-4]\d{6}(?!\d)")),
]
CALC_KEYS = {"N", "P", "M", "c", "CAC", "VC", "FC", "k"}

errors, warnings = [], []


def err(f, msg):
    errors.append(f"[오류] {f}: {msg}")


def warn(f, msg):
    warnings.append(f"[경고] {f}: {msg}")


def check_date(f, where, value, allow_null=True, stale_check=False):
    if value is None:
        if not allow_null:
            err(f, f"{where} 날짜가 비어 있음")
        return
    if not isinstance(value, str) or not DATE_RE.match(value):
        err(f, f"{where} 날짜 형식이 YYYY-MM-DD가 아님: {value!r}")
        return
    try:
        d = datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        err(f, f"{where} 없는 날짜: {value}")
        return
    if stale_check and (date.today() - d).days > 90:
        warn(f, f"{where} 확인일 {value}이 90일을 넘음 → 재확인 필요")


def check_grade(f, where, g):
    if g not in GRADES:
        err(f, f"{where} 등급이 A/B/C/null이 아님: {g!r}")


def walk_strings(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}" if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(obj, str):
        yield path, obj


def load(name):
    p = DATA / name
    if not p.exists():
        err(name, "파일 없음")
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err(name, f"JSON 형식 오류: {e}")
        return None


def main():
    files = {n: load(n) for n in
             ["hypothesis.json", "sources.json", "calc.json", "meetings.json", "posts.json", "plan.json"]}

    for name, d in files.items():
        if d is None:
            continue
        check_date(name, "updated", d.get("updated"), allow_null=False)
        for path, s in walk_strings(d):
            if path.endswith("url") or "url" in path.split(".")[-1]:
                continue
            for label, rx in PII:
                if rx.search(s):
                    err(name, f"{path}에 {label}로 보이는 값이 있음")

    h = files["hypothesis.json"]
    if h:
        for k in ["cycle", "card", "start_conditions", "next_steps", "timing", "history"]:
            if k not in h:
                err("hypothesis.json", f"'{k}' 없음")
        for i, c in enumerate(h.get("card", [])):
            check_grade("hypothesis.json", f"card[{i}]", c.get("grade"))
        if h.get("verdict") not in (None, "유지", "수정", "중단"):
            err("hypothesis.json", "verdict는 null/유지/수정/중단")
        cy = h.get("cycle", {})
        check_date("hypothesis.json", "cycle.start_date", cy.get("start_date"))
        if cy.get("status") == "진행 중" and not all(x.get("done") for x in h.get("start_conditions", [])):
            err("hypothesis.json", "시작 조건이 다 채워지지 않았는데 status가 '진행 중'")
        for i, x in enumerate(h.get("history", [])):
            if x.get("verdict") not in ("유지", "수정", "중단"):
                err("hypothesis.json", f"history[{i}].verdict는 유지/수정/중단")

    s = files["sources.json"]
    if s:
        ids = set()
        for i, it in enumerate(s.get("items", [])):
            w = f"items[{i}] {it.get('id')}"
            if it.get("id") in ids:
                err("sources.json", f"{w} id 중복")
            ids.add(it.get("id"))
            check_grade("sources.json", w, it.get("grade"))
            check_date("sources.json", w, it.get("checked"), stale_check=True)
            if it.get("url") and not re.match(r"^https?://", it["url"], re.I):
                err("sources.json", f"{w} url은 http:// 또는 https://로 시작해야 함")
            if it.get("grade") in ("A", "B") and not it.get("url"):
                warn("sources.json", f"{w} A/B 등급인데 url 없음")
            if it.get("grade") in ("A", "B") and not it.get("checked"):
                warn("sources.json", f"{w} A/B 등급인데 확인일 없음")

    c = files["calc.json"]
    if c:
        keys = {i.get("key") for i in c.get("inputs", [])}
        if keys != CALC_KEYS:
            err("calc.json", f"inputs key는 {sorted(CALC_KEYS)} 이어야 함 (현재 {sorted(k for k in keys if k)})")
        if c.get("status") not in ("example", "draft", "approved"):
            err("calc.json", "status는 example/draft/approved")
        for i in c.get("inputs", []):
            check_grade("calc.json", f"inputs.{i.get('key')}", i.get("grade"))
            if i.get("value") is not None and i.get("grade") is None:
                warn("calc.json", f"inputs.{i.get('key')} 값은 있는데 등급이 없음")
        for k, r in (c.get("recommendations") or {}).items():
            if len(r.get("options", [])) != 3:
                err("calc.json", f"recommendations.{k} 추천안은 정확히 3개")

    m = files["meetings.json"]
    if m:
        for i, e in enumerate(m.get("events", [])):
            check_date("meetings.json", f"events[{i}]", e.get("date"))
        for i, x in enumerate(m.get("meetings", [])):
            check_date("meetings.json", f"meetings[{i}]", x.get("date"), allow_null=False)
            for a in x.get("actions", []):
                if a.get("status") not in ("완료", "진행", "지연"):
                    err("meetings.json", f"meetings[{i}] action status는 완료/진행/지연")
            if x.get("summary") and not x.get("full_minutes_url"):
                warn("meetings.json", f"meetings[{i}] 전체 회의록 링크(full_minutes_url) 없음")

    p = files["posts.json"]
    if p:
        for i, x in enumerate(p.get("posts", [])):
            w = f"posts[{i}] {x.get('id')}"
            for k in ["id", "title", "type", "conclusion", "sources"]:
                if not x.get(k):
                    err("posts.json", f"{w} '{k}' 비어 있음")
            if x.get("type") not in ("경쟁사", "유사 모델", "벤치마크", "시장 동향"):
                err("posts.json", f"{w} type은 경쟁사/유사 모델/벤치마크/시장 동향")
            if len(x.get("implications", [])) > 3:
                err("posts.json", f"{w} 시사점은 최대 3개")
            for f in x.get("facts", []):
                check_grade("posts.json", w + " facts", f.get("grade"))
            for j, src in enumerate(x.get("sources", [])):
                check_grade("posts.json", f"{w} sources[{j}]", src.get("grade"))
                check_date("posts.json", f"{w} sources[{j}]", src.get("checked"), stale_check=True)

    pl = files["plan.json"]
    if pl:
        for i, x in enumerate(pl.get("conclusions", [])):
            check_date("plan.json", f"conclusions[{i}]", x.get("date"))
            if not x.get("restricted_url"):
                warn("plan.json", f"conclusions[{i}] 제한 문서 링크(restricted_url) 없음")

    for line in errors + warnings:
        print(line)
    print(f"\n오류 {len(errors)}건, 경고 {len(warnings)}건")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
