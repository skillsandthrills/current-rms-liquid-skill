# Example layouts

Complete, importable Current-RMS document layout files in the exact export format (`*** LAYOUT SECTION ***` sections). Sanitized: all data comes from Liquid objects, nothing company-specific.

| File | Module | Demonstrates |
|---|---|---|
| `opportunity-quotation.txt` | Opportunity | Canonical items loop (subtotal/group/item branch), header/body/footer/stylesheet sections, layout attributes (colors, fields, flags), schedule handling, `{% cycle %}` striping, PDF-safe float/table CSS, page numbers |
| `barcode-label.txt` | Product | Custom label-printer page size, `qrcode` / `code128B` / `base64` barcode filters, per-asset loop, `page-break-inside: avoid` |

To use one: copy the file contents, then in Current-RMS go to System Setup → Document Layouts → import/paste into a new layout (or use these as a structural starting point when asking an AI assistant for a new document).
