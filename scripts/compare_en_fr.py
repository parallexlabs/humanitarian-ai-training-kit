#!/usr/bin/env python3
"""Compare EN/FR markdown pairs for structural parity."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"

NEGATION_PATTERNS_EN = [
    r"\bnot\b",
    r"\bnever\b",
    r"\bnone\b",
    r"\bnothing\b",
    r"\bneither\b",
    r"\bnor\b",
    r"\bdon'?t\b",
    r"\bdoesn'?t\b",
    r"\bcan'?t\b",
    r"\bwon'?t\b",
    r"\bwithout\b",
    r"\bno\s+(?:ai|account|login|breakout|camera|personal)\b",
]
NEGATION_PATTERNS_FR = [
    r"\bne\s+\w+\s+pas\b",
    r"\bplus\b",
    r"\bjamais\b",
    r"\baucun\b",
    r"\baucune\b",
    r"\brien\b",
    r"\bsans\b",
]


def normalize_times(text: str) -> str:
    text = re.sub(r"\b(\d{1,2})\s*h\s*(\d{2})\b", r"\1:\2", text, flags=re.I)
    return text


def normalize_numbers(text: str) -> str:
    text = re.sub(r"(\d)[\s\u00a0](\d{3})\b", r"\1\2", text)
    text = re.sub(r"(\d),(\d{3})\b", r"\1\2", text)
    return text


def count_items(text: str, lang: str) -> dict:
    text = normalize_times(normalize_numbers(text))
    neg_patterns = NEGATION_PATTERNS_EN if lang == "en" else NEGATION_PATTERNS_FR
    return {
        "numbers": len(re.findall(r"\b\d+(?:[.,]\d+)?%?\b", text)),
        "dates": len(
            re.findall(
                r"\b\d{1,2}\s+\w+\s+\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{4}\b",
                text,
            )
        ),
        "times": len(re.findall(r"\b\d{1,2}:\d{2}\b", text)),
        "ordered_steps": len(re.findall(r"^\s*\d+\.\s", text, re.M)),
        "unordered_items": len(re.findall(r"^\s*[-*+]\s", text, re.M)),
        "table_rows": len(
            [
                ln
                for ln in text.splitlines()
                if ln.strip().startswith("|") and not re.match(r"^\s*\|[-:| ]+\|\s*$", ln)
            ]
        ),
        "negations": sum(len(re.findall(p, text, re.I)) for p in neg_patterns),
    }


def compare_pair(en_path: Path, fr_path: Path) -> list[dict]:
    en_counts = count_items(en_path.read_text(encoding="utf-8"), "en")
    fr_counts = count_items(fr_path.read_text(encoding="utf-8"), "fr")
    mismatches = []
    for key in en_counts:
        if en_counts[key] != fr_counts[key]:
            mismatches.append(
                {
                    "file": str(en_path.relative_to(CONTENT)),
                    "metric": key,
                    "en": en_counts[key],
                    "fr": fr_counts[key],
                }
            )
    return mismatches


def find_pairs() -> list[tuple[Path, Path]]:
    pairs = []
    for en_file in sorted((CONTENT / "en").rglob("*.md")):
        rel = en_file.relative_to(CONTENT / "en")
        fr_file = CONTENT / "fr" / rel
        if fr_file.exists():
            pairs.append((en_file, fr_file))
    return pairs


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare EN/FR content parity")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    all_mismatches: list[dict] = []
    for en_path, fr_path in find_pairs():
        all_mismatches.extend(compare_pair(en_path, fr_path))

    if args.json:
        print(json.dumps({"mismatches": all_mismatches, "count": len(all_mismatches)}, indent=2))
    else:
        for m in all_mismatches:
            print(f"{m['file']}: {m['metric']} en={m['en']} fr={m['fr']}")
        print(f"Total mismatches: {len(all_mismatches)}")
    return 1 if all_mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
