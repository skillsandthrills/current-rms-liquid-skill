# Service

Generally speaking, [services](https://help.current-rms.com/en/articles/457927-what-is-a-service) are for non-tangible things like labor and transport. Products are for physical things that you rent and sell.

Take care not to confuse services with bookable resources. Your company supplies a service; bookable resources are people, vehicles, or venues who fulfil that service.

### Document layouts

The `service` object can be accessed in document layouts created against the following modules:

#### Opportunity

```
{% for item in order.items %}
  {% if item.is_item? and item.is_service? %}
    {{ item.service.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

```
{% for item in order.items %}
  {% if item.is_item? and item.is_service? %}
    {{ item.service.name }}
  {% endif %}
{% endfor %}
```

#### Invoice

Where a service item has been added directly to an invoice:

```
{% for item in invoice.items %}
  {% if item.is_item? %}
    {% if item.invoiceable_type == "Item" %}
      {{ item.invoicable_object.name }}
    {% endif %}
  {% endif %}
{% endfor %}
```

Where an invoice item is linked to an opportunity item:

```
{% for item in invoice.items %}
  {% if item.is_item? %}
    {% if item.invoiceable_type == "Opportunity Item" %}
      {% if item.invoiceable_object.is_service? %}
        {{ item.invoiceable_object.service.name }}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
```

> **Important:**
> If the original opportunity or opportunity item is deleted, the link between the invoice item and the opportunity item is broken and you won't be able to access service objects in this way.

See: [Invoice items](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md)

### Discussion templates

The `service` object can be accessed in discussion templates created against the following modules:

#### Opportunity

```
{% for item in opportunity.items %}
  {% if item.is_item? and item.is_service? %}
    {{ item.service.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

```
{% for item in purchase_order.items %}
  {% if item.is_item? and item.is_service? %}
    {{ item.service.name }}
  {% endif %}
{% endfor %}
```

#### Invoice

Where a service item has been added directly to an invoice:

```
{% for item in invoice.items %}
  {% if item.is_item? %}
    {% if item.invoiceable_type == "Item" %}
      {{ item.invoicable_object.name }}
    {% endif %}
  {% endif %}
{% endfor %}
```

Where an invoice item is linked to an opportunity item:

```
{% for item in invoice.items %}
  {% if item.is_item? %}
    {% if item.invoiceable_type == "Opportunity Item" %}
      {% if item.invoiceable_object.is_service? %}
        {{ item.invoiceable_object.service.name }}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
```

> **Important:**
> If the original opportunity or opportunity item is deleted, the link between the invoice item and the opportunity item is broken and you won't be able to access service objects in this way.

See: [Invoice items](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md)

## `attachments`

Returns attachment objects for attachments stored against a service.

#### Input

```
{% for attachment in service.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `description` 

Returns the description for a service.

#### Input

```
{{ service.description }}
```

#### Output

```
Whether you’re setting the mood with a few uplighters or bathing a whole stage in light, our skilled folks behind the lighting desk will make sure your event is truly lit.
```

## `discountable?` 

Returns `true` where a service is discountable; `false` otherwise.

#### Input

```
{{ service.discountable }}
```

#### Output

```
true
```

## `external_service_cost_group`

Returns the external service cost group against a service. 

This is the cost group used where a bookable resource is external.

#### Input

```
{{ service.external_service_cost_group }}
```

#### Output

```
Other
```

## `icon_url` 

Returns a URL pointing at the service image. The full size image is returned.

#### Input

```
{{ service.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/icons/247/original/jakob-owens-317800-unsplash.jpg
```

## `id` 

Returns the service ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ service.id }}
```

#### Output

```
1
```

## `image_attachments`

Returns attachment objects for attachments stored against a service where the attachment file type is an image.

#### Input  <a href="#input-5" id="input-5"></a>

```
{% for attachment in service.image_attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output  <a href="#ouput-1" id="ouput-1"></a>

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `internal_service_cost_group` 

Returns the external service cost group against a service. 

This is the cost group used where a bookable resource is external.

#### Input

```
{{ service.external_service_cost_group }}
```

#### Output

```
Other
```

## `name` 

Returns the service name.

#### Input

```
{{ service.name }}
```

#### Output

```
Lighting Tech
```

## `service_revenue_group` 

Returns the revenue group name for a service.

#### Input

```
{{ service.revenue_group }}
```

#### Output

```
Service
```

## `service_type` 

Returns the service type code.

| Code    | Service type |
| ------- | ------------ |
| `10001` | Crew         |
| `10002` | Transport    |
| `10003` | Location     |
| `10004` | Other        |

#### Input

```
{{ service.service_type }}
```

#### Output

```
10001
```

## `service_type_name`

Returns the service type name.

* Crew
* Transport
* Location
* Other

#### Input

```
{{ service.service_type_name }}
```

#### Output

```
Crew
```

## Rates

### `day_price` 

Returns the day rate for a service.

#### Input

```
{{ service.day_price }}
```

#### Output

```
100.00
```

### `hour_price` 

Returns the hour rate for a service.

#### Input

```
{{ service.hour_price }}
```

#### Output

```
10.00
```

### `distance_price`

Returns the distance rate for a service.

#### Input

```
{{ service.distance_price }}
```

#### Output

```
1.00
```

### `flat_rate_price` 

Returns the flat rate for a service.

#### Input

```
{{ service.flat_rate_price }}
```

#### Output

```
1000.00
```

---
*Source: [Service — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/service/service.md)*
