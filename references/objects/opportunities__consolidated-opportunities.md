# Consolidated opportunities

When working with a project, the consolidated opportunities object merges opportunities in a project with the same date and end date, then lets you access a list of consolidated opportunity items for those dates. 

It's only available from the project object.

See: [Project](https://current-rms.gitbook.io/liquid-syntax/project/project.md)

```markup
{% for order in project.consolidated_opportunities %}
  <h1>{{ order.starts_at | localedate }} - {{ order.ends_at | localedate }}</h1>
  <table class="table table-condensed">
    <thead>
      <tr>
        <th class="align-right" style="width: 75px;">Qty</th>
        <th>Item</th>
      </tr>
    </thead>
    <tbody>
      {% for item in order.consolidated_items %}
        <tr>
          <td class="align-right">{{ item.quantity | number }}</td>
          <td style="padding-left: 16px">{{ item.name }}</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endfor %}
```

## `consolidated_items` 

Returns consolidated opportunity item objects on the project during this period.

See: [Consolidated opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md)

## `ends_at`

Returns the end date for the list of consolidated opportunity items. 

#### Input

```markup
{{ order.starts_at }}
```

#### Output

```markup
2021-04-12 16:00:00 +0000 
```

## `starts_at`

Returns the start date for the list of consolidated opportunity items. 

#### Input

```markup
{{ order.ends_at }}
```

#### Output

```markup
2021-04-11 16:00:00 +0000 
```

---
*Source: [Consolidated opportunities — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunities.md)*
