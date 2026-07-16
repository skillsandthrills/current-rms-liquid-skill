# Phones

You may add as many telephone number as you like when creating organization, contacts, users, vehicles, or venues.

Using the `telephone` object against the organization, contact, user, vehicle, or venue object will return the first work telephone number associated with the record. For example, from an opportunity document:

```
{{ customer.telephone }}
```

Use the `phones` object to return all email addresses.

```
{% for phone in customer.phones %}
  {{ phone.number }}
{% endfor %}
```

## `number`

Returns telephone numbers stored against a record.

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

## `type_id`

Returns the telephone type ID. 

> **Note:**
> The ID is an internal reference for a value entry. It's not exposed in our web interface.

| ID     |       |
| ------ | ----- |
| `6001` | Work  |
| `6002` | Cell  |
| `6003` | Fax   |
| `6004` | Skype |
| `6005` | Home  |

#### Input

```
{% for telephone in order.store.phones %}
  {{ telephone.type_id }}
{% endfor %}
```

#### Output

```
6001
```

## `type_name`

Returns the telephone type name.

* Work
* Cell
* Fax
* Skype
* Home

#### Input

```
{% for telephone in order.store.phones %}
  {{ telephone.type_name }}
{% endfor %}
```

#### Output

```
Work
```

---
*Source: [Phones — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/telephone.md)*
