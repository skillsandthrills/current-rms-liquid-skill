# Liquid filters

Filters let you change the way that a Liquid object is displayed. In Current, you'll find the `currency`, `number`, and `localedate` filters used a lot in our document layouts. 

Filters are placed within an object after a pipe character( `|` ), with optional data supplied after a colon.

## Common filters

### **`localedate`**

Formats a date as per the logged in user’s language settings. 

#### Input

```
{{ invoice.invoiced_at | localedate }}
```

#### Output

In “English (United States),” this might output `1/12/2021` (M/D/YYY) but in other languages this might output `12/01/2021`  (DD/MM/YYYY).

### **`localedatetime`**

Formats the date and time as per the logged in user’s language settings.

#### Input

```
{{ order.deliver_starts_at | localedatetime }}
```

#### Output

In “English (United States),” this might output `1/12/2021 5:30PM` (M/D/YYY 12hr clock) but in other languages this might output `12/01/2021 17:30`  (DD/MM/YYYY 24hr clock).

### **`timezone`**

When using `'now'` to return the date and time now, Current RMS returns the UTC time. Use `timezone`  to change the date and time to a particular region.

```
{{ 'now' | timezone:"Europe/London" | localedatetime }}
```

For a list of timezones, edit your user profile and check the “Timezone” drop-down.

See: [Date filter reference](https://current-rms.gitbook.io/liquid-syntax/information/date-filter.md)

### **`number`**

A decimal precision formatter. You can specify how many decimal places you’d like to add.

#### Input

```
{{ item.quantity | number }}
{{ item.quantity | number:3 }}
```

#### Output

```
1
1.000
```

### **`currency`**

Formats a number using the currency symbol set in System Preferences and the user’s language settings.

#### Input

```
{{ item.price | currency }}
```

#### Output

```
$149.00
```

### **`newline_to_br`**

Where you’ve inserted a new line into a text field (`\n` ), this filter inserts an HTML break (`<br>` ).

#### Input

```
{{ order.external_description | newline_to_br }}
```

#### Output

```
Thanks for your interest.
Contact us if we can do anything.
```

### **`markdown`**

Tells Current to format text as [Markdown](http://daringfireball.net/projects/markdown/basics).

#### Input

```
{{ order.external_description | markdown }}
```

Where the external description is... 

```
**Thank you for your interest!** Contact us if we can do _anything_.
```

#### Output

**Thank you for your interest!** Contact us if we can do anything.

### `bool_to_word`

Converts true or false into “Yes” and “No” in your local language.

#### Input

```
{{ item.has_discount? | bool_to_word }}
```

#### Output

```
Yes
```

### `to_words`

Outputs numbers to words, useful for regions where invoices must show the amount due in words.

#### Input

```
{{ invoice.charge_including_tax_total | to_words }} 
```

#### Output

```
One hundred and ninety nine
```

## String filters

### **`append`**

Add information to the end of a string:

#### Input

```
{{ order.name | append:"!" }}
```

#### Output

```
V-Blast Music Festival!
```

### **`capitalize`**

Makes the first letter of a string capitalized.

#### Input

```
{{ order.name | capitalize }}
```

#### Output

```
V-blast music festival
```

### **`downcase`**

Change the output to lowercase.

#### Input

```
{{ order.name | downcase }}
```

#### Output

```
v-blast music festival
```

### **`prepend`**

Add information to the start of a string:

#### Input

```
{{ order.name | prepend:"We are preparing your order: " }}
```

#### Output

```
We are preparing your order: V-Blast Music Festival
```

### **`remove`**

Removes every occurrence of a particular substring from a string.

#### Input

```
{{ order.name | remove:"Festival" }}
```

#### Output

```
V-Blast Music
```

### **`remove_first`**

Removes the first occurrence of a particular substring from a string.

#### Input

```
{{ order.name | remove_first:"Festival" }}
```

#### Output

```
V-Blast Music
```

### **`truncate`**

Truncate a string to a particular number of characters.

#### Input

```
{{ order.name | truncate:3 }}
```

#### Output

```
V-Bl
```

### `upcase`

Change the output to uppercase.

#### Input

```
{{ order.name | upcase }}
```

#### Output

```
V-BLAST MUSIC FESTIVAL
```

## Maths filters

### **`ceil`**

Rounds up to the nearest integer.

#### Input

```
{{ item.price | ceil }}
```

#### Output

If the item price is 1.60, this will be 2. 

If the item price is 1.30, this will still be 2.

### **`divided_by`**

Divides an output by a number. 

#### Input

```
{{ item.price | divided_by:2 }}
```

### **`floor`**

Rounds down to the nearest integer.

#### Input

```
{{ item.price | floor }}
```

#### Output

If the item price is 1.60, this will be 1. 

If the item price is 1.30, this will also be 1.

### **`minus`**

Subtracts a number from an output.

#### Input

```
{{ order.charge_including_tax_total | minus:order.tax_total }}
```

### **`modulo`**

Divides an output by a number and returns the remainder.

### **`plus`**

Adds a number to an output.

#### Input

```
{{ item.price | plus:10 }}
```

### **`round`**

Rounds the output to the nearest integer or specified number of decimals.

#### Input

```
{{ item.price | round }}
```

#### Output

If the item price is 1.60, this will be 2.

 If the item price is 1.30, this will be 1.

### **`times`**

Multiplies an output by a number.

#### Input

```
{{ item.price | times:2 }}
```

## Array filters

### **`first`**

Returns the first item in an array.

#### Input 

```
{{ item.accessories | first }}
```

### **`last`**

Returns the last item in an array.

#### Input

```
{{ item.accessories | last }}
```

### **`sort`**

Sorts an array by a given attribute.

#### Input

```
{% assign sorted_quotations = project.quotations | sort:'name' %}
```

---
*Source: [Liquid filters — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md)*
