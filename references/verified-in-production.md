# Verified in production — beyond the official docs

Syntax and attributes below are **not in the official Current-RMS Liquid documentation** but have been verified working in real production document layouts. Prefer documented syntax when equivalent; use these when needed.

## Document layout export file format

Exported layouts are a single text file with four sections separated by `*** LAYOUT SECTION ***` markers, each with its own mini front matter:

```
---
name: 'My Quotation'
module: Opportunity                  # Opportunity | Invoice | Project | PurchaseOrder | Product | ...
states: ["Quotation", "Order"]       # which opportunity states the doc is offered for
statuses: ["Open", "Provisional"]    # which statuses
types: ["Invoice", "Credit"]         # Invoice module only
page_size: A4                        # A4 | Letter | Custom
page_width: 120                      # only with page_size: Custom (mm)
page_height: 24
orientation: Portrait
margin: { top: 10, left: 10, bottom: 15, right: 10 }
colors:   { body_text: '#666666', ... }     # -> {{ attributes.colors.x }}
fields:   { closing_text: '' }              # -> {{ attributes.fields.x }}
layout_flags: { show_images: 'true' }       # -> {{ attributes.flags.x }}
filename_fields: ["number", "subject", "document_name", "id"]
active: true
---

*** LAYOUT SECTION ***
---
section: header
---
...repeated at top of every PDF page...

*** LAYOUT SECTION ***
---
section: body
---
...main content...

*** LAYOUT SECTION ***
---
section: footer
---
...repeated at bottom of every page...

*** LAYOUT SECTION ***
---
section: stylesheet
---
<style> ... Liquid works inside CSS too ... </style>
```

- **Page numbers** (footer): `Page <span class="page">1</span> of <span class="topage">1</span>` — the renderer replaces the contents of `.page` and `.topage`.
- Custom page sizes are used for label/tag printers (e.g. 120×24 prep tags, 62×35 barcode labels).
- `<link rel="stylesheet" href="...">` to external fonts (Typekit/Google) works; test PDF kerning.
- HTML form elements (`<input type="checkbox">`, `<textarea>`) render in the browser preview — useful for interactive checklists viewed on tablets (not meaningful in PDF).

## Filters verified working (undocumented)

| Filter | Example | Notes |
|---|---|---|
| `split` | `{{ list \| split: ',' }}` | returns array; combine with `first`/`last`/indexing |
| `replace` | `{{ order.name \| replace: ' ', '%20' }}` | also seen replacing substrings in URLs |
| `slice` | `{{ phone \| slice: 0, 3 }}` | substring by offset,length |
| `url_encode` | `{{ text \| url_encode \| replace: '+', '%20' }}` | for mailto:/query strings; encodes spaces as `+`, hence the follow-up replace |
| `default` | `{{ x \| default: "0.00" }}` | fallback for blank values |
| `truncatewords` | `{{ order.name \| truncatewords: 3, "" }}` | second arg replaces the "..." suffix |
| `truncate` (2-arg) | `{{ s \| truncate: 2, '' }}` | first N chars with custom/empty ellipsis |
| `qrcode` | `{{ asset.url \| qrcode }}` | emits inline QR SVG (Current-RMS specific) |
| `code128B` | `{{ asset.asset_number \| code128B }}` | Code 128 barcode SVG (Current-RMS specific) |
| `base64` | `<img src="data:image/svg+xml;base64,{{ asset.asset_number \| code128B \| base64 }}">` | base64-encode, pairs with barcode filters |

**String→number cast:** attributes that return numeric strings (e.g. `item.sku_dealer_price`) can be cast with `| plus: 0` before math: `{% assign n = item.sku_dealer_price | plus: 0 %}`.

## Tags & operators verified working (undocumented)

- `{% break %}` — exit a `for` loop early.
- `{% raw %} ... {% endraw %}` — emit literal `{{ }}`/`{% %}` (needed for prebuilt URLs containing braces).
- `<>` — not-equals alias for `!=` (legacy Liquid), seen in production: `{% if x <> blank %}`. Prefer `!=` in new code.
- `forloop.index0` / `forloop.index` — loop counters inside `{% for %}`.
- Array indexing: `{{ myArray[forloop.index0] }}` works (variable index).
- `{% cycle 'group name': 'a', 'b' %}` — named cycle groups for row striping.

