# Current-RMS Liquid — Claude Skill

A [Claude skill](https://docs.claude.com/en/docs/claude-code/skills) that teaches Claude the **Current-RMS dialect of Liquid**, so AI-generated document layouts and discussion templates stop using Shopify-only objects, filters, and tags that don't exist in Current-RMS.

## Why

Liquid is used by many platforms (Shopify, Jekyll, Zendesk…), and most Liquid content online is Shopify-specific. Without guardrails, AI assistants routinely emit `| money`, `{% render %}`, `product.title`, `line_items`, and other Shopify vocabulary — which either errors or **silently renders blank** on a real quotation or invoice.

This skill provides:

- **Rule 0**: an explicit deny-list of Shopify-isms with the correct Current-RMS equivalents
- The complete documented **filter, tag, and operator** sets — anything else is off-limits
- **Root object tables** per module (opportunity document layouts use `order`, discussion templates use `opportunity`, invoices use `invoice`, …)
- The classic gotchas: boolean custom fields return `"Yes"`/`"No"` strings, operators evaluate right-to-left, `layout_flags` are read as `attributes.flags`, `'now'` is UTC, statuses are numeric codes
- **PDF renderer constraints** (no flexbox/grid/columns — table-based layout only)
- **Discussion template knowledge**: Liquid-enabled subject lines, `document_approval_url`, email-safe HTML rules
- A full offline reference: every documented object with its complete attribute allow-list

## 🚧 ⚙️ Install — Claude Desktop App 🚧 ⚙️ (no technical experience needed)

This is the easiest way to install if you've never used a terminal. You need the **Claude desktop app** — the skill cannot be installed from the claude.ai website in your browser.

**Step 1 — Get the Claude desktop app.**
Download it from [claude.ai/download](https://claude.ai/download) (Mac or Windows), install it, and sign in with your Claude account. If you already have the app, make sure it's up to date.

**Step 2 — Open a Claude Code window.**
In the desktop app's sidebar, click **Code** (the `>_` icon). This opens Claude Code — it looks like a normal Claude chat, but it can install skills and work with files. If it asks you to choose a folder, pick any folder (your Documents folder is fine — the skill installs globally, not into that folder).

**Step 3 — Add this skill's marketplace.**
Click into the message box at the bottom, paste this exactly, and press Enter:

```
/plugin marketplace add skillsandthrills/current-rms-liquid-skill
```

Claude will confirm the marketplace was added.

**Step 4 — Install the skill.**
Now paste this and press Enter:

```
/plugin install current-rms-liquid@current-rms-liquid-skill
```

If Claude asks you to confirm or trust the plugin, accept.

**Step 5 — Try it out.**
That's it. In the same window (or any new Claude Code chat), ask something like:

> *"Write a Current-RMS quotation document layout with our logo at the top, an equipment table, and totals with tax."*

Claude will automatically use the skill and produce a layout you can paste into Current-RMS under **System Setup → Document Layouts**. The first time you use it, Claude may spend a moment downloading the official Current-RMS reference pages — that's normal.

**Updating later:** paste `/plugin marketplace update current-rms-liquid-skill` into a Claude Code window, then reinstall with the Step 4 command.

## Install — Terminal (for developers)

The same two `/plugin` commands above work inside `claude` in any terminal. Or install manually:

```bash
git clone https://github.com/skillsandthrills/current-rms-liquid-skill.git
cp -r current-rms-liquid-skill/skills/current-rms-liquid ~/.claude/skills/
python3 ~/.claude/skills/current-rms-liquid/scripts/fetch-references.py
```

The fetch script downloads the detailed reference pages from the official Current-RMS documentation into `references/` (see [Attribution](#attribution) for why they aren't bundled). Restart Claude Code afterwards. The skill activates automatically whenever a task mentions Current-RMS templates, or invoke it directly with `/current-rms-liquid`.

## Structure

```
.claude-plugin/               # Marketplace + plugin metadata
skills/current-rms-liquid/
  SKILL.md                    # Core dialect rules Claude loads when the skill triggers
  references/
    object-index.md           # Every object + complete attribute allow-list
    verified-in-production.md # Export file formats + undocumented syntax verified in real layouts
    objects/                  # Full per-object reference (fetched on demand)
    filters.md, tags.md, ...  # Syntax references (fetched on demand)
  scripts/
    fetch-references.py       # Downloads + cleans the official docs (stdlib only)
```

## Contributing

Issues and PRs welcome — especially:

- Shopify-isms you've caught an AI generating (they go on the Rule 0 deny-list)
- Undocumented behavior you've verified in a real Current-RMS system

## Attribution

This is an **unofficial community skill**, not affiliated with or endorsed by Current RMS. The detailed reference pages are © Current RMS and are therefore not redistributed in this repository — `scripts/fetch-references.py` downloads them from the [official Liquid syntax documentation](https://current-rms.gitbook.io/liquid-syntax) onto your own machine. The skill's own content is MIT-licensed.
