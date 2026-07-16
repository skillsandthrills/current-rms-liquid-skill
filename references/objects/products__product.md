# Product

[Products](https://help.current-rms.com/en/articles/402487-what-is-a-product) in Current RMS are things you rent and sell to customers. They're generally physical, tangible things that you stock.

### Document layouts

The `product` object can be accessed in document layouts created against the following records:

#### Product

```
{{ product.name }}
```

#### Opportunity

```
{% for item in order.products %}
  {% if item.is_item? %}
    {{ item.product.name }}
  {% endif %}
{% endfor %}
```

#### Quarantine

```
{{ quarantine.product.name }}
```

#### Inspection result

```
{{ inspection_result.product.name }}
```

#### Inventory check

```
{{ stock_check.product.name }}
```

#### Purchase order

```
{% for item in order.items %}
  {% if item.is_item? and item.is_product? %}
    {{ item.product.name }}
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
      {% if item.invoiceable_object.is_product? %}
        {{ item.invoiceable_object.service.name }}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
```

> **Important:**
> If the original opportunity or opportunity item is deleted, the link between the invoice item and the opportunity item is broken and you won't be able to access service objects in this way.

### Discussion templates

The `product` object can be accessed in discussion templates created against the following records:

#### Product

```
{{ product.name }}
```

#### Opportunity

```
{% for item in opportunity.products %}
  {% if item.is_item? %}
    {{ item.product.name }}
  {% endif %}
{% endfor %}
```

#### Quarantine

```
{{ quarantine.product.name }}
```

#### Inspection result

```
{{ inspection_result.product.name }}
```

#### Inventory check

```
{{ stock_check.product.name }}
```

#### Purchase order

```
{% for item in purchase_order.items %}
  {% if item.is_item? and item.is_product? %}
    {{ item.product.name }}
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
      {% if item.invoiceable_object.is_product? %}
        {{ item.invoiceable_object.service.name }}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}
```

> **Important:**
> If the original opportunity or opportunity item is deleted, the link between the invoice item and the opportunity item is broken and you won't be able to access service objects in this way.

## `accessories` 

Returns product accessory objects for accessory products against this product.

#### Input

```
<ul>
  {% for accessory in product.accessories %}
    <li>{{ accessory.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Pioneer HDJ2000 DJ Headphones
• XLR 10m
```

See: [Product accessories](https://current-rms.gitbook.io/liquid-syntax/products/product-accessories.md)

## `accessory_only` 

Returns `true` where this product is accessory only; `false` otherwise.

> **Note:**
> There's no question mark at the end of this object.

#### Input

```
{{ product.accessory_only }}
```

#### Output

```
false
```

## `assets` 

Returns product asset objects for stock levels against a product.

#### Input

```
{% for asset in product.assets %}
  {{ asset.asset_number }}
{% endfor %}
```

#### Output

```
ABC-123
```

See: [Product assets](https://current-rms.gitbook.io/liquid-syntax/products/product-assets.md)

## `attachments` <a href="#attachments" id="attachments"></a>

Returns attachment objects for attachments stored against a product.

#### Input <a href="#input-3" id="input-3"></a>

```
{% for attachment in product.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output <a href="#output-3" id="output-3"></a>

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `barcode` 

Where bulk or non-stock, returns the barcode set against a product.

To return a barcode number for a serialized asset, use [the `stock_level` object](https://current-rms.gitbook.io/liquid-syntax/products/product.md#stock_levels).

#### Input

```
{{ product.barcode }}
```

#### Output

```
BAR-001
```

## `charging_periods` 

Returns charging period objects for a rental charge against a product.

#### Input

```
{% for charge_period in product.charging_periods %}
  {{ charge_period.name }}
{% endfor %}
```

#### Output

```
day
```

See: [Charging period](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md)

## country\_of\_origin\_code

Returns the country of origin set against a product.

#### Input

```
{{ product.country_of_origin_code }}
```

#### Output

```
United Kingdom
```

## `description` 

Returns the description for a product.

#### Input

```
{{ product.description }}
```

#### Output

```
Let there be light, and there was! Soft bright white light -- to be more precise -- illuminating your special event and making everyone feel cozy and warm.
```

## `discountable?` 

Returns `true` if a product is discountable; `false` otherwise.

#### Input

```
{{ product.discountable? }}
```

#### Output

```
true
```

## `has_accessories?` 

Returns `true` if a product has accessories; `false` otherwise.

#### Input

```
{{ product.has_accessories? }}
```

#### Output

```
true
```

## `icon_url` 

Returns a URL pointing at a product's image. The full size image is returned.

#### Input

```
{{ product.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/icons/52/original/Logi_CREATE_Keyboard_Case_Blue.0.jpg
```

## `id` 

Returns a product's ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ product.id }}
```

#### Output

```
1
```

## `image_attachments` 

Returns attachment objects for attachments stored against a product. Only returns those that have a file type of image.

#### Input <a href="#input-2" id="input-2"></a>

```
{% for attachment in product.attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output <a href="#output-2" id="output-2"></a>

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `is_bulk_stock?` 

Returns `true` if a product is bulk; `false` otherwise.

#### Input

```
{{ product.is_bulk_stock? }}
```

#### Output

```
true
```

## `is_non_stock?` 

Returns `true` if a product is non-stock; `false` otherwise.

#### Input

```
{{ product.is_non_stock? }}
```

#### Output

```
false
```

## `is_serialised_stock?` 

Returns `true` if a product is serialized; `false` otherwise.

#### Input

```
{{ product.is_serialised_stock? }}
```

#### Output

```
false
```

## `name` 

Returns a product's name.

#### Input

```
{{ product.name }}
```

#### Output

```
Pioneer XDJ RX
```

## `post_rent_unavailability` 

Returns a product's post rent unavailability value.

A unit, i.e. your system availability period, is not returned.

#### Input

```
{{ product.post_rent_unavailability }}
```

#### Output

```
1
```

## `product_group` 

Returns product group objects for a product's related product group.

#### Input

```
{{ product.product_group.description }}
```

#### Output

```
Things that make noise.
```

See: [Product group](https://current-rms.gitbook.io/liquid-syntax/products/product-group.md)

## `product_group_name` 

Returns a product's related product group name.

#### Input

```
{{ product.product_group_name }}
```

#### Output

```
Audio
```

## `purchase_cost_group` 

Returns the purchase cost group for a product.

#### Input

```
{{ product.purchase_cost_group }}
```

#### Output

```
Sales
```

## `rental_charge_period_name` 

Returns the rental charge period name for a product.  

#### Input

```
{{ product.rental_charge_period_name }}
```

#### Output

```
daily
```

## `rental_price` 

Returns the rental price for a product.

#### Input

```
{{ product.rental_price }}
```

#### Output

```
100.0
```

## `rental_rate_definition_name` 

Returns the rental rate definition name against a product.

#### Input

```
{{ product.rental_rate_definition_name }}
```

#### Output

```
Daily Rate
```

## `rental_revenue_group` 

Returns the rental revenue group against a product.

#### Input

```
{{ product.rental_revenue_group }}
```

#### Output

```
Rental
```

## `replacement_charge` 

Returns the replacement charge against a product.

#### Input

```
{{ product.replacement_charge }}
```

#### Output

```
100.0
```

## `sale_price` 

Returns the sale price for a product.

#### Input

```
{{ product.sale_price }}
```

#### Output

```
1000.0
```

## `sale_revenue_group` 

Returns the sale revenue group against a product.

#### Input

```
{{ product.sale_revenue_group }}
```

#### Output

```
Sales
```

## `stock_levels` 

Returns stock level objects for stock levels against a product.

#### Input

```
{% for stock_level in product.stock_levels %}
  {{ stock_level.asset_number }}
{% endfor %}
```

#### Output

```
ABC-123
```

See: [Stock level](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md)

## `sub_rental_cost_group` 

Returns the sub-rental cost group for a product.

#### Input

```
{{ product.sub_rental_cost_group }}
```

#### Output

```
Sub-Rental
```

## `weight`

Returns a product's weight.

#### Input

```
{{ product.weight }}
```

#### Output

```
10.0
```

> **Note:**
> Use the `weight_unit` against [the company object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to print your company's weight unit.

---
*Source: [Product — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/products/product.md)*
