# Inventory check items (stock check items)

An inventory check is a record of an audit of your inventory. Inventory check items are stock levels that were counted as part of that particular check.

Inventory check item objects are available from the inventory check object. They'r accessed in a forloop that iterates through inventory check items.

```
{% for item in stock_check.stock_check_items %}
  {{ item.asset_number }}
{% endfor %}
```

See: [Inventory check (stock check)](https://current-rms.gitbook.io/liquid-syntax/inventory-check/inventory-check-stock-check.md)

## `asset_number`

If serialized, returns the asset number of an inventory check item.

#### Input

```
{{ item.asset_number }}
```

#### Output

```
ABC-123
```

## `quantity_available` 

Returns the quantity available on an inventory check item.

#### Input

```
{{ item.quantity_available }}
```

#### Output

```
1
```

## `quantity_booked` 

Returns the quantity booked on an inventory check item.

#### Input

```
{{ item.quantity_booked }}
```

#### Output

```
1
```

## `quantity_change` 

Returns the quantity change on an inventory check item.

#### Input

```
{{ item.quantity_change }}
```

#### Output

```
1
```

## `quantity_counted`

Returns the quantity counted on an inventory check item.

#### Input

```
{{ item.quantity_counted }}
```

#### Output

```
1
```

## `quantity_held`

Returns the quantity held on an inventory check item.

#### Input

```
{{ item.quantity_held }}
```

#### Output

```
1
```

## `stock_level`

Returns stock level objects for an inventory check item's related stock level.

#### Input

```
{{ item.stock_level.item_name }}
```

#### Output

```
MacBook Pro
```

---
*Source: [Inventory check items (stock check items) — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/inventory-check/inventory-check-items-stock-check-items.md)*
