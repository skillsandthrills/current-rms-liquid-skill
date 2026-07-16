# Liquid operators

If you've done any computer programming before, you'll be familiar with operators. In Liquid, operators let you make logical decisions and comparisons. 

For example, you might need to check if a particular number is bigger than another number, or check to see if something has been filled in.

> **Note:**
> Mathematical operations are performed using [Liquid filters](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md), rather than operators.

## Main operators

| Operator | Function                 |
| -------- | ------------------------ |
| `==`     | equals                   |
| `!=`     | does not equal           |
| `>`      | greater than             |
| `<`      | less than                |
| `>=`     | greater than or equal to |
| `<=`     | less than or equal to    |
| `or`     | logical or               |
| `and`    | logical and              |

For example, here we use less than to print a statement if an opportunity charge total is less than 100.

```markup
{% if order.charge_excluding_tax_total < 100 %}
  Spend some more money with us!
{% endif %}
```

## `contains`

Use `contains` to check for the presence of a substring in a string.

```
{% if customer.email contains "current-rms.com" %}
  You work for Current RMS, lucky you!
{% endif %}
```

It's especially useful for multi-select [custom fields](https://current-rms.gitbook.io/liquid-syntax/information/custom-fields.md), where selected list options are stored as a comma-separated string.

> **Note:**
> You can't use `contains` to check for an object in an array of objects. It only searches strings.

## Order of operations

In tags with more than one `and` or `or` operator, operators are checked in order from right to left. 

```markup
{% if true or false and false %}
  This evaluates to true, since the 'and' condition is checked first.
{% endif %}
```

```markup
{% if true and false and false or true %}
  This evaluates to false, since the tags are checked like this:

  true and (false and (false or true))
  true and (false and true)
  true and false
  false
{% endif %}
```

---
*Source: [Liquid operators — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/introduction/operators.md)*
