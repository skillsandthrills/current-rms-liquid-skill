# Opportunity item surcharges

[Surcharges](https://help.current-rms.com/en/articles/660477-use-surcharges-to-apply-surcharges-to-products) are a way of adding a percentage or fixed fee to rental products. You can set them up in System Setup. 

A surcharge belongs to a surcharge group. A surcharge group typically has multiple surcharges, e.g. a "Cleaning" group might have "Glassware cleaning" and "Cutlery cleaning" surcharges. You can set one surcharge per surcharge group against a product or opportunity item.

On opportunities, surcharges are included in an opportunity item's charge total. You can hover over an opportunity item to see how a charge total is calculated and see the surcharge charge included.

Use Liquid to work with surcharges on an opportunity, for example:

* calculating the total for a surcharge or surcharge group
* deducting surcharges from opportunity items

On invoices generated from an opportunity, a line is created for each surcharge group.

Surcharge objects are always accessed within a forloop that iterates for each surcharge. 

### Document layouts

The `surcharge` object can be accessed in document layouts created against the following modules:

#### Opportunity

Returns opportunity item objects for opportunity items on an opportunity

```
{% for item in order.items %}
  {% if item.is_item? %}
    {% for surcharge in item.surcharges %}
      {{ surcharge.name }}
    {% endfor %} 
  {% endif %}
{% endfor %}
```

You may also use `order.products`:

```
{% for item in order.products %}
  {% if item.is_item? %}
    {% for surcharge in item.surcharges %}
      {{ surcharge.name }}
    {% endfor %} 
  {% endif %}
{% endfor %}
```

#### Member

Returns opportunity item objects for opportunity items on any opportunities linked to an organization.

```
{% for order in member.opportunities %}
  {% for item in order.items %}
    {% if item.is_item? %}
      {% for surcharge in item.surcharges %}
        {{ surcharge.name }}
      {% endfor %} 
    {% endif %}
  {% endfor %}
{% endfor %}
```

Returns opportunity item objects for opportunity items on any live opportunities linked to an organization.

```
{% for order in member.live_opportunities %}
  {% for item in order.items %}
    {% if item.is_item? %}
      {% for surcharge in item.surcharges %}
        {{ surcharge.name }}
      {% endfor %} 
    {% endif %}
  {% endfor %}
{% endfor %}
```

### Discussion templates

The `surcharge` object can be accessed in discussion templates created against the following modules:

#### Opportunity

Returns opportunity item objects for opportunity items on an opportunity.

```
{% for item in opportunity.items %}
  {% if item.is_item? %}
    {% for surcharge in item.surcharges %}
      {{ surcharge.name }}
    {% endfor %} 
  {% endif %}
{% endfor %}
```

You may also use `order.products`:

```
{% for item in opportunity.products %}
  {% if item.is_item? %}
    {% for surcharge in item.surcharges %}
      {{ surcharge.name }}
    {% endfor %} 
  {% endif %}
{% endfor %}
```

#### Organization

Returns opportunity item objects for opportunity items on any opportunities linked to an organization.

```
{% for order in organisation.opportunities %}
  {% for item in order.items %}
    {% if item.is_item? %}
      {% for surcharge in item.surcharges %}
        {{ surcharge.name }}
      {% endfor %} 
    {% endif %}
  {% endfor %}
{% endfor %}
```

Returns opportunity item objects for opportunity items on any live opportunities linked to an organization.

```
{% for order in organisation.live_opportunities %}
  {% for item in order.items %}
    {% if item.is_item? %}
      {% for surcharge in item.surcharges %}
        {{ surcharge.name }}
      {% endfor %} 
    {% endif %}
  {% endfor %}
{% endfor %}
```

## `charge`

Returns an opportunity item surcharge charge total.

#### Input

```
{{ surcharge.charge }}
```

#### Output

```
1.5
```

## `group_name`

Returns an opportunity item surcharge group name.

#### Input

```
{{ surcharge.group_name }}
```

#### Output

```
Cleaning
```

## `name`

Returns an opportunity item surcharge name.

#### Input

```
{{ surcharge.name }}
```

#### Output

```
Lens cleaning fee
```

## `original_charge`

Returns an opportunity item surcharge charge total before deal pricing.

#### Input

```
{{ surcharge.charge }}
```

#### Output

```
1.5
```

---
*Source: [Opportunity item surcharges — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-surcharge.md)*
