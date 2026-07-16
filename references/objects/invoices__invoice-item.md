# Invoice items

When printed, an items list will consist of a group, the items inside the group, and then a subtotal row.

To build this in Liquid, you'd use a similar structure:

```markup
{% for item in invoice.items %}
  {% if item.is_group? %}
    {{ item.name }} <!-- Group name -->
  {% elsif item.is_item? %}
    {{ item.name }} <!-- Item name -->
  {% elsif item.is_subtotal? %}
    {{ item.subtotal_name }} <!-- Subtotal name, i.e. group name -->
  {% endif %}
{% endfor %}
```

There's no subtotal row in the web interface. Subtotal items are included in the invoice items object to make it easy to include and style a subtotal row. A subtotal item iterates after a group and its items have iterated. They're purely informational rows, so most of the objects below will return "Liquid error" when used with a subtotal item.

Invoice items may depend slightly differently depending on how an invoice was generated. An invoice can be created manually, from an opportunity, or from a project. 

When created from an opportunity or project, you can choose to itemize, or create summed lines for opportunity groups, product groups, or opportunities. Keep this in mind when building custom documents: some objects might make sense when itemized, but not when grouped by opportunity.

Invoice item objects are always accessed within a forloop that iterates for each item.

### Document layouts

The `item` object can be accessed in document layouts created against the following modules:

#### Invoice

```
{% for item in invoice.items %}
  {{ item.name }}
{% endfor %}
```

#### Opportunity

Returns invoice items for invoices linked to a particular opportunity.

