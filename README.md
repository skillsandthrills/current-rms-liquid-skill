# Current-RMS Liquid — Claude Skill

A [Claude Code / Claude.ai skill](https://docs.claude.com/en/docs/claude-code/skills) that teaches Claude the **Current-RMS dialect of Liquid** so generated document layouts and discussion templates don't use Shopify-only objects, filters, or tags that don't exist in Current-RMS.

## Why

Liquid is used by many platforms (Shopify, Jekyll, Zendesk…), and most Liquid content online is Shopify-specific. Without guardrails, AI assistants routinely emit `| money`, `{% render %}`, `product.title`, `line_items`, and other Shopify vocabulary — which either errors or silently renders blank in Current-RMS documents.

This skill provides:

- **Rule 0**: an explicit deny-list of Shopify-isms with the correct Current-RMS equivalents
- The complete documented **filter, tag, and operator** sets (anything else is off-limits)
- **Root object tables** per module (opportunity docs use `order`, discussion templates use `opportunity`, etc.)
- All the classic gotchas: boolean custom fields returning `"Yes"`/`"No"` strings, right-to-left operator evaluation, `layout_flags` vs `attributes.flags`, UTC `'now'`, numeric status codes
- **PDF renderer constraints** (no flexbox/grid/columns — table-based layout only)
- A full offline reference: every documented object with its complete attribute allow-list, in `references/`

## Install

### Claude Code (Mac/Linux)

```bash
git clone https://github.com/<your-username>/current-rms-liquid-skill.git ~/.claude/skills/current-rms-liquid
```

Restart Claude Code. The skill activates automatically whenever a task mentions Current-RMS templates, or invoke it directly with `/current-rms-liquid`.

### Claude Code (Windows)

```powershell
git clone https://github.com/<your-username>/current-rms-liquid-skill.git $env:USERPROFILE\.claude\skills\current-rms-liquid
```

### Claude.ai (web)

Zip this folder and upload it as a skill under Settings → Capabilities → Skills (available on paid plans).

## Update

Reference content is distilled from the official Current-RMS Liquid documentation. To refresh after Current-RMS updates their docs:

```bash
cd ~/.claude/skills/current-rms-liquid && git pull
```

## Structure

```
SKILL.md                      # Core rules Claude loads when the skill triggers
references/
  object-index.md             # Every object + complete attribute allow-list
  objects/                    # Full per-object reference (40 objects)
  filters.md, tags.md, ...    # Syntax references
  pdf-limitations.md          # PDF renderer constraints
```

## Attribution

Reference material is derived from the official [Current-RMS Liquid syntax documentation](https://current-rms.gitbook.io/liquid-syntax) (© Current RMS). This is an unofficial community skill, not affiliated with Current RMS. Keep this repository **private** unless you have permission to redistribute the documentation content.
