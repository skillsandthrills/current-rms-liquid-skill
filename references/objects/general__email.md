# Emails

You may add as many email addresses as you like when creating organization, contacts, users, vehicles, or venues.

Using the `email` object against the organization, contact, user, vehicle, or venue object will return the first work email address associated with the record. For example, from an opportunity document:

```
{{ customer.email }}
```

Use the `emails` object to return all email addresses.

```
{% for email in customer.emails %}
  {{ email.address }}
{% endfor %}
```

See: [People & Organizations](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)

## `address`

Returns email addresses stored against a record.

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

## `type_id`

Returns the email address type ID. 

> **Note:**
> The ID is an internal reference for a value entry. It's not exposed in our web interface.

| ID     | Email type |
| ------ | ---------- |
| `4001` | Work       |
| `4002` | Home       |

#### Input

```
{% for email in order.store.emails %}
  {{ email.type_id }}
{% endfor %}
```

#### Output

```
4001
```

## `type_name`

Returns the email address type name.

* Home
* Work

#### Input

```
{% for email in order.store.emails %}
  {{ email.type_name }}
{% endfor %}
```

#### Output

```
Work
```

---
*Source: [Emails — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/email.md)*
