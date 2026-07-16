# Liquid tags

Tags are really powerful and are used extensively in document layouts in Current RMS. They’re a way of performing logic operations and controlling flow in document layouts.

> **Warning:**
> Liquid syntax is used in other web apps, so resources online might make reference to tags that aren't supported in Current.

## `comment`

Any content that you put between `{% comment %}` and `{% endcomment %}` tags is turned into a comment.

```
{% comment %} 
  The object below outputs our company name 
{% endcomment %}

<h1>{{ company.name }}</h1>
```

## `if`/`else`/`elsif`

Use an `if` tag to determine whether content should be shown if a certain condition is true. 

For example, you can check to see if a customer’s telephone number is blank and display a different message by adding a `{% else %}`  depending on whether or not this is true.

```
{% if customer.telephone == blank %}
  We do not have a telephone number on record for you.
{% else %}
  {{ customer.telephone }}
{% endif %}
```

Use `elsif` to add more conditions. For example:

```
{% if order.status == 0 %}
  This is open.
{% elsif order.status == 1 %}
  This is provisional.
{% elsif order.status == 5 %}
  This is reserved.
{% endif %}
```

## `unless`

An `unless`  tag is the opposite of an `if` tag. It tells Current RMS to only show content if the condition isn’t met.

```
{% unless order.discount_total == 0 %}
  We’re happy to offer you a discount for being a loyal customer.
{% endunless %}
```

## `for`

`for` loops run through items in a collection (array), e.g. opportunity items or contacts against an organisation.

In the example below, a list item is created for each item within the `order.items`  loop – this is the list of items on an opportunity:

```
<ul>
  {% for item in order.items %}
    <li>{{ item.name }}</li>
  {% endfor %}
</ul>
```

This might output something like:

* ETC Source 4
* Martin Mac Entour
* Pioneer XDJ
* Apple MacBook Pro

## `cycle`

The cycle tag is used within a `for` loop. It’s a way of looping through a group of strings and outputting them in the order they were listed. 

For example, we could run through `order.items`  as above but have every other list item as italicized or bold:

```
<ul>
  {% for item in order.items %}
    <li>
      {% cycle '<em>', '<strong>' %}
        {{ item.name }}
      {% cycle '</em>', '</strong>' %}
    </li>
  {% endfor %}
</ul>
```

This might output something like:

* *ETC Source 4*
* **Martin Mac Entour**
* *Pioneer XDJ*
* **Apple MacBook Pro**

## `assign` 

Use `assign` to create a variable. Variables are used to store information that you can reference and manipulate later.

For example:

```
{% assign product_number = 0 %}
```

Use quotation marks to save as a string:

```
{% assign tagline = "Powering you rental business" %}
```

## `capture`

Use `capture` to capture something between the opening and closing tags and assign to a variable.  Variables that you create are stored as strings.

```
{% capture hello_message %}
  Hello {{ customer.name }}, thank you for ordering from {{ company.name }}!
{% endcapture %}

{{ hello_message }}
```

`{{ hello_message }}`  will then output something like:

```
Hello Jo & Sam, thank you for ordering from Happily Ever After Events!
```

## `case`

Creates a switch statement to compare a variable with different values. `case`initializes the switch statement, and `when` compares its values.

```
{% case order.status %}
  {% when 1 %}
    The opportunity is open.
  {% when 5 %}
    The opportunity is active.
  {% when 20 %}
    This is a reserved opportunity.
  {% when 40 %}
     The opportunity is active.
  {% when 50 or 60 or 70 %}
    The opportunity is inactive i.e. canceled, lost, or dead.
  {% else %}
    Place your default code here.
{% endcase %}
```

---
*Source: [Liquid tags — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-tags.md)*
