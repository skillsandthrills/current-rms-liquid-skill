# Opportunity items

Opportunity items are items that you've added to an opportunity.

When printed, an items list will consist of a group, the items inside the group, and then a subtotal row.

To build this in Liquid, you'd use a similar structure:

```markup
{% for item in order.items %}
  {% if item.is_group? %}
    {{ item.name }} <!-- Group name -->
  {% elsif item.is_item? %}
    {{ item.name }} <!-- Item name -->
  {% elsif item.is_subtotal? %}
    {{ item.subtotal_name }} <!-- Subtotal name, i.e. group name -->
  {% endif %}
{% endfor %}
```

There's no subtotal row in the web interface. Subtotal items are included in the opportunity items object to make it easy to include and style a subtotal row. A subtotal item iterates after a group and its items have iterated. They're purely informational rows, so most of the objects below will return "Liquid error" when used with a subtotal item.

Opportunity item objects are always accessed within a forloop that iterates for each item.

### Document layouts

The `item` object can be accessed in document layouts created against the following modules:

#### Opportunity

```
{% for item in order.items %}
  {{ item.name }}
{% endfor %}
```

#### Project

Returns opportunity items for opportunities on a project.

```
{% for order in project.opportunities %} 
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Invoice

Returns opportunity items for opportunities that are sources on a particular invoice. 

```
{% for order in invoice.sources %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Member

Returns opportunity items for opportunities linked to a particular organization.

```
{% for order in member.opportunities %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

Returns opportunities items for active opportunities linked to a particular organization.

```
{% for order in member.live_opportunities %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Quarantine

Returns opportunity item objects for the source opportunity of a quarantine.

```
{% for item in quarantine.source.items %}
  {{ item.name }}
{% endfor %}
```

Returns opportunity item objects for the opportunity that a quarantined asset is next booked on.

```
{% for item in quarantine.next_booking.items %}
  {{ item.name }}
{% endfor %}
```

### Discussion templates

The `item` object can be accessed in discussion templates created against the following modules:

#### Opportunity

```
{% for item in opportunity.items %}
  {{ item.name }}
{% endfor %}
```

#### Project

Returns opportunity items for opportunities on a project.

```
{% for order in project.opportunities %} 
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Invoice

Returns opportunity items for opportunities that are sources on a particular invoice. 

```
{% for order in invoice.sources %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Member

Returns opportunity items for opportunities linked to a particular organization.

```
{% for order in organisation.opportunities %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

Returns opportunities items for active opportunities linked to a particular organization.

```
{% for order in organisation.live_opportunities %}
  {% for item in order.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Quarantine

Returns opportunity item objects for the source opportunity of a quarantine.

```
{% for item in quarantine.source.items %}
  {{ item.name }}
{% endfor %}
```

Returns opportunity item objects for the opportunity that a quarantined asset is next booked on.

```
{% for item in quarantine.next_booking.items %}
  {{ item.name }}
{% endfor %}
```

## `accessories`

Returns opportunity item objects for an opportunity item. Works in the same way that the [`children` object](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md#children) does.

#### Input

```
{% for item in item.accessories %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
```

## `accessory_is_default?`

Returns `true` if an opportunity item is an accessory and the accessory’s inclusion type is “Default”.

#### Input

```
{{ item.accessory_is_default }}
```

#### Output

```
false
```

## `accessory_is_mandatory?`

Returns `true` if an opportunity item is an accessory and the accessory’s inclusion type is “Mandatory”.

#### Input

```
{{ item.accessory_is_mandatory? }}
```

#### Output

```
false
```

## `accessory_is_optional?`

Returns `true` if an opportunity item is an accessory and the accessory’s inclusion type is “Optional”.

#### Input

```
{{ item.accessory_is_optional? }}
```

#### Output

```
false
```

## `accessory_mode_is_accessory?`

Returns `true` if an opportunity item is an accessory and the accessory’s mode is “Accessory”.

#### Input

```
{{ item.accessory_mode_is_accessory? }}
```

#### Output 

```
false
```

## `accessory_mode_is_component?`

Returns `true` if an opportunity item is an accessory and the accessory’s mode is “Component”.

#### Input

```
{{ item.accessory_mode_is_component? }}
```

#### Output 

```
false
```

## `accessory_mode_is_safety?`

Returns `true` if an opportunity item is an accessory and the accessory’s mode is “Safety”.

#### Input

```
{{ item.accessory_mode_is_safety? }}
```

#### Output 

```
false
```

## `accessory_mode_name`

Returns the accessory’s mode name where an opportunity item is an accessory; blank otherwise.

* accessory
* component
* safety item

#### Input

```
{{ item.accessory_mode_name }}
```

#### Output

```
accessory
```

## `assets`

Returns opportunity item assets for an opportunity item. Keep in mind that an opportunity item might have multiple asset allocations.

#### Input 

```
{% for item in item.assets %}
  {{ asset.asset_number }}<br>
{% endif %}
```

#### Output 

```
ETC-001
ETC-002
ETC-003
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `charge_excluding_tax_total`

Returns an opportunity item charge total excluding tax.

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

Returns an opportunity item charge total including tax.

#### Input

```
{{ item.charge_including_tax_total }}
```

#### Output

```
60.0
```

## `charge_total_including_children`

Returns an opportunity item charge total, including the charge total of any accessory items. 

Generally used where you’d like to roll up the price of accessories into their parent item, like when working with packages or kits. 

#### Input

```
{{ item.charge_total_including_children }}
```

#### Output

```
120.0
```

## `charge_total`

Returns an opportunity item charge total. 

This may be including or excluding tax depending on the value of the “Catalog Prices” setting in System Preferences.

#### Input

```
{{ item.charge_total }}
```

#### Output

```
50.0
```

## `chargeable_days`

Returns the number of chargeable days for an opportunity item. 

For service items, the value of the “Rate Quantity” field is returned. The rate type may be hour or distance.

For sale items, returns `0`.

#### Input

```
{{ item.chargeable_days }}
```

#### Output

```
8.0
```

## `charging_periods`

Returns [charging period objects](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md) for an opportunity item.

#### Input

```
{% for charge_period in item.charging_periods %}
  {{ charge_period.name }}
{% endfor %}
```

#### Output

```
Daily
```

See: [Charging period](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md)

## `children`

Returns opportunity item objects for an opportunity item.

* When an item is an item, this will return accessories.
* When the item is a group, this will return items within that group.

The `children` object only returns objects that are the next level deep in the tree. For example, accessories on accessories aren't returned.

#### Input

```
{% for item in item.children %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
```

## `combined_discount_total`

Returns the total discount from both percentage and deal discounting for opportunity items that are groups.

For items, returns `0`. For subtotals, returns an error.

#### Input

```
{% if item.is_group? %}
  {{ item.combined_discount_total }}
{% endif %}
```

#### Output

```
150.0
```

See: [Deal pricing](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)

## `deal_discount_total`

Returns the total discount from deal discounting for opportunity items that are groups.

For items, returns `0`. For subtotals, returns an error.

#### Input

```
{% if item.is_group? %}
  {{ item.deal_discount_total }}
{% endif %}
```

#### Output

```
100.0
```

See: [Deal pricing](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)

## `depth`

Returns the depth of an opportunity item in the tree. An item’s depth is determined by how it is nested under items. 

#### Input

```
{{ item.depth }}
```

#### Output

```
1
```

## `depth_padding`

Returns the depth padding for an opportunity item. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

Increments in multiples of 16.

#### Input

```
<td style="padding-left: {{ item.depth_padding }}px;">
  {{ item.name }}
</td>
```

#### Output

```markup
<td style="padding-left: 16px;">
  Leica R-Series 180mm f/2.8
</td>
```

## `description`

Returns an opportunity item’s description.

#### Input

```
{{ item.description }}
```

#### Output

```
Supplied with a memory card.
```

## `discount_amount`

Returns the amount of discount applied to an opportunity item. 

Returns `0` for groups and subtotals.

Use [`discount_total` for groups](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md#discount_total).

#### Input

```
{{ item.discount_amount }}
```

#### Output

```
10.0
```

## `discount_percent`

Returns the percentage discount applied to an opportunity item.

Returns `0` for groups and subtotals.

#### Input

```
{{ item.discount_percent }}
```

#### Output

```
50.0
```

## `discount_total`

Returns the amount of discount for items inside of an opportunity group.

Returns `0` for items and subtotals.

Use [`discount_amount` for items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md#discount_amount).

#### Input

```
{% if item.is_group? %}
  {{ item.discount_total }}
{% endif %}
```

#### Output

```
50.0
```

## `discounted_price`

Returns an opportunity item’s price after discount.

#### Input

```
{{ item.discounted_price }}
```

#### Output

```
100.0
```

## `ends_at`

Returns the charging end date for an opportunity item. Generally used for service items.

* For service items, returns the end date and time for the opportunity item.
* For rental and sale items, returns the end date and time for the opportunity.
* For groups, returns blank.
* For subtotals, returns the date and time that the document was generated in UTC.

#### Input

```
{{ item.ends_at }}
```

#### Output

```
2021-05-15 09:00:00 +0100
```

## `group_has_deal?`

Returns `true` where an opportunity item is a group that has been deal priced; `false` otherwise.

Deal priced groups have a red ”Deal Price” label in the list.

#### Input

```
{% if item.is_group?
  {% if item.group_has_deal? %} <!-- true -->
    "{{ item.name }}" has deal
  {% endif %}
{% endif %}
```

#### Output

```
"Lighting" has deal
```

See: [Deal pricing](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)

## `has_child_items?`

Returns `true` if an opportunity item has children items; `false` otherwise. Generally used for detecting if an opportunity item has accessories.

#### Input

```
{{ item.has_child_items? }}
```

#### Output

```
true
```

## `has_discount?`

Returns `true` if an opportunity item has a discount applied; `false` otherwise.

Where an opportunity item has a negative discount applied, `has_discount` will return `false`. For example, -50% would increment the charge total by 50% so `has_discount` will return `false`.

#### Input

```
{{ item.has_discount? }}
```

#### Output

```
true
```

## `has_shortage?`

Returns `true` where an opportunity item has a shortage; `false` otherwise.

Shortages are highlighted in red and have an ⚠️ exclamation icon next to them in the list.

#### Input

```
{{ item.has_shortage? }}
```

#### Output

```
true
```

## `id`

Returns an opportunity item ID. 

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ item.id }}
```

#### Output

```
1	
```

## `is_accessory?`

Returns `true` if an opportunity item is an accessory; `false` otherwise.

#### Input

```
{{ item.is_accessory? }}
```

#### Output

```
true
```

## `is_group?`

Returns `true` if an opportunity item is a group; `false` otherwise.

#### Input

```
{{ if item.is_group? %}
  {{ item.name }}
{% endif %}
```

#### Output

```
Lighting
```

## `is_in_deal?`

Returns `true` if an opportunity item is inside a deal, i.e. if it is part of a deal priced group or opportunity; `false` otherwise.

#### Input

```
{{ item.is_in_deal? }}
```

#### Output

```
true
```

See: [Deal pricing](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)

## `is_item?`

Returns `true` if an opportunity item is an item; `false` otherwise.

#### Input

```
{% if item.is_item? %}
  {{ item.name }}
{% endif %}
```

#### Output

```
Avolites ART 2000 Power Cube
```

## `is_principal?`

Returns `true` if an opportunity item has accessory items nested underneath it; `false` otherwise.

#### Input

```
{% item.is_principal? %}
```

#### Output

```
true
```

## `is_product?`

Returns `true` if an opportunity item is linked to a product record; `false` otherwise.

#### Input

```
{% item.is_product? %}
```

#### Output

```
true
```

## `is_rental?`

Returns `true` if an opportunity item is a rental charge, i.e. its transaction type is "Rental"; `false` otherwise.

#### Input

```
{{ item.is_rental? %}
```

#### Output

```
true
```

## `is_sale?`

Returns `true` if an opportunity item is for a sale charge, i.e. its transaction type is "Sale"; `false` otherwise.

#### Input

```
{{ item.is_sale? %}
```

#### Output

```
false
```

## `is_service?`

Returns `true` if an opportunity item is for a service charge, i.e. its transaction type is "Service"; `false` otherwise.

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

## `is_subtotal?`

Returns `true` if an opportunity item is a group item's subtotal; `false` otherwise.

Subtotal rows are informational only and many opportunity item item objects will print "Liquid error: internal" rather than return `blank` or `false`.

#### Input

```
{% if item.is_subtotal? %}
  Total for {{ item.subtotal_name }}
{% endif %}
```

#### Output

```
Total for Lighting
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

## `name`

Returns an opportunity item's name.

#### Input

```
{{ item.name }}
```

#### Output

```
Robe RoboSpot
```

## `opportunity`

Returns opportunity objects for the opportunity that an opportunity item is related to.

When working with a document or discussion template on an opportunity record, you may simply wish to access the opportunity object as normal. For example, use `{{ order.name }}` to print the opportunity subject.

#### Input

```
{{ item.opportunity.name }}
```

#### Output

```
V-Blast Music Festival
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `price`

Returns an opportunity item's price without discount.

#### Input

```
{{ item.price }}
```

#### Output

```
200.0
```

## `price_unit`

Returns an opportunity item's price unit name. 

The price unit name output depends on the rental charge used. Some common examples:

* Daily
* Weekly
* Per period
* Each

#### Input

```
{{ item.price_unit }}
```

#### Output

```
Weekly
```

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

## `rate_definition_name`

Returns the rate definition name for an opportunity item where the item is a rental. 

Returns blank for sales, services, and group items.

#### Input

```
{{ item.rate_definition_name }}
```

#### Output

```
Daily Rate
```

## `replacement_charge_total`

Returns the replacement charge total for an opportunity item.

This is calculated by multiplying the quantity by the product replacement charge.

> **Note:**
> Current uses the product replacement charge at the time the opportunity item was added to the opportunity. [Recalculate](https://help.current-rms.com/en/articles/1621254-recalculate) to get the latest product replacement charges.

#### Input

```
{{ item.replacement_charge_total }}
```

#### Output

```
2000.0
```

## `replacement_charge_total_including_children`

Returns the replacement charge total for an opportunity item, including the charge total of any accessory items. 

Generally used where you’d like to roll up the replacement charge of accessories into their parent item, like when working with packages or kits. 

#### Input

```
{{ item.replacement_charge_total_including_children }}
```

#### Output

```
3000.0
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

## `service_unit_name`

Returns the service unit name for an opportunity item. 

* Day
* Days
* Hour
* Hours
* miles
* km

#### Input

```
{{ item.service_unit_name }}
```

#### Output

```
Days
```

## `starts_at`

Returns the charging start date for an opportunity item. Generally used for service items.

* For service items, returns the start date and time for the opportunity item.
* For rental and sale items, returns the start date and time for the opportunity.
* For groups, returns blank.
* For subtotals, returns the date and time that the document was generated in UTC.

#### Input

```
{{ item.starts_at }}
```

#### Output

```
2021-04-15 09:00:00 +0100
```

## `sub_contract?`

Returns `true` if an opportunity item is for a sub-contract service or sub-rent product.

#### Input

```
{{ item.sub_contract? }}
```

#### Output

```
true
```

## `sub_rent?`

Returns `true` if an opportunity item is for a sub-contract service or sub-rent product.

#### Input

```
{{ item.sub_rent? }}
```

#### Output

```
true
```

## `subtotal`

Returns the subtotal amount for an opportunity group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `charge_total` of the corresponding opportunity item group.

#### Input

```
{% if item.is_subtotal? %}
  {{ item.subtotal }}
{% endif %}
```

#### Output

```
1000.0
```

## `subtotal_including_tax`

Returns the subtotal amount for an opportunity group including tax.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `charge_total` of the corresponding opportunity item group.

#### Input

```
{% if item.is_subtotal? %}
  {{ item.subtotal_including_tax }}
{% endif %}
```

#### Output

```
1200.0
```

## `subtotal_name`

Returns the subtotal name for an opportunity item group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `name` of the corresponding opportunity item group.

#### Input

```
{% if item.is_subtotal? %}
  {{ item.subtotal_name }}
{% endif %}
```

#### Output

```
Lighting
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

## `surcharges`

Returns opportunity item surcharge objects for surcharges applied to the opportunity item.

#### Input

```
{% for surcharge in item.surcharges %}
  {{ surcharge.name }}
{% endfor %}
```

#### Output

```
Lens Cleaning
```

See: [Opportunity item surcharges](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-surcharge.md)

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

## `unit_charge`

Returns the unit charge for an opportunity item.

The unit charge is the price for one unit of an opportunity item.

#### Input

```
{{ item.unit_charge }}
```

#### Output

```
100.0
```

## `unit_charge_amount`

Returns the unit charge for an opportunity item excluding discount.

The unit charge is the price for one unit of an opportunity item.

#### Input

```
{{ item.unit_charge_amount }}
```

#### Output

```
50.0
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

## `warehouse_notes`

Returns the warehouse notes for an opportunity item.

**Input**

```
{{ item.warehouse_notes }}
```

#### Output

```
These are my warehouse notes
```

## `weight_total`

Returns the weight total for an opportunity item.

This is calculated by multiplying the quantity by the product weight.

> **Note:**
> Current uses the product weight at the time the opportunity item was added to the opportunity. [Recalculate](https://help.current-rms.com/en/articles/1621254-recalculate) to get the latest product weights.

#### Input

<pre><code><strong>{{ item.weight_total }}
</strong></code></pre>

#### Output

```
50.0
```

> **Note:**
> Use [the `company` object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to return your company weight unit, e.g. lbs or kg.

## `weight_total_including_children`

Returns the weight total for an opportunity item.

This is calculated by multiplying the quantity by the product weight.

#### Input

```
{{ item.weight_total_including_children }}
```

#### Output

```
100.0
```

---
*Source: [Opportunity items — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)*
