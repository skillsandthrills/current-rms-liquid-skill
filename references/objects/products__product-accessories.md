# Product accessories

[Accessories](https://help.current-rms.com/en/articles/402500-link-products-together-using-accessories) are a way of saying that a particular product is rented or sold with other products. The classic example that we use because it's easily understandable is a MacBook Pro that's sold with a mouse and some headphones.

In this example:

* The MacBook Pro is the parent product.
* The mouse and headphones are accessory products.

Accessories are products in Current RMS. They may be rented or sold on their own, depending on how they're set up.

When you set up a product as an accessory against another product, it creates a product accessory record. The product accessory object lets you access information about this record, such as when the product is included.

### Terminology

Some of the terminology can be a little confusing at first, so it's worth creating or editing an accessory in the web interface to understand.

In the example above, we can see:

> When you **rent** an **Apple MacBook Pro**, this **\[Apple Wireless Mouse]** will be **rented** as a **default accessory**.

Thinking in terms of objects, we can break this down like this:

> When you (parent transaction type) the (parent product), the (product) will be (item transaction type) as a (inclusion type) (mode).

| Object                  | Example              |
| ----------------------- | -------------------- |
| Parent transaction type | rent                 |
| Parent product          | Apple MacBook Pro    |
| Accessory product       | Apple Wireless Mouse |
| Item transaction type   | rented               |
| Inclusion type          | default              |
| Mode                    | accessory            |

### Objects that return product accessories

`product_accessories` is an object of the product object, so you may access it anywhere you may access the product object.

It's generally only useful for documents and discussion templates created against the product module. 

For example, while you may access product accessories on an opportunity document using opportunity items, there's little reason to do this. Consider:

```markup
<ul>
  {% for item in order.products %}
    {% if item.is_item? %}
      <li><strong>{{ item.name }}</strong></li>
      <ul>
        {% for accessory in item.product.accessories %}
          <li>{{ accessory.product.name }}</li>
        {% endfor %}
      </ul>
    {% endif %}
  {% endfor %}
</ul>
```

This will return items in a list, with product accessories as a sub-list. However, it will return product accessories as they are against a product in Resources > Products. It won't return an opportunity item's accessories, which may be different. It also won't tell you anything about the quantities or prices of those opportunity item accessories.

In this case, you'd be better using the `is_accessory?` object against opportunity items to determine whether or not they're accessories. You may also access an opportunity item's mode, inclusion type, and other information.

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

### Document layouts

The `product_accessories` object can be accessed in document layouts created against the following modules:

#### Product

```
{% for accessory in product.accessories %}
  {{ accessory.mode_name }}
{% endfor %}
```

### Discussion templates

The `product_accessories` object can be accessed in discussion templates created against the following modules:

#### Product

```
{% for accessory in product.accessories %}
  {{ accessory.mode_name }}
{% endfor %}
```

## for\_parent\_rental? 

Returns `true` if an accessory's parent product is rented; `false` otherwise.

#### Input

```
{{ accessory.for_parent_rental? }}
```

#### Output

```
true
```

## for\_parent\_sale? 

Returns `true` if an accessory's parent product is sold; `false` otherwise.

#### Input

```
{{ accessory.for_parent_sale? }}
```

#### Output

```
false
```

## id 

Returns the ID for a product accessory.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ accessory.id }}
```

#### Output

```
1
```

## is\_default? 

Returns `true` if an accessory's inclusion type is default; `false` otherwise.

#### Input

```
{{ accessory.is_default? }}
```

#### Output

```
true
```

## is\_mandatory? 

Returns `true` if an accessory's inclusion type is mandatory; `false` otherwise.

#### Input

```
{{ accessory.is_mandatory? }}
```

#### Output

```
false
```

## is\_optional? 

Returns `true` if an accessory's inclusion type is optional; `false` otherwise.

#### Input

```
{{ accessory.is_optional? }}
```

#### Output

```
false
```

## item\_transaction\_type\_is\_rental? 

Returns `true` if an accessory's transaction type is rental; `false` otherwise.

#### Input

```
{{ accessory.item_transaction_type_is_rental? }}
```

#### Output

```
true
```

## item\_transaction\_type\_is\_sale? 

Returns `true` if an accessory's transaction type is sale; `false` otherwise.

#### Input

```
{{ accessory.item_transaction_type_is_sale? }}
```

#### Output

```
false
```

## item\_transaction\_type\_name 

Returns the accessory transaction type name for an accessory.

* Rental
* Sale

#### Input

```
{{ accessory.item_transaction_type_name }}
```

#### Output

```
Rental
```

## mode 

Returns the accessory mode code for an accessory.

| Code | Mode        |
| ---- | ----------- |
| 0    | Accessory   |
| 1    | Safety item |
| 2    | Component   |

#### Input

```
{{ accessory.mode }}
```

#### Output

```
1
```

## mode\_is\_accessory? 

Returns `true` if an accessory's mode is accessory; `false` otherwise.

#### Input

```
{{ accessory.mode_is_accessory? }}
```

#### Output

```
true
```

## mode\_is\_component? 

Returns `true` if an accessory's mode is component; `false` otherwise.

#### Input

```
{{ accessory.mode_is_component? }}
```

#### Output

```
```

## mode\_is\_safety? 

Returns `true` if an accessory's mode is safety; `false` otherwise.

#### Input

```
{{ accessory.mode_is_safety? }}
```

#### Output

```
```

## mode\_name 

Returns an accessory's mode name.

* Accessory
* Safety Item
* Component

#### Input

```
{{ accessory.mode_name }}
```

#### Output

```
Accessory
```

## parent\_transaction\_type 

Returns the parent product's accessory transaction type code.

| Code |        |
| ---- | ------ |
| `0`  | Both   |
| `1`  | Rental |
| `2`  | Sale   |

#### Input

```
{{ accessory.parent_transaction_type }}
```

#### Output

```
1
```

## parent\_transaction\_type\_is\_both? 

Returns `true` if an accessory is included when the parent is both rented and sold; `false` otherwise.

#### Input

```
{{ accessory.parent_transaction_type_is_both? }}
```

#### Output

```
false
```

## parent\_transaction\_type\_is\_rental? 

Returns `true` if an accessory is included when the parent is rented; `false` otherwise.

#### Input

```
{{ accessory.parent_transaction_type_is_rental? }}
```

#### Output

```
true
```

## parent\_transaction\_type\_is\_sale? 

Returns `true` if an accessory is included when the parent is sold; `false` otherwise.

#### Input

```
{{ accessory.parent_transaction_type_is_sale? }}
```

#### Output

```
false
```

## parent\_transaction\_type\_name 

Returns the parent product's accessory transaction type code.

* Both
* Rental
* Sale

#### Input

```
{{ accessory.parent_transaction_type_name }}
```

#### Output

```
Rental
```

## product 

Returns product objects for a product accessory.

#### Input

```
{{ accessory.product.description }}
```

#### Output

```
Clicking. Double-clicking. Everything a mouse should do.
```

See: [Product](https://current-rms.gitbook.io/liquid-syntax/products/product.md)

## quantity 

Returns an accessory product's quantity.

#### Input

```
{{ accessory.quantity }}
```

#### Output

```
1.0
```

## sort\_order 

Returns an accessory product's sort order. This is the order that they're in the list of accessories against a product page. 

The sort order determines the initial order in which an accessory is listed under a parent product when added to an opportunity.

#### Input

```
{{ accessory.sort_order }}
```

#### Output

```
0
```

## zero\_priced?

Returns `true` if an accessory product is included at zero price; `false` otherwise.

#### Input

```
{{ accessory.zero_priced? }}
```

#### Output

```
true
```

---
*Source: [Product accessories — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/products/product-accessories.md)*
