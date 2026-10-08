# tafsiri-mcp
<!-- mcp-name: io.github.gabrielmahia/tafsiri-mcp -->

## Why This Exists

Kenyan civic and legal life happens in Swahili, Kikuyu, Luo and English at once, but the terminology that matters — what a succession petition is called, what a gazette notice means — rarely appears in general translation tools. Getting a civic term wrong in the wrong language has consequences a mistranslated menu does not.

## Install

```bash
pip install tafsiri-mcp
```

## Tools (6)

- **`swahili_english_glossary`** — Translate civic and government terminology between Swahili and English.  
  <sub>args: term</sub>
- **`kikuyu_language_guide`** — Return linguistic information and key phrases for the Kikuyu language.  
  <sub>args: term</sub>
- **`luo_language_guide`** — Return linguistic information and key phrases for the Luo language.  
  <sub>args: term</sub>
- **`official_document_glossary`** — Return standard terminology for Kenya official documents and certificates.  
  <sub>args: document_type</sub>
- **`language_detection_guide`** — Identify which Kenyan language a text sample is written in.  
  <sub>args: text_sample</sub>
- **`civic_terminology_swahili`** — Return Swahili terminology for Kenya government processes and civic interactions.  
  <sub>args: process</sub>

## Example

```python
from tafsiri_mcp.server import swahili_english_glossary

result = swahili_english_glossary(term='urithi')
# civic term, translation, how it is used, documents needed
```

## Claude Desktop Integration

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "tafsiri-mcp": {
      "command": "python",
      "args": ["-m", "tafsiri_mcp.server"]
    }
  }
}
```

## Data & Disclaimers

Glossaries are reference material for civic navigation, not certified translation. For court filings or official submissions, use a sworn translator.

Every tool response carries a `source` field. Responses labelled `DEMO` are
illustrative reference data, not a live feed — verify against the authority
named in the response before acting on it.

## Part of the East Africa Coordination Stack

This MCP server is part of the Kenya coordination infrastructure.
Connect it to [`africa-coord-bus`](https://github.com/gabrielmahia/africa-coord-bus) —
the coordination event bus that routes signals between domains automatically.

```bash
pip install africa-coord-bus
```

All servers: [pypi.org/user/gmahia](https://pypi.org/user/gmahia/)
Live demo: [coord-cascade-demo](https://github.com/gabrielmahia/coord-cascade-demo)

## IP & Collaboration

MIT licensed. Feedback via GitHub Issues only — pull requests are not accepted. Demo data is labeled DEMO and is not suitable for operational decisions. Full policy: [docs/architecture/IP_POLICY.md](docs/architecture/IP_POLICY.md). Security reports: see [SECURITY.md](SECURITY.md).

<!-- interconnect:v1 -->
## Part of the East Africa coordination stack

- **Install & run:** `pip install reli-cli && reli list` — the MCP servers on the [official MCP Registry](https://registry.modelcontextprotocol.io) under `io.github.gabrielmahia`
- **Evaluate any model on Swahili agent tasks:** [kipimo](https://github.com/gabrielmahia/kipimo) · [dataset](https://huggingface.co/datasets/gmahia/kipimo) · [leaderboard](https://huggingface.co/spaces/gmahia/kipimo-leaderboard)
- **Coordinate across servers:** [africa-coord-bus](https://pypi.org/project/africa-coord-bus/) — offline-first event bus with a built-in Kenya routing table
- **Datasets:** [huggingface.co/gmahia](https://huggingface.co/gmahia) · **Docs hub:** [nairobi-stack](https://github.com/gabrielmahia/nairobi-stack)

Model-agnostic by design: closed APIs, open-weight models, and small distilled models are all first-class citizens.
<!-- /interconnect:v1 -->
