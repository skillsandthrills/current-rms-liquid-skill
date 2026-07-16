# Purchase order

Purchase orders can be created directly from an opportunity. Current RMS will take opportunity costs and create a purchase order per supplier.

## `activities` <a href="#activities" id="activities"></a>

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to the purchase order.

#### Input  <a href="#input" id="input"></a>

```
{% for activity in order.activities %}
  {{ activity.subject }}
{% endif %}
```

#### Output  <a href="#output" id="output"></a>

```
Call to follow up
```

See: [Activity](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md)

## `attachments` <a href="#attachments" id="attachments"></a>

Returns attachment objects for attachments stored against a purchase order.

#### Input <a href="#input-3" id="input-3"></a>

```
{% for attachment in order.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output <a href="#output-3" id="output-3"></a>

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `authorised_at`

Returns the date and time that the purchase order was authorized.

#### Input

```
{{ order.authorised_at }}
```

#### Output

{% code title="" %}

```markup
2021-02-21 10:00:00 +0000
```

{% endcode %}

> **Note:**
> Use [a date filter](https://current-rms.gitbook.io/liquid-syntax/information/date-filter.md) to change the way that the date is formatted.

## `authoriser`

Returns [user objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md) with information about the user who authorized the purchase order.

#### Input

```
{{ order.authoriser.name }}
```

#### Output

```
Peter Miller
```

See: [User](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md)

## `charge_excluding_tax_total`

Returns the purchase order charge total excluding tax.

#### Input

```
{{ order.charge_excluding_tax_total }}
```

#### Output

```
450.0
```

> **Note:**
> Use [the currency filter or a number filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the number is formatted.

## `charge_including_tax_total`

Returns the purchase order charge total including tax.

#### Input

```
{{ order.charge_including_tax_total }}
```

#### Output

```
550.0
```

## `charge_total`

Returns the purchase order charge total.

#### Input

```
{{ order.charge_total }}
```

#### Output

```
450.0
```

## `customer_collecting`

Returns if the customer is collecting.

#### Input

```
{{ order.self_collecting }}
```

#### Output

```
true
```

## `customer_returning`

Returns if the customer is returning.

#### Input

```
{{ order.self_returning }}
```

#### Output

```
true
```

## `delivery_address`

Returns the purchase order delivery address. 

You may also use [the venue object (below)](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md#venue).

#### Input

```
{{ order.delivery_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `delivery_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the delivery address against the purchase order.

#### Input 

```
{{ order.delivery_address_detail.state }}
```

#### Output 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `delivery_address_name`

Returns the name of the delivery address against the purchase order.

You may also use [the venue object (below)](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md#venue).

#### Input

```
{{ order.delivery_address_name }}
```

#### Output

```
Seaview Convention Center
```

## `delivery_at`

Returns the purchase order delivery date and time.

#### Input

```
{{ order.delivery_at }}	
```

#### Output

```
2021-03-29 11:00:00 +0000
```

## `delivery_attention`

Returns the value of the purchase order “Delivery For Attention Of” field.

#### Input

```
{{ order.delivery_attention }}
```

#### Output

```
Michael McGovern
```

## `delivery_instructions`

Returns the purchase order delivery instructions.

#### Input

```
{{ order.delivery_instructions }}
```

#### Output

```
Around the back.
```

## `description`

Returns the purchase order (internal) description.

#### Input

```
{{ order.description }}
```

#### Output

```
Take extra care with this sub-rented stock.
```

## `expected_at`

Returns the purchase order expected arrival date and time.

#### Input

```
{{ order.expected_at }}
```

#### Output

```
2021-04-10 14:00:00 +0000
```

## `expected_note`

Returns the purchase order expected arrival notes.

#### Input

```
{{ order.expected_note }}
```

#### Output

```
Vendor is running late; delivery Thursday.
```

## `external_description`

Returns the purchase order external description.&#x9;

#### Input

```
{{ order.external_description }}
```

#### Output

```
Purchase Order raised as agreed.
```

## `id`

Returns the purchase order ID.

> **Warning:**
> The ID is an internal reference for a record. It's not exposed in our web interface and shouldn't be confused with the order number (below).

#### Input

```
{{ order.id }}
```

#### Output

```
1
```

## `image_attachments` <a href="#image_attachments" id="image_attachments"></a>

Returns attachment objects for attachments stored against a purchase order where the attachment file type is an image.

#### Input  <a href="#input-5" id="input-5"></a>

```
{% for attachment in order.image_attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output  <a href="#ouput-1" id="ouput-1"></a>

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `items`

Returns [purchase order item objects](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order-items.md) for items on the purchase order.

#### Input

```
{% for item in order.items %}
  {% if item.is_item? %}
    {{ item.name }}
  {% endif %}
{% endfor %}
```

#### Output

```
Pioneer XDJ RX
```

See: [Purchase order items](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order-items.md)

## `name`

Returns the purchase order subject.

#### Input

```
{{ order.name }}
```

#### Output

```
V-Blast Music Festival
```

## `number`

Returns the purchase order number.

#### Input

```
{{ order.number }}
```

#### Output

```
PO-001
```

## `ordered_at`

Returns the value of the purchase order “Order Date” field.&#x9;

#### Input

```
{{ order.ordered_at }} 
```

#### Output

```
2021-03-11 14:00:00 +0000
```

## `participants`

Returns [contact](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md), [organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md), [user](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md), [vehicle](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/vehicle.md), or [venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md) objects for participants on the purchase order.

#### Input

```
{% for participant in order.participants %}
  {{ participant.name }} - {{ participant.type }}
{% endfor %}
```

#### Output

```
Michael McGovern - Contact
```

## `reference` 

Returns the purchase order customer reference.

#### Input

```
{{ order.reference }}
```

#### Output

```
I3804
```

## `sources`

Returns [opportunity objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md) for the purchase order sources.

A purchase order may have multiple sources, or no sources at all.

#### Input

```
{% for source in order.sources %}
  {{ source.name }}
{% endfor %}
```

#### Output

```
Omni Consumer Products New Product Launch
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `state`

Returns the purchase order state code.

| Code | State name |
| ---- | ---------- |
| `0`  | Draft      |
| `1`  | Order      |

#### Input

```
{{ order.state }}
```

#### Output 

```
1
```

## `state_name`

Returns the purchase order state name. 

State names are in the language set against your user profile. 

* Draft
* Order

#### Input

```
{{ order.state_name }}
```

#### Output

```
Order
```

## `status`

Returns the purchase order status code.

| Code | Status name |
| ---- | ----------- |
| `0`  | Open        |
| `10` | Authorized  |
| `20` | Sent        |
| `30` | Completed   |
| `40` | Canceled    |

#### Input

```
{{ order.status }}
```

#### Output

```
10
```

## `status_name`

Returns the purchase order status name.

Status names are in the language set against your user profile. 

* Open
* Authorized
* Sent
* Completed
* Canceled

#### Input

```
{{ order.status_name }}
```

#### Output

```
Authorized
```

## `store`

Returns [store objects](https://current-rms.gitbook.io/liquid-syntax/general/store.md) for the store against the purchase order.

#### Input

```
{{ order.store.name }}
```

#### Output

```
The Banana Stand
```

See: [Store](https://current-rms.gitbook.io/liquid-syntax/general/store.md)

## `supplier`

Returns [organization objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md) for the supplier against the purchase order.

#### Input

```
{{ supplier.name }}
```

#### Output

```
Omni Consumer Products
```

See: [Organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)

## `tax_class_name`

Returns the purchase order tax class.

This may differ from the organization tax class.

#### Input

```
{{ order.tax_class_name }}
```

#### Output

```
Default
```

## `tax_total`

Returns the purchase order tax total.

#### Input

```
{{ order.tax_total }}
```

#### Output

```
100.0
```

## `venue`

Returns [venue objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md) for the venue against the purchase order.

> **Warning:**
> A delivery address can be a venue, but a venue might not always be a purchase order's delivery address. If you don't choose a venue when creating a purchase order, using `{{ order.venue.name }}` won't return the same as `{{ order.delivery_address_name }}`.

#### Input

```
{{ order.venue.name }}
```

#### Output

```
Seaview Conference Center
```

See: [Venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md)

## `weight_total`

Returns the purchase order weight total.

#### Input

```
{{ order.weight_total }}
```

#### Output

```
250.0
```

> **Note:**
> Use the [company object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) weight unit to print the weight unit for your system.

---
*Source: [Purchase order — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md)*
