# Current-RMS Liquid — object & attribute index

Every documented object and its attributes. If an attribute is not listed here or in the object's reference file, DO NOT use it.
Full details per object: `references/objects/<file>`.

## Activity  (`objects/activity__activity.md`)

`activity_type_name`, `completed?`, `completed_at`, `description`, `ends_at`, `for_service?`, `opportunity_item_asset`, `owner`, `participants`, `priority`, `regarding`, `starts_at`, `subject`, `time_status_name`

## Address detail  (`objects/general__address.md`)

`city`, `postcode`, `single_line_address`, `state`, `street`

## Attachments  (`objects/general__attachments.md`)

`attachment_content_type`, `attachment_file_name`, `attachment_file_size`, `attachment_thumb_url`, `attachment_url`, `description`, `name`

## Company  (`objects/general__company.md`)

`address`, `address_detail`, `company_registration_number`, `subdomain`, `tax_registration_number`, `weight_unit`

## Emails  (`objects/general__email.md`)

`address`, `type_id`, `type_name`

## Links  (`objects/general__links.md`)

`address`, `type_id`, `type_name`

## Store  (`objects/general__store.md`)

`website`

## Phones  (`objects/general__telephone.md`)

`number`, `type_id`, `type_name`

## Inventory check items (stock check items)  (`objects/inventory-check__inventory-check-items-stock-check-items.md`)

`asset_number`, `quantity_counted`, `quantity_held`, `stock_level`

## Inventory check (stock check)  (`objects/inventory-check__inventory-check-stock-check.md`)

`tag_filter`

## Invoice items  (`objects/invoices__invoice-item.md`)

`accessory_is_default?`, `accessory_is_mandatory?`, `accessory_is_optional?`, `accessory_mode_is_accessory?`, `accessory_mode_is_component?`, `accessory_mode_is_safety?`, `accessory_mode_name`, `charge_ends_at`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_starts_at`, `charge_total`, `chargeable_days`, `charging_periods`, `children`, `depth`, `depth_padding`, `description`, `discount_amount`, `discount_percent`, `discounted_price`, `has_child_items?`, `has_discount?`, `id`, `invoiceable_item_description`, `invoiceable_name`, `invoiceable_object`, `invoiceable_type`, `is_accessory?`, `is_deal_item?`, `is_group?`, `is_in_deal?`, `is_item?`, `is_principal?`, `is_product?`, `is_rental?`, `is_sale?`, `is_service?`, `is_service_item?`, `is_subtotal?`, `is_text_item?`, `name`, `order`, `price`, `price_unit`, `project_name`, `quantity`, `rate_definition_name`, `service_unit_name`, `source_name`, `subtotal`, `subtotal_name`, `tax_class_name`, `tax_total`, `transaction_type_name`, `unit_charge`, `unit_charge_amount`, `use_chargeable_days`

## Invoice taxes  (`objects/invoices__invoice-tax.md`)

`name`, `taxable_charge`

## Invoice transactions  (`objects/invoices__invoice-transactions.md`)

`id`, `payment_method_name`, `reference`, `transaction_at`, `transaction_type`, `transaction_type_name`

## Invoice  (`objects/invoices__invoice.md`)

`balance`, `billing_address`, `billing_address_detail`, `billing_address_name`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total`, `combined_discount_total`, `deal_discount_total`, `delivery_address`, `delivery_address_detail`, `delivery_address_name`, `description`, `discount_total`, `due_at`, `external_description`, `has_discount?`, `id`, `invoiced_at`, `is_paid?`, `is_posted?`, `items`, `name`, `number`, `payment_total`, `payments`, `reference`, `refunds`, `sources`, `status`, `status_name`, `tax_class_name`, `tax_total`, `taxes`, `transaction_total`, `transactions`, `type`, `type_name`, `venue`

## Consolidated opportunities  (`objects/opportunities__consolidated-opportunities.md`)

`ends_at`, `starts_at`

## Consolidated opportunity items  (`objects/opportunities__consolidated-opportunity-items.md`)

`charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total`, `is_product?`, `is_rental?`, `is_sale?`, `is_service?`, `is_service_item?`, `is_text_item?`, `product_stock_levels`, `quantity`, `revenue_group`, `surcharge_amount`, `tax_total`, `transaction_type_name`, `use_chargeable_days`

## Opportunity costs  (`objects/opportunities__opportunity-costs.md`)

`chargeable_days`, `charging_periods`, `description`, `image_attachments`, `manual_cost?`, `price_unit`, `quantity`, `reference`, `service_unit_name`, `starts_at`, `subject`, `supplier`, `supplier_reference`, `unit_charge_amount`

## Opportunity item assets  (`objects/opportunities__opportunity-item-assets.md`)

