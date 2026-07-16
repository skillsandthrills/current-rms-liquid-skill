# Stock level

Stock levels in Current RMS belong to products. They contain information about the physical units that you rent or sell.

* For serialized products, one stock level is one physical unit (i.e. an asset). A serialized product typically has multiple stock levels.
* For bulk products, a stock level is for many physical units. When creating a bulk stock level, you set a quantity against it.

Current RMS shows you a list of stock levels for serialized and bulk stock products on a product page in Resources > Products.

### Stock levels for non-stock and sub-rent bookings

Non-stock products, by their nature, do not have stock levels you can edit in the web interface. You've told Current RMS that you don't want to track (or even don't hold any) stock of them. 

Similarly, stock that you sub-rent from a vendor doesn't have a stock level page. You hold it temporarily for an opportunity, so there's no way to edit or work with it.

However, Current RMS creates system stock levels for non-stock and sub-rent bookings behind the scenes. 

These stock levels are created for internal use only and aren't exposed in our web interface. They are exposed in our document layout objects for compatibility.

### Resource (service) bookings

Where products have stock levels, services have (bookable) resources. These are people or vehicles or venues used to fulfil a service.

The `asset_number` object will return the name of the related bookable resource. 

Other objects will return blank or an error.

### Group bookings

Where a serialized product is added to a reserved quotation or order but an asset hasn't been allocated, this is called a "Group Booking." A quantity is removed from availability, but no particular serialized stock levels are marked as unavailable.

Behind the scenes, Current RMS creates system "Group Booking" stock levels. They aren't exposed in the web interface and are internal only. They are exposed in our document layout objects for compatibility.

### Barcode images

In early versions of our standard barcode labels, we printed barcode and QR code images using objects that pointed at URLs:

* `barcode_url`
* `qrcode_url`

For example, to print a barcode image:

```
<img src="{{ asset.barcode_url }}" style="max-height: 50px;">
```

> **Important:**
> **Do not use these objects.** Support may be withdrawn in future.

This works, but was slow when working with a large number of stock levels. We've deprecated the `barcode_url` and `qrcode_url` objects in favor of new Liquid filters:

* `qrcode`
* `code39`
* `code128B`

These filters convert an object into an SVG.

For example:

```
<img src="data:image/svg+xml;base64,{{ asset.asset_number | code128B | base64 }}" style="max-height: 25px; padding-left: 44px">
```

### Main use cases

There's a couple of reasons that the stock level object is useful:

* Printing barcode numbers of or other product documents.
* Accessing detailed information about an asset allocated on an opportunity.

### Document layouts

The `stock_level` object can be accessed in document layouts created against the following records:

#### Product

```
{% for asset in product.assets %}
  {{ asset.asset_number }}
{% endfor %}
```

#### Opportunity

```
{% for asset in order.product_assets %}
  {{ asset.stock_level.serial_number }}
{% endfor %}
```

#### Inspection result

```
{{ inspection_result.stock_level.asset_number }}
```

#### Quarantine

```
{{ quarantine.stock_level.asset_number }}
```

### Discussion templates

The `stock_level` object can be accessed in discussion templates created against the following records:

#### Product

```
{% for asset in product.assets %}
  {{ asset.asset_number }}
{% endfor %}
```

#### Opportunity

```
{% for asset in opportunity.product_assets %}
  {{ asset.stock_level.serial_number }}
{% endfor %}
```

#### Quarantine

```
{{ quarantine.stock_level.asset_number }}
```

## `asset_number`

Where serialized, returns a stock level asset number.

Returns blank for bulk or non-stock.

#### Input

```
{{ asset.asset_number }}
```

#### Output

```
DB-001
```

## `container_components_and_descendants`

Where a serialized container, returns stock level objects for container components. Includes components for containers inside containers.

#### Input

```
{% for component in stock_level.container_components_and_descendants %}
  {{ component.item_name }}
{% endfor %}
```

#### Output

```
Tecpro Comms LS731 2 Channel Station
```

## `container_weight` 

Returns the weight of a serialized container and its components.

Where a stock level isn't a container, returns the item weight.

#### Input

```
{{ stock_level.container_weight }}
```

#### Output

```
100
```

> **Note:**
> Use `weight_unit` against [the company object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to return your company's weight unit.

## `depth_padding`

Where a stock level is a serialized component, returns the depth padding. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

Increments in multiples of 16.

#### Input

```
<td style="padding-left: {{ stock_level.depth_padding }}px;">
  {{ stock_level.item_name }}
</td>
```

#### Output

```markup
<td style="padding-left: 16px;">
  Leica R-Series 180mm f/2.8
</td>
```

## `icon_url`

Returns a URL pointing at the stock level image.

#### Input

```
{{ stock_level.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-ca9a7ac0-2539-0131-ba41-0050569ba36f/icons/590/original/Screen_Shot_2018-07-13_at_13.47.09.png
```

## `id`

Returns the stock level ID. 

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ stock_level.id }}
```

#### Output

```
1	
```

## `inspection_results`

Returns inspection result objects for all inspection results for a stock level. 

#### Input

```
{% for inspection_result in stock_level.inspection_results %}
  {{ inspection_result.inspection_name }}
{% endfor %}
```

#### Output

```
PAT
```

See: [Inspection results](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-results.md)

## `is_bulk_stock?`

Returns `true` if a stock level is for bulk stock; `false` otherwise.

#### Input

```
{{ stock_level.is_bulk_stock? }}
```

#### Output

```
true
```

## `is_non_stock_booking?`

Returns true if a stock level is a non-stock booking; false otherwise.

#### Input

```
{{ stock_level.is_non_stock_booking? }}
```

#### Output

```
false
```

## `is_permanent_serialised_container?` 

Returns `true` if a stock level is a permanent serialized container; `false` otherwise.

#### Input

```
{{ stock_level.is_permanent_serialised_container? }}
```

#### Output

```
false
```

## `is_resource_stock?` 

Returns `true` if a stock level is for a service booking; `false` otherwise.

#### Input

```
{{ stock_level.is_resource_stock? }}
```

#### Output

```
false
```

## `is_serialised_container?` 

Returns `true` if a stock level is a serialized container; `false` otherwise.

A serialized container may be permanent or temporary.

#### Input

```
{{ stock_level.is_serialised_container? }}
```

#### Output

```
false
```

## `is_serialised_stock?` 

Returns `true` if a stock level is serialized; `false` otherwise.

#### Input

```
{{ stock_level.is_serialised_stock? }}
```

#### Output

```
true
```

## `is_sub_rent_booking?` 

Returns `true` if a stock level is a sub-rent booking; `false` otherwise.

Typically used on opportunity documents to filter out sub-rentals. Will never return `true` on product documents.

#### Input

```
{{ stock_level.is_sub_rent_booking? }}
```

#### Output

```
true
```

## `is_temporary_serialised_container?` 

Returns `true` if a stock level is a temporary serialized container; `false` otherwise.

#### Input

```
{{ stock_level.is_temporary_serialised_container? }}
```

#### Output

```
false
```

## `item_name` 

Returns the product name for the related product for a stock level.

#### Input

```
{{ stock_level.item_name }}
```

#### Output

```
D&B E3
```

## `latest_inspection_results` 

Returns inspection result objects for the most recent inspection results for a stock level. 

#### Input

```
{% for inspection_result in stock_level.latest_inspection_results %}
  {{ inspection_result.inspection_name }}
{% endfor %}
```

#### Output

```
PAT
```

See: [Inspection results](https://current-rms.gitbook.io/liquid-syntax/testing-and-inspection/inspection-results.md)

## `location`

Returns the location for a stock level.

#### Input

```
{{ stock_level.location }}
```

#### Output

```
Bay A2 Shelf G4
```

## `product` 

Returns product objects for a stock level's related product.

#### Input

```
{{ stock_level.product.name }}
```

#### Output

```
D&B E3
```

## `quantity_held` 

Where bulk stock, returns the quantity held against a stock level.

The quantity is as of now in the current store.

#### Input

```
{{ stock_level.quantity_held }}
```

#### Output

```
16.0
```

## `serial_number` 

Returns the serial number for a stock level.

> **Note:**
> In Current RMS we make a distinction between serial numbers and asset numbers. Asset numbers are used for allocation.

#### Input

```
{{ stock_level.serial_number }}
```

#### Output

```
D03VGP9CNHT20
```

## serialised\_component\_quantity

## `serialised_components`

Where a serialized container, returns stock level objects for container components.

#### Input

```
{% for component in stock_level.serialised_components %}
  {{ component.item_name }}
{% endfor %}
```

#### Output

```
Tecpro Comms LS731 2 Channel Station
```

## `serialised_components_and_descendants` 

See: [`container_components_and_descendants`](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md#container_components_and_descendants)

## `store`

Returns store objects for a stock level's related store.

#### Input

```
{{ stock_level.store.name }}
```

#### Output

```
The Barnhouse
```

## `url`

Where bulk or non-stock, returns a URL pointing at the product page.

Where serialized, returns a URL pointing at the stock level page.

Typically used for generating a QR code using the `qrcode` filter that you may use for quick access to a product or stock level page, as well as asset lookup.

#### Input

```
{{ stock_level.url }}
```

#### Output

```
http://abcrentals.current-rms.com/stock_levels/3212
```

> **Warning:**
> Returns an error for resource stock.

---
*Source: [Stock level — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md)*
