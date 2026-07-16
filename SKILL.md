---
name: current-rms-liquid
description: Write and debug Liquid markup for Current-RMS document layouts and discussion templates (quotations, rental agreements, invoices, delivery notes, pull sheets, PDFs). Use whenever the task involves Current-RMS, Current RMS, or CurrentRMS templates. Current-RMS Liquid is NOT Shopify Liquid — this skill enforces the documented Current-RMS dialect so generated templates don't reference objects, filters, or tags that don't exist.
---

# Current-RMS Liquid

Current-RMS (rental management software) uses the Ruby Liquid template engine for **document layouts** (HTML → PDF: quotes, rental agreements, invoices, delivery notes) and **discussion templates** (emails/messages). It shares Liquid's basic syntax with Shopify but has a **completely different object model and its own filter set**. Most Liquid content online is Shopify-specific and will produce broken Current-RMS templates.

## Rule 0 — never use Shopify vocabulary

These are the most common hallucinations. None of them exist in Current-RMS:

| ❌ Shopify (does not exist) | ✅ Current-RMS equivalent |
|---|---|
| `{{ x \| money }}`, `money_with_currency`, `money_without_currency` | `{{ x \| currency }}` |
| `{{ product.title }}`, `product.price`, `cart`, `collection`, `shop` | `{{ item.name }}`, `{{ item.price }}` inside `{% for item in order.items %}` |
| `{% render %}`, `{% include %}`, `{% section %}`, `{% snippet %}` | Not available — write everything inline in one layout |
| `{% form %}`, `{% paginate %}`, `{% schema %}`, `{% style %}`, `{% liquid %}`, `{% echo %}` | Not available |
| `img_url`, `asset_url`, `asset_img_url`, `file_url`, `stylesheet_tag`, `script_tag` | Not available — use full external URLs in plain HTML `<img>`/`<link>` tags |
| `handleize`, `json`, `t` (translation), `pluralize`, `weight_with_unit` | Not available |
| `where`, `map`, `escape`, `sort_by`, `multiply` | Unverified or nonexistent in Current-RMS — do not rely on them (`multiply` is a common hallucination; use `times`) |
| `customer.orders`, `order.line_items` | `member.opportunities`, `order.items` |

**Vocabulary tiers — how to decide if something is allowed:**

1. **Documented in this skill's `references/`** → safe, use freely.
2. **Verified in production** (`references/verified-in-production.md`) — undocumented but confirmed working in real layouts: `split`, `join`, `replace`, `slice`, `strip`, `url_encode`, `default`, `truncatewords`, two-arg `truncate`, `.size`, barcode filters `qrcode`/`code128B`/`base64`, `{% break %}`, `{% raw %}`, `forloop.index0`, array indexing → safe.
3. **Anything else** — including standard-Liquid filters not on either list, and any attribute not in `references/object-index.md` or `references/verified-in-production.md` — → **do not emit it.** If it seems genuinely necessary, flag it in your response as unverified and tell the user to test it in the document preview before relying on it. Never silently include unverified markup.

An undefined object in Liquid renders as *empty output, not an error* — a wrong attribute name produces a silently blank field on a real quote or invoice. Treat unverified names as bugs even though they "work."

## Root objects by context

The root variable depends on which module the layout/template is created against. Getting this wrong is the #2 error after Shopify vocabulary.

| Context | Root objects |
|---|---|
| Opportunity **document layout** (quote, rental agreement, delivery note) | `order` (the opportunity), `order.items`, `order.member` / `customer`, `company` (your business), `user` / `current_user` (rendering user), `owner_user` (opportunity owner), `order.store` (branch), `attributes` |
| Opportunity **discussion template** (email) | `opportunity` (not `order`!), `customer`, `current_user`, `current_store`, and `{{ document_approval_url }}` — the link to the online quote/agreement approval page (essential in quote/agreement emails) |
| Invoice **discussion template** (email) | `invoice`, `customer`, `current_user`, `current_store` |
| Invoice document layout | `invoice`, `invoice.items`, `invoice.sources` (source opportunities), `company` |
| Project layout | `project`, `project.opportunities` |
| Purchase order layout | `purchase_order`, `purchase_order.items` |
| Inventory/stock check | `stock_check`, `stock_check.items` |
| Quarantine | `quarantine`, `quarantine.source`, `quarantine.next_booking` |
| People/organizations | `member`, `organisation` (British spelling!), `contact`, `user`, `venue`, `vehicle` |

