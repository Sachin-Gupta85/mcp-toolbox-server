"""Read-only SQLite query tool with a SELECT-only safety gate."""
from __future__ import annotations

import re
import sqlite3

_FORBIDDEN = re.compile(
    r"\b(insert|update|delete|drop|alter|create|replace|attach|detach|pragma|vacuum)\b",
    re.IGNORECASE,
)


def is_safe_select(sql: str) -> bool:
    """True only for a single read-only SELECT/WITH statement."""
    stripped = sql.strip().rstrip(";")
    if ";" in stripped:                       # no statement chaining
        return False
    if not re.match(r"(?is)^\s*(select|with)\b", stripped):
        return False
    return _FORBIDDEN.search(stripped) is None


def run_query(db_path: str, sql: str, limit: int = 100) -> list[dict]:
    if not is_safe_select(sql):
        raise ValueError("only a single read-only SELECT statement is allowed")
    conn = sqlite3.connect(db_path)
    try:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(sql).fetchmany(limit)
        return [dict(r) for r in rows]
    finally:
        conn.close()
