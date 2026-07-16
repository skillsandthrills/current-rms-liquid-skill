# Company

Most company settings are configured in [System Preferences](https://help.current-rms.com/set-up-your-system/your-settings/change-a-variety-of-company-options-in-system-preferences) or System Setup > [Company Information](https://help.current-rms.com/set-up-your-system/your-account/add-your-logo-and-update-your-contact-information).

It might be tempting to hardcode details like your company name into your documents or discussion templates, but we always recommend using `company` objects. If you make a change to your company details in future, these changes will be reflected automatically.

Contact information like telephone numbers and email addresses are held against the [store object](https://current-rms.gitbook.io/liquid-syntax/general/store.md).

### Document layouts

The `company` object can be accessed in document layouts created against the following modules:

* Invoice
* Opportunity
* Project
* Product
* Quarantine
* Member
* Purchase order

### Discussion templates

The `company` object can be accessed discussion templates created against the following modules:

* None
* Organization
* Contact
* User account
* Venue
* Activity
* Invoice
* Opportunity
* Project
* Product
* Service
* Quarantine
* Purchase order

## `address`

Returns the company address.

#### Input

```
{{ company.address }}
```

#### Output

```
333 North Sam Houston Parkway East Houston TX 77060
```

## `address_detail`

Returns address objects for the company address.

#### Input

```
{{ company.address_detail.street }}
```

#### Output

```
15201 Maple Systems Road
```

## `company_registration_number`

Returns the company registration number. You might also call this an ABN.

#### Input

```
{{ company.company_registration_number }}
```

#### Output

```
10648973
```

## `distance_unit` 

Returns the distance unit set in System Preferences.

| Option     | Output  |
| ---------- | ------- |
| Miles      | `miles` |
| Kilometers | `km`    |

#### Input

```
{{ company.distance_unit }}
```

#### Output

```
miles
```

## `icon_url` 

Returns a URL pointing at the company logo. The full size image is returned.

#### Input

```
{{ company.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/1090cdd0-11f9-0133-abf1-125cc0dc331b/icons/437/original/image.png
```

## `name` 

Returns the company name.

#### Input

```
{{ company.name }}
```

#### Output

```
The Rental Factory
```

## `size_unit` 

Returns the size unit set in System Preferences.

| Option     | Output   |
| ---------- | -------- |
| Millimeter | `mm`     |
| Centimeter | `cm`     |
| Meters     | `metres` |
| Inches     | `inches` |
| Feet       | `feet`   |
| Yards      | `yards`  |

#### Input

```
{{ company.size_unit }}
```

#### Output

```
mm
```

## subdomain

Returns the company subdomain as set in System Setup > Company Information.

Your subdomain is used to access Current RMS. This will look something like `http://yourcompany.current-rms.com`, where `yourcompany` is your subdomain.

#### Input

```
{{ company.subdomain }}
```

#### Output

```
abcproductions
```

## `tax_registration_number`

Returns the company tax registration number. 

You might also call this a VAT number, GST number, or simply tax number.

#### Input

```
{{ company.tax_registration_number }}
```

#### Output

```
ABC-1234
```

## `weight_unit`

Returns the weight unit set in System Preferences.

| Option    | Output |
| --------- | ------ |
| Kilograms | `kgs`  |
| Pounds    | `lbs`  |

**Input**

```
{{ company.weight_unit }}
```

**Output**

```
kgs
```

---
*Source: [Company — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/company.md)*
