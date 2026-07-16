# Inventory check (stock check)

An [inventory check](https://help.current-rms.com/en/articles/3532962-count-your-inventory-using-inventory-check) is a way of scanning or manually counting your stock to make sure your inventory is accurate. An inventory check record in Current RMS is a record of a particular count that took place.

In some regions, it's called a stock check. We also call it a `stock_check` under the hood.

### Document layouts

The `stock_check` object can be accessed in document layouts created against the following records:

#### Inventory check

```
{{ stock_check.subject }}
```

## `allowed_stock_type` 

Returns an ID for the allowed stock type against the stock check.

| ID  | Allowed stock type |
| --- | ------------------ |
| `0` | All                |
| `1` | Rental             |
| `2` | Sale               |

#### Input

```
{{ stock_check.allowed_stock_type }}
```

#### Output

```
0
```

## `allowed_stock_type_name` 

Returns the allowed stock type against the inventory check:

* All
* Rental
* Sale

#### Input

```
{{ stock_check.allowed_stock_type_name }}
```

#### Output

```
All
```

## `auto_return_bookings` 

Returns `true` if "Auto Return Bookings" is set to YES; `false` otherwise.

#### Input

```
{{ stock_check.auto_return_bookings }}
```

#### Output

```
true
```

## `auto_return_bookings_to_word` 

Returns the value of "Auto Return Bookings" in the user's locale language.

#### Input

```
{{ stock_check.auto_return_bookings_to_word }}
```

#### Output

```
Yes
```

## `item_name` 

When checking a product, the name of the product.

#### Input

```
{{ stock_check.item_name }}
```

#### Output

```
MacBook Pro
```

## `product` 

When checking a product, returns product objects.

#### Input

```
{{ stock_check.product.description }}
```

#### Output

```
Loaded with everything you need to get your job done.
```

See: [Product](https://current-rms.gitbook.io/liquid-syntax/products/product.md)

## `product_group` 

When checking a product group, returns product group objects.

#### Input

```
{{ stock_check.product_group.description }}
```

#### Output

```
Things that make noise
```

See: [Product group](https://current-rms.gitbook.io/liquid-syntax/products/product-group.md)

## `product_group_name` 

When checking a product group, returns the product group name.

#### Input

```
{{ stock_check.product_group_name }}
```

#### Output

```
Audio
```

## `status` 

Returns the status ID for an inventory check.

| ID  | Status        |
| --- | ------------- |
| `0` | Open          |
| `1` | Submitted     |
| `2` | Completed     |
| `3` | Failed        |
| `4` | Revering      |
| `5` | Revert failed |
| `6` | Canceled      |

#### Input

```
{{ stock_check.status }}
```

#### Output

```
0
```

## `status_name` 

Returns the status name for an inventory check.

* Open
* Submitted
* Completed
* Failed
* Reverted
* Revert failed
* Canceled

#### Input

```
{{ stock_check.status_name }}
```

#### Output

```
Open
```

## `stock_check_at` 

Returns the date and time of an inventory check.

#### Input

```
{{ stock_check.stock_check_at }}
```

#### Output

```
2021-04-12 16:00:00 +0000 
```

## `stock_check_items` 

Returns inventory check items for items on an inventory check.

#### Input

```
{% for item in stock_check.stock_check_items %}
  {{ stock_check_item.asset_number }}
{% endfor %}
```

#### Output

```
ABC-123
```

See: [Inventory check items (stock check items)](https://current-rms.gitbook.io/liquid-syntax/inventory-check/inventory-check-items-stock-check-items.md)

## `subject` 

Returns the subject of an inventory check.

#### Input

```
{{ stock_check.subject }}
```

#### Output

```
Quarterly count
```

## `tag_filter`

Returns a comma separated list of tags used to filter an inventory check.

#### Input

```
{{ stock_check.tag_filter }}
```

#### Output

```
Apple, Retina
```

---
*Source: [Inventory check (stock check) — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/inventory-check/inventory-check-stock-check.md)*
