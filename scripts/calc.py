#!/usr/bin/env python3
"""site/data/calc.json으로 수익 계산 (지침서 6장).

R = M × P, Reach = M / c, BEP = FC / (P − VC − CAC), LTV = P × k − VC
전환율 c를 ×0.5(보수) ×1(기준) ×1.5(낙관)로 바꾼 3개 시나리오를 함께 출력한다.
LTV/CAC 3배는 업계 경험칙(B) 점검선이다.

사용: python3 scripts/calc.py            # 마크다운 표 출력
      python3 scripts/calc.py --json     # JSON 출력
"""
import json
import math
import sys
from pathlib import Path

CALC = Path(__file__).resolve().parent.parent / "site" / "data" / "calc.json"


def compute(v, c_mult=1.0):
    P, M, CAC, VC, FC, k = (v.get(x) for x in ["P", "M", "CAC", "VC", "FC", "k"])
    c = (v.get("c") or 0) / 100 * c_mult
    out = {}
    out["R"] = M * P if None not in (M, P) else None
    out["Reach"] = math.ceil(M / c) if M is not None and c > 0 else None
    margin = None if None in (P, VC, CAC) else P - VC - CAC
    out["BEP"] = math.ceil(FC / margin) if FC is not None and margin and margin > 0 else None
    out["LTV"] = P * k - VC if None not in (P, k, VC) else None
    out["LTV/CAC"] = round(out["LTV"] / CAC, 2) if out["LTV"] is not None and CAC else None
    return out


def main():
    d = json.loads(CALC.read_text(encoding="utf-8"))
    v = {i["key"]: i.get("value") for i in d["inputs"]}
    grades = {i["key"]: i.get("grade") for i in d["inputs"]}
    scen = {"보수 (c×0.5)": compute(v, 0.5), "기준": compute(v), "낙관 (c×1.5)": compute(v, 1.5)}
    if "--json" in sys.argv:
        print(json.dumps({"status": d.get("status"), "inputs": v, "grades": grades, "scenarios": scen}, ensure_ascii=False, indent=2))
        return
    fmt = lambda x: "계산 불가" if x is None else (f"{x:,}" if isinstance(x, int) else f"{x:,.2f}")
    print(f"상태: {d.get('status')} · 기준일 {d.get('updated')}\n")
    print("| 변수 | 값 | 등급 |\n|---|---|---|")
    for i in d["inputs"]:
        print(f"| {i['key']} {i['name']} | {fmt(i.get('value'))} {i['unit']} | {i.get('grade') or '미확인'} |")
    print("\n| 지표 | " + " | ".join(scen) + " |\n|---|" + "---|" * len(scen))
    for key in ["R", "Reach", "BEP", "LTV", "LTV/CAC"]:
        print(f"| {key} | " + " | ".join(fmt(s[key]) for s in scen.values()) + " |")
    base = scen["기준"]
    if base["LTV/CAC"] is not None:
        ok = "넘음" if base["LTV/CAC"] >= 3 else "못 미침"
        print(f"\nLTV/CAC {base['LTV/CAC']}배 → 점검선 3배(B)를 {ok}.")
    if base["BEP"] is not None and v.get("M") is not None:
        print(f"목표 판매 {v['M']}명, 손익분기 {base['BEP']}명.")
    if any(g == "C" or g is None for g in grades.values()):
        print("가정(C) 또는 미확인 값이 들어 있으므로 의사결정 근거로 쓰지 않는다.")


if __name__ == "__main__":
    main()
