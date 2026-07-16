# Quarantine

When an item is damaged, lost, or in for service, you may move it to the [quarantine](https://help.current-rms.com/en/articles/422143-what-is-the-quarantine). 

A quarantine record holds information about the damage, loss, or service. It's common for folks to upload attachments to record details of the damage and store detailed notes in the description.

### Document layouts

The `quarantine` object can be accessed in document layouts created against the following records:

#### Quarantine

```
{{ quarantine.reference }}
```

### Discussion templates

The `quarantine` object can be accessed in discussion templates created against the following records:

#### Quarantine

```
{{ quarantine.reference }}
```

## `activities`

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to a quarantine.

#### Input  <a href="#input" id="input"></a>

```
{% for activity in order.activities %}
  {{ activity.subject }}
{% endif %}
```

#### Output  <a href="#ouput" id="ouput"></a>

```
Call to follow up
```

See: [Activity](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md)

## `attachments`

Returns attachment objects for attachments stored against a quarantine.

#### Input

```
{% for attachment in quarantine.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `description` 

Returns the description for a quarantine

#### Input

```
{{ quarantine.description }}
```

#### Output

```
Screen damaged
```

## `ends_at`

Returns the end date and time for a quarantine.

> **Warning:**
> If open ended, a quarantine's end date will default to years in future. Use [`is_open_ended?`](https://current-rms.gitbook.io/liquid-syntax/quarantine/quarantine.md#is_open_ended) to handle this.

#### Input

```
{{ quarantine.ends_at }}
```

#### Output

```
2021-04-12 16:00:00 +0000 
```

> **Note:**
> Use [a date filter](https://current-rms.gitbook.io/liquid-syntax/information/date-filter.md) to change the way that the date is formatted.

## `id` 

Returns a quarantine ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ quarantine.id }}
```

#### Output

```
1
```

## `image_attachments`

Returns attachment objects for attachments stored against a quarantine where the attachment file type is an image.

> **Note:**
> Use [`images`](https://current-rms.gitbook.io/liquid-syntax/quarantine/quarantine.md#images) where you just need to return image URLs. Use `image_attachments` where you'd like to return image names, file names, and other data.

#### Input  <a href="#input" id="input"></a>

```
{% for attachment in quarantine.image_attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output  <a href="#ouput" id="ouput"></a>

```
Photograph of damage
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `images` 

Returns an array of URLs for image attachments against this quarantine. 

Typically used to included photographs of damaged goods on a quarantine note.

#### Input

```
{% for image in quarantine.images %}
  <img src="{{ image }}">
{% endfor %}
```

#### Output

```
<img src="https://s3.amazonaws.com/current-rms/1090cdd0-11f9-0133-abf1-125cc0dc331b/attachments/551/original/damage.png">
```

## `is_open_ended?` 

Returns `true` if a quarantine is open ended; `false` otherwise.

#### Input

```
{{ quarantine.is_open_ended? }}
```

#### Output

```
false
```

## `name` 

Returns the name of the quarantined product.

#### Input

```
{{ quarantine.name }}
```

#### Output

```
Atari Z-1520
```

## `next_booking` 

Returns opportunity objects for the next opportunity that a quarantine is booked on.

#### Input

```
{{ quarantine.next_booking.name }}
```

#### Output

```
Bluth Company Picnic
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `product` 

Returns product objects for a quarantine.

#### Input 

```
{{ quarantine.product.description }}
```

#### Output

```
Want to add colors to your fog effects? Not a problem! Let Antari Z-1520 RGB fulfill your dreams. With additional 22 RGB bright LED to shine the fog output produced by Antari Z-1520, the evolutionary successor of well-known Z-1020.
```

See: [Product](https://current-rms.gitbook.io/liquid-syntax/products/product.md)

## `quantity` 

Returns the quantity quarantined. Useful for bulk and non-stock stock products.

#### Input

```
{{ quarantine.quantity }}
```

#### Output

```
10
```

## `quantity_booked_out` 

Returned the quantity booked out of quarantine. 

#### Input

```
{{ quarantine.quantity_booked_out }}
```

#### Output

```
1
```

## `quantity_outstanding` 

Returns the quantity yet to be booked out of quarantine.

#### Input

```
{{ quarantine.quantity_outstanding }}
```

#### Output

```
9
```

## `reference` 

Returns the reference (subject) of a quarantine.

#### Input

```
{{ quarantine.reference }}
```

#### Output

```
Damaged
```

## `source` 

Returns opportunity objects for the source opportunity related to a quarantine.

A quarantine will have a source opportunity where an item was checked-in as lost, damaged, or a sale return from an opportunity. 

#### Input

```
{{ quarantine.source.name }}
```

#### Output

```
Omni Consumer Products Launch
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `starts_at` 

Returns the start date and time for a quarantine.

#### Input

```
{{ quarantine.starts_at }}
```

#### Output

```
2021-03-12 16:00:00 +0000 
```

## `stock_level` 

Returns stock level objects for a quarantine.

#### Input

```
{{ quarantine.stock_level.asset_number }}
```

#### Output

```
AA-1234
```

## `supplier` 

Returns organization objects for the supplier related to this opportunity.

A quarantine will have a related supplier where it is a supplier return, or is damaged or lost sub-rent stock.

#### Input

```
{{ quarantine.supplier.name }}
```

#### Output

```
Happily Ever After, Inc.
```

See: [Organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)

## `type`

Returns the quarantine type name

* Damaged
* Lost
* Service
* Supplier Return
* Sale Return
* Swapped Component

#### Input

```
{{ quarantine.type }}
```

#### Output

```
Damaged
```

---
*Source: [Quarantine — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/quarantine/quarantine.md)*
