# Liquid objects

Objects let you output content from your system onto your document layouts or discussion templates. They're also sometimes called “output” or “output markup”.

For example, the `order` object has an object called `name` that outputs the opportunity name.

#### Input

```
{{ order.name }}
```

#### Output

```
V-Blast Music Festival
```

## Which objects can I use?

All the objects that you can use are documented on this site. Use the list of the left to get started

## Where can I access objects?

Some objects can only be accessed in particular document layouts or discussion templates. Generally speaking, records must be related in order to access an object. For example:

* You can access the `invoice.items` object from an invoice document because items are against the invoice record.
* You can access the `invoice.items` object from an opportunity document where an opportunity has linked invoices. The opportunity is related to the invoices, and invoice items are against the invoices.
* You can't access the `invoice.items` from a quarantine document. There's no relation between a quarantine record and an invoice.

There's information and examples at the top of each of the object guides to let you know where and how you can access an object.

---
*Source: [Liquid objects — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-objects.md)*
