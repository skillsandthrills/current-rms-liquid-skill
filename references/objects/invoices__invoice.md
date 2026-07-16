# Invoice

Invoice records in Current include both invoices and credits. Use the `type` object to determine whether you’re working with an invoice or credit.

Invoices and credit notes can be created manually, from an opportunity, or from a project. The link between an invoice and its sources is created on each invoice item. 

### Document layouts

The `invoice` object can be accessed in document layouts created against the following modules:

#### Invoice

```
{{ invoice.name }}
```

#### Opportunity

Returns invoices linked to a particular opportunity.

```
{% for invoice in order.invoices %}
  {{ invoice.name }}
{% endfor %}
```

#### Member

Returns invoices linked to a particular organization.

```
{% for invoice in member.invoices %}
  {{ invoice.name }}
{% endfor %}
```

Returns active invoices linked to a particular organization.

```
{% for invoice in member.live_invoices %}
  {{ invoice.name }}
{% endfor %}
```

### Discussion templates

The `invoice` object can be accessed in discussion templates created against the following modules:

#### Invoice

```
{{ invoice.name }}
```

#### Opportunity

Returns invoices linked to a particular opportunity.

```
{% for invoice in opportunity.invoices %}
  {{ invoice.name }}
{% endfor %}
```

#### Organization

Returns invoices linked to a particular organization.

```
{% for invoice in organisation.invoices %}
  {{ invoice.name }}
{% endfor %}
```

Returns active invoices linked to a particular organization.

```
{% for invoice in organisation.live_invoices %}
  {{ invoice.name }}
{% endfor %}
```

## `balance`

Returns the invoice balance, i.e. the invoice charge total including tax after any payments or refunds.

> **Important:**
> Payments logged in Xero, QuickBooks Online, or Sage are not included. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

#### Input

```
{{ invoice.balance }}
```

#### Output

```
100.0
```

## `billing_address`

Returns the invoice billing address.

#### Input

```
{{ invoice.billing_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `billing_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the billing address against the invoice.

#### Input 

```
{{ invoice.billing_address_detail.state }}
```

#### Ouput 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `billing_address_name`

Returns the name of the billing address against the invoice.

#### Input

```
{{ invoice.delivery_address_name }}
```

#### Output

```
Omni Consumer Products
```

## `charge_excluding_tax_total`

Returns the invoice charge total excluding tax.

#### Input

```
{{ invoice.charge_excluding_tax_total }}
```

#### Output

```
450.0
```

## `charge_including_tax_total`

Returns the invoice charge total including tax.

#### Input

```
{{ invoice.charge_including_tax_total }}
```

#### Output

```
550.0
```

## `charge_total`

Returns the invoice charge total. 

This may be including or excluding tax depending on the value of the “Catalog Prices” setting in System Preferences.

#### Input

```
{{ invoice.charge_total }}
```

#### Output

```
450.0
```

## `combined_discount_total`

Returns the total discount from deal pricing and percentage discounting on the invoice.

#### Input

```
{{ invoice.combined_discount_total }}
```

#### Output

```
100.0
```

## `deal_discount_total`

Returns the total discount from deal pricing on the invoice.

#### Input 

```
{{ invoice.deal_discount_total }}
```

#### Output

```
50.0
```

## `delivery_address`

Returns the invoice delivery address.

#### Input

```
{{ invoice.delivery_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `delivery_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the delivery address against the invoice.

#### Input 

```
{{ invoice.delivery_address_detail.state }}
```

#### Ouput 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `delivery_address_name`

Returns the name of the delivery address against the invoice.

