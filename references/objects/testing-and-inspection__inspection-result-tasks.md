# Inspection result tasks

When creating inspection results, you may set up inspection result tasks. These are other values that you might want to store during a test, e.g. weights or electrical results.

Inspection result tasks are stored in an array against an inspection result.

See: [Inspection results](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-results.md)

## `name`

Returns the name of the inspection task.

#### Input

```
{% for result in inspection_result.task_list_results %}
  {{ result.name }}
{% endfor %}
```

#### Output

```
Meter reading
```

## `value`

Returns the recorded value for the inspection task.

#### Input

```
{% for result in inspection_result.task_list_results %}
  {{ result.value }}
{% endfor %}
```

#### Output

```
200
```

---
*Source: [Inspection result tasks — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-result-tasks.md)*
