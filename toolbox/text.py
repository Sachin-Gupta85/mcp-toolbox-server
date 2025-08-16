"""Text utility tools (pure functions)."""
from __future__ import annotations

import hashlib
import re


def text_stats(text: str) -> dict:
    words = text.split()
    return {
        "characters": len(text),
        "words": len(words),
        "lines": text.count("\n") + 1 if text else 0,
        "unique_words": len({w.lower() for w in words}),
    }


def slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9\s-]", "", text.lower().strip())
    return re.sub(r"-+", "-", re.sub(r"\s+", "-", s)).strip("-")


def hash_text(text: str, algorithm: str = "sha256") -> str:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"unknown algorithm: {algorithm}")
    return hashlib.new(algorithm, text.encode("utf-8")).hexdigest()
