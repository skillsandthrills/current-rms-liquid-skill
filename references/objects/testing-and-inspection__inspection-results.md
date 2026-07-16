# Inspection results

[Testing & Inspection](https://help.current-rms.com/en/articles/3822294-how-does-testing-inspection-work-in-current-rms) in Current RMS lets you log inspection results against serialized assets. It's designed for tests like PAT, Test & Tag, LOLER, and other periodic inspections.

You can print documents against a logged inspection result against a stock level. Out of the box, we include an "Test & Inspection Result Sheet" document that prints key information about a test. 

You can also access inspection results against the stock level object. The most common use for this is for printing a list of inspection results for assets on an opportunity.

An asset can be set up for more than one test type, so use the name to filter if you just need to show a certain kind of test on a document.

### Inspection result tasks

When setting up your inspection results, you may create inspection tasks. These are other values that you might want to store during a test, e.g. weights or electrical results.

Inspection tasks are stored as an array against the inspection result.

See: [Inspection result tasks](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-result-tasks.md)

### Product and asset information

It's common to want to print product and asset information on an inspection result document. Use the stock level object to do this. For example:

#### Asset number

```
{{ inspection_result.stock_level.asset_number }}
```

#### Product name

```
{{ inspection_result.stock_level.product.name }}
```

### Example

Here’s an example document that prints inspection results for an opportunity.

{% file src="/files/-MOaQcNo0K77E9s5ckTR" %}
Testing & Inspection certificate
{% endfile %}

### Objects that return inspection results

Inspection results can be accessed within a forloop that iterates for each result. You may use:

#### `inspection_results`

Returns all inspection results for a stock level. For example, from an opportunity document layout:

```
{% for asset in order.product_assets %}
  {% for inspection_result in asset.stock_level.inspection_results %}
    {{ inspection_result.inspection_name }}
  {% endfor %}
{% endfor %}
```

#### `latest_inspection_results`

Returns the latest inspection results for .stock level , i.e. the most recent. For example, from an opportunity document layout:

```
{% for asset in order.product_assets %}
  {% for inspection_result in asset.stock_level.latest_inspection_results %}
    {{ inspection_result.inspection_name }}
  {% endfor %}
{% endfor %}
```

### Document layouts

The `inspection_result` object can be accessed in document layouts created against the following modules:

#### Inspection result&#x9;

```
{{ inspection_result.inspection_name }}
```

#### Opportunity

```
{% for asset in order.product_assets %}
  {% for inspection_result in asset.stock_level.latest_inspection_results %}
    {{ inspection_result.inspection_name }}
  {% endfor %}
{% endfor %}  
```

#### Product

```
{% for asset in product.assets %}
  {% for inspection_result in asset.latest_inspection_results %}
    {{ inspection_result.inspection_name }}    
  {% endfor %}
{% endfor %}
```

#### Quarantine

```
{% for inspection_result in quarantine.stock_level.latest_inspection_results %}
  {{ inspection_result.inspection_name }}
{% endfor %}
```

### Discussion templates

The `inspection_result` object can be accessed in discussion templates created against the following modules:

#### Opportunity

```
{% for asset in opportunity.product_assets %}
  {% for inspection_result in asset.stock_level.latest_inspection_results %}
    {{ inspection_result.inspection_name }}
  {% endfor %}
{% endfor %}  
```

#### Product

```
{% for asset in product.assets %}
  {% for inspection_result in asset.latest_inspection_results %}
    {{ inspection_result.inspection_name }}    
  {% endfor %}
{% endfor %}
```

#### Quarantine

```
{% for inspection_result in quarantine.stock_level.latest_inspection_results %}
  {{ inspection_result.inspection_name }}
{% endfor %}
```

## `description`

Returns the inspection result description.

#### Input

```
{{ inspection_result.description }}
```

#### Output

```
Had problems with tester for this one.
```

## `inspection_at`

Returns the date of the inspection result.

#### Input

```
{{ inspection_result.inspection_at }}
```

#### Output

```
2021-04-24 14:00:00 +0100
```

## `passed`

Returns `true` if the inspection result is passed; `false` otherwise.

#### Input

```
{{ inspection_result.passed }}
```

#### Output

```
true
```

## `passed_to_word`

Returns `Yes` in the user's locale language if the inspection result is passed; `No` otherwise.

#### Input

```
{{ inspection_result.passed_to_word }}
```

#### Output

```
Yes
```

> **Note:**
> You may also use [the bool\_to\_word filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) on a boolean to convert true or false into "Yes" or "No" in the user's locale language.

## `stock_level`

Returns stock level objects for an inspection result's related stock level.

Usually used to print the asset number or access the product object.

#### Input

```
{{ inspection_result.stock_level.asset_number }}
```

#### Output

```
AA-1234
```

See: [Stock level](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md)

## `task_list_results`

Returns inspection result task objects for any tasks against this inspection result.

#### Input

```
{% for result in inspection_result.task_list_results %}
  {{ result.
{% endfor %}
```

#### Output

```
200
```

See: [Inspection result tasks](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-result-tasks.md)

---
*Source: [Inspection results — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-results.md)*
