# Opportunity

Opportunities are the beginning and the end of the order process in Current RMS. They are one of the most complex records, with many related records like opportunity items, opportunity item assets, and opportunity costs.

Opportunity documents are the most commonly used documents. Quotations, rental agreements, delivery notes, and other documents are printed from the opportunity module.

Because the opportunity module is so complex, it touches lots of other records so there are many ways of accessing opportunity objects.

### Document layouts

The `order` object can be accessed in document layouts created against the following modules:

#### Opportunity

```
{{ order.name }}
```

#### Project

Returns opportunity items for opportunities on a project.

```
{% for order in project.opportunities %}
  {{ order.name }}
{% endfor %}
```

#### Invoice

Returns opportunity items for opportunities that are sources on a particular invoice. 

```
{% for order in invoice.sources %}
  {{ order.name }}
{% endfor %}
```

#### Member

Returns opportunity items for opportunities linked to a particular organization.

```
{% for order in member.opportunities %}
  {{ order.name }}
{% endfor %}
```

Returns opportunities items for active opportunities linked to a particular organization.

```
{% for order in member.live_opportunities %}
  {{ order.name }}
{% endfor %}
```

#### Quarantine

Returns opportunity item objects for the source opportunity of a quarantine.

```
{{ quarantine.source.name }}
```

Returns opportunity item objects for the opportunity that a quarantined asset is next booked on.

```
{% quarantine.next_booking.name }}
```

### Discussion templates

The `item` object can be accessed in discussion templates created against the following modules:

#### Opportunity

```
{{ opportunity.name }}
```

#### Project

Returns opportunity items for opportunities on a project.

```
{% for order in project.opportunities %}
  {{ order.name }}
{% endfor %}
```

#### Invoice

Returns opportunity items for opportunities that are sources on a particular invoice. 

```
{% for order in invoice.sources %}
  {{ order.name }}
{% endfor %}
```

#### Member

Returns opportunity items for opportunities linked to a particular organization.

```
{% for order in organisation.opportunities %}
  {{ order.name }}
{% endfor %}
```

Returns opportunities items for active opportunities linked to a particular organization.

```
{% for order in organisation.live_opportunities %}
  {{ order.name }}
{% endfor %}
```

#### Quarantine

Returns opportunity item objects for the source opportunity of a quarantine.

```
{{ quarantine.source.name }}
```

Returns opportunity item objects for the opportunity that a quarantined asset is next booked on.

```
{% quarantine.next_booking.name }}
```

## `activities`

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md) for the activities relating to the opportunity.

#### Input 

```
{% for activity in order.activities %}
  {{ activity.subject }}
{% endif %}
```

#### Output 

```
Call to follow up
```

See: [Activity](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md)

## `actual_cost_total`

Returns the actual cost total against an opportunity.

The actual cost total is calculated by totaling actual costs.

#### Input

```
{{ order.actual_cost_total }}
```

#### Output

```
120.0
```

