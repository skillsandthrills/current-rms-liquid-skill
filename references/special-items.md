# Special items

When [allocating a temporary container to an opportunity](https://help.current-rms.com/en/articles/3040166-work-with-temporary-or-permanent-serialized-containers-on-an-opportunity), Current adds container components that aren't already on the opportunity to a special “Spares & Containers” group. It adds the container to this group, too.

We don't print this group on customer-facing document layouts by default.

Items that make up this “Spares & Containers” group are known as ‘special items’ internally. If you like, you may access special items on opportunity document layouts. 

To print special items on our standard quotation or rental agreement documents, it should be as simple as swapping `order.items` for `order.items_including_special_items` and changing your logic to include special items. You may use booleans to determine whether an opportunity item is a special group, item, or accessory.

Serialized component information is also available in the stock level object, useful for creating documents against the product module.

## Naming conventions

Before the launch of temporary containers, we used the term ‘serialized components’ to refer to components inside of a serialized container. Temporary containers may include bulk and non-stock, so we changed the terminology in the web interface to ‘container components’ for clarity.

For compatibility, our Liquid objects still use the term ‘serialized components’ to refer to components inside of a serialized container. Keep in mind that container components themselves might not be serialized.

## Opportunity objects

The `items`, `products`, and `rentals` objects do not return any special items.

### `special_items`

Returns [opportunity item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) for special items on an opportunity.

### `items_including_special_items`

Returns [opportunity item objects](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) for all opportunity items, including special items.

## Opportunity item objects

### `is_special?`

Returns `true` if the opportunity item is a special item; `false` otherwise.

### `is_special_group?`

Returns `true` if an opportunity item is a special group; `false` otherwise. 

This will usually be called “Spares & Containers”, but the special group name can be changed on an opportunity.

### `is_special_principal?`

Returns `true` if an opportunity item is special and has accessory items nested underneath it; `false` otherwise.

### `is_special_accessory?`

Returns `true` if an opportunity item is special and an accessory; `false` otherwise.

## Opportunity item asset

### `is_permanent_serialised_container?`

Returns `true` if an opportunity item asset is a permanent serialized container; `false` otherwise.

### `is_temporary_serialised_container?`

Returns `true` if an opportunity item asset is a temporary serialized container; `false` otherwise.

### `is_permanent_serialised_component?`

Returns `true` if an opportunity item asset is a permanent container container; `false` otherwise.

### `is_temporary_serialised_component?`

Returns `true` if an opportunity item asset is a temporary container container; `false` otherwise.

## Stock level

We added new stock level objects when we launched temporary containers. They're used in the ‘Container Contents’ document layout that's available to print from product, stock level, and serialized container screens.

### `container_components_and_descendants`

Returns [stock level objects](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md) for container components of this serialized container. 

#### Input

```
{% for component in asset.container_components_and_descendants %}
  {{ component.asset_number }}
{% endfor %}
```

#### Output

```
D&B E3 Speaker
```

### `serialised_components_and_descendants`

Returns [stock level objects](https://current-rms.gitbook.io/liquid-syntax/products/stock-level.md) for container components of this serialized container. This is the same as above and is included to maintain consistency in naming conventions.

### `is_permanent_serialised_container?`

Returns `true` if a stock level is a permanent serialized container; `false` otherwise.

### `is_temporary_serialised_container?`

Returns `true` if a stock level is a temporary serialized container; `false` otherwise.

### `container_weight`

Returns the weight of a serialized container, including all component stock levels.

> **Note:**
> Use the [company object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) weight unit to print the weight unit for your system.

### `depth_padding`

Returns the depth padding for a container component stock level. Generally used to apply an inline style to a table cell in HTML so that items appear nested.

Increments in multiples of 16.

### `serialised_component_quantity`

Returns the quantity against the container component record if this stock level has been created for the container contents.

---
*Source: [Special items — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/special-objects.md)*
