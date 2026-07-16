# Opportunity item assets

When you add a product or service to an opportunity, it creates an opportunity item on that opportunity. Opportunity items have opportunity item assets, which are records for allocations for that item.

An allocation might be a serialized asset or a sub-rent booking. 

Generally, the opportunity item asset object is used to print operations documents like Picking Lists, Delivery Notes, and Collection Notes.

### Document layouts

The `asset` object can be accessed in document layouts against the following modules:

#### Opportunity

```
{% for asset in order.product_assets %}
  {{ asset.asset_number }}
{% endfor %}
```

To print assets against an opportunity item:

```
{% for item in order.items %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {{ asset.asset_number }}
    {% endfor %}
  {% endif %}
{% endfor %}
```

To print assets inside a container:

```
{% for asset in order.container_item_asset %}
  {{ asset.asset_number }}
{% endfor %}
```

To print assets for a sub-rent supplier:

```
{% for asset in order.supplier_item_assets %}
  {{ asset.asset_number }}
{% endfor %}
```

#### Member

To print sub-rent allocations for a particular supplier:

```
{% for sub_rent in member.active_sub_rentals %}
  {{ sub_rent.opportunity_item.name }}
{% endfor %}
```

### Discussion templates 

The `asset` object can be accessed in document layouts against the following modules:

#### Opportunity

```
{% for asset in opportunity.product_assets %}
  {{ asset.asset_number }}
{% endfor %}
```

To print assets against an opportunity item:

```
{% for item in opportunity.items %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {{ asset.asset_number }}
    {% endfor %}
  {% endif %}
{% endfor %}
```

To print assets inside a container:

```
{% for asset in opportunity.container_item_asset %}
  {{ asset.asset_number }}
{% endfor %}
```

To print assets for a sub-rent supplier:

```
{% for asset in opportunity.supplier_item_assets %}
  {{ asset.asset_number }}
{% endfor %}
```

#### Member

To print sub-rent allocations for a particular supplier:

```
{% for sub_rent in organisation.active_sub_rentals %}
  {{ sub_rent.opportunity_item.name }}
{% endfor %}
```

## `asset_number`

Where serialized, returns an opportunity item asset asset number.

Returns blank for bulk or non-stock.

#### Input

```
{{ asset.asset_number }}
```

#### Output

```
DB-001
```

## `barcode_number`

Where bulk or non-stock, returns an opportunity item asset's related product barcode number.

Returns blank for serialized.

#### Input

```
{{ asset.barcode_number }}
```

#### Output

```
HDMI-000
```

## `container`

Returns the opportunity item asset container name. 

Returns blank where no container is set.

#### Input

```
{{ asset.container }}
```

#### Output

```
Box 1
```

## `cost`

Returns opportunity cost objects for an opportunity item asset.

#### Input

```
{% for cost in asset.costs %}
  {{ cost.price }}
{% endfor %}
```

#### Output

```
100.0
```

See: [Opportunity costs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-costs.md)

## `depth`

Returns the depth of an opportunity item asset in the tree. An item’s depth is determined by how it is nested under items. 

#### Input

```
{{ asset.depth }}
```

#### Output

```
1
```

## `depth_padding`

Returns the depth padding for an opportunity item asset. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

Increments in multiples of 16.

#### Input

```
<td style="padding-left: {{ asset.depth_padding }}px;">
  {{ asset.name }}
</td>
```

#### Output

```markup
<td style="padding-left: 16px;">
  Leica R-Series 180mm f/2.8
</td>
```

## `description`

Returns an opportunity item asset’s related opportunity item description.

#### Input

```markup
{{ asset.description }}
```

#### Output

```markup
Supplied with power cable.
```

## `group_depth_padding`

Returns the depth padding for an opportunity item asset's related opportunity group.

Used in our default documents where the `order.product_assets` is looped, which doesn't include groups.

#### Input

```markup
<td style="padding-left: {{ asset.group_depth_padding }}px;">
  {{ asset.group_name }}
</td>
```

#### Output

```markup
<td style="padding-left: 0px;">
  Cameras
</td>
```

## `group_description`

Returns the description for an opportunity item asset's related opportunity group.

Used in our default documents where the `order.product_assets` is looped, which doesn't include groups.

#### Input

```markup
{{ asset.group_description }}
```

#### Output

```markup
This kit goes in the main area.
```

## `group_name` 

Returns the name for an opportunity item asset's related opportunity group.

Used in our default documents where the `order.product_assets` is looped, which doesn't include groups.

#### Input

```markup
{{ asset.group_name }}
```

#### Output

```markup
Cameras
```

## `has_shortage?`

Returns `true` where an opportunity item asset has a shortage; `false` otherwise.

Shortages are highlighted in red and have an ⚠️ exclamation icon next to them in the list.

#### Input

```
{{ asset.has_shortage? }}
```

#### Output

```
true
```

## `id`

