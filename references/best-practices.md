# Best practices

Wondering how our team of document specialists work at Current RMS? We share some of our best practices.

## Editor

The document layout and discussion template editors in Current RMS will highlight Liquid syntax, HTML, and CSS as you type.

Use the blue preview buttons to preview your work. Remember to update your document regularly to avoid losing work.

### Atom

If you're creating a document from scratch or working on something more complex, we recommend using [Atom](https://atom.io/).

With Atom, you can:

* Split panes to display your HTML and stylesheet side by side.
* Use [the `language-liquid` package](https://atom.io/packages/language-liquid) to enable Liquid syntax highlighting.
* Use [the `space-tab` package](https://atom.io/packages/space-tab) to convert tabs to two-space indentation.
* Save work to your local machine.

You won't be able to preview on your local machine. Copy and paste code from Atom into the editor in Current to preview.

## Indentation

Indentation is a way of conveying structure and hierarchy. It's not strictly necessary in HTML or Liquid, but proper indentation makes a document or discussion template much easier to read and understand. It's especially helpful when working on complex code and when troubleshooting.

Here’s an example of good indentation:

```markup
<ul>
  {% for item in order.items %}
    {% if item.is_item? %}
      <li>{{ item.name }}</li>
    {% endif %}
  {% endfor %}
</ul>
```

We recommend using two spaces for indentation. You can use `cmd + [` and `cmd + ]` to increase or decrease indentation in the document layout editor in Current RMS. 

> **Important:**
> The `tab` key  insert a tab character rather than two spaces.

## Commenting

Leaving comments may seem like extra effort, but makes it much easier to understand what's going on in a document or discussion template when you come to revisit it months (or years!) down the line. 

We recommend popping in a comment for each key section of a document and leaving comments to explain any complicated Liquid operations.

`<!-- HTML comments -->` are output in the code of the document when generated, so they can be viewed when you inspect element or view source. 

`{% comment %} Liquid comments {% endcomment %}` are not. 

## Proper planning

Create as little work for yourself in future by planning properly and not trying not to take shortcuts.

* Use `if` statements to hide fields if they're blank. For example, don't show a discount column or total if there's no discount on the opportunity. 
* Add [attributes](https://current-rms.gitbook.io/liquid-syntax/information/attributes.md) to documents for data that might change.
* Be wary when hard-coding arithmetic operations into documents. Never do this for tax rates. 

## Troubleshooting

Use [the developer tools in your browser](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) to troubleshoot HTML or CSS that doesn't look quite right.

Liquid syntax is sometimes tricker to troubleshoot because errors won't show up in your browser's developer tools.

Where there's a breaking problem, Current RMS will tell you. For example:

```
Failed to preview the document due to the error:
Liquid syntax error: 'if' tag was never closed
```

Proper indentation will help you spot where you've left tags open.

If a logic operation isn't working as expected, print objects to make sure that they're outputting what you expect. For example:

```markup
{% if order.custom_field_name == "yes" %}
  <p>My custom field is ticked.</p>
{% endif %}
```

If you expect the if statement above to return true and that content to print and it's not, outputting the value of `order.custom_field_name` will help troubleshoot. For example

```
{{ order.custom_field_name }}
```

If a boolean custom field, this will return `Yes` (rather than a lowercase `yes`) We can see that our condition above wasn't met, so our Liquid wasn't output.

---
*Source: [Best practices — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/introduction/best-practices.md)*
