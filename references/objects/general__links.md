# Links

You may add as many links as you like when creating a store.

Use the `links` object to return all links against the store.

```
{% for link in order.store.links %}
  {{ link.address }}
{% endfor %}
```

## `address`

Returns websites stored against a record.

#### Input

```
{% for links in order.store.links %}
  {{ link.address }}
{% endfor %}
```

#### Output

```
www.current-rms.com
```

## `type_id`

Returns the link type ID. 

> **Note:**
> The ID is an internal reference for a value entry. It's not exposed in our web interface.

| ID     | Link type |
| ------ | --------- |
| `5001` | Website   |
| `5002` | Facebook  |
| `5003` | Twitter   |
| `5004` | LinkedIn  |
| `5005` | IM        |

#### Input

```
{% for link in order.store.links %}
  {{ link.type_id }}
{% endfor %}
```

#### Output

```
5001
```

## `type_name`

Returns the link type name.

* Website
* Facebook
* Twitter
* LinkedIn
* IM

#### Input

```
{% for link in order.store.links %}
  {{ link.type_name }}
{% endfor %}
```

#### Output

```
Website
```

---
*Source: [Links — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/links.md)*
