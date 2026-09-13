# Calculator MCP Server

A simple calculator MCP (Model Context Protocol) server built with [FastMCP](https://gofastmcp.com/). Exposes basic arithmetic tools that you can plug into any MCP client such as Claude Desktop.

## Tools

| Tool       | Description                                   |
| ---------- | --------------------------------------------- |
| `add`      | Add two numbers                               |
| `subtract` | Subtract `b` from `a`                         |
| `multiply` | Multiply two numbers                          |
| `divide`   | Divide `a` by `b` (raises on zero divisor)    |
| `power`    | Raise `base` to the power of `exponent`       |
| `sqrt`     | Square root of a non-negative number          |

## Prerequisites

- [Python](https://python.org) ≥ 3.12
- [uv](https://docs.astral.sh/uv/) — fast Python package/environment manager

## Setup

```bash
# 1. Create a virtual environment
uv venv .venv

# 2. Install dependencies (reads pyproject.toml)
uv sync

# 3. (Optional) Activate the venv
source .venv/bin/activate
```

## Run the server

```bash
# Runs over stdio (default)
uv run python main.py
```

Or use the FastMCP CLI:

```bash
uv run fastmcp dev main.py            # runs with auto-reload
uv run fastmcp list main.py           # list exposed tools
uv run fastmcp call --server-spec main.py --target add --input-json '{"a": 3, "b": 4}'
```

## Claude Desktop Configuration

1. Quit Claude Desktop completely.
2. Open `claude_desktop_config.json`:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`
3. Add (or merge) the following `mcpServers` entry, replacing the project path with your local path:

```json
{
  "mcpServers": {
    "calculator": {
      "command": "uv",
      "args": [
        "run",
        "--project",
        "/absolute/path/to/calculator",
        "--directory",
        "/absolute/path/to/calculator",
        "python",
        "/absolute/path/to/calculator/main.py"
      ]
    }
  }
}
```

> **Note:** If `uv` is not on Claude Desktop's `PATH` (common for GUI apps), use the absolute path instead, e.g. `"/Users/<you>/.local/bin/uv"`. Find yours with `which uv`.

4. Relaunch Claude Desktop. You should see a calculator icon, and the 6 tools will be available to use in chat.

## Project Layout

```
calculator/
├── main.py            # FastMCP server with all tools
├── pyproject.toml     # Project metadata + dependencies
├── uv.lock            # Lock file
└── README.md
```
