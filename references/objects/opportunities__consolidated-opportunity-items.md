# Consolidated opportunity items

An item might appear on an opportunity in multiple places. The consolidated opportunity items object merges all opportunity items related to the same product or service into a single line. 

See: [Consolidation](https://current-rms.gitbook.io/liquid-syntax/information/consolidation.md)

### Objects that return consolidated opportunity items

#### `order.consolidated_items`

Returns consolidated items 

```
{% for item in order.consolidated_items %}
  {{ item.name }}
{% endfor %}
```

#### `order.consolidated_principal_opportunity_items`

Merges only opportunity items that are principal items. This means this doesn't return any accessories.

```
{% for item in order.consolidated_items %}
  {{ item.name }}
{% endfor %}
```

The consolidated opportunity items object is available anywhere you can access opportunity items.

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## `charge_excluding_tax_total`

Returns a consolidated opportunity item charge total excluding tax.

#### Input

```
{{ item.charge_excluding_tax_total }}
```

#### Output

```
50.0
```

> **Note:**
> Use [the currency filter or a number filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the number is formatted.

## `charge_including_tax_total`

Returns a consolidated opportunity item charge total including tax.

#### Input

```
{{ item.charge_including_tax_total }}
```

#### Output

```
120.0
```

## `charge_total`

Returns a consolidated opportunity item charge total. 

This may be including or excluding tax depending on the value of the “Catalog Prices” setting in System Preferences.

#### Input

```
{{ item.charge_total }}
```

#### Output

```
50.0
```

## `is_product?`

Returns `true` if a consolidated opportunity item is linked to a product record; `false` otherwise.

#### Input

```
{% item.is_product? %}
```

#### Output

```
true
```

## `is_rental?`

Returns `true` if a consolidated opportunity item is a rental charge, i.e. its transaction type is "Rental"; `false` otherwise.

#### Input

```
{{ item.is_rental? %}
```

#### Output

```
true
```

## `is_sale?`

Returns `true` if a consolidated opportunity item is for a sale charge, i.e. its transaction type is "Sale"; `false` otherwise.

#### Input

```
{{ item.is_sale? %}
```

#### Output

```
false
```

## `is_service?`

Returns `true` if a consolidated opportunity item is for a service charge, i.e. its transaction type is "Service"; `false` otherwise.

This doesn't determine necessarily whether an opportunity item is linked to a service record; a text item may have the transaction type "Service".

#### Input

```
{{ item.is_service? }}
```

#### Output

```
false
```

## `is_service_item?`

Returns `true` if an opportunity item is linked to a service record; `false` otherwise.

#### Input

```
{{ item.is_service_item? }}
```

#### Output

```
false
```

## `is_text_item?`

Returns `true` if an opportunity item is a text item; `false` otherwise.

#### Input

```
{{ item.is_text_item? }}
```

#### Output

```
true
```

## `name` <a href="#name" id="name"></a>

Returns an opportunity item's name.

#### Input <a href="#input-43" id="input-43"></a>

```
{{ item.name }}
```

#### Output <a href="#output-42" id="output-42"></a>

```
Robe RoboSpot
```

## `opportunity` <a href="#opportunity" id="opportunity"></a>

Returns opportunity objects for the opportunity that an opportunity item is related to.

When working with a document or discussion template on an opportunity record, you may simply wish to access the opportunity object as normal. For example, use `{{ order.name }}` to print the opportunity subject.

#### Input <a href="#input-44" id="input-44"></a>

```
{{ item.opportunity.name }}
```

#### Output <a href="#output-43" id="output-43"></a>

```
V-Blast Music Festival
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `product_stock_levels`

Returns stock level objects for opportunity item's related stock levels where:

* the item is a product
* it's bulk or serialized
* stock levels are in the same store
* stock levels have a stock type matching the opportunity item’s stock type (i.e. rental or sale)

> **Warning:**
> Keep in mind that this returns any stock levels that match the criteria above. Use [the `assets` object](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md#assets) to return allocated assets.

#### Input

```
{% for stock_level in item.product_stock_levels %}
  {{ stock_level.asset_number }}<br>
{% endfor %}
```

#### Output

```
ETC-001
ETC-002
ETC-003
```

See: [Stock level](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md)

## `quantity`

Returns the quantity of an opportunity item.

#### Input

```
{{ item.quantity }}
```

#### Output

```
1.0
```

## `revenue_group`

Returns the revenue group name for an opportunity item.

#### Input

```
{{ item.revenue_group }}
```

#### Output

```
Rental
```

## `surcharge_amount`

Returns the surcharge amount for an opportunity item. 

Surcharges are percentage or fixed fees that are applied to rental items. An opportunity item might have multiple surcharges applied.

Returns blank for groups, sale items, and service items. Returns an error for subtotals.

#### Input

```
{{ item.surcharge_amount }}
```

#### Output

```
120.0
```

## `tax_total`

Returns the tax total for an opportunity item. Works for items and groups.

#### Input

```
{{ item.tax_total }}
```

#### Output

```
50.0
```

## `transaction_type_name`

Returns the transaction type name for an opportunity item.

* Rental
* Sale
* Service

#### Input

```
{{ item.transaction_type_name }}
```

#### Output

```
Rental
```

## `use_chargeable_days`

Returns `true` if an opportunity item has overriden chargeable days. 

This will be the case where the opportunity has the "Chargeable Days" toggle set to YES.

#### Input

```
{{ item.use_chargeable_days }}
```

#### Output

```
true
```

---
*Source: [Consolidated opportunity items — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md)*
