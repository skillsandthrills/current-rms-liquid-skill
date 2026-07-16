# Consolidation

Some objects in Current RMS are consolidated. For example, `order.items` has a consolidated counterpart: `order.consolidated_items`. 

When you consolidate, Current RMS groups all items with the same attribute into one single line. For example, the consolidated order items object groups all opportunity items with the same name into a single line.

Consolidation is especially useful where the same product or service is listed on an opportunity in more than one place and you want a sum total of that product or service on the opportunity. 

For example, this opportunity has two opportunity groups with the same items in each:

When printed to a document, `order.items` will print the items list as it is. `order.consolidated_items` will sum all of the items that are the same into a single line and give you a total quantity.

## Inaccessible objects

Because Current sums all similar items into a single line, you lose access to information that's stored against the individual line items. For example, if you're using the consolidated opportunity items loop then you can't access things such as:

* Opportunity item descriptions
* Whether or not an item is sub-rented
* Opportunity groups
* Asset numbers
* Information stored against the stock level, such as the location

The consolidated items object returns product and service records, so you might find the attribute you need there. For example, there's no weight total against a consolidated opportunity item, but you could access the product's weight using the product object.

---
*Source: [Consolidation — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/information/consolidation.md)*
