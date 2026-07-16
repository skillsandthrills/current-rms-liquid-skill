# Store

[Stores](https://help.current-rms.com/set-up-your-system/static-data/set-up-multiple-locations-using-stores) in Current RMS are locations where you hold stock. Every system is created with a store called “Default”. If you operate out of multiple warehouses, branches, or depots then you may wish to create multiple stores.

Stores are configured in System Setup > Stores. Each store has its own address and contact information. Most of our default documents pull through store contact information.

### Document layouts

In document layouts, the `store` object always relates to another object. For example, `store.name` this will not output anything. Prefixing it with `order.` in an opportunity document will resolve this.

Keep in mind that the store objects that you’re accessing will always be related to the store set against the record. This might not always be the same as the active store, set at the top-right.

The `store` object can be accessed in document layouts created against the following modules:

| Module         | Example                       |
| -------------- | ----------------------------- |
| Invoice        | `{{ invoice.store.name }}`    |
| Opportunity    | `{{ order.store.name }}`      |
| Project        | `{{ project.store.name }}`    |
| Quarantine     | `{{ quarantine.store.name }}` |
| Purchase order | `{{ order.store.name }}`      |

### Discussion templates

In discussion templates, use `current_store` to access information about the active store, set at the top-right. This works for discussion templates created against all modules.

To access store objects for the store set against a record, for example an opportunity‘s store, the process is similar to that of document layouts.

The `store` object can be accessed in discussion templates created against the following modules:

| Module         | Example                           |
| -------------- | --------------------------------- |
| Invoice        | `{{ invoice.store.name }}`        |
| Opportunity    | `{{ opportunity.store.name }}`    |
| Project        | `{{ project.store.name }}`        |
| Quarantine     | `{{ quarantine.store.name }}`     |
| Purchase order | `{{ purchase_order.store.name }}` |

## `address_detail` 

Returns address objects for the store address.

#### Input

```
{{ order.store.address_detail.street }}
```

#### Output

```
15201 Maple Systems Road
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `emails` 

Returns email objects for email addresses listed against the store.

#### Input

```
{% for email in order.store.emails %}
  {{ email.address }}
{% endfor %}
```

#### Output

```
help@current-rms.com
```

See: [Emails](https://current-rms.gitbook.io/liquid-syntax/general/email.md)

## `icon_url` 

Returns a URL pointing at the store logo. The full size image is returned.

#### Input

```
{{ order.store.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/1090cdd0-11f9-0133-abf1-125cc0dc331b/icons/437/original/image.png
```

## `id` 

Returns the store ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ order.store.id }}
```

#### Output

```
1
```

## `links` 

Returns link objects for the links listed against the store.

#### Input

```
{% for link in order.store.links %}
  {{ link.address %}
{% endfor %}
```

#### Output

```
www.current-rms.com
```

See: [Links](https://current-rms.gitbook.io/liquid-syntax/general/links.md)

## `mobile` 

Returns the store cell phone number. The first telephone number with the type “cell” or “mobile” is returned.

#### Input

```
{{ order.store.mobile }}
```

#### Output

```
(756) 555 1939
```

## `name` 

Returns the store name.

#### Input

```
{{ order.store.name }}
```

#### Output

```
The Banana Stand
```

## `phones` 

Returns telephone objects for telephone numbers listed against the store.

#### Input

```
{% for telephone in order.store.phones %}
  {{ telephone.number }}
{% endfor %}
```

#### Output

```
(636) 555 0113
```

See: [Phones](https://current-rms.gitbook.io/liquid-syntax/general/telephone.md)

## `telephone` 

Returns the store telephone. The first telephone number with the type “work” is returned.

#### Input

```
{{ order.store.telephone }}
```

#### Output

```
(636) 555 0113
```

## `website`

Returns the store website. The first link with the type “website” is returned.

> **Note:**
> Links are stored without `http://` or `https://` so remember to include these when creating hyperlinks.

#### Input

```
{{ order.store.website }}
```

#### Output

```
www.current-rms.com
```

---
*Source: [Store — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/store.md)*
