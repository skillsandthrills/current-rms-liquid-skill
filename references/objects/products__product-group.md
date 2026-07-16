# Product group

A product group is a way of categorizing products. You can create and maintain product groups in System Setup > Product Groups.

### Opportunity groups

Take care not to confuse product groups with opportunity groups. Opportunity groups categorize opportunity items. 

When you add products to an opportunity, opportunity groups are created with the same names as your product groups. You can change and rename opportunity groups, nest groups, and even delete them.

Though the names may be the same, opportunity groups will not return product group objects. They are opportunity items and return opportunity item objects. 

### Objects that return product group objects

`product_group` is an object of the product object, so you may access it anywhere you may access the product object.

See: [Product](https://current-rms.gitbook.io/liquid-syntax/products/product.md)

Where you're counting a product group on an inventory check, you may access the `product_group` object there, too:

```
{{ stock_check.product_group.name }}
```

## `description`

Returns the description against a product group.

#### Input

```
{{ product.product_group.description }}
```

#### Output

```
Things that make noise.
```

## `icon_url`

Returns a URL pointing at the image for a product group.

#### Input

```
{{ product_group.description }}
```

#### Output

```
https://s3.amazonaws.com/cobra-ca9a7ac0-2539-0131-ba41-0050569ba36f/icons/267/thumb/wa.png
```

## `name`

Returns the name of a product group.

#### Input

```
{{ product_group.name }}
```

#### Output

```
Audio
```

---
*Source: [Product group — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/products/product-group.md)*
