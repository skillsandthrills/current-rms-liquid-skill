# Invoice transactions

Use the Take Payment functionality to log payments and refunds against invoices in Current RMS. 

> **Warning:**
> We don't recommend using invoice transaction objects when linked to Xero or QuickBooks Online. Transactions logged in Xero and QuickBooks Online are not accessible in document layouts or discussion templates.

When integrated with QuickBooks Online, there's no facility to record payments in Current RMS.

When integrated with Xero, the Take Payment function posts payments across to Xero. **Only transactions recorded using the Take Payment function can be accessed on document layouts and discussion templates.** Transactions logged directly in Xero are not accessible in document layouts or discussion templates. 

### Example

Here's an example of a document that prints transactions. 

{% file src="/files/-LdTL0NZhe\_VkvrRn-wx" %}
Example invoice receipt document
{% endfile %}

### Objects that return transactions

Transaction objects are always accessed within a forloop that iterates for each transaction. You may use:

#### `transactions`

Returns all transactions. For example, from an invoice document layout:

```
{% for transaction in invoice.transactions %}
  {{ transaction.name }}
{% endfor %}
```

#### `payments`

Returns transactions with the type payment. For example, from an invoice document layout:

```
{% for transaction in invoice.payments %}
  {{ transaction.name }}
{% endfor %}
```

#### `refunds`

Returns transactions with the type refund. For example, from an invoice document layout:

```
{% for transaction in invoice.refunds %}
  {{ transaction.name }}
{% endfor %}
```

### Document layouts

The `transaction` object can be accessed in document layouts created against the following modules:

#### Invoice

```
{% for transaction in invoice.transactions %}
  {{ transaction.name }}
{% endfor %}
```

#### Opportunity

Returns invoice taxes for invoices linked to a particular opportunity.

```
{% for invoice in order.invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

#### Member

Returns invoice transactions for invoices linked to a particular organization.

```
{% for invoice in member.invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice transactions for active invoices linked to a particular organization.

```
{% for invoice in member.live_invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

### Discussion templates

The `transaction` object can be accessed in discussion templates created against the following modules:

#### Invoice

```
{% for transaction in invoice.transactions %}
  {{ transaction.name }}
{% endfor %}
```

#### Opportunity

Returns invoice transactions for invoices linked to a particular opportunity

```
{% for invoice in opportunity.invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

#### Organization

Returns invoice transactions for invoices linked to a particular organization.

```
{% for invoice in organisation.invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

Returns invoice transactions for active invoices linked to a particular organization.

```
{% for invoice in organisation.live_invoices %}
  {% for transaction in invoice.transactions %}
    {{ transaction.name }}
  {% endfor %}
{% endfor %}
```

## `amount` 

Returns the transaction amount.

#### Input

```
{{ transaction.amount }}
```

#### Output

```
100.0
```

> **Note:**
> Use [the currency filter or a number filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change the way that the number is formatted.

## `id`

Returns the transaction ID. 

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ transaction.id }}
```

#### Output

```
1
```

## `payment_method_name`

Returns the transaction payment method name.

Payment methods are configured in System Setup > List of Values.

Nothing is returned for transactions posted to Xero.

#### Input

```
{{ transaction.payment_method_name }}
```

#### Output

```
Credit card
```

## `reference`

Returns the transaction reference.

#### Input

```
{{ transaction.reference }}
```

#### Output

```
Initial payment
```

## `transaction_at`

Returns the date and time of the transaction.

#### Input

```
{{ transaction.transaction_at }}
```

#### Output

```
2021-03-01 16:00 +0000
```

## `transaction_type`

Returns the transaction type code.

| Code | Transaction type |
| ---- | ---------------- |
| 4    | Payment          |
| 5    | Refund           |

#### Input

```
{{ transaction.transaction_type }}
```

#### Output

```
4
```

## `transaction_type_name`

Returns the transaction type name.

* Payment
* Refund

#### Input

```
{{ transaction.transaction_type_name }}
```

#### Output 

```
Payment
```

---
*Source: [Invoice transactions — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-transactions.md)*
