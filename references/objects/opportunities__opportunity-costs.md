# Opportunity costs

In Current RMS, you may set [costs](https://help.current-rms.com/en/articles/2625454-what-is-the-costs-view) up against your products and services. When you add items to an opportunity, Current will automatically cost your opportunity and calculate profitability for you.

Costs are related to opportunity item assets. You can add and change costs on the Costs view on an opportunity.

### Document layouts

The `cost` object can be accessed in document layouts against the following modules:

#### Opportunity

```
{% for cost in order.costs %}
  {{ cost.subject }}
{% endfor %}
```

Against an opportunity item asset:

```
{{ asset.cost.subject }}
```

#### Purchase order

```
{% for item in order.items %}
  {% if item.is_item? %}
    {{ item.opportunity_cost.subject }}
  {% endif %}
{% endfor %}
```

### Discussion templates

The `cost` object can be accessed in discussion templates against the following modules:

#### Opportunity

```
{% for cost in opportunity.costs %}
  {{ cost.subject }}
{% endfor %}
```

Against an opportunity item asset:

```
{{ asset.cost.subject }}
```

#### Purchase order

```
{% for item in purchase_order.items %}
  {% if item.is_item? %}
    {{ item.opportunity_cost.subject }}
  {% endif %}
{% endfor %}
```

## `actual_cost` 

Returns an opportunity cost's actual cost.

#### Input

```
{{ cost.actual_cost }}
```

#### Output

```
1200.0
```

## `asset` 

Returns opportunity item asset objects for an opportunity cost's related asset.

#### Input

```
{{ cost.asset.asset_number }}
```

#### Output

```
ETC-001
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `attachments` 

Returns attachment objects for an opportunity cost.

#### Input

```
{% for attachment in cost.attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `chargeable_days`

Returns an opportunity cost's chargeable days.

#### Input

```
{{ cost.chargeable_days }}
```

#### Output

```
1.0
```

## `charging_periods`

Returns charging period objects for an opportunity cost.

#### Input

```
{% for period in cost.charging_periods %}
  {{ period.name }}
{% endfor %}
```

#### Output

```
Week
```

See: [Charging period](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md)

## `cost_date` 

Returns an opportunity cost's date.

* For sub-rentals and purchases, this is the start date of the opportunity.
* For sub-contracts and services, this is the start date of the related service opportunity item.
* For manual costs, this is the date you set against the cost when creating it.

#### Input

```
{{ cost.cost_date }}
```

#### Output

```
2022-07-17
```

## `cost_group_name` 

Returns an opportunity cost's cost group name. 

Configure cost groups in System Setup > Cost Groups.

#### Input

```
{{ cost.cost_group_name }}
```

#### Output

```
Crew
```

## `cost_type_name` 

Returns an opportunity cost's cost type name.

* Manual
* Purchase
* Service
* Sub-Contract
* Sub-Rental

Cost type names are returned in your locale language, set against your user profile.

#### Input

```
{{ cost.cost_type_name }}
```

#### Output

```
Sub-Rental
```

## `description`

Returns an opportunity cost's description. This is called a note in the web interface.

#### Input

```
{{ cost.description }}
```

#### Output

```
Collection from 4pm Tuesday.
```

## `ends_at` 

Returns an opportunity cost's end date. 

* For sub-rentals and purchases, this is the end date of the opportunity.
* For sub-contracts and services, this is the start date of the related service opportunity item.
* For manual costs, this is the date you set against the cost when creating it.

#### Input

```
{{ cost.ends_at }}
```

#### Output

```
2022-06-17 09:00:00 +0100
```

## `id` 

Returns an opportunity cost's ID.

> **Note:**
> The ID is an internal identifier for a record in our databases. It's not exposed in our web interface.

#### Input

```
{{ cost.id }}
```

#### Output

```
5901
```

## `image_attachments`

Returns attachment objects for an opportunity cost. Only returns those that have a file type of image.

#### Input

```
{% for attachment in cost.image_attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

## `manual_cost?`

Returns `true` where an opportunity cost is a manual cost; `false` otherwise.

#### Input

```
{{ cost.manual_cost? }}
```

#### Output

```
true
```

## `price` 

Returns an opportunity cost's price.

When working with automatic costs, the price is used to calculate the provisional cost total. Returns `0.0` for manual costs.

#### Input

```
{{ cost.price }}
```

#### Output

```
20.0
```

## `price_unit`

Returns an opportunity cost's price unit. Used for sub-rentals only.

#### Input

```
{{ cost.price_unit }}
```

#### Output

```
Weekly
```

## `provisional_cost` 

Returns an opportunity cost's provisional cost.

* Automatic costs are entered as provisional by the system. This is because you might like to 'correct' them by adding an actual cost.
* When creating a manual cost, you may specify the provisional and actual costs.

#### Input

```
{{ cost.provisional_cost }}
```

#### Output

```
140.0
```

## `purchase_order` 

Returns purchase order objects for an opportunity cost.

#### Input

```
{{ cost.purchase_order.number }}
```

#### Output

```
101
```

See: [Purchase order](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md)

## `quantity`

Returns an opportunity cost's quantity.

Manual costs return `1.0`.

#### Input

```
{{ cost.quantity }}
```

#### Output

```
1.0
```

## `reference`

Returns an opportunity cost's reference. Only returned for manual costs.

#### Input

```
{{ cost.reference }}
```

#### Output

```
AB
```

## `service_unit_name`

Returns an opportunity cost's service unit name. 

#### Input

```
{{ cost.service_unit_name }}
```

#### Output

```
Miles
```

## `starts_at`

Returns an opportunity cost's start date.

* For sub-rentals and purchases, this is the start date of the opportunity.
* For sub-contracts and services, this is the start date of the related service opportunity item.
* For manual costs, this is the date you set against the cost when creating it.

#### Input

```
{{ cost.starts_at }}
```

#### Output

```
2022-07-17 16:00:00 +0100
```

## `subject`

Returns an opportunity cost's subject. 

* For automatic costs, this is the name of the related opportunity item.
* For manual costs, this is the name of the subject you enter when you create a cost.

#### Input

```
{{ cost.subject }}
```

#### Output

```
Canon C300 (EF)
```

## `supplier`

Returns organization, contact, or vehicle objects for an opportunity cost's related supplier.

#### Input

```
{{ cost.supplier.name }}
```

#### Output

```
AV Excellence, Inc.
```

See: [People & Organizations](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)

## `supplier_name` 

Returns the name of the organization set as a sub-rent or sub-contract supplier for an opportunity item asset.

#### Input

```
{{ cost.supplier_name }}
```

#### Output

```
AV Excellence, Inc.
```

## `supplier_reference`

Returns an opportunity cost's supplier reference. Only returned for manual costs.

#### Input

```
{{ cost.supplier_reference }} 
```

#### Output

```
CDE
```

## `unit_charge_amount`

Returns an opportunity cost's unit charge amount.

The unit charge is the price for one unit.

#### Input

```
{{ cost.unit_charge_amount }}
```

#### Output

```
1200.0
```

---
*Source: [Opportunity costs — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-costs.md)*