Returns an opportunity item asset ID. 

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ asset.id }}
```

#### Output

```
1	
```

## `is_bulk_stock?`

Returns `true` if an opportunity item asset is for bulk stock; `false` otherwise.

#### Input

```
{{ asset.is_bulk_stock? }}
```

#### Output

```
true
```

## `is_non_stock_booking?`

Returns `true` if an opportunity item asset is a non-stock allocation; `false` otherwise.

Text items are considered non-stock allocations.

#### Input

```
{{ asset.is_non_stock_booking? }}
```

#### Output

```
true
```

## `is_resource_stock?`

Returns `true` if an opportunity item asset is a service with bookable resource, i.e. a bookable resource has been allocated; `false` otherwise.

#### Input

```
{{ asset.is_resource_stock? }}
```

#### Output

```
true
```

## is\_serialised\_component? 

Returns true if an opportunity item asset is a serialized component, i.e. it is part of a serialized container; false otherwise.

## is\_serialised\_container?

Returns true if an opportunity item asset is a serialized container; false otherwise.

## `is_serialised_stock?`

Returns `true` if an opportunity item asset is a serialized stock allocation, i.e. a serialized asset has been allocated; `false` otherwise.

#### Input

```
{{ asset.is_serialised_stock? }}
```

#### Output

```
true
```

## `location`

Returns the stock level location for an opportunity item asset.

#### Input

```
{{ asset.location }}
```

#### Output

```
Bay A2 Shelf G4
```

## `name`

Returns an opportunity item asset's name. This will always be the name of the opportunity item.

#### Input

```
{{ asset.name }}
```

#### Output

```
D&B E3 Speaker
```

## opportunity\_item

Returns opportunity item objects for an opportunity item asset.

Generally used to access information like the opportunity item charge total or description.

#### Input

```
{{ asset.opportunity_item.charge_total }}
```

#### Output

```
180.0
```

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## outer\_container

Returns the container attribute of a serialised component's serialised container. Otherwise returns the same as the container method.

## `product`

Returns product objects for an opportunity item asset, where related to a product.

#### Input

```
{{ asset.product.description }}
```

#### Output

```
The E3 is an extremely small and versatile high performance system with astonishing sound and excellent headroom. The horn, which may be rotated to give either 90° x 60° or 60° x 90° coverage, has the necessary flexibility in directivity to enable a variety of applications such as delay, infill or distributed sound reinforcement applications. 
```

See: [Product](https://current-rms.gitbook.io/liquid-syntax/products/product.md)

## `quantity`

Returns the quantity against an opportunity item asset.

#### Input

```
{{ asset.quantity }}
```

#### Output

```
2
```

## `replacement_value`

Returns the replacement charge for an opportunity item asset. This may differ from the opportunity item replacement charge depending on the quantity.

#### Input

```
{{ asset.replacement_value }}
```

#### Output

```
20.0
```

## `resource`

Returns contact, user, or vehicle objects for a bookable resource allocation.

#### Input

```
{{ asset.resource.name }}
```

#### Output

```
Jo Swanson
```

See: [People & Organizations](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)

## `resource_name`

Returns the name of the contact, user, or vehicle for a bookable resource allocation.

#### Input

```
{{ asset.resource_name }}
```

#### Output

```
Jo Swanson
```

## `return_assets`

Returns opportunity item return assets for an opportunity item asset.

#### Input

```
{% for return in asset.return_assets %}
  {{ return.return_at }}
{% endfor %}
```

#### Output

```
2021-07-28 10:00:00 +0000
```

See: [Opportunity return item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-return-assets.md)

## `serial_number`

Returns the stock level serial number for an opportunity item asset.

> **Note:**
> In Current RMS we make a distinction between serial numbers and asset numbers. Asset numbers are used for allocation.

#### Input

```
{{ asset.serial_number }}
```

#### Output

```
D03VGP9CNHT20
```

## `service`

Returns service objects for an opportunity item asset, where related to a service.

#### Input

```
{{ asset.service.description }}
```

#### Output

```
Let us take care of all of the setup for you!
```

## `service_name`

Returns the name of the related service for an opportunity item asset.

#### Input

```
{{ asset.service_name }}
```

#### Output

```
Install
```

## `status`

Returns the opportunity item asset status ID.

| ID   | Status name |
| ---- | ----------- |
| `1`  | Provisional |
| `2`  | (Allocated) |
| `5`  | Reserved    |
| `10` | Allocated   |
| `15` | Prepared    |
| `20` | Booked Out  |
| `30` | Checked In  |
| `40` | Completed   |
| `45` | Moved       |

> **Note:**
> Note the difference between `2` and `10`. 
> 
> * `2` (Allocated) is for allocations on a provisional quotation. 
> * `10` Allocated is for allocations on a reserved quotation or order.

#### Input

```
{{ asset.status }}
```

#### Output

```
5
```

## `status_name`

Returns the opportunity item asset status name.

Status names are in the language set against your user profile. 

* Provisional
* (Allocated)
* Reserved
* Allocated
* Prepared
* Booked Out
* Checked In
* Completed
* Moved

#### Input

```
{{ asset.status_name }}
```

#### Output

```
Reserved
```

## `stock_level`

Returns stock level objects for the related stock level of an opportunity item asset.

#### Input

```
{{ asset.stock_level.location }}
```

#### Output

```
Bay A2 Shelf G4
```

See: [Stock level](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md)

## `supplier`

Returns organization objects for a sub-rent or sub-contract supplier related to an opportunity item asset.

#### Input

```
{{ asset.supplier.address }}
```

#### Output

```
3934 Giraffe Hill Drive, Farmers Branch, TX 75234
```

See: [Organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)

## `supplier_name` 

Returns the name of the organization set as a sub-rent or sub-contract supplier for an opportunity item asset.

#### Input

```
{{ asset.supplier_name }}
```

#### Output

```
Vita Sound
```

## `weight`

Returns the weight for an opportunity item asset's related opportunity item.

#### Input

```
{{ asset.weight }}
```

#### Output

```
10.0
```

> **Note:**
> Use [the `company` object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to return your company weight unit, e.g. `lbs` or `kg`.

## `weight_total`

Returns the weight total for an opportunity item asset. This may differ from the opportunity item replacement charge depending on the quantity.

#### Input

```
{{ asset.weight_total }}
```

#### Output

```
20.0
```

---
*Source: [Opportunity item assets — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)*
