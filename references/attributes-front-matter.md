# Attributes

When you edit a default document in Current RMS, you'll notice that there are text boxes and color pickers let you change the appearance of the document. These are called "Attributes".

Generally speaking, if you're adding data to a document that isn't pulled dynamically from Current RMS and you think it might change, it should be an attribute. For example:

* Bank details on an invoice.
* Disclaimers or closing text on a delivery note.
* Terms and conditions on a rental agreement.

You may also create checkboxes and color pickers to change the way that a layout looks.

## Attribute types

There are three types of attribute:

* Field (text box)
* Color (color picker)
* Flag (checkbox)

## Add attributes

We don't anticipate end users changing attributes. For this reason, you can't add or edit them from the web interface. They're stored at the top of an exported document layout.

To add attributes, export a layout from Current RMS and open it in a text editor. At the top, you'll see the front matter at the top between three dashes. 

Here's an example:

```yaml
---
name: 'Example Document'
module: Project
page_size: A4
orientation: Portrait
margin:
  top: 85
  left: 10
  bottom: 15
  right: 10
colors:
  headings: '#3eb9ed'
  heading_text: 'white'
  info_bars: '#e6e6e6'
  info_bars_text: '#666666'
  body_text: '#666666'
  document_title: '#999999'
  borders: '#d1d1d1'
fields:
  closing_text: ''
  signature_text: ''
layout_flags:
  include_items_table: 'true'
active: true
description: ''
---
```

Add attributes in the front matter. 

* `colors` are color pickers
* `fields` are text boxes
* `layout_flags` are checkboxes 

If a field type isn't present, you may add it in under the `margin` properties.

### Format attributes

When adding attributes:

* Prefix your attributes with two spaces (not a tab character)
* Add a colon at the end, followed by a space
* Enter your value between two single quotation marks

Replace spaces in your attribute name with underscores and remove punctuation. Use lower case letters only.

For example, to create a field called "New Field Name": 

```
  new_field_name: 'Content here'
```

Colors must only have [a hex color value](https://www.w3schools.com/colors/colors_picker.asp) or [an HTML color name](https://htmlcolorcodes.com/color-names/).

Flags must only have the value `true` or `false`. These should be wrapped between single quotation marks. 

## Work with attributes

### Fields

To access fields, use:

```
{{ attributes.fields.attribute_name }}
```

You may wrap fields in HTML and use [Liquid filters](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to change their display. For example:

```markup
<p>{{ attributes.fields.disclaimer_text | newline_to_br }}</p>
```

### Colors

To access colors, use:

```
{{ attributes.colors.attribute_name }}
```

You'll probably want to use colors in your CSS. For example:

```css
p {
  color: {{ attributes.colors.body_text }};
}
```

### Flags

To access flags, use:

```
{{ attributes.flags.attribute_name }}
```

Printing a flag will return either `true` or `false`. You'll probably want to use them with Liquid tags to perform logic operations. For example:

```markup
{% if attributes.flags.include_description == true %}
  <p>{{ order.external_description | newline_to_br }}</p>
{% endif %}
```

> **Warning:**
> Flags are defined in the front matter using `layout_flag`, but accessed in document layouts using `flag`.

---
*Source: [Attributes — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/attributes.md)*