Common loop variables established by convention: `item` (opportunity/invoice items), `asset`, `accessory`, `cost`, `surcharge`, `transaction`, `tax`, `activity`, `attachment`, `participant`, `period`, `stock_level`.

Before writing a template, open `references/object-index.md` to confirm every attribute you plan to use, then the specific file in `references/objects/` for access patterns and examples.

## Documented filters — the complete list

Anything not on this list or in `references/verified-in-production.md` is tier 3 (do not emit).

- **Formatting:** `currency`, `number` / `number:N` (decimal places), `localedate`, `localedatetime`, `timezone:"Region/City"`, `date:"%strftime"`, `newline_to_br`, `markdown`, `bool_to_word` (true/false → localized Yes/No), `to_words` (number → words, for invoices)
- **String:** `append:"x"`, `prepend:"x"`, `capitalize`, `upcase`, `downcase`, `remove:"x"`, `remove_first:"x"`, `truncate:N`
- **Math** (math is done with filters, not operators): `plus`, `minus`, `times`, `divided_by`, `modulo`, `ceil`, `floor`, `round`
- **Array:** `first`, `last`, `sort`

## Documented tags — the complete list

`{% comment %}`, `{% if %}` / `{% elsif %}` / `{% else %}`, `{% unless %}`, `{% for %}` (with `forloop` object), `{% cycle %}`, `{% assign %}`, `{% capture %}`, `{% case %}` / `{% when %}`.

**Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`, `and`, `or`, `contains` (strings only — cannot search arrays of objects). No parentheses; multiple `and`/`or` evaluate **right to left**, which regularly surprises people — split complex conditions into nested `if`s instead.

## Money, numbers, dates

- Raw numeric attributes output like `120.0` — always pipe totals/prices through `| currency` (uses the system's currency symbol) or `| number:2`.
- Dates output as `YYYY-MM-DD HH:MM:SS` (UTC). Use `| localedate` / `| localedatetime` (respects user's locale — what default documents use), or build your own with `| date:"%a, %-d %b %Y"` (Ruby strftime; see `references/date-formats.md`).
- `{{ 'now' }}` returns UTC — chain `| timezone:"America/New_York"` before the date filter for local time.
- Opportunity `status` is a numeric code: 0 Open, 1 Provisional, 5 Reserved, 20 Active, 40 Completed, 50 Canceled, 60 Lost, 70 Dead, 80 Postponed. `{{ order.status_name }}`-style name attributes exist on most objects — check the object file rather than hardcoding code→name mappings when a name attribute is available.

## Custom fields

- Access by **Document Layout Field Name** (System Setup > Custom Fields) — usually the field name lowercased with underscores: "Test Date" → `test_date`.
- Access path depends on the module the field was created against: opportunity field on an opportunity doc → `{{ order.field_name }}`; organization field → `{{ customer.field_name }}`; product field inside the items loop → `{{ item.product.field_name }}`.
- **Boolean custom fields return the strings `"Yes"` / `"No"` / blank — never `true`/`false`.** Compare with `{% if customer.rented_before == "No" %}`. (Layout *flags* are different: they return real `true`/`false`.)
- Multi-select fields return a comma-separated string — check with `contains`.
- Custom field names are account-specific. If the user hasn't confirmed a field name exists in their system, say so and ask them to check System Setup > Custom Fields.

## Layout attributes (front matter)

Document layouts start with YAML front matter defining `name`, `module`, `page_size`, `orientation`, `margin`, plus user-configurable attributes:

- `fields:` (text boxes) → `{{ attributes.fields.x }}`
- `colors:` (color pickers, hex or HTML color names) → `{{ attributes.colors.x }}` — typically interpolated in CSS
- `layout_flags:` (checkboxes, `'true'`/`'false'` in quotes) → accessed as `{{ attributes.flags.x }}` — **defined as `layout_flags` but read as `flags`**, and they compare against real booleans: `{% if attributes.flags.show_images == true %}`

Static content that might change (bank details, disclaimers, T&Cs) belongs in an attribute field, not hardcoded HTML. See `references/attributes-front-matter.md`.

## Layout file structure (exports)

Exported/imported document layouts are one file with four `*** LAYOUT SECTION ***` blocks — `header`, `body`, `footer`, and `stylesheet` — each with its own `---` mini front matter, after the main front matter (which also supports `states:`, `statuses:`, `types:`, `filename_fields:`, and `page_size: Custom` + `page_width`/`page_height` in mm for label printers). Liquid works inside the stylesheet section too (`color: {{ attributes.colors.body_text }};`). Footer page numbers: `Page <span class="page">1</span> of <span class="topage">1</span>`.

Exported **discussion templates** (emails) are a single HTML body with front matter `name`, `module`, and `subject:` — **the subject line supports Liquid** (`subject: 'Quote: "{{ opportunity.name }}"'`). Emails must use email-safe HTML: inline styles, nested tables, no external CSS reliance. See `references/verified-in-production.md` for both formats.

## PDF renderer constraints (document layouts)

The HTML→PDF converter is an old WebKit-era engine. Violating these produces PDFs that don't match the browser preview:

- **No CSS flexbox, no CSS columns/grid, no animations, no iframes/embeds.** Use `<table>`-based layout and floats — this is the #1 cause of "looks right in preview, broken in PDF."
- Add vendor prefixes for anything modern (Autoprefixer target `Chrome >= 13`).
- Layouts have **header / body / footer** sections; header and footer repeat on **every** page and can't vary per page. No cover pages with different headers.
- Content cannot be pinned to the bottom of the body (dynamic length) — bottom-of-page content belongs in the footer.
- Browser preview body has `id="print_preview"` — use `body#print_preview { }` for preview-only CSS and `body:not(#print_preview) { }` for PDF-only CSS.
- Web fonts (Google Fonts) may render with kerning/spacing glitches in PDF — tell the user to test-preview any custom font.

