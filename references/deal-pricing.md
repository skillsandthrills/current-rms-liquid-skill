# Deal pricing

Set [a deal price against opportunities or opportunity groups](https://help.current-rms.com/en/articles/1826147-set-a-deal-price-on-an-opportunity-or-group) to override the charge total with a figure that you specify. 

When you set a deal price, opportunity item charge totals are hidden in the web interface. Current RMS intelligently apportions revenue to your products, services, and assets based on their share of the deal price, but there's no accessible figure for the opportunity item charge total after deal price. This is because:

* the figure isn't relevant: you've told the system that you're doing a deal.
* revenue is apportioned to many decimal places: when rounding to two decimal places, there may be rounding issues.

Our default documents mirror the web interface and won't show opportunity item or group charge totals where they're part of a deal.

If you like, you may display the value before a deal price was applied in your document layouts and discussion templates.

#### Deal pricing impacts:

* [opportunity item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)
* [invoice item objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md)
* [opportunity item surcharge objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-surcharge.md)
* [opportunity objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)
* [invoice objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md)

## Detect a deal on an opportunity

### Deal exists

Where an opportunity is deal priced or includes a deal priced group, we say that a “deal exists” on it.

Use `order.deal_exists?` to detect whether a deal exists. It will return `true` or `false`.

### Opportunity “has deal”

When an opportunity is deal priced, we say that it “has deal”.

Use `order.opportunity_has_deal?` to detect whether an opportunity has a deal. It will return `true` or `false`.

> **Warning:**
> Where ~~`opportunity_has_deal?`~~ is `true`, `deal_exists?` will also be `true`. However, `deal_exists?` will be `true` when `opportunity_has_deal?` is `false` when the opportunity contains a deal priced group.

### Opportunity group “has deal”

When an opportunity group is deal priced, we say that it “has deal”. 

Use `item.group_has_deal?` in the `order.items` loop to detect whether a group has a deal. It will return `true` or `false`.

```markup
{% for item in order.items %}
  {% if item.is_group? %}
    {% if item.group_has_deal? %}
      <!-- This is a group with a deal -->
    {% endif %}
  {% endif %}
{% endfor %}
```

### Opportunity items “in a deal”

When opportunity items are deal priced, we say that they're “in a deal”.

Use `item.is_in_deal?` to in the `order.items` loop to detect whether an item is in a deal. It will return `true` or `false`.

```markup
{% for item in order.items %}
  {% if item.is_item? %}
    {% if item.is_in_deal? %}
      <!-- This is an item in a deal -->
    {% endif %}
  {% endif %}
{% endfor %}
```

If a deal is set on an opportunity, `item.is_in_deal?` will return `true` for all items on the opportunity. This includes group items.

If a deal is set on a group, `item.is_in_deal?` will return `true` for all items inside that group. This includes sub-groups. `item.is_in_deal?` will not return true for the group that has a deal.

## Detect a deal on an invoice

When you [create an invoice from an opportunity with a deal price](https://help.current-rms.com/en/articles/1871169-create-an-invoice-from-a-deal-priced-opportunity), the invoice is created slightly differently to an invoice created otherwise.

When you invoice by item, Current will create an invoice item for each tax class within a deal. These deal price line items will have a red “Deal Price” label and are styled as group items in the web interface, but are actually standard invoice items in the backend. We call these ”deal items”.

> **Note:**
> Keep in mind that, because deal items are standard invoice items, they will not be returned when iterating through group items in the `invoice.items` loop. 
> 
> You could use `{% if item.is_group? or item.is_deal_item? %}` to display deal items as groups on your invoices.

Use `item.is_deal_item?` in the `invoice.items` loop to detect whether an item is a deal item. This will return `true` or `false`.

Nested underneath a deal item, Current creates informational lines for items that are part of the deal. We say that these are “in a deal”.

Use `item.is_in_deal?` in the `invoice.items` loop to detect whether an item is an informational line for items that are part of a deal.

> **Note:**
> You cannot use `has_deal` or `deal_exists` on an invoice. These are opportunity objects.

## Objects that return `nil`

When part of a deal, opportunity item objects that display pricing information now return `nil`. This means that they won't display anything on document layouts or discussion templates.

To return the value of the object before it was part of a deal, prefix with `original_`.

### Opportunity item

| Object that returns `nil`          | Equivalent object                           |
| ---------------------------------- | ------------------------------------------- |
| `price`                            | `original_price`                            |
| `discount_percent`                 | `original_discount_percent`                 |
| `discounted_price`                 | `original_discounted_price`                 |
| `discounted_amount`                | `original_discounted_amount`                |
| `discount_total`                   | `original_discount_total`                   |
| `unit_charge_amount`               | `original_unit_charge_amount`               |
| `charge_amount_excluding_discount` | `original_charge_amount_excluding_discount` |
| `charge_amount`                    | `original_charge_amount`                    |
| `surcharge_amount`                 | `original_surcharge_amount`                 |
| `charge_total`                     | `original_charge_total`                     |
| `charge_excluding_tax_total`       | `original_charge_excluding_tax_total`       |
| `tax_total`                        | `original_tax_total`                        |
| `charge_including_tax_total`       | `original_charge_including_tax_total`       |

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

### Opportunity item surcharge

| Object that returns `nil` | Equivalent object |
| ------------------------- | ----------------- |
| `charge`                  | `original_charge` |

See: [Opportunity item surcharges](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-surcharge.md)

## Opportunity charge totals before deal

You may also prefix opportunity charge totals with `original_` to return the value before a deal price.

| Object                       | Equivalent object                     |
| ---------------------------- | ------------------------------------- |
| `charge_total`               | `original_charge_total`               |
| `charge_excluding_tax_total` | `original_charge_excluding_tax_total` |
| `charge_including_tax_total` | `original_charge_including_tax_total` |
| `tax_total`                  | `original_tax_total`                  |
| `discount_total`             | `original_discount_total`             |
| `rental_charge_total`        | `original_rental_charge_total`        |
| `sale_charge_total`          | `original_sale_charge_total`          |
| `service_charge_total`       | `original_service_charge_total`       |
| `surcharge_total`            | `original_surcharge_total`            |

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## Percentage discounts

When you set a deal price, you may still set a percentage discount on opportunity items -- including discounting items that are deal priced.

Our default documents don't show the saving from deal pricing. This is because `discount_total` returns the total discount obtained using percentage discounting of items not in a deal.

On opportunity and invoice documents or discussion templates:

* `discount_total` shows the total discount using percentage discounting of items not in a deal.
* `deal_discount_total` shows the total discount from items that are part of a deal.
* `combined_discount_total` shows the total discount from both percentage and deal discounting.

---
*Source: [Deal pricing — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)*
