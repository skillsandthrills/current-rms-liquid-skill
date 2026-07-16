# Address detail

In most cases where you want to access an address, simply use the record‘s `address` object. For example, to output your company address:

```
{{ company.addresss }}
```

If you need to access a particular component of an address, use the `address_detail` object. For example, to output your company's country:

```
{{ company.address_detail.country }}
```

The `address_detail` object always relates to another object. For example, this will not output anything:

```
{{ address_detail.country }}
```

Prefixing it with `company.`, `venue.`, or another object where `address` is an object will resolve this.

Opportunities, invoices, and purchase orders have a billing and a delivery address, so use `billing_address_detail` and `delivery_address_detail` to access those address components. For example, to print the billing address country on an opportunity document: 

```
{{ order.billing_address_detail.country }}
```

### Document layouts

The `address_detail` object can be accessed in document layouts created against the following modules:

* Invoice
* Opportunity
* Project
* Product
* Quarantine
* Member
* Purchase order

### Discussion templates

The `address_detail` object can be accessed discussion templates created against the following modules:

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

## `city`

Returns the address city.

#### Input

```
{{ company.address_detail.city }}
```

#### Output

```
Cypress Creek
```

## `country` 

Returns the address country.

#### Input

```
{{ company.address_detail.country }}
```

#### Output

```
United States
```

## `county` 

For countries with regions, returns the address county.

#### Input

```
{{ company.address_detail.county }}
```

#### Output

```
Nottinghamshire
```

## `name` 

Returns the address name. 

#### Input

```
{{ company.address_detail.name }}
```

#### Output

```
Globex Corporation
```

## `postcode`

Returns the zip code or post code.

#### Input

```
{{ company.address_detail.postcode }}
```

#### Output

```
90210
```

## `single_line_address`

Returns the address on a single line.

#### Input

```
{{ company.address_detail.single_line_address}}
```

#### Output

```
333 North Sam Houston Parkway East, Ste 1100, Suite 1100, Houston, TX 77060
```

## `state`

For countries with states, returns the address state.

#### Input

```
{{ company.address_detail.state }}
```

#### Output

```
Texas
```

## `street`

Returns the address street.

#### Input

```
{{ company.address_detail.street }}
```

#### Output

```
15201 Maple Systems Road
```

---
*Source: [Address detail — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/address.md)*