> **Note:**
> Use [the currency filter or a number filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the number is formatted.

## `assets`

Returns [opportunity item asset objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md) for items on the opportunity.

#### Input

```
{% for asset in order.assets %}
  {{ asset.name }}
{% endfor %}
```

#### Output

```
Robe ROBIN CycFX 8
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `attachments`

Returns attachment objects for attachments stored against an opportunity.

#### Input

```
{% for attachment in order.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `billing_address`

Returns the opportunity billing address.

#### Input

```
{{ order.billing_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `billing_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the billing address against the opportunity.

#### Input 

```
{{ order.billing_address_detail.state }}
```

#### Output 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `billing_address_name`

Returns the name of the billing address against the opportunity.

#### Input

```
{{ order.delivery_address_name }}
```

#### Output

```
Omni Consumer Products
```

## `charge_excluding_tax_total`

Returns the opportunity charge total excluding tax.

#### Input

```
{{ order.charge_excluding_tax_total }}
```

#### Output

```
450.0
```

## `charge_including_tax_total`

Returns the opportunity charge total including tax.

#### Input

```
{{ order.charge_including_tax_total }}
```

#### Output

```
550.0
```

## `charge_total`

Returns the opportunity charge total.

This may be including or excluding tax depending on the value of the “Catalog Prices” setting in System Preferences.

#### Input

```
{{ order.charge_total }}
```

#### Output

```
450.0
```

## `chargeable_days`

Returns the number of chargeable days for the opportunity.

#### Input

```
{{ order.chargeable_days }}
```

#### Output 

```
1.0
```

## `collection_address`

Returns the opportunity collection address.

You may also use the venue object (below).

#### Input

```
{{ order.collection_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `collection_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the collection address against the opportunity.

#### Input 

```
{{ order.collection_address_detail.state }}
```

#### Output 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `collection_address_name`

Returns the name of the collection address against the opportunity.

You may also use the venue object (below).

#### Input

```
{{ order.collection_address_name }}
```

#### Output

```
Seaview Convention Center
```

## `combined_discount_total`

Returns the total discount from deal pricing and percentage discounting on the opportunity.

#### Input

```
{{ order.combined_discount_total }}
```

#### Output

```
100.0
```

## `consolidated_container_item_assets`

Returns [consolidated asset objects](broken://pages/-LcAVcUbBsX31l5lIhiz) for assets on the opportunity, grouped by container.

#### Input

```
{% for container in order.consolidated_container_item_assets %}
  {% for asset in container[1] %}
    {{ asset.name }}
  {% endfor %}
{% endfor %}
```

#### Output

```
Anton/Bauer Dionic HC battery
Mackie SRM450 Active PA Speaker (PAIR)
Schoeps MK41 Directional Mic
Philips eSTRIP 10 Batten
```

> **Note:**
> Container names are converted to uppercase. Use [a string filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the text is formatted.

See: [Broken mention](broken://pages/-LcAVcUbBsX31l5lIhiz)

## `consolidated_items`

Returns [consolidated item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md) for items on the opportunity.

#### Input

```
{% for item in order.consolidated_items %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
Antari F-1520 RGB Vertical Fogger
Apple MacBook Pro
Doughty Trigger Clamp
i360 Apple iPad Stand
Philips eSTRIP 10 Batten
```

See: [Consolidated opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md)

## `consolidated_principal_items`

Returns [consolidated item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md) for principal items on an opportunity. 

Similar to the `consolidated_items` object (above), but only returns principal items. Accessories are not included.

#### Input

```
{% for item in order.consolidated_principal_items %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
Antari F-1520 RGB Vertical Fogger
Apple MacBook Pro
Doughty Trigger Clamp
i360 Apple iPad Stand
Philips eSTRIP 10 Batten
```

See: [Consolidated opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md)

## `container_item_assets`

Returns [container asset objects](broken://pages/-LcAT8kZxRo0zsDtxUe-) for assets on an opportunity.

#### Input

```
{% for asset in order.container_item_assets %}
  {{ asset.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
D&B E15X Subwoofer
Electric Chain Hoist Controller
Lexar CR2 CFast 2.0 Reader
QTX VHF Wireless Headset Microphone
```

See: [Broken mention](broken://pages/-LcAT8kZxRo0zsDtxUe-)

## `costs`

Returns [opportunity cost objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-costs.md) for costs on an opportunity.

#### Input

```
{% for cost in order.costs %}
  {% cost.subject %}
{% endfor %}
```

#### Output

```
Accomodation
```

See: [Opportunity costs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-costs.md)

## `customer_collecting`

Returns `true` if the “Customer collecting” box is ticked against an opportunity; `false` otherwise.

#### Input

```
{% order.customer_collecting %}
```

#### Output

```
true
```

## `customer_returning`

Returns `true` if the “Customer returning‘ box is ticked against an opportunity; `false` otherwise.

#### Input

```
{% order.customer_returning %}
```

#### Output

```
true
```

## `deal_discount_total`

Returns the total discount from deal pricing on the opportunity.

#### Input 

```
{{ order.deal_discount_total }}
```

#### Output

```
50.0
```

## `deal_exists?`

Returns `true` if the opportunity has deal-priced groups or a deal price; `false` otherwise.

#### Input

```
{{ order.deal_exists? }}
```

#### Output

```
true
```

## `delivery_address`

Returns the opportunity delivery address.

You may also use the venue object (below).

#### Input

```
{{ order.delivery_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `delivery_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the delivery address against the opportunity.

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

Returns the name of the delivery address against the opportunity.

You may also use the venue object (below).

#### Input

```
{{ order.delivery_address_name }}
```

#### Output

```
Seaview Convention Center
```

## `description`

Returns the opportunity (internal) description.

#### Input

```
{{ order.description }}
```

#### Output

```
This client is FUSSY, so let's make sure everything goes right.
```

## `discount_total`

Returns the total discount from percentage discounting on the opportunity.

#### Input

```
{{ order.discount_total }}
```

#### Output

```
50.0
```

## `discussion_email_address`

Returns the discussion email address for the opportunity.

#### Input

```
{{ order.discussion_email_address }}
```

#### Output

```
reply+0+1090cdd0-11f9-0133-abf1-125cc0dc331b++1@app.current-rms.com
```

## `ends_at` 

Returns the end date and time for the opportunity. You may also use `charge_ends_at`.

#### Input

```
{{ order.ends_at }}
```

#### Output

```
2021-04-12 16:00:00 +0000 
```

> **Note:**
> Use [a date filter](https://current-rms.gitbook.io/liquid-syntax/information/date-filter.md) to change the way that the date is formatted.

## `external_description`

Returns the opportunity external description.&#x9;

#### Input

```
{{ order.external_description }}
```

#### Output

```
Every event is special, so we're here to make sure that it all runs smoothly.
```

## `has_discount?`

Returns `true` if the opportunity has percentage based discounts; `false` otherwise.

#### Input

```
{{ order.has_discount? %}
```

#### Output

```
false
```

## `has_invoices?`

Returns `true` if the opportunity has linked invoices; `false` otherwise.

#### Input

```
{{ order.has_invoices? %}
```

#### Output

```
false
```

## `image_attachments` <a href="#image_attachments" id="image_attachments"></a>

Returns attachment objects for attachments stored against an opportunity where the attachment file type is an image.

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

## `id`

Returns the opportunity ID.

> **Warning:**
> The ID is an internal reference for a record. It's not exposed in our web interface and shouldn't be confused with the [opportunity number (below)](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md#number).

#### Input

```
{{ order.id }}
```

#### Output

```
1
```

## `invoiced`

Returns `true` if the opportunity “Invoiced‘ toggle is set to YES; otherwise `false`.

#### Input

```
{{ order.invoiced }}
```

#### Output

```
true
```

## `invoices`

Returns [invoice objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md) for invoices linked to the opportunity.

#### Input

```
{% for invoice in order.invoices %}
  {{ invoice.name }}
{% endfor %}
```

#### Output

```
Deposit for Omni Consumer Products Launch
```

## `items`

Returns [opportunity item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) for items on the opportunity.

#### Input

```
{% for item in order.items %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
D&B E15X Subwoofer
QTX VHF Wireless Headset Microphone
```

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## `items_sorted_by_principal`

Investigate further.

#### Input

```
{% for item in order.items %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
D&B E15X Subwoofer
Selecon Lui Flood 10001 (16A)
```

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## `items_sorted_by_tag`

Investigate further

## `name`

Returns the opportunity subject.

#### Input

```
{{ order.name }}
```

#### Output

```
V-Blast Music Festival
```

## `number`

Returns the opportunity number.

`nil` if the opportunity is an inquiry or a draft.

#### Input

```
{{ order.number }}
```

#### Output

```
PO-001
```

## `open_ended_rental`

Returns `true` if the “Open Ended Rental” toggle against the opportunity is set to YES; otherwise `false`.

#### Input

```
{{ order.open_ended_rental }}
```

#### Output

```
false
```

## `opportunity_has_deal?`

Returns `true` if the entire opportunity has a deal; `false` otherwise. 

> **Note:**
> This will only return `true` if the entire opportunity has a deal; it will return `false` if there are deal priced groups. Use [`deal_exists?` (above)](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md#deal_exists) to check if there's a deal anywhere on the opportunity, including deal priced groups.

#### Input

```
{{ order.opportunity_has_deal? }}
```

#### Output 

```
false
```

## `ordered_at`

Returns the date entered in the opportunity “Document Date” field.&#x9;

#### Input

```
{{ order.ordered_at }} 
```

#### Output

```
2021-03-11 14:00:00 +0000
```

## `original_charge_excluding_tax_total`

Returns the opportunity charge excluding tax total before deal pricing was applied.

#### Input

```
{{ order.original_charge_excluding_tax_total }} 
```

#### Output

```
1201.40
```

## `original_charge_including_tax_total`

Returns the opportunity charge including tax total before deal pricing was applied.

#### Input

```
{{ order.original_charge_including_tax_total }} 
```

#### Output

```
120.14
```

## `original_charge_total`

Returns the opportunity charge total before deal pricing was applied.

#### Input

```
{{ order.original_charge_total }}
```

#### Output

```
1201.4
```

## `original_discount_total`

Returns the opportunity discount total before deal pricing was applied.

#### Input

```
{{ order.original_discount_total }}
```

#### Output

```
100.0
```

## `original_rental_charge_total`

Returns the opportunity rental charge total before deal pricing was applied.

#### Input

```
{{ order.original_rental_charge_total }}
```

#### Output

```
553.97
```

## `original_sale_charge_total`

Returns the opportunity sale charge total before deal pricing was applied.

#### Input

```
{{ order.original_sale_charge_total }}
```

#### Output

```
228.45
```

## `original_service_charge_total`

Returns the opportunity service charge total before deal pricing was applied.

#### Input

```
{{ order.original_service_charge_total }}
```

#### Output

```
1040.72
```

## `original_surcharge_total`

Returns the opportunity surcharge total before deal pricing was applied.

#### Input

```
{{ order.original_surcharge_total }}
```

#### Output

```
108.33
```

## `original_tax_total`

Returns the opportunity tax total before deal pricing was applied.

#### Input

```
{{ order.original_tax_total }}
```

#### Output

```
2300.55
```

## `owner`

Returns [user objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md) with information about the user who owns the opportunity.

#### Input

```
{{ order.owner.name }}
```

#### Output

```
Michael McGovern
```

See: [User](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md)

## `part_invoice_charge_total`

Returns the total of part invoices against the opportunity.

#### Input

```
{{ order.part_invoice_charge_total }}
```

#### Output

```
200.0
```

## `participants`

Returns [contact](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md), [organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md), [user](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md), [vehicle](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/vehicle.md), or [venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md) objects for participants on the opportunity.

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

## `predicted_cost_total`

Returns the predicted cost total for an opportunity. 

The predicted cost total is calculated by totalling actual costs where possible. Where an actual cost hasn't been set, the provisional cost is used. 

#### Input

```
{{ order.predicted_cost_total }}
```

#### Output

```
100.0
```

## `product_assets`

Returns [opportunity item asset objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md) for products on the opportunity. 

Similar to the `assets` object (above), but only returns product assets. Does not return service booking resource allocations.

#### Input

```
{% for asset in order.product_assets %}
  {% asset.name }}
{% endfor %}
```

#### Output

```
Angenieux Optimo 28-76 Zoom Lens T2.6
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `products`

Returns [opportunity item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) for products on the opportunity.

Similar to the `items` object (above), but only returns product opportunity items. Does not return services.

#### Input

```
{% for item in order.products %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
PCE IMST Distro
```

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## `project`

Returns [project objects](https://current-rms.gitbook.io/liquid-syntax/project/project.md) for the project that the opportunity is part of.

`empty` if the opportunity isn't linked to a project.

#### Input

```
{{ order.project.name }}
```

#### Output

```
Bluth Family Homes Roadshow
```

See: [Project](https://current-rms.gitbook.io/liquid-syntax/project/project.md)

## `project_name`

Returns the name of the project that the opportunity is a part of.

`nil` if the opportunity isn't linked to a project.

#### Input

```
{{ order.project.name }}
```

#### Output

```
Bluth Family Homes Roadshow
```

## `provisional_cost_total`

Returns the provisional cost total for an opportunity.

The provisional cost total is calculated by totaling provisional costs.

#### Input

```
{{ order.provisional_cost_total }}
```

#### Output

```
50.0
```

## `purchase_orders`

Returns [purchase order objects](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md) for purchase orders linked to the opportunity.

#### Input

```
{% for purchase_order in order.purchase_order %}
  {{ purchase_order.name }}
{% endfor %}
```

#### Output

```
Sub-rentals for Globex Annual Conference
```

See: [Purchase order](https://current-rms.gitbook.io/liquid-syntax/purchase-orders/purchase-order.md)

## `quote_invalid_at`

Returns the value of the opportunity "Quotation valid until" field.

`nil` if the opportunity isn't a quotation.

#### Input

```
{{ order.quote_invalid_at }}
```

#### Output

```
{{ 2021-04-19 10:00:00 +0000 }}
```

## `reference`

Returns the value of the opportunity customer reference.

#### Input

```
{{ order.reference }}
```

#### Output

```
PO-1099
```

## `rental_charge_total`

Returns the rental charge total for an opportunity.

> **Warning:**
> [Opportunity item](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) charge totals include surcharges, but the opportunity rental charge total object does not. You may wish to add the surcharge total object (below) to the rental charge total.

#### Input

```
{{ order.rental_charge_total }}
```

#### Output

```
803.39
```

## `rentals`

Investigate further

## `replacement_charge_total`

Returns the replacement charge total for the opportunity.

#### Input

```
{{ order.replacement_charge_total }}
```

#### Output

```
22007.20
```

## `sale_charge_total`

Returns the sale charge total for an opportunity.

#### Input

```
{{ order.sale_charge_total }}
```

#### Output

```
213.99
```

## `sales`

Investigate further

## `schedule_type_is_extended?`

Returns `true` if the opportunity uses the extended scheduler; `false` otherwise. 

The scheduler type is set in System Preferences, but the scheduler type on existing opportunities won't be updated.

#### Input

```
{{ order.schedule_type_is_extended? }}
```

#### Output

```
true
```

## `schedule_type_is_extended?`

Returns `true` if the opportunity uses the extended scheduler; `false` otherwise. 

The scheduler type is set in System Preferences, but the scheduler type on existing opportunities won't be updated.

#### Input

```
{{ order.schedule_type_is_extended? }}
```

#### Output

```
true
```

## `schedule_type_is_standard?`

Returns `true` if the opportunity uses the standard scheduler; `false` otherwise. 

The scheduler type is set in System Preferences, but the scheduler type on existing opportunities won't be updated.

#### Input

```
{{ order.schedule_type_is_standard? }}
```

#### Output

```
false
```

## `service_charge_total`

Returns the service charge total for an opportunity.

#### Input

```
{{ order.service_charge_total }}
```

#### Output

```
10290.4
```

## `services`

Investigate further

## `starts_at`

Returns the start date and time for the opportunity. You may also use `charge_starts_at`.

#### Input

```
{{ order.starts_at }}
```

#### Output

```
2021-04-12 10:00:00 +0000
```

## `state`

Returns the opportunity state code.

| Code | State name |
| ---- | ---------- |
| `0`  | Inquiry    |
| `1`  | Draft      |
| `2`  | Quotation  |
| `3`  | Order      |

#### Input

```
{{ order.state }}
```

#### Output 

```
2
```

## `state_name`

Returns the opportunity state name. 

State names are in the language set against your user profile. 

* Inquiry
* Draft
* Quotation
* Order

#### Input

```
{{ order.state_name }}
```

#### Output

```
Quotation
```

## `status`

Returns the opportunity status code.

| Code | Status name |
| ---- | ----------- |
| `0`  | Open        |
| `1`  | Provisional |
| `5`  | Reserved    |
| `20` | Active      |
| `40` | Completed   |
| `50` | Canceled    |
| `60` | Lost        |
| `70` | Dead        |
| 8`0` | Postponed   |

#### Input

```
{{ order.status }}
```

#### Output

```
5
```

## `status_name`

Returns the opportunity status name.

Status names are in the language set against your user profile. 

* Open
* Provisional
* Reserved
* Active
* Completed
* Canceled
* Lost
* Dead

#### Input

```
{{ order.status_name }}
```

#### Output

```
Reserved
```

## `store` <a href="#store" id="store"></a>

Returns [store objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/general/store) for the store against the opportunity.

#### Input <a href="#input-27" id="input-27"></a>

```
{{ order.store.name }}
```

#### Output <a href="#output-26" id="output-26"></a>

```
The Banana Stand
```

See: [Store](https://current-rms.gitbook.io/liquid-syntax/general/store.md)

## `supplier_item_assets`

Returns a list of sub-rented opportunity item assets sorted by supplier.

See: [Broken mention](broken://pages/-LcAVRmHFD6Q9-YIvd5D)

## `surcharge_total`

Returns the surcharge total for an opportunity. 

This isn't returned in the rental charge total object (above).

#### Input

```
{{ order.rental_charge_total }}
```

#### Output

```
803.39
```

## `tax_class_name`

Returns the opportunity tax class.

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

Returns the opportunity tax total.

#### Input

```
{{ order.tax_total }}
```

#### Output

```
100.0
```

## `use_chargeable_days`

Returns `true` if the "Use Chargeable Days" toggle against the opportunity is set to YES; otherwise `false`.

#### Input

```
{{ order.use_chargeable_days }}
```

#### Output

```
true
```

## `venue`

Returns venue objects for the venue against the opportunity.

> **Warning:**
> An opportunity delivery address can be a venue, but a venue might not always be an opportunity's delivery address. If you don't choose a venue when creating an opportunity, using `{{ order.venue.name }}` won't return the same as `{{ order.delivery_address_name }}`.

#### Input

```
{{ order.venue.name }}
```

#### Output

```
Seaview Conference Center
```

## `weight_total`

Returns the opportunity weight total.

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

## Extended scheduler dates

### `prep_starts_at`

Returns the “Prep“ start date and time for the opportunity.

#### Input

```
{{ order.prep_starts_at }}
```

#### Output

```
2021-04-12 10:00:00 +0100 
```

### `prep_ends_at`

Returns the “Prep“ end date and time for the opportunity.

#### Input

```
{{ order.prep_ends_at }}
```

#### Output

```
2021-04-12 11:00:00 +0100 
```

### `load_starts_at`

Returns the “Load“ start date and time for the opportunity.

#### Input

```
{{ order.load_starts_at }}
```

#### Output

```
2021-04-12 11:00:00 +0100 
```

### `load_ends_at`

Returns the “Load“ end date and time for the opportunity.

#### Input

```
{{ order.load_ends_at }}
```

#### Output

```
2021-04-12 12:00:00 +0100 
```

### `deliver_starts_at`

Returns the “Delivery” start date and time for the opportunity.

#### Input

```
{{ order.deliver_starts_at }}
```

#### Output

```
2021-04-12 12:00:00 +0100
```

### `deliver_ends_at`

Returns the “Delivery” end date and time for the opportunity.

#### Input

```
{{ order.deliver_ends_at }}
```

#### Output

```
2021-04-12 13:00:00 +0100 
```

### `setup_starts_at`

Returns the “Setup” start date and time for the opportunity.

#### Input

```
{{ order.setup_starts_at }}
```

#### Output

```
2019-04-12 13:00:00 +0100 
```

### `setup_ends_at`

Returns the “Setup” end date and time for the opportunity.

#### Input

```
{{ order.setup_ends_at }}
```

#### Output

```
2019-04-12 14:00:00 +0100 
```

### `show_starts_at`

Returns the “In Use” start date and time for the opportunity.

#### Input

```
{{ order.show_starts_at }}
```

#### Output

```
2019-04-12 14:00:00 +0100 
```

### `show_ends_at`

Returns the “In Use” end date and time for the opportunity.

#### Input

```
{{ order.show_ends_at }}
```

#### Output

```
2021-04-13 05:00:00 +0100 
```

### `takedown_starts_at`

Returns the “Take Down“ start date for an opportunity.

#### Input

```
{{ order.takedown_starts_at }}
```

#### Output

```
2021-04-13 05:00:00 +0100 
```

### `takedown_ends_at`

Returns the “Take Down“ end date for an opportunity.

#### Input

```
{{ order.takedown_ends_at }}
```

#### Output

```
2021-04-13 06:00:00 +0100 
```

### `collect_starts_at`

Returns the “Pickup“ start date for an opportunity.

Take care not to confuse with the delivery date when customer collection is true. 

#### Input

```
{{ order.collect_starts_at }}
```

#### Output

```
2021-04-13 07:00:00 +0100 
```

### `collect_ends_at`

Returns the “Pickup“ end date for an opportunity.

Take care not to confuse with the delivery date when customer collection is true. 

#### Input

```
{{ order.collect_ends_at }}
```

#### Output

```
2021-04-13 08:00:00 +0100 
```

### `unload_starts_at`

Returns the “Unload“ start date for an opportunity.

#### Input

```
{{ order.unload_starts_at }}
```

#### Output

```
2021-04-13 08:00:00 +0100 
```

### `unload_ends_at`

Returns the “Unload“ end date for an opportunity.

#### Input

```
{{ order.unload_ends_at }}
```

#### Output

```
2021-04-13 09:00:00 +0100 
```

### `deprep_starts_at`

Returns the “De-Prep“ start date for an opportunity.

#### Input

```
{{ order.deprep_starts_at }}
```

#### Output

```
2021-04-13 09:00:00 +0100 
```

### `deprep_ends_at`

Returns the “De-Prep“ ends date for an opportunity.

#### Input

```
{{ order.deprep_ends_at }}
```

#### Output

```
2021-04-13 10:00:00 +0100
```

---
*Source: [Opportunity — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)*
