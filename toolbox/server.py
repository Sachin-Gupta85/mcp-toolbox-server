"""FastMCP server exposing the toolbox as MCP tools.

Run with:  python -m toolbox          (stdio transport, for an MCP client)
The tool bodies delegate to the pure functions in this package, which are unit
tested independently of the MCP protocol.
"""
from __future__ import annotations

from fastmcp import FastMCP

from . import calculator, text, units
from .sqltool import run_query

mcp = FastMCP("toolbox")


@mcp.tool
def calculate(expression: str) -> float:
    """Safely evaluate a numeric expression (e.g. '2 * (3 + 4) ** 2')."""
    return calculator.calculate(expression)


@mcp.tool
def text_stats(text_input: str) -> dict:
    """Return character/word/line/unique-word counts for a block of text."""
    return text.text_stats(text_input)


@mcp.tool
def slugify(text_input: str) -> str:
    """Turn a title into a URL slug."""
    return text.slugify(text_input)


@mcp.tool
def hash_text(text_input: str, algorithm: str = "sha256") -> str:
    """Hash text with the named hashlib algorithm (default sha256)."""
    return text.hash_text(text_input, algorithm)


@mcp.tool
def convert_units(value: float, from_unit: str, to_unit: str) -> float:
    """Convert a value between compatible length/mass/temperature units."""
    return units.convert(value, from_unit, to_unit)


@mcp.tool
def sqlite_query(db_path: str, sql: str, limit: int = 100) -> list[dict]:
    """Run a read-only SELECT against a SQLite database file."""
    return run_query(db_path, sql, limit)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
