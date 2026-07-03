# tafsiri-mcp

[![tafsiri-mcp Glama score](https://glama.ai/mcp/servers/gabrielmahia/tafsiri-mcp/badges/score.svg)](https://glama.ai/mcp/servers/gabrielmahia/tafsiri-mcp)
[![smithery badge](https://smithery.ai/badge/@gabrielmahia/tafsiri-mcp)](https://smithery.ai/server/@gabrielmahia/tafsiri-mcp)


---
**Compatible with `claude-sonnet-5`** (released 2026-06-30) — Anthropic's most agentic
Sonnet yet. Runs multi-step tool chains end-to-end without stopping short.
Install: `pip install tafsiri-mcp` · Use with any MCP client.

---


> Kenya translation infrastructure via MCP — Swahili/English glossary, Kikuyu guide, Luo guide, official document terms, language detection, civic terminology. 6 tools.

[![PyPI](https://img.shields.io/badge/PyPI-v0.1.0-blue?logo=pypi)](https://pypi.org/project/tafsiri-mcp/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://github.com/gabrielmahia/tafsiri-mcp)
[![Thesis Layer](https://img.shields.io/badge/Thesis_Layer-L5-purple)](https://gabrielmahia.github.io/nairobi-stack)

**1st world equivalent:** DeepL, Google Translate API, Masakhane

## Install
```bash
pip install tafsiri-mcp
```

## Tools (6)
| Tool | Description |
|------|-------------|
| `swahili_english_glossary` | Swahili-English civic and government glossary |
| `kikuyu_language_guide` | Kikuyu (Gĩkũyũ) language basics and resources |
| `luo_language_guide` | Luo (Dholuo) language basics and resources |
| `official_document_glossary` | Kenya official document terminology and costs |
| `language_detection_guide` | Language detection and translation resources for Kenya |
| `civic_terminology_swahili` | Swahili translations of Kenya civic and legal processes |


→ [The Nairobi Stack](https://gabrielmahia.github.io/nairobi-stack)

## License
MIT © Gabriel Mahia | contact@aikungfu.dev

## Part of the East Africa Coordination Stack

This MCP server is one of 32 tools in the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All 32 servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).
