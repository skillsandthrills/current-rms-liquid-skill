# Purchase order items

> **Note:**
> urchase orders are in beta. It's unlikely these object will change, but new objects may be added in future.

## `accessories` 

Returns opportunity item objects for a purchase order item. Works in the same way that the `children` object does.

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

## `charge_total_including_children` 

Returns a purchase order item charge total, including the charge total of any accessory items. 

Generally used where you’d like to roll up the price of accessories into their parent item, like when working with packages or kits. 

#### Input

```
{{ item.charge_total_including_children }}
```

#### Output

```
120.0
```

## accessory\_is\_default? 

Returns `true` if a purchase order is an accessory and the accessory’s inclusion type is “Default”.

#### Input

```
{{ item.accessory_is_default }}
```

#### Output

```
false
```

## `accessory_is_mandatory?`

Returns `true` if a purchase order item is an accessory and the accessory’s inclusion type is “Mandatory”.

#### Input

```
{{ item.accessory_is_mandatory? }}
```

#### Output

```
false
```

## `accessory_is_optional?`

Returns `true` if a purchase order is an accessory and the accessory’s inclusion type is “Optional”.

#### Input

```
{{ item.accessory_is_optional? }}
```

#### Output

```
false
```

## `accessory_mode_is_accessory?`

Returns `true` if a purchase order is an accessory and the accessory’s mode is “Accessory”.

#### Input

```
{{ item.accessory_mode_is_accessory? }}
```

#### Output 

```
false
```

## `accessory_mode_is_component?`

Returns `true` if a purchase order is an accessory and the accessory’s mode is “Component”.

#### Input

```
{{ item.accessory_mode_is_component? }}
```

#### Output 

```
false
```

## `accessory_mode_is_safety?`

Returns `true` if a purchase order is an accessory and the accessory’s mode is “Safety”.

#### Input

```
{{ item.accessory_mode_is_safety? }}
```

#### Output 

```
false
```

## `accessory_mode_name`

Returns the accessory’s mode name where a purchase order is an accessory; blank otherwise.

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

## `charge_excluding_tax_total`

Returns a purchase order item charge total excluding tax.

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

Returns a purchase order item charge total including tax.

#### Input

```
{{ item.charge_including_tax_total }}
```

#### Output

```
60.0
```

## `charge_total_including_children`

Returns a purchase order charge total, including the charge total of any accessory items. 

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

Returns a purchase order item charge total. 

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

Returns the number of chargeable days for a purchase order item. 

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

Returns [charging period objects](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md) for a purchase order item.

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

## children 

Returns purchase order item objects for a purchase order item.

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

## `depth`

Returns the depth of a purchase order item in the tree. An item’s depth is determined by how it is nested under items. 

#### Input

```
{{ item.depth }}
```

#### Output

```
1
```

## `depth_padding`

Returns the depth padding for a purchase order item. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

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

Returns a purchase order item’s description.

#### Input

```
{{ item.description }}
```

#### Output

```
Supplied with a memory card.
```

## `discount_amount`

Returns the amount of discount applied to a purchase order item. 

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

Returns the percentage discount applied to a purchase order item.

Returns `0` for groups and subtotals.

#### Input

```
{{ item.discount_percent }}
```

#### Output

```
50.0
```

## `discounted_price`

Returns a purchase order item’s price after discount.

#### Input

```
{{ item.discounted_price }}
```

#### Output

```
100.0
```

## `ends_at` 

Returns the charging end date for a purchase order item. Generally used for service items.

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

## `has_child_items?` 

Returns `true` if a purchase order item has children items; `false` otherwise. Generally used for detecting if an opportunity item has accessories.

#### Input

```
{{ item.has_child_items? }}
```

#### Output

```
true
```

## `has_discount?`

Returns `true` if a purchase order item has a discount applied; `false` otherwise.

Where a purchase order item has a negative discount applied, `has_discount` will return `false`. For example, -50% would increment the charge total by 50% so `has_discount` will return `false`.

#### Input

```
{{ item.has_discount? }}
```

#### Output

```
true
```

## id 

Returns a purchase order item ID. 

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

## image\_url 

Returns a URL pointing at the product or service's picture. The full size image is returned.

#### Input

