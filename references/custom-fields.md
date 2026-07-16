# Custom fields

[Custom fields](http://help.current-rms.com/set-up-your-system/your-settings/store-additional-data-by-creating-custom-fields) let you add things like text boxes, tick boxes, drop-down lists, date pickers, and other fields to any screen in your Current RMS system so you can store additional information.

If you like, you can pull through custom fields to document layouts and discussion templates. They behave like Liquid objects.

## Example use cases

#### **Product translations**

Do you operate in multiple languages? Create custom fields against your products to store an alternative name or description and pull those through to opportunity documents.

#### **Additional product information**

Create fields for product website, dimensions, or other data and display this on your opportunity documents.

**Risk assessments**

Make tickbox custom fields against an opportunity and pull through the values of those for a handy risk assessment checklist that can be shown on opportunity documents.

#### **Hiding information**

Liquid can be used to manipulate data that’s displayed on your documents, great for selectively hiding information. For example, you might have a boolean against an opportunity item or product that determines whether it's visible on a printed document. 

## Create custom fields

If you’ve not already, [create your custom fields](http://help.current-rms.com/set-up-your-system/your-settings/store-additional-data-by-creating-custom-fields) in System Setup > Custom Fields. 

## Document layout field name

To add custom fields to documents layouts, use the Document Layout Field Name in System Setup > Custom Fields.

This is generally the name of the custom field with underscores replacing spaces. For example, “Test Date” becomes `test_date` . 

The field name is your Liquid object. The way that you access the custom field depends on both the module where you created the field, as well as the document you wish to access it in. Check the guide that relates to the module that you created the custom field against for information on how to access it.

### **Examples**

* To access a product custom field in the opportunity items loop\
  `{{ item.product.custom_field_name }}` 
* To access an organization custom field on an opportunity or invoice document\
  `{{ customer.custom_field_name }}` 
* To access opportunity custom fields on an opportunity document\
  `{{ order.custom_field_name }}` 

## Data types

Most types of custom field return data in a way that you'd expect. For example, a text custom field returns a string. There are a couple of exceptions.

### Boolean

You might expect booleans to return `true` or `false`. However, they return a string with the values:

* `Yes`
* `No`
* blank

When you create a boolean against a module, existing records in that module have their type set as blank because they haven't explicitly been set as `true` or `false`. When you update records, they're set as `true` or `false`.

To use a boolean in your documents in liquid tags, check to see if a string is “Yes” or “No”. For example:

```markup
{% if customer.rented_before == "No" %}
  <p>Welcome to the family!</p>
{% elsif customer.rented_before == "Yes" %}
  <p>It’s good to see you again!</p>
{% endif %}
```

Remember to cater for blank values where necessary.

### Multi list of values

Custom fields with the type multi list of values (i.e. a list of tick boxes) store data as a string containing all of the list items.

To check whether a value is present, use the `contains` operator. For example:

```markup
{% if order.opportunity_notes contains "Fire Safety Kit Needed" %}
  <p>You’ve asked us not to supply a fire safety kit, so remember to bring your own.</p>
{% endif %}
```

There's no operator for “does not contain”, but you may use an unless statement to check to see if a condition isn't met.

```markup
{% unless order.opportunity_notes contains "Fire Safety Kit Needed" %}
  <p>You don't need a fire safety kit for this job.</p>
{% endunless %}
```

---
*Source: [Custom fields — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/custom-fields.md)*