## Objects & attributes verified working (undocumented or easy to miss)

**Opportunity (`order`):**
- `order.order_id_code` — internal ID for deep links: `https://<subdomain>.current-rms.com/opportunities/{{ order.order_id_code }}`
- `order.store.name / .email / .telephone` and flat `order.store_name / store_email / store_telephone / store_website / store_address`
- `order.billing_address`, `order.billing_address_name`, `order.delivery_address(_name)`
- `order.customer_collecting`, `order.customer_returning` (booleans)
- `order.schedule_type_is_standard?` / `order.schedule_type_is_extended?` and the full schedule pairs: `prep/load/deliver/setup/show/takedown/collect/unload/deprep` + `_starts_at`/`_ends_at`
- `order.charge_starts_at/_ends_at`, `order.chargeable_days`, `order.replacement_charge_total`
- `order.rental_charge_total`, `order.sale_charge_total`, `order.service_charge_total`, `order.surcharge_total`, `order.deal_exists?`
- `order.participants` (each with `.type` — `'User'`/`'Organisation'` — `.name`, `.contacts`)
- `order.product_assets` (each with `.return_assets` → `.quantity_damaged/.quantity_lost/.quantity_sold`, `.product.replacement_charge`, `.barcode_number`, `.group_name`)
- `order.supplier_item_assets` (sub-rented assets, each with `.supplier_name`, `.opportunity_item`)
- `order.services` — loop of service items only

**Opportunity items (`item` in the loop):** `is_subtotal?`, `subtotal`, `subtotal_name`, `is_group?`, `is_item?`, `is_accessory?`, `is_principal?`, `is_sale?`, `is_service?`, `accessory_mode_name` (`"accessory"`/component), `accessory_mode_is_component?`, `depth`, `depth_padding`, `image_url`, `transaction_type_name` (`"Rental"`/`"Sale"`/`"Purchase"`...), `chargeable_days`, `discount_percent`, `discount_amount`, `discounted_price`, `surcharge_amount`, `service_unit_name`, `sku`, `supplier_reference`, `item.assets` (assigned asset records).

**Invoice (`invoice`):** `balance` (remaining due; negative = refund), `transaction_total` (payments received), `type_name`, `taxes` (loop: `.name`, `.rate`, `.taxable_charge`, `.tax`), `sources` (source opportunities: `.starts_at`, `.ends_at`, `.name`, `.number`), `store.*`, and the same address/total attributes as `order`.

**Users:** `user` (the rendering user / rental agent: `.name`, `.email`, `.telephone`), `current_user`, `owner_user` (opportunity owner).

**Company:** `company.icon_url` (your logo), `company.email`, `company.address.city / .county`, `company.single_line_address`.

## The canonical items-loop pattern

Every real items table uses this three-way branch — copy it:

```liquid
{% for item in order.items %}
  {% if item.is_subtotal? %}
    {% if item.depth == 1 %}
      <tr><td colspan="5">Total for {{ item.subtotal_name }}:</td>
          <td>{{ item.subtotal | currency }}</td></tr>
    {% endif %}
  {% elsif item.is_group? %}
    <tr><td colspan="6" style="padding-left: {{ item.depth_padding }}px;">
      <h4>{{ item.name }}</h4></td></tr>
  {% elsif item.is_item? %}
    {% if item.is_accessory? and item.accessory_mode_is_component? and item.charge_total == 0 %}
      {% comment %} hide zero-charge components {% endcomment %}
    {% else %}
      <tr><td style="padding-left: {{ item.depth_padding }}px;">{{ item.name }}</td>
          <td>{{ item.quantity | number }}</td>
          <td>{{ item.price | number:2 }}</td>
          <td>{{ item.charge_total | number:2 }}</td></tr>
    {% endif %}
  {% endif %}
{% endfor %}
```

Use `item.depth_padding` (a px number) for hierarchy indentation, and `{% cycle %}` for row striping.