```
{% for invoice in order.invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Member

Returns invoice items for invoices linked to a particular organization.

```
{% for invoice in member.invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice items for active invoices linked to a particular organization.

```
{% for invoice in member.live_invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

### Discussion templates

The `item` object can be accessed in discussion templates created against the following modules:

#### Invoice

```
{% for item in invoice.item %}
  {{ item.name }}
{% endfor %}
```

#### Opportunity

Returns invoice items for invoices linked to a particular opportunity

```
{% for invoice in opportunity.invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

#### Organization

Returns invoice taxes for invoices linked to a particular organization.

```
{% for invoice in organisation.invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice items for active invoices linked to a particular organization.

```
{% for invoice in organisation.live_invoices %}
  {% for item in invoice.items %}
    {{ item.name }}
  {% endfor %}
{% endfor %}
```

## `accessory_is_default?`

Returns `true` if an invoice item is an accessory and the accessory’s inclusion type is “Default”.

#### Input

```
{{ item.accessory_is_default }}
```

#### Output

```
false
```

## `accessory_is_mandatory?`

Returns `true` if an invoice item is an accessory and the accessory’s inclusion type is “Mandatory”.

#### Input

```
{{ item.accessory_is_mandatory? }}
```

#### Output

```
false
```

## `accessory_is_optional?`

Returns `true` if an invoice item is an accessory and the accessory’s inclusion type is “Optional”.

#### Input

```
{{ item.accessory_is_optional? }}
```

#### Output

```
false
```

## `accessory_mode_is_accessory?`

Returns `true` if an invoice item is an accessory and the accessory’s mode is “Accessory”.

#### Input

```
{{ item.accessory_mode_is_accessory? }}
```

#### Output 

```
false
```

## `accessory_mode_is_component?`

Returns `true` if an invoice item is an accessory and the accessory’s mode is “Component”.

#### Input

```
{{ item.accessory_mode_is_component? }}
```

#### Output 

```
false
```

## `accessory_mode_is_safety?`

Returns `true` if an invoice item is an accessory and the accessory’s mode is “Safety”.

#### Input

```
{{ item.accessory_mode_is_safety? }}
```

#### Output 

```
false
```

## `accessory_mode_name`

Returns the accessory’s mode name where an invoice item is an accessory; blank otherwise.

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

## `charge_ends_at`

Returns the charging end date for an invoice item. Generally used for invoice items with transaction types of rental or service.

#### Input

```
{{ item.charge_ends_at }}
```

#### Output

```
2025-08-22 17:00:00 +0100
```

## `charge_excluding_tax_total`

Returns an invoice item charge total excluding tax.

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

Returns an invoice item charge total including tax.

#### Input

```
{{ item.charge_including_tax_total }}
```

#### Output

```
60.0
```

## `charge_starts_at`

Returns the charging start date for an invoice item. Generally used for invoice items with transaction types of rental or service.

#### Input

```
{{ item.charge_starts_at }}
```

#### Output

```
2025-08-20 09:00:00 +0100
```

## `charge_total`

Returns an invoice item charge total. 

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

Returns the number of chargeable days for an invoice item. 

For service items, the value of the “Rate Quantity” field is returned. The rate type may be hour or distance.

For sale items, returns `0.0`.

#### Input

```
{{ item.chargeable_days }}
```

#### Output

```
8.0
```

## `charging_periods`

Returns [charging period objects](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md) for an invoice item.

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

Returns invoice item objects for an invoice item.

* When an item is an item, this will return accessories .
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

Returns the depth of an item in the tree. An item’s depth is determined by how it is nested under items. 

#### Input

```
{{ item.depth }}
```

#### Output

```
1
```

## `depth_padding`

Returns the depth padding for an invoice item. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

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

Returns an invoice item’s description.

#### Input

```
{{ item.description }}
```

#### Output

```
Supplied with a memory card.
```

## `discount_amount`

Returns the amount of discount applied to an invoice item. 

Returns `0.0` for groups and subtotals.

#### Input

```
{{ item.discount_amount }}
```

#### Output

```
10.0
```

## `discount_percent`

Returns the percentage discount applied to an invoice item.

Returns `0.0` for groups and subtotals.

#### Input

```
{{ item.discount_percent }}
```

#### Output

```
50.0
```

## `discounted_price`

Returns an invoice item’s price after discount.

#### Input

```
{{ item.discounted_price }}
```

#### Output

```
100.0
```

## `has_child_items?`

Returns `true` if an `invoice` item has children items; `false` otherwise. Generally used for detecting if an invoice item has accessories.

#### Input

```
{{ item.has_child_items? }}
```

#### Output

```
true
```

## `has_discount?`

Returns `true` if an invoice item has a discount applied; `false` otherwise.

Where an invoice item has a negative discount applied, `has_discount` will return `false`. For example, -50% would increment the charge total by 50% so `has_discount` will return `false`.

#### Input

```
{{ item.has_discount? %}
```

#### Output

```
true
```

## `id`

Returns an invoice item ID. 

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

## `invoiceable_item_description`

Returns the description of the record that this invoice item is linked to. 

* When invoicing by item, this will return the description set against the product or service records.
* When invoicing by product group, this will return the product group description set in System Setup > Product Groups.
* When invoicing by opportunity, this will return the (internal) description set against the opportunity.
* Returns blank for part invoice line items.

#### Input

```
{{ item.invoiceable_item_description }}
```

#### Output

```
A compact, dimmable LED light which can be mounted on camera, lighting stand, arm, or used handheld.	
```

## `invoiceable_name`

#### Input

Returns the name of the record that this invoice item is linked to. 

* When invoicing by item, this will return the name of the product or service.
* When invoicing by product group, this will return the product group name set in System Setup > Product Groups.
* When invoicing by opportunity, this will return the name set against the opportunity.

The `invoiceable_name` should generally be the same as the item `name`; it may be different if you’ve changed the name of a record after it’s been added to an invoice.

For part invoice line items, returns the value of the “Final Invoice Credit Text” in System Preferences. This is used when your final invoice is created at a later point.

```
{{ item.name }}
```

#### Output

```
PCE IMST Distro
```

## `invoiceable_object`

Returns [opportunity item](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md), [product](https://current-rms.gitbook.io/liquid-syntax/products/product.md), [service](https://current-rms.gitbook.io/liquid-syntax/service/service.md), or [opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md) objects for an invoice item. 

The type of object depends on an invoice item’s invoiceable type.

#### Input

| Invoiceable type   | Object             |
| ------------------ | ------------------ |
| `Opportunity`      | opportunity        |
| `Opportunity Item` | opportunity item   |
| `Item`             | product or service |

> **Warning:**
> Items with the invoiceable type `Item` may be part invoice line items; be sure to cater for this in your code.

#### Input

```
{{ item.invoiceable_object.name }}
```

#### Output

```
ETC Source 4
```

## `invoiceable_type`

Returns the type of an invoice item. Generally describes the circumstances why an invoice item was created.

| Invoiceable type   | Description                                                             |
| ------------------ | ----------------------------------------------------------------------- |
| `Opportunity`      | An item created from an invoice grouped by opportunity.                 |
| `Opportunity Item` | An item created from an invoice grouped by opportunity item.            |
| `Product Group`    | An item created from an invoice grouped by product group.               |
| `Surcharge`        | An item created for an opportunity item surcharge total.                |
| `OpportunityDeal`  | An item created for an opportunity or opportunity group deal price.     |
| `Item`             | An item created by adding it directly to an invoice, or any other item. |

> **Note:**
> There's no space between `OpportunityDeal`

#### Input

```
{{ item.invoiceable_type }}
```

#### Output

```
Opportunity Item
```

## `is_accessory?`

Returns `true` if an invoice item is an accessory; `false` otherwise.

#### Input

```
{{ item.is_acessory? }}
```

#### Output

```
true
```

## `is_deal_item?`

Returns `true` if an invoice item is a deal item, i.e. it is an item created with a charge total for a deal; `false` otherwise.

Deal items have a red ”Deal Price” label in the list.

#### Input

```
{{ item.is_deal_item? }}
```

#### Output

```
false
```

See: [Deal pricing](https://current-rms.gitbook.io/liquid-syntax/information/deal-pricing.md)

## `is_group?`

Returns `true` if an invoice item is a group; `false` otherwise.

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

Returns `true` if an invoice item is inside a deal, i.e. if it is an informational line included underneath a deal price line on an invoice; `false` otherwise.

An item that `is_in_deal?` will always be nested under an item that `is_deal_item?`.

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

Returns `true` if an invoice item is an item; `false` otherwise.

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

Returns `true` if an invoice item has accessory items nested underneath it; `false` otherwise.

#### Input

```
{% item.is_principal? %}
```

#### Output

```
true
```

## `is_product?`

Returns `true` if an invoice item is linked to a product record; `false` otherwise.

#### Input

```
{% item.is_product? %}
```

#### Output

```
true
```

## `is_rental?`

Returns `true` if an invoice item is a rental charge, i.e. its transaction type is "Rental"; `false` otherwise.

#### Input

```
{{ item.is_rental? %}
```

#### Output

```
true
```

## `is_sale?`

Returns `true` if an invoice item is for a sale charge, i.e. its transaction type is "Sale"; `false` otherwise.

#### Input

```
{{ item.is_sale? %}
```

#### Output

```
false
```

## `is_service?`

Returns `true` if an invoice item is for a service charge, i.e. its transaction type is "Service"; `false` otherwise.

This doesn't determine necessarily whether an invoice item is linked to a service record; a text item may have the transaction type "Service".

#### Input

```
{{ item.is_service? }}
```

#### Output

```
false
```

## `is_service_item?`

Returns `true` if an invoice item is linked to a service record; `false` otherwise.

#### Input

```
{{ item.is_service_item? }}
```

#### Output

```
false
```

## `is_subtotal?`

Returns `true` if an invoice item is a group item's subtotal; `false` otherwise.

Subtotal rows are informational only and many invoice item objects will print "Liquid error: internal" rather than return `blank` or `false`.

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

Returns `true` if an invoice item is a text item; `false` otherwise.

#### Input

```
{{ item.is_text_item? }}
```

#### Output

```
true
```

## `name`

Returns an invoice item's name.

#### Input

```
{{ item.name }}
```

#### Output

```
Robe RoboSpot
```

## `order`

Returns opportunity objects for the opportunity that an invoice item is related to.

#### Input

```
{{ item.order.name }}
```

#### Output

```
V-Blast Music Festival
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `price`

Returns an invoice item's price without discount.

#### Input

```
{{ item.price }}
```

#### Output

```
200.0
```

## `price_unit`

Returns an invoice item's price unit name. 

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

## `project_name`

Returns the name of the project that an invoice item is related to. Generally the name of the project linked to the opportunity that was the origin of an invoice item.

#### Input

```
{{ item.project_name }}
```

#### Output

```
Omni Consumer Products: Launch Roadshow
```

## `quantity`

Returns the quantity of an invoice item.

#### Input

```
{{ item.quantity }}
```

#### Output

```
1.0
```

## `rate_definition_name`

Returns the rate definition name for an invoice item where the item is a rental. 

Returns blank for sales, services, surcharges, and group items.

#### Input

```
{{ item.rate_definition_name }}
```

#### Output

```
Daily Rate
```

## `service_unit_name`

Returns the service unit name for an invoice item. 

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

## `source_name`

Returns the name of the source of an invoice item. Generally the name of the opportunity that was the origin of an invoice item.

#### Input

```
{{ item.source_name }}
```

#### Output

```
V-Blast Music Festival
```

## `subtotal`

Returns the subtotal amount for an invoice item group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `charge_total` of the corresponding invoice item group.

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

Returns the subtotal name for an invoice item group.

Subtotal rows are informational only. This will only return a value for subtotal rows. This will match the `name` of the corresponding invoice item group.

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

## `tax_class_name`

Returns the tax class name against an invoice item. This is set against the product or service record, or when creating a text item.

#### Input

```
{{ item.tax_class_name }}
```

#### Output

```
Florida State Tax
```

## `tax_total`

Returns the tax total for an invoice item.

#### Input

```
{{ item.tax_total }}
```

#### Output

```
50.0
```

## `transaction_type_name`

Returns the transaction type name for an invoice item.

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

Returns the unit charge for an invoice item.

The unit charge is the price for one unit of an invoice item.

#### Input

```
{{ item.unit_charge }}
```

#### Output

```
100.0
```

## `unit_charge_amount`

Returns the unit charge for an invoice item excluding discount.

The unit charge is the price for one unit of an invoice item.

#### Input

```
{{ item.unit_charge_amount }}
```

#### Output

```
50.0
```

## `use_chargeable_days`

Returns `true` if an invoice item has overriden chargeable days. 

This will be the case where the source opportunity of an invoice has the "Chargeable Days" toggle set to YES.

#### Input

```
{{ item.use_chargeable_days }}
```

#### Output

```
true
```

---
*Source: [Invoice items — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md)*
