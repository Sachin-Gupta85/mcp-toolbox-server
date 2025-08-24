import sqlite3
import pytest
from toolbox.sqltool import is_safe_select, run_query


def test_safety_gate():
    assert is_safe_select("SELECT * FROM t")
    assert is_safe_select("  with x as (select 1) select * from x ")
    assert not is_safe_select("DELETE FROM t")
    assert not is_safe_select("SELECT 1; DROP TABLE t")
    assert not is_safe_select("UPDATE t SET a=1")
    assert not is_safe_select("select 1; select 2")


def test_run_query(tmp_path):
    db = tmp_path / "x.db"
    conn = sqlite3.connect(db)
    conn.execute("CREATE TABLE users(id INTEGER, name TEXT)")
    conn.executemany("INSERT INTO users VALUES (?,?)", [(1, "a"), (2, "b")])
    conn.commit(); conn.close()
    rows = run_query(str(db), "SELECT name FROM users ORDER BY id")
    assert rows == [{"name": "a"}, {"name": "b"}]
    with pytest.raises(ValueError):
        run_query(str(db), "DROP TABLE users")