```
{{ item.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `is_accessory?`

Returns `true` if a purchase order item is an accessory; `false` otherwise.

#### Input

```
{{ item.is_accessory? }}
```

#### Output

```
true
```

## `is_group?`

Returns `true` if a purchase order item is a group; `false` otherwise.

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

## `is_item?`

Returns `true` if a purchase order item is an item; `false` otherwise.

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

Returns `true` if a purchase order item has accessory items nested underneath it; `false` otherwise.

#### Input

```
{% item.is_principal? %}
```

#### Output

```
true
```

## `is_product?`

Returns `true` if a purchase order item is linked to a product record; `false` otherwise.

#### Input

```
{% item.is_product? %}
```

#### Output

```
true
```

## `is_service_item?`

Returns `true` if a purchase order item is linked to a service record; `false` otherwise.

#### Input

```
{{ item.is_service_item? }}
```

#### Output

```
false
```

## `is_subtotal?`

Returns `true` if a purchase order item is a group item's subtotal; `false` otherwise.

Subtotal rows are informational only and many purchase order item objects will print "Liquid error: internal" rather than return `blank` or `false`.

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

Returns `true` if a purchase order item is a text item; `false` otherwise.

#### Input

```
{{ item.is_text_item? }}
```

#### Output

```
true
```

## `name`

Returns a purchase order item's name.

#### Input

```
{{ item.name }}
```

#### Output

```
Robe RoboSpot
```

## `opportunity` 

Returns opportunity objects for the opportunity that a purchase order item is related to.

#### Input

```
{{ item.opportunity.name }}
```

#### Output

```
V-Blast Music Festival
```

## `opportunity_cost` 

Returns opportunity cost objects for the opportunity cost that a purchase order item is related to.

#### Input

```
{{ item.opportunity_cost.subject }}
```

#### Output

```
Sub-rental 
```

## `price` 

Returns a purchase order item's price without discount.

#### Input

```
{{ item.price }}
```

#### Output

```
200.0
```

## `price_unit`

Returns a purchase order item's price unit name. 

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

## `product` 

Where related to a product, returns product objects for a purchase order item.

#### Input

```
{{ item.product.description }}
```

#### Output

```
Isn't it about time you upgraded to the best? The new Hemingway X10 is all the audio you never knew you needed.
```

## `product_group_name` 

Where related to a product, returns the related product's product group name for a purchase order item.

#### Input

```
{{ item.product_group_name }}
```

#### Output

```
Cameras 
```

## `purchase_order` 

Returns purchase order objects for the purchase order that a purchase order item is related to.

#### Input

```
{{ item.purchase_order.name }}
```

#### Output

```
Extra gear for show
```

## `quantity`

Returns the quantity of a purchase order item.

#### Input

```
{{ item.quantity }}
```

#### Output

```
1.0
```

## `rate_definition_name`

Returns the rate definition name for a purchase order item where the item is a sub-rental. 

Returns blank for sales, services, and group items.

#### Input

```
{{ item.rate_definition_name }}
```

#### Output

```
Daily Rate
```

## `service` 

Where related to a service, returns service objects for a purchase order item.

#### Input

```
{{ item.service.description }}
```

#### Output

```
Let our techs take care of everything for you!
```

## `service_unit_name`

Returns the service unit name for a purchase order item. 

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

Returns the charging start date for a purchase order item. Generally used for service items.

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

## `subtotal`

Returns the subtotal amount for a purchase order group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `charge_total` of the corresponding purchase order item group.

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

## `subtotal_name`

Returns the subtotal name for a purchase order item group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `name` of the corresponding purchase order group.

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

## `supplier_reference`

Returns the supplier reference for a purchase order item's related opportunity cost.

#### Input

```
{{ item.supplier_reference }}
```

#### Output

```
JJ110
```

## `tax_class_name` 

Returns the tax class name against a purchase order item.

#### Input

```
{{ item.tax_class_name }} 
```

#### Output

```
VAT Standard
```

## `tax_total`

Returns the tax total for a purchase order item. Works for items and groups.

#### Input

```
{{ item.tax_total }}
```

#### Output

```
50.0
```

## `thumbnail_url`

Returns a URL pointing at the product or service's picture. A thumbnail size image is returned.

#### Input

```
{{ item.thumbnail_icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `transaction_type_name`

Returns the transaction type name for a purchase order item.

#### Input

```
{{ item.transaction_type_name }}
```

#### Output

```
Sub-Rental
```

## `unit_charge`

Returns the unit charge for a purchase order.

The unit charge is the price for one unit of a purchase order.

#### Input

```
{{ item.unit_charge }}
```

#### Output

```
100.0
```

## `unit_charge_amount`

Returns the unit charge for a purchase order excluding discount.

The unit charge is the price for one unit of a purchase order.

#### Input

```
{{ item.unit_charge_amount }}
```

#### Output

```
50.0
```

## `weight_total`

Returns the weight total for a purchase order item.

This is calculated by multiplying the quantity by the product weight.

> **Note:**
> Current uses the product weight at the time the opportunity item was added to the purchase order. [Recalculate](https://help.current-rms.com/en/articles/1621254-recalculate) to get the latest product weights.

#### Input

```
{{ item.weight_total }}
```

#### Output

```
50.0
```

> **Note:**
> Use [the `company` object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to return your company weight unit, e.g. lbs or kg.

## `weight_total_including_children`

Returns the weight total for a purchase order item.

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
*Source: [Purchase order items — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order-items.md)*