You may also use the [venue object (below)](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md#venue).

#### Input

```
{{ invoice.delivery_address_name }}
```

#### Output

```
Seaview Convention Center
```

## `description`

Returns the invoice (internal) description.

#### Input

```
{{ invoice.description }}
```

#### Output

```
This client is FUSSY, so let's make sure everything goes right.
```

## `discount_total`

Returns the total discount from percentage discounting on the invoice.

#### Input

```
{{ invoice.discount_total }}
```

#### Output

```
50.0
```

## `due_at`

Returns the date and time that the invoice is due at.

#### Input

```
{{ invoice.due_at }}
```

#### Output 

```
2021-04-12 16:00:00 +0000 
```

## `external_description`

Returns the invoice external description.&#x9;

#### Input

```
{{ invoice.external_description }}
```

#### Output

```
Every event is special, so we're here to make sure that it all runs smoothly.
```

## `has_discount?`

Returns `true` if the invoice has percentage based discounts; `false` otherwise.

#### Input

```
{{ invoice.has_discount? %}
```

#### Output

```
false
```

## `id`

Returns the invoice ID.

> **Warning:**
> The ID is an internal reference for a record. It's not exposed in our web interface and shouldn't be confused with the [invoice number (below)](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md#number).

#### Input

```
{{ invoice.id }}
```

#### Output

```
1
```

## `invoiced_at`

Returns the date entered in the invoice “Document Date” field.

#### Input

```
{{ invoice.invoiced_at }} 
```

#### Output

```
2021-03-11 14:00:00 +0000
```

## `is_paid?`

Returns `true` if the invoice has the status “Paid”; `false` otherwise.

> **Important:**
> Invoices posted to Xero, QuickBooks Online, or Sage have the status “Posted”. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

#### Input

```
{{ invoice.is_paid? }}
```

#### Output

```
false
```

## `is_posted?`

Returns `true` if the invoice has the status “Posted”; `false` otherwise.

An integration with Xero or QuickBooks Online is required for an invoice to be posted.

#### Input

```
{{ invoice.is_posted? }}
```

#### Output

```
false
```

## `items`

Returns [invoice item objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md) for items on the invoice.

#### Input

```
{% for item in invoice.items %}
  {{ item.name }}
{% endfor %}
```

#### Output

```
ETC Source Four
D&B E15X Subwoofer
QTX VHF Wireless Headset Microphone
```

See: [Invoice items](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-item.md)

## `name`

Returns the invoice subject.

#### Input

```
{{ invoice.name }}
```

#### Output

```
V-Blast Music Festival
```

## `number`

Returns the invoice number.

[Issue an invoice](https://help.current-rms.com/invoices-and-credits/work-with-an-invoice/issue-an-invoice-or-credit-to-make-it-legal) to give it a number.

#### Input

```
{{ invoice.number }}
```

#### Output

```
PO-001
```

## `payment_total`

Returns the total of any payments logged against the invoice.

> **Important:**
> Payments logged in Xero, QuickBooks Online, or Sage are not included. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

#### Input

```
{{ invoice.payment_total }}
```

#### Output

```
100.0
```

## `payments`

Returns [invoice transaction objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-transactions.md) for payments logged against the invoice.

#### Input

```
{% for payment in invoice.payments %}
  {{ payment.reference }}
{% endfor %}
```

#### Output

```
Initial payment
```

## `reference`

Returns the value of the invoice customer reference.

#### Input

```
{{ invoice.reference }}
```

#### Output

```
PO-1099
```

## `refunds`

Returns [invoice transaction objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-transactions.md) for refunds logged against the invoice.

#### Input

```
{% for refund in invoice.refunds %}
  {{ refund.reference }}
{% endfor %}
```

#### Output

```
Overpayment
```

## `sources`

Returns [opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md) or [project](https://current-rms.gitbook.io/liquid-syntax/project/project.md) objects for the invoice sources.

Sources are set against invoice items rather than the invoice itself. 

* When an invoice is raised from an opportunity, it will generally have one source: the originating opportunity.
* When an invoice is raised from a project, it will have sources for each of the invoiced opportunities in the project.
* When a part invoice is created for a project, the project will be source.
* A manual invoice may have no sources.

#### Input <a href="#input-23" id="input-23"></a>

```
{% for source in invoice.sources %}
  {{ source.name }}
{% endfor %}
```

#### Output <a href="#output-22" id="output-22"></a>

```
Omni Consumer Products New Product Launch
```

## `status`

Returns the invoice status code.

> **Important:**
> Invoices posted to Xero, QuickBooks Online, or Sage have the status “Posted”. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

| Code | Status name |
| ---- | ----------- |
| `0`  | Open        |
| `10` | Issued      |
| `20` | Paid        |
| `30` | Posted      |
| `40` | Voided      |

#### Input

```
{{ invoice.status }}
```

#### Output

```
10
```

## `status_name`

Returns the invoice status name.

Status names are in the language set against your user profile. 

* Open
* Issued
* Paid
* Posted
* Voided

> **Important:**
> Invoices posted to Xero, QuickBooks Online, or Sage have the status “Posted”. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

#### Input

```
{{ invoice.status_name }}
```

#### Output

```
Issued
```

## `tax_class_name`

Returns the invoice tax class.

This may differ from the organization tax class.

#### Input

```
{{ invoice.tax_class_name }}
```

#### Output

```
Default
```

## `tax_total`

Returns the invoice tax total.

#### Input

```
{{ invoice.tax_total }}
```

#### Output

```
100.0
```

## `taxes`

Returns invoice tax objects for taxes on the invoice.

#### Input

```
{% for tax in invoice.taxes %}
  {{ tax.name }}
{% endfor %}
```

#### Output

```
FL State Sales Tax
```

## `transaction_total`

Returns the total of any transactions logged against the invoice.

This includes both payments and refunds.

> **Important:**
> Payments logged in Xero, QuickBooks Online, or Sage are not included. We can't access payment information from linked accounting solutions in document layouts or discussion templates.

#### Input

```
{{ invoice.payment_total }}
```

#### Output

```
100.0
```

## `transactions`

Returns [invoice transaction objects](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice-transactions.md) for transactions logged against the invoice.

This includes both payments and refunds.

#### Input

```
{% for transaction in invoice.transactions %}
  {{ transaction.reference }}
{% endfor %}
```

#### Output

```
Initial payment
```

## `type`

Returns the invoice type ID.

| ID  | Type name   |
| --- | ----------- |
| `0` | Invoice     |
| `1` | Credit note |

#### Input

```
{{ invoice.type }}
```

#### Output

```
0
```

## `type_name`

Returns the invoice type name. 

Type names are in the language set against your user profile. 

* Invoice
* Credit Note

#### Input

```
{{ invoice.type_name }}
```

#### Output

```
Invoice
```

## `venue`

Returns venue objects for the venue against the invoice.

> **Warning:**
> An invoice delivery address can be a venue, but a venue might not always be an invoice's delivery address. If you don't choose a venue when creating an invoice, using `{{ invoice.venue.name }}` won't return the same as `{{ invoice.delivery_address_name }}`.

#### Input

```
{{ invoice.venue.name }}
```

#### Output

```
Seaview Conference Center
```

---
*Source: [Invoice — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md)*
