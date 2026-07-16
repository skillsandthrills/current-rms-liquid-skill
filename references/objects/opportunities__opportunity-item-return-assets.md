# Opportunity return item assets

An opportunity return item asset is a record of a check-in. It lets you know how many units were checked-in as damaged, lost, ok, returned, or sold against an opportunity item asset.

### Objects that return opportunity return item assets

You can access opportunity return item assets against the opportunity item asset object.

```
{% for asset in order.product_assets %}
  {% for return in asset.return_assets %} 
    {{ return.return_at }}
  {% endfor %}
{% endfor %}
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

### Example

Print from an order with finalized stock to see how the opportunity return item assets object works.

{% file src="/files/-MOkzZOMQZXa8fYTTekF" %}
Opportunity return item assets
{% endfile %}

## `asset_number`

Returns a return item asset's asset number.

#### Input

```
{{ return.asset_number }}
```

#### Output

```
APP-101
```

## `damage_description`

Returns a return item asset's damage description.

#### Input

```
{{ return.damage_description }}
```

#### Output

```
Dropped when loading.
```

## `quantity_damaged`

Returns the quantity damaged for a return item asset.

#### Input

```
{{ return.quantity_damaged }}
```

#### Output

```
0.0
```

## `quantity_lost`

Returns the quantity lost for a return item asset.

#### Input

```
{{ return.quantity_lost }} 
```

#### Output

```
0.0
```

## `quantity_ok`

Returns the quantity OK for a return item asset.

#### Input

```
{{ return.quantity_ok }}
```

#### Output

```
1.0
```

## `quantity_returned`

Returns the quantity returned for a return item asset. For sales only.

#### Input

```
{{ return.quantity_returned }} 
```

#### Output

```
0.0
```

## `quantity_sold`

Returns the quantity sold for a return item asset. For sales only.

#### Input

```
{{ return.quantity_returned }}
```

#### Output

```
0.0
```

## `return_at`

Returns an opportunity return item asset's check-in date.

#### Input

```
{{ return.return_at }}
```

#### Output

```
2021-05-23 17:00:00 +0100	
```

---
*Source: [Opportunity return item assets — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-return-assets.md)*
