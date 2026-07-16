# Charging period

The charging period object will give you roughly the information that you see when you hover over a charge total on an opportunity. It lets you know how a charge total was calculated.

In the example above, we see:

> Days: $11.20 x 2\
> Weeks: $56.00 x 7

We can break this into `name`, `rate`, and `count` objects:

| Name  | Rate  | Count |
| ----- | ----- | ----- |
| Days  | 11.20 | 2     |
| Weeks | 56.00 | 7     |

While many rates will have just one period (e.g. a daily rate), charging period objects are printed using a forloop for cases like above where there are multiple periods.

When using a rate that uses a daily multiplier engine, the count object gives you the multiplier.

### Document layouts

The `charging_period` object can be accessed in document layouts created against the following modules:

#### Opportunity

```
{% for item in order.products %}
  {% if item.is_item? and item.is_rental? %}
    {% for period in item.charging_period %}
      {{ period.count }} {{ period.name }}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Product

```
{% for period in product.charging_periods %}
  {{ period.name }}
{% endfor %}
```

### Discussion templates

The `charging_period` object can be accessed in discussion templates created against the following modules:

#### Opportunity

```
{% for item in opportunity.products %}
  {% if item.is_item? and item.is_rental? %}
    {% for period in item.charging_period %}
      {{ period.count }} {{ period.name }}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Product

```
{% for period in product.charging_periods %}
  {{ period.name }}
{% endfor %}
```

## `base_rate` 

Returns the charging period rate excluding discount.

#### Input

```
{{ period.base_rate }}
```

#### Output

```
200.0
```

## `count` 

Returns the number of periods against a charging period.

#### Input

```
{{ period.count }}
```

#### Output

```
2.0
```

## `name` 

Returns the charging period rate excluding discount.

#### Input

```
{{ period.name }}
```

#### Output

```
days
```

## `rate`

Returns the charging period rate excluding discount.

#### Input

```
{{ period.rate }}
```

#### Output

```
50.0
```

---
*Source: [Charging period — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/products/charging-period.md)*
