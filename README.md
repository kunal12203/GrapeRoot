<div align="center">

<br>

<img src="./assets/graperoot-icon.svg" width="60" alt="GrapeRoot" align="middle">&nbsp;&nbsp;&nbsp;<picture><source media="(prefers-color-scheme: dark)" srcset="./assets/graperoot-wordmark-light.svg"><source media="(prefers-color-scheme: light)" srcset="./assets/graperoot-wordmark.svg"><img src="./assets/graperoot-wordmark.svg" width="350" alt="GRAPEROOT" align="middle"></picture>

<br><br>

**Compounding Context for AI Coding Assistants**

<br>

[![PyPI](https://img.shields.io/pypi/v/graperoot?label=version&color=brightgreen)](https://pypi.org/project/graperoot/)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](./LICENSE)
[![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)](#install)
[![Discord](https://img.shields.io/badge/Discord-community-5865F2?logo=discord&logoColor=white)](https://discord.com/invite/YwKdQATY2d)
[![Stars](https://img.shields.io/github/stars/kunal12203/Codex-CLI-Compact?style=social)](https://github.com/kunal12203/Codex-CLI-Compact/stargazers)

<br>

[**Website**](https://graperoot.dev) · [**Docs**](https://graperoot.dev/docs) · [**Benchmarks**](https://graperoot.dev/benchmarks) · [**Discord**](https://discord.com/invite/YwKdQATY2d)

<br>

---

🌐 **Read this in your language:**
[English](./README.md) · [中文](./docs/README_zh-CN.md) · [Español](./docs/README_es.md) · [हिंदी](./docs/README_hi.md) · [Français](./docs/README_fr.md) · [Deutsch](./docs/README_de.md) · [日本語](./docs/README_ja.md) · [한국어](./docs/README_ko.md) · [Português](./docs/README_pt-BR.md) · [Русский](./docs/README_ru.md) · [العربية](./docs/README_ar.md) · [Türkçe](./docs/README_tr.md) · [Bahasa Indonesia](./docs/README_id.md)

</div>

---

## What is GrapeRoot?

GrapeRoot is an **open-source launcher** that sits between you and your AI coding assistant. It builds a semantic graph of your codebase — files, symbols, imports, call chains — and pre-loads exactly the right code into every prompt before your AI sees it.

> The launcher scripts in this repo are Apache 2.0. The graph engine (`graperoot` pip package) is proprietary.

The result: your AI spends tokens **reasoning**, not exploring.

```
You run: dgc /path/to/project
              ↓
1. Project scanned → semantic graph built (files, symbols, imports)
2. You ask a question
3. Graph identifies the relevant files → packs them into context
4. AI gets your question + the right code already loaded
5. Fewer turns, fewer tokens, better answers
```

Token savings **compound** across a session. The graph remembers which files were read, edited, and queried — each turn gets cheaper.

---

## Other Tools vs GrapeRoot

**Other tools** (CodeGraph, code-graph-mcp, and similar) give your AI a graph and let it explore:

```
You ask a question
  → AI calls search_symbol / get_callers / trace_route
  → AI reads results, decides what else to look up
  → AI calls more tools
  → AI finally has enough context to answer
```

Your AI spends turns exploring before it can reason.

---

**GrapeRoot** pre-loads the right context before your AI sees your question:

```
You ask a question
  → Graph identifies relevant files automatically
  → Files packed into the prompt
  → AI answers immediately
```

No exploration. No extra tool calls. Your AI starts reasoning from turn one.

---

| | Other tools | GrapeRoot |
|---|---|---|
| How context is delivered | AI pulls on demand via tool calls | Pre-loaded before every turn |
| Session memory | No | Yes — compounds across turns |
| Token budget control | AI decides | Hard-capped per turn |
| Turns spent exploring | Multiple | Zero |
| Savings compound | No | Yes — each turn gets cheaper |

---

## Results

Benchmarked across multiple real-world codebases (7,700+ files) and 50+ engineering prompts:

| Metric | Without GrapeRoot | With GrapeRoot |
|--------|:-----------------:|:--------------:|
| Cost per prompt | $0.49 | **$0.27** |
| Avg turns per task | 11.7 | **3.5** |
| Avg response time | 172s | **124s** |
| Quality (scored) | 76.6 / 100 | **86.6 / 100** |
| Cost win rate | — | **10 out of 10 prompts** |

### Cost reduction by task type

| Task type | Cost reduction |
|-----------|:--------------:|
| Migration & architecture design | **up to 81%** |
| Performance analysis | **up to 80%** |
| Testing & test generation | **up to 76%** |
| Full-stack debugging | **up to 73%** |
| Feature development | **up to 71%** |
| Code explanation & audit | **up to 55%** |
| Large codebase (7k+ files, avg) | **43% average** |

> Savings **compound** across a session — a token avoided on turn 3 also skips cache re-billing on every subsequent turn. Quality stays equal or improves on every task type above.

Full benchmark methodology and results: [graperoot.dev/benchmarks](https://graperoot.dev/benchmarks)

---

## Supported AI Tools

| Tool | Command | Status |
|------|---------|--------|
| Claude Code | `dgc` | ✅ Full support |
| OpenAI Codex CLI | `dg` | ✅ Full support |
| Cursor | `graperoot . --cursor` | ✅ Full support |
| Gemini CLI | `graperoot . --gemini` | ✅ Full support |
| OpenCode | `graperoot . --opencode` / `dgo` | ✅ Full support |
| GitHub Copilot | `graperoot . --copilot` | ✅ Full support |
| OpenClaw | `graperoot . --openclaw` | ✅ Full support |
| Kilocode | `graperoot . --kilocode` | ✅ Full support |
| MiMo Code | `graperoot . --mimocode` | ✅ Full support |
| Antigravity | `graperoot . --antigravity` | ✅ Full support |
| Kiro CLI | `graperoot . --kiro` | ✅ Full support |
| Command Code | `graperoot . --command-code` | ✅ Full support |

---

## Supported Languages

TypeScript · JavaScript · Python · Go · Swift · Rust · Java · Kotlin · Scala · C# · Ruby · PHP

---

## Install

**macOS / Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.sh | bash
source ~/.zshrc   # or ~/.bashrc / ~/.profile
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/kunal12203/Codex-CLI-Compact/main/install.ps1 | iex
```

**Windows (Scoop):**
```powershell
scoop bucket add dual-graph https://github.com/kunal12203/scoop-dual-graph
scoop install dual-graph
```

> **Prerequisites:** Python 3.10+, Node.js 18+, and one of the supported AI tools. The installer detects missing tools and offers to install them automatically.

---

## Usage

> **Important:** Always use `dgc` (not `claude` directly) to ensure the MCP server is running.

### Claude Code

```bash
dgc                                      # scan current directory, launch Claude
dgc /path/to/project                     # scan a specific project
dgc /path/to/project "fix the login bug" # start with a prompt
```

### OpenAI Codex CLI

```bash
dg                              # scan current directory
dg /path/to/project             # scan a specific project
dg /path/to/project "add tests" # start with a prompt
```

### MiniMax

With the Bash launchers, set `MINIMAX_API_KEY`, then select
`MiniMax-M3.1-Flash` (the `minimax` default) or `MiniMax-M3`.

```bash
export MINIMAX_API_KEY="your-api-key"
dg --model=minimax /path/to/project
dg --model=minimax-m3.1-flash /path/to/project
dg --model=minimax-m3 /path/to/project
```

`MINIMAX_REGION` selects the endpoint region and defaults to `global_en`.
`MINIMAX_API_MODE` selects the compatible API mode and defaults to `openai`;
set it to `anthropic` to use the Anthropic-compatible endpoint. Both current
models use a 1,000,000-token context window. Explicit legacy selections
`--model=minimax-m2.7` and `--model=MiniMax-M2.7` remain available with their
204,800-token context window; existing saved or custom model arguments are
not rewritten. Native PowerShell launchers do not implement this routing.

| Region | OpenAI-compatible base URL | Anthropic-compatible base URL |
|--------|----------------------------|-------------------------------|
| `global_en` | `https://api.minimax.io/v1` | `https://api.minimax.io/anthropic` |
| `cn_zh` | `https://api.minimaxi.com/v1` | `https://api.minimaxi.com/anthropic` |

```bash
MINIMAX_REGION=cn_zh dg --model=minimax-m3 /path/to/project
MINIMAX_API_MODE=anthropic dgc --model=minimax-m3.1-flash /path/to/project
```

### Interactive Picker (new in v3.9.99)

```bash
graperoot          # shows directory confirm + arrow-key tool picker
graperoot .        # same, picks from current directory
graperoot --version   # print current version
graperoot --update    # force self-update
```

### OpenCode

```bash
dgo                             # scan current directory
dgo /path/to/project            # scan a specific project
dgo /path/to/project "refactor" # start with a prompt
```

### All Tools via `graperoot`

```bash
graperoot . --cursor          # Cursor
graperoot . --gemini          # Gemini CLI
graperoot . --opencode        # OpenCode
graperoot . --copilot         # GitHub Copilot
graperoot . --openclaw        # OpenClaw
graperoot . --kilocode        # Kilocode
graperoot . --mimocode        # MiMo Code
graperoot . --kiro            # Kiro CLI
graperoot . --command-code    # Command Code
graperoot /path --gemini "add tests"   # specific project + prompt
```

### Windows

```powershell
dgc .                          # from inside the project directory
dgc "D:\projects\my-app"       # any drive, any path
dg "C:\work\backend"           # Codex CLI
dgc --gemini "D:\projects\app" # Gemini CLI on Windows
```

---

## How It Works

1. **Graph scan** — on first run, GrapeRoot extracts files, functions, classes, and import relationships into a local graph stored in `.dual-graph/`.
2. **Context retrieval** — each time you ask a question, the graph ranks the most relevant files and packs them into the prompt before your AI sees it.
3. **Session memory** — files you've read, edited, or queried are weighted higher in future turns. Context compounds.
4. **MCP tools** — your AI can still drill deeper via graph-aware tools (`graph_read`, `graph_retrieve`, `graph_neighbors`) when it needs to explore.

All processing is **local**. No code leaves your machine.

---

## Data & Files

All data lives in `<project>/.dual-graph/` (auto-added to `.gitignore`):

| File | Description |
|------|-------------|
| `info_graph.json` | Semantic graph: files, symbols, edges |
| `chat_action_graph.json` | Session memory: reads, edits, queries |
| `context-store.json` | Persistent decisions/tasks/facts across sessions |

Global install at `~/.dual-graph/`:

| File | Description |
|------|-------------|
| `dgc.ps1` / `dg.ps1` | Launcher scripts (auto-updated) |
| `venv/` | Python virtual environment |
| `version.txt` | Installed version |

---

## Configuration

All optional, via environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `DG_HARD_MAX_READ_CHARS` | `4000` | Max characters per file read |
| `DG_TURN_READ_BUDGET_CHARS` | `18000` | Total read budget per turn |
| `DG_FALLBACK_MAX_CALLS_PER_TURN` | `1` | Max fallback grep calls per turn |
| `DG_RETRIEVE_CACHE_TTL_SEC` | `900` | Retrieval cache TTL (15 min) |
| `DG_MCP_PORT` | auto (8080–8099) | Force a specific MCP server port |

---

## Self-Update

The launcher checks for updates on every run and auto-updates silently. To force an update:
```bash
graperoot --update
```

To disable auto-update (shows a notice instead):
```bash
graperoot --no-auto-update
```

To re-enable:
```bash
graperoot --auto-update
```

Current version: **3.10.19**

---

## Telemetry

GrapeRoot collects **anonymous crash reports** to help us fix bugs. What's sent:

- Error type and which step failed (e.g. "scan", "mcp start")
- OS and Python version
- GrapeRoot version

What's **never** sent: your code, file paths, project names, prompts, or any personal data.

Telemetry is on by default. To opt out:
```bash
graperoot --no-telemetry    # disable
graperoot --telemetry       # re-enable
```

---

## Troubleshooting

### "MCP Server Connection Failed"

Always use `dgc` instead of `claude` directly. `dgc` starts the MCP server automatically.

```bash
# Fix:
claude mcp remove dual-graph
dgc   # re-registers everything
```

### Full troubleshooting guide

See [TROUBLESHOOTING.md](./TROUBLESHOOTING.md) or [graperoot.dev/docs](https://graperoot.dev/docs).

---

## Contributing

The launcher scripts (`bin/`) are open source under Apache 2.0. PRs welcome — bug fixes, new AI assistant support, install improvements, docs.

**Note:** The graph engine (`graperoot` pip package) is proprietary. The launchers and tooling in this repo are fully open source.

---

## Community

Have a question, found a bug, or want to share feedback?

**[Join the Discord →](https://discord.com/invite/YwKdQATY2d)**

---

## Star History

<a href="https://star-history.dera.page/#kunal12203/GrapeRoot&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://star-history.dera.page/svg?repos=kunal12203/GrapeRoot&type=date&legend=top-left" />
 </picture>
</a>

---

## License

Launcher scripts and tooling in this repository: [Apache License 2.0](./LICENSE)

The `graperoot` graph engine (PyPI): proprietary. See [graperoot.dev](https://graperoot.dev).

---

<div align="center">

Made with ❤️ · [graperoot.dev](https://graperoot.dev) · [Discord](https://discord.com/invite/YwKdQATY2d)

</div>
