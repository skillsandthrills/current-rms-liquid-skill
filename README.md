# Current-RMS Liquid — Claude Skill

A [Claude Code / Claude.ai skill](https://docs.claude.com/en/docs/claude-code/skills) that teaches Claude the **Current-RMS dialect of Liquid**, so AI-generated document layouts and discussion templates stop using Shopify-only objects, filters, and tags that don't exist in Current-RMS.

## Why

Liquid is used by many platforms (Shopify, Jekyll, Zendesk…), and most Liquid content online is Shopify-specific. Without guardrails, AI assistants routinely emit `| money`, `{% render %}`, `product.title`, `line_items`, and other Shopify vocabulary — which either errors or **silently renders blank** on a real quotation or invoice.

This skill provides:

- **Rule 0**: an explicit deny-list of Shopify-isms with the correct Current-RMS equivalents
- The complete documented **filter, tag, and operator** sets — anything else is off-limits
- **Root object tables** per module (opportunity document layouts use `order`, discussion templates use `opportunity`, invoices use `invoice`, …)
- The classic gotchas: boolean custom fields return `"Yes"`/`"No"` strings, operators evaluate right-to-left, `layout_flags` are read as `attributes.flags`, `'now'` is UTC, statuses are numeric codes
- **PDF renderer constraints** (no flexbox/grid/columns — table-based layout only)
- A full offline reference: every documented object with its complete attribute allow-list

## Install

**Claude Code (Mac/Linux):**

```bash
git clone https://github.com/skillsandthrills/current-rms-liquid-skill.git ~/.claude/skills/current-rms-liquid
python3 ~/.claude/skills/current-rms-liquid/scripts/fetch-references.py
```

**Claude Code (Windows, PowerShell):**

```powershell
git clone https://github.com/skillsandthrills/current-rms-liquid-skill.git $env:USERPROFILE\.claude\skills\current-rms-liquid
python $env:USERPROFILE\.claude\skills\current-rms-liquid\scripts\fetch-references.py
```

The second command downloads the detailed reference pages from the official Current-RMS documentation into `references/` (see [Attribution](#attribution) for why they aren't bundled). Restart Claude Code afterwards. The skill activates automatically whenever a task mentions Current-RMS templates, or invoke it directly with `/current-rms-liquid`.

**Claude.ai (web):** run the fetch script locally first, then zip the folder and upload it under Settings → Capabilities → Skills (paid plans).

## Updating

```bash
cd ~/.claude/skills/current-rms-liquid
git pull
python3 scripts/fetch-references.py   # re-fetches the latest official docs
```

## Structure

```
SKILL.md                      # Core dialect rules Claude loads when the skill triggers
references/
  object-index.md             # Every object + complete attribute allow-list
  verified-in-production.md   # Export file formats + undocumented syntax verified in real layouts
  objects/                    # Full per-object reference (fetched at install)
  filters.md, tags.md, ...    # Syntax references (fetched at install)
scripts/
  fetch-references.py         # Downloads + cleans the official docs (stdlib only)
```

## Contributing

Issues and PRs welcome — especially:

- Shopify-isms you've caught an AI generating (they go on the Rule 0 deny-list)
- Undocumented behavior you've verified in a real Current-RMS system

## Attribution

This is an **unofficial community skill**, not affiliated with or endorsed by Current RMS. The detailed reference pages are © Current RMS and are therefore not redistributed in this repository — `scripts/fetch-references.py` downloads them from the [official Liquid syntax documentation](https://current-rms.gitbook.io/liquid-syntax) onto your own machine at install time. The skill's own content (SKILL.md, scripts) is MIT-licensed.