`asset_number`, `barcode_number`, `container`, `cost`, `depth`, `depth_padding`, `description`, `group_depth_padding`, `group_description`, `has_shortage?`, `id`, `is_bulk_stock?`, `is_non_stock_booking?`, `is_resource_stock?`, `is\_serialised\_component?`, `is\_serialised\_container?`, `is_serialised_stock?`, `location`, `name`, `opportunity\_item`, `outer\_container`, `product`, `quantity`, `replacement_value`, `resource`, `resource_name`, `return_assets`, `serial_number`, `service`, `service_name`, `status`, `status_name`, `stock_level`, `supplier`, `weight`, `weight_total`

## Opportunity return item assets  (`objects/opportunities__opportunity-item-return-assets.md`)

`asset_number`, `damage_description`, `quantity_damaged`, `quantity_lost`, `quantity_ok`, `quantity_returned`, `quantity_sold`, `return_at`

## Opportunity item surcharges  (`objects/opportunities__opportunity-item-surcharge.md`)

`charge`, `group_name`, `name`, `original_charge`

## Opportunity items  (`objects/opportunities__opportunity-items.md`)

`accessories`, `accessory_is_default?`, `accessory_is_mandatory?`, `accessory_is_optional?`, `accessory_mode_is_accessory?`, `accessory_mode_is_component?`, `accessory_mode_is_safety?`, `accessory_mode_name`, `assets`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total_including_children`, `charge_total`, `chargeable_days`, `charging_periods`, `children`, `combined_discount_total`, `deal_discount_total`, `depth`, `depth_padding`, `description`, `discount_amount`, `discount_percent`, `discount_total`, `discounted_price`, `ends_at`, `group_has_deal?`, `has_child_items?`, `has_discount?`, `has_shortage?`, `id`, `is_accessory?`, `is_group?`, `is_in_deal?`, `is_item?`, `is_principal?`, `is_product?`, `is_rental?`, `is_sale?`, `is_service?`, `is_service_item?`, `is_subtotal?`, `is_text_item?`, `name`, `opportunity`, `price`, `price_unit`, `product_stock_levels`, `quantity`, `rate_definition_name`, `replacement_charge_total`, `replacement_charge_total_including_children`, `revenue_group`, `service_unit_name`, `starts_at`, `sub_contract?`, `sub_rent?`, `subtotal`, `subtotal_including_tax`, `subtotal_name`, `surcharge_amount`, `surcharges`, `tax_total`, `transaction_type_name`, `unit_charge`, `unit_charge_amount`, `use_chargeable_days`, `warehouse_notes`, `weight_total`, `weight_total_including_children`

## Opportunity  (`objects/opportunities__opportunity.md`)

`activities`, `actual_cost_total`, `assets`, `attachments`, `billing_address`, `billing_address_detail`, `billing_address_name`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total`, `chargeable_days`, `collection_address`, `collection_address_detail`, `collection_address_name`, `combined_discount_total`, `consolidated_container_item_assets`, `consolidated_items`, `consolidated_principal_items`, `container_item_assets`, `costs`, `customer_collecting`, `customer_returning`, `deal_discount_total`, `deal_exists?`, `delivery_address`, `delivery_address_detail`, `delivery_address_name`, `description`, `discount_total`, `discussion_email_address`, `external_description`, `has_discount?`, `has_invoices?`, `id`, `invoiced`, `invoices`, `items`, `items_sorted_by_principal`, `items_sorted_by_tag`, `name`, `number`, `open_ended_rental`, `opportunity_has_deal?`, `ordered_at`, `original_charge_excluding_tax_total`, `original_charge_including_tax_total`, `original_charge_total`, `original_discount_total`, `original_rental_charge_total`, `original_sale_charge_total`, `original_service_charge_total`, `original_surcharge_total`, `original_tax_total`, `owner`, `part_invoice_charge_total`, `participants`, `predicted_cost_total`, `product_assets`, `products`, `project`, `project_name`, `provisional_cost_total`, `purchase_orders`, `quote_invalid_at`, `reference`, `rental_charge_total`, `rentals`, `replacement_charge_total`, `sale_charge_total`, `sales`, `schedule_type_is_extended?`, `schedule_type_is_extended?`, `schedule_type_is_standard?`, `service_charge_total`, `services`, `starts_at`, `state`, `state_name`, `status`, `status_name`, `supplier_item_assets`, `surcharge_total`, `tax_class_name`, `tax_total`, `use_chargeable_days`, `venue`, `weight_total`, `Extended scheduler dates`

## Contact  (`objects/people-and-organizations__contact.md`)

`activities`, `address`, `address_detail`, `attachments`, `department`, `description`, `email`, `emails`, `icon_url`, `image_attachments`, `id`, `lawful_basis_type_name`, `location_type_name`, `mobile`, `name`, `organisations`, `phones`, `purchase_tax_class_name`, `telephone`, `title`, `venue`

## Organization  (`objects/people-and-organizations__organization.md`)

