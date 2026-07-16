# Invoice taxes

In some regions, it’s a requirement to show a breakdown of each tax applied on an invoice. Use the invoice `tax` objects to get information about each tax applied to an invoice. 

Tax objects are always accessed within a forloop that iterates for each tax.

### Document layouts

The `tax` object can be accessed in document layouts created against the following modules:

#### Invoice

```
{% for tax in invoice.taxes %}
  {{ tax.name }}
{% endfor %}
```

#### Opportunity

Returns invoice taxes for invoices linked to a particular opportunity.

```
{% for invoice in order.invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

#### Member

Returns invoice taxes for invoices linked to a particular organization.

```
{% for invoice in member.invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice taxes for active invoices linked to a particular organization.

```
{% for invoice in member.live_invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

### Discussion templates

The `tax` object can be accessed in discussion templates created against the following modules:

#### Invoice

```
{% for tax in invoice.taxes %}
  {{ tax.name }}
{% endfor %}
```

#### Opportunity

Returns invoice taxes for invoices linked to a particular opportunity

```
{% for invoice in opportunity.invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

#### Organization

Returns invoice taxes for invoices linked to a particular organization.

```
{% for invoice in organisation.invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice taxes for active invoices linked to a particular organization.

```
{% for invoice in organisation.live_invoices %}
  {% for tax in invoice.taxes %}
    {{ tax.name }}
  {% endfor %}
{% endfor %}
```

## `id` 

Returns the invoice tax ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ tax.id }}
```

#### Output

```
1
```

## `name`

Returns the invoice tax name.

#### Input

```
{{ tax.name }}
```

#### Output

```
Florida State Sales Tax
```

## `rate` 

Returns the tax rate.

#### Input

```
{{ tax.rate }}
```

#### Output

```
6.0
```

## `tax` 

Returns the amount of tax charged for this tax rate.

#### Input

```
{{ tax.tax }}
```

#### Output

```
15.0
```

> **Note:**
> Use [the currency filter or a number filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the number is formatted.

## `taxable_charge`

Returns the value of goods charged at this tax rate.

#### Input

```
{{ tax.taxable_charge }}
```

#### Output

```
250.0
```

---
*Source: [Invoice taxes — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-tax.md)*