## Workflow for writing a template

1. Identify the target: which module (opportunity/invoice/project/...) and which kind (document layout vs discussion template). This decides the root objects.
2. Read `references/object-index.md` and the relevant `references/objects/*.md` files for every object you'll touch.
3. Draft using only tier-1/tier-2 vocabulary. Use `{% comment %}` blocks to annotate sections. Guard optional data with `{% if x == blank %}` checks.
4. For document layouts: include front matter, table-based CSS (no flexbox), and put changeable text in attribute fields.
5. Self-check before delivering — grep your own output for the forbidden list in Rule 0, verify every `object.attribute` pair appears in the object index, verify every filter and tag is on the documented lists.
6. Tell the user to test via the layout preview in Current-RMS (Documents section) and to check the PDF output, not just the browser preview.

## Reference files

| File | Contents |
|---|---|
| `references/verified-in-production.md` | Export file formats (layouts + discussion templates), undocumented-but-verified filters/tags/attributes, canonical patterns |
| `references/object-index.md` | Every object with its complete attribute list — the allowlist |
| `references/objects/*.md` | Full per-object docs: access patterns per module, examples, outputs |
| `references/filters.md`, `references/tags.md`, `references/operators.md` | Full syntax docs with examples |
| `references/date-formats.md` | strftime tokens, `'now'`, timezones |
| `references/custom-fields.md` | Custom field access, data types, boolean gotcha |
| `references/attributes-front-matter.md` | Front matter format, fields/colors/flags |
| `references/pdf-limitations.md` | PDF renderer constraints in full |
| `references/special-items.md` | Special items, serialised containers/components |
| `references/consolidation.md`, `references/deal-pricing.md` | Consolidated opportunities, deal pricing |
| `references/best-practices.md` | Indentation, commenting, troubleshooting |

If the files above (other than `object-index.md`) are missing, they haven't been fetched yet — run `python3 scripts/fetch-references.py` from the skill directory to download them from the official docs.

Official docs (source of these references): https://current-rms.gitbook.io/liquid-syntax — machine-readable index at `/llms.txt`, any page fetchable as Markdown by appending `.md`. When in doubt, fetch the live page.
