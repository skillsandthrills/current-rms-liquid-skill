# Date filter reference

Date conventions vary by country and region. We output dates in a format that's similar to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) to avoid confusion between regions.

For example, January 2nd 2021 at 2:30pm would look like this:

```
2021-01-02 15:30:00
```

The format we're using is:

```
YYYY-MM-DD HH:MM:SS
```

This isn't especially friendly for your customers or colleagues, so you'll probably want to change the way that dates are displayed using a date filter.

### Locale date

Use `localedate` and `localedatetime` to print the date or date and time as formatted for your region. Our default documents use the locale date filters.

#### Input

```
{{ order.ordered_at | localedatetime }}
```

#### Output

Assuming the date is January 2nd 2021 at 2:30pm, where your user profile language is set to “English (United States)”:

```
01-02-2021 3:30 PM
```

Where your user profile language is set to “English (United Kingdom)”:

```
02/01/2021 15:30
```

### Build your own date

If you prefer, you can build your own date format. Use the filter `date:` , followed by date blocks in quotation marks. 

#### Input

```
{{ order.ordered_at | date:"%a, %-d %b %Y" }}
```

#### Output

```
Sat, Jan 2 2021
```

All the available date blocks that you may use are listed below.

### `'now'`

To print the date and time at the moment a document is generated, use `'now'`. For example:

```
{{ 'now' | date:"%a, %-d %b %Y" }}
```

The date and time returned will be UTC, or Coordinated Universal Time. UTC is a standard time that computers use to store dates and times, avoiding confusion between timezones.

You may adjust the time that is output by adding an additional timezone filter. For example:

```
{{ 'now' | timezone:"US/Mountain" | date:"%a, %-d %b %Y" }}
```

You can see a full list of timezones by editing your user profile. Use the list in the timezone drop-down.

## Date

### Presets

| Parameter        | Description                                | Output     |
| ---------------- | ------------------------------------------ | ---------- |
| `localedate`     | Date as formatted for your region          |            |
| `localedatetime` | Date and time as formatted for your region |            |
| `%F`             | Date in ISO 8601 format (yyyy-mm-dd)       | 2021-01-02 |

### Week

| Parameter | Description                                                  | Output |
| --------- | ------------------------------------------------------------ | ------ |
| `%a`      | Abbreviated weekday name                                     | Sun    |
| `%A`      | Full weekday name                                            | Sunday |
| `%w`      | Day of the week, 0-6 with Sunday being 0                     | 0      |
| `%U`      | Number of the week in the current year, starting with Sunday | 16     |
| `%W`      | Number of the week in the current year, starting with Monday | 15     |

### Year

| Parameter | Description          | Output |
| --------- | -------------------- | ------ |
| `%y`      | Year without century | 21     |
| `%Y`      | Year with century    | 2021   |

### Month

| Parameter | Description            | Output  |
| --------- | ---------------------- | ------- |
| `%b`      | Abbreviated month name | Jan     |
| `%B`      | Full month name        | January |

### Day

| Parameter | Description                           | Output |
| --------- | ------------------------------------- | ------ |
| `%d`      | Day of month, zero padded             | 01     |
| `%-d`     | Day of month, not zero padded         | 1      |
| `%e`      | Day of month, blank padded            | 1      |
| `%j`      | Number of the day in the current year | 21     |

## Time

### Presets

| Parameter | Description                  | Output      |
| --------- | ---------------------------- | ----------- |
| `%R`      | 24 hour time (`%H:%M`)       | 23:30       |
| `%T`      | 24 hour time (`%H:%M:%S`)    | 23:30:00    |
| `%r`      | 12 hour time (`%I:%M:%S %p`) | 11:30:00 PM |

### Hours

| Parameter | Description                              | Output |
| --------- | ---------------------------------------- | ------ |
| `%H`      | 24 hour hour                             | 23     |
| `%I`      | 12 hour hour                             | 11     |
| `%w`      | Day of the week, 0-6 with Sunday being 0 | 0      |
| `%p`      | Meridian indicator (AM or PM)            | PM     |

### Minutes and seconds

| Parameter | Description          | Output |
| --------- | -------------------- | ------ |
| `%M`      | Minute of the hour   | 30     |
| `%I`      | Second of the minute | 20     |

---
*Source: [Date filter reference — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/date-filter.md)*
