# 🧰 mcp-toolbox-server — a Model Context Protocol tool server

> A production-shaped **MCP server** (built on **FastMCP**) that exposes a suite of safe utility tools to any MCP client — Claude Desktop, IDEs, or your own agent.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![MCP](https://img.shields.io/badge/MCP-FastMCP%204-6f42c1)
![Tests](https://img.shields.io/badge/tests-pytest%20(9)-brightgreen)

## 🧠 What it does
Model Context Protocol lets LLM clients call external tools over a standard
transport. This server registers six tools:

| Tool | Description |
|---|---|
| `calculate` | safe arithmetic via a **restricted AST** (no `eval`, no code execution) |
| `text_stats` | character / word / line / unique-word counts |
| `slugify` | title → URL slug |
| `hash_text` | hash text with any `hashlib` algorithm |
| `convert_units` | length / mass / temperature conversions |
| `sqlite_query` | **read-only** SELECT against a SQLite file (SELECT-only safety gate) |

## 🏗️ Architecture
```
toolbox/
  calculator.py  text.py  units.py  sqltool.py   # pure, unit-tested logic
  server.py                                       # FastMCP wiring (@mcp.tool)
  __main__.py                                     # python -m toolbox  (stdio)
```
The tool **bodies delegate to pure functions**, so the entire toolbox is tested
without speaking the MCP protocol or needing a client. Safety is enforced in code:
the calculator walks a whitelisted AST, and the SQL tool rejects anything but a
single read-only `SELECT`/`WITH`.

## 🚀 Run
```bash
pip install -r requirements.txt
python -m toolbox          # starts the MCP server on stdio
```
Register it with an MCP client (e.g. Claude Desktop `mcpServers` config):
```json
{ "mcpServers": { "toolbox": { "command": "python", "args": ["-m", "toolbox"] } } }
```

## ✅ Test
```bash
pip install -r requirements-dev.txt && python -m pytest -q
```

## 📝 License
MIT — see [LICENSE](LICENSE).