`active_sub_rentals`, `activities`, `address`, `address_detail`, `attachments`, `description`, `emails`, `icon_url`, `image_attachments`, `invoice\_term\_name`, `lawful_basis_type_name`, `purchase\_orders`, `purchase_tax_class_name`, `sale_tax_class_name`, `tax_class_name`, `telephone`

## User  (`objects/people-and-organizations__user.md`)

(see file)

## Vehicle  (`objects/people-and-organizations__vehicle.md`)

`length`, `location_type_name`, `volume`, `width`

## Venue  (`objects/people-and-organizations__venue.md`)

`location_type_name`, `purchase_tax_class_name`

## Charging period  (`objects/products__charging-period.md`)

`rate`

## Product accessories  (`objects/products__product-accessories.md`)

`for\_parent\_rental?`, `for\_parent\_sale?`, `id`, `is\_default?`, `is\_mandatory?`, `is\_optional?`, `item\_transaction\_type\_is\_rental?`, `item\_transaction\_type\_is\_sale?`, `item\_transaction\_type\_name`, `mode`, `mode\_is\_accessory?`, `mode\_is\_component?`, `mode\_is\_safety?`, `mode\_name`, `parent\_transaction\_type`, `parent\_transaction\_type\_is\_both?`, `parent\_transaction\_type\_is\_rental?`, `parent\_transaction\_type\_is\_sale?`, `parent\_transaction\_type\_name`, `product`, `quantity`, `sort\_order`, `zero\_priced?`

## Product assets  (`objects/products__product-assets.md`)

(see file)

## Product group  (`objects/products__product-group.md`)

`description`, `icon_url`, `name`

## Product  (`objects/products__product.md`)

`country\_of\_origin\_code`, `weight`

## Stock level  (`objects/products__stock-level.md`)

`asset_number`, `container_components_and_descendants`, `depth_padding`, `icon_url`, `id`, `inspection_results`, `is_bulk_stock?`, `is_non_stock_booking?`, `location`, `serialised\_component\_quantity`, `serialised_components`, `store`, `url`

## Project  (`objects/project__project.md`)

`attachments`, `billing_address`, `billing_address_detail`, `billing_address_name`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total`, `consolidated_items`, `consolidated_opportunities`, `customer`, `delivery_address`, `delivery_address_detail`, `delivery_address_name`, `description`, `drafts`, `ends_at`, `enquiries`, `icon_url`, `id`, `image_attachments`, `name`, `opportunities`, `orders`, `owner`, `participants`, `project_invoicing`, `quotations`, `reference`, `rental_charge_total`, `sale_charge_total`, `service_charge_total`, `starts_at`, `store`, `surcharge_total`, `tax_class_name`, `tax_total`, `venue`

## Purchase order items  (`objects/purchase-orders__purchase-order-items.md`)

`accessory\_is\_default?`, `accessory_is_mandatory?`, `accessory_is_optional?`, `accessory_mode_is_accessory?`, `accessory_mode_is_component?`, `accessory_mode_is_safety?`, `accessory_mode_name`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total_including_children`, `charge_total`, `chargeable_days`, `charging_periods`, `children`, `depth`, `depth_padding`, `description`, `discount_amount`, `discount_percent`, `discounted_price`, `has_discount?`, `id`, `image\_url`, `is_accessory?`, `is_group?`, `is_item?`, `is_principal?`, `is_product?`, `is_service_item?`, `is_subtotal?`, `is_text_item?`, `name`, `price_unit`, `quantity`, `rate_definition_name`, `service_unit_name`, `starts_at`, `subtotal`, `subtotal_name`, `supplier_reference`, `tax_total`, `thumbnail_url`, `transaction_type_name`, `unit_charge`, `unit_charge_amount`, `weight_total`, `weight_total_including_children`

## Purchase order  (`objects/purchase-orders__purchase-order.md`)

`authorised_at`, `authoriser`, `charge_excluding_tax_total`, `charge_including_tax_total`, `charge_total`, `customer_collecting`, `customer_returning`, `delivery_address`, `delivery_address_detail`, `delivery_address_name`, `delivery_at`, `delivery_attention`, `delivery_instructions`, `description`, `expected_at`, `expected_note`, `external_description`, `id`, `items`, `name`, `number`, `ordered_at`, `participants`, `sources`, `state`, `state_name`, `status`, `status_name`, `store`, `supplier`, `tax_class_name`, `tax_total`, `venue`, `weight_total`

## Quarantine  (`objects/quarantine__quarantine.md`)

`activities`, `attachments`, `ends_at`, `image_attachments`, `type`

## Service  (`objects/service__service.md`)

`attachments`, `external_service_cost_group`, `image_attachments`, `service_type_name`, `Rates`

## Inspection result tasks  (`objects/testing-and-inspection__inspection-result-tasks.md`)

`name`, `value`

## Inspection results  (`objects/testing-and-inspection__inspection-results.md`)

`description`, `inspection_at`, `passed`, `passed_to_word`, `stock_level`, `task_list_results`

