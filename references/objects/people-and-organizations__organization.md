# Organization

Organizations in Current RMS are billing entities. They're customers or vendors that you bill.

You can set an organization as a sub-rent supplier and raise a purchase order for them. You can also invoice an organization. 

### Members

Contacts, organizations, vehicles, venues, and users are all known as members in the database. Members have some shared attributes, along with attributes that are specific to that particular member type.

When you're checking a list of members, you can use the type object to determine what type of member you're working with. 

For example, the participants object against an opportunity returns participant objects for any members who are participants on the opportunity. To print only organizations:

```
<ul>
  {% for participant in order.participants %}
    {% if participant.type == "Organization" %}
      <li>{{ participant.name }}</li>
    {% endif %}
  {% endfor %}
</ul>
```

### Document layouts

The `organization` object can be accessed in document layouts created against the following modules:

#### Member

From an organization record:

```
{{ member.name }}
```

From a contact record:

```
{% for organization in member.organisations %}
  {{ organization.name }}
{% endfor %}
```

#### Opportunity

To print information about the opportunity's related organization:

```
{{ customer.name }}
```

To print organizations that are a participant against an opportunity: 

```
{% for participant in order.participants %}
  {% if participant.type == "Organization" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print organizations that are sub-rent suppliers for opportunity items:

```
{% for item in order.product_assets %}
  {% if asset.sub_rent? %}
    {{ asset.supplier.name }}
  {% endif %}
{% endfor %}
```

To print organizations that are sub-contract suppliers for service bookings:

```
{% for item in order.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Organization" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print information about the project's related organization:

```
{{ customer.name }}
```

To print organizations that are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "Organization" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

Where the supplier is an organization:

```
{{ supplier.name }}
```

To print organizations against a purchase order's related contact: 

```
{% for organization in supplier.organisations %}
  {{ organization.name }}
{% endfor %}
```

#### Invoice

To print information about the invoice's related organization:

```
{{ customer.name }}
```

#### Quarantine

To print information about the sub-rent supplier against a quarantine:

```
{{ quarantine.supplier.name }}
```

To print information about the source opportunity's related organization:

```
{{ quarantine.source.customer.name }}
```

To print information about the next opportunity booking's related organization: 

```
{{ quarantine.next_booking.customer.name }}
```

#### Activity

To print information about organizations that are participants against an activity:

```
{% for participant in activity.participants %}
  {% if participant.type == "Organization" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

### Discussion templates

The `organization` object can be accessed in discussion templates created against the following modules:

#### Member

From an organization record:

```
{{ organisation.name }}
```

From a contact record:

```
{% for organization in contact.organisations %}
  {{ organization.name }}
{% endfor %}
```

#### Opportunity

To print information about the opportunity's related organization:

```
{{ customer.name }}
```

To print organizations that are a participant against an opportunity: 

```
{% for participant in opportunity.participants %}
  {% if participant.type == "Organization" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print organizations that are sub-rent suppliers for opportunity items:

```
{% for item in opportunity.product_assets %}
  {% if asset.sub_rent? %}
    {{ asset.supplier.name }}
  {% endif %}
{% endfor %}
```

To print organizations that are sub-contract suppliers for service bookings:

```
{% for item in opportunity.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Organization" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print information about the project's related organization:

```
{{ customer.name }}
```

To print organizations that are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "Organization" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

Where the supplier is an organization:

```
{{ supplier.name }}
```

To print organizations against a purchase order's related contact: 

```
{% for organization in supplier.organisations %}
  {{ organization.name }}
{% endfor %}
```

#### Invoice

To print information about the invoice's related organization:

```
{{ customer.name }}
```

#### Quarantine

To print information about the sub-rent supplier against a quarantine:

```
{{ quarantine.supplier.name }}
```

To print information about the source opportunity's related organization:

```
{{ quarantine.source.customer.name }}
```

To print information about the next opportunity booking's related organization: 

```
{{ quarantine.next_booking.customer.name }}
```

## `active_sub_rentals`

Returns opportunity item asset objects for active opportunities where this organization is a sub-rent supplier.

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `activities`

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to an organization.

#### Input  <a href="#input" id="input"></a>

```
{% for activity in member.activities %}
  {{ activity.subject }}
{% endif %}
```

#### Output  <a href="#ouput" id="ouput"></a>

```
Call to follow up
```

See: [Activity](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md)

## `address`

Returns the primary address for an organization.

#### Input

```
{{ member.address }}
```

#### Output

```
882 Broderick Flats Lake Erlingchester MA 67553-4548
```

## `address_detail`

Returns address objects for an organization's primary address.

#### Input

```
{{ member.address_detail.state }}
```

#### Output

```
MA
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `attachments`

Returns attachment objects for attachments stored against an organization.

#### Input <a href="#input-2" id="input-2"></a>

```
{% for attachment in member.attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output <a href="#output-2" id="output-2"></a>

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `contacts` 

Returns contact objects for linked contacts against an organization.

#### Input

```
{% for contact in member.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Output

```
Peter Miller
```

See: [Contact](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)

## `description`

Returns the description for an organization.

#### Input

```
{{ member.description }}
```

#### Output

```
I mean it's one banana, Michael. What could it cost, $10?
```

## `discount_category_name` 

Returns the discount category name for an organization.

#### Input

```
{{ member.discount_category_name }}
```

#### Output

```
Charity
```

## `email` 

Returns the first work email address stored against an organization

#### Input

```
{{ member.email }}
```

#### Output

```
gob@bluthcompany.com
```

## `emails`

Returns email objects for email addresses stored against an organization.

#### Input

```
{% for email in member.emails %}
  {{ email.address }}
{% endfor %}
```

#### Output

```
help@current-rms.com
```

See: [Emails](https://current-rms.gitbook.io/liquid-syntax/general/email.md)

## `icon_url`

Returns a URL pointing at the organization's picture. The full size image is returned.

#### Input

```
{{ member.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `image_attachments`

Returns attachment objects for attachments stored against an organization. Only returns those that have a file type of image.

#### Input <a href="#input-2" id="input-2"></a>

```
{% for attachment in member.attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output <a href="#output-2" id="output-2"></a>

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `id` 

Returns an organization's ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input

```
{{ member.id }}
```

#### Output

```
10
```

## `invoice_term_length` 

Returns the value of the invoice term type. Typically used with `invoice_term_name` to print invoice terms on documents.

#### Input

```
{{ member.invoice_term_length }}
```

#### Output

```
30
```

## invoice\_term\_name 

Returns the invoice term type. Typically used with `invoice_term_length` to print invoice terms on documents.

#### Input

```
{{ member.invoice_term_length }}
```

#### Output

```
days from invoice date
```

## `invoices` 

Returns invoice objects for invoices against an organization. All invoices and credits are returned.

#### Input

```
<ul>
  {% for invoice in member.invoices %}
    <li>{{ invoice.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Engagement Dinner
• Wedding
• Baby Shower
• Divorce Party
```

See: [Invoice](https://current-rms.gitbook.io/liquid-syntax/invoices/invoice.md)

## `is_cash?` 

Returns `true` where the cash customer toggle is set to YES; `false` otherwise.

#### Input

```
{{ member.is_cash? }}
```

#### Output

```
false
```

## `lawful_basis_type_id` 

Returns the legal basis type ID for an organization.

| Type    | Legal basis type                        |
| ------- | --------------------------------------- |
| `11001` | Legitimate interest - prospect          |
| `11002` | Legitimate interest - existing customer |
| `11003` | Performance of a contract               |
| `11004` | Freely given consent                    |
| `11005` | Employee                                |
| `11006` | Unknown                                 |

#### Input

```
{{ member.lawful_basis_type_id }}
```

#### Output

```
11005
```

## `lawful_basis_type_name`

Returns an organization's legal basis type name.

You may add legal basis types in System Setup > List of Values.

*  Legitimate interest - prospect
* Legitimate interest - existing customer
* Performance of a contract
* Freely given consent
* Employee
* Unknown

#### Input

```
{{ member.lawful_basis_type_name }}
```

#### Output

```
Employee
```

## `live_invoices` 

Returns invoice objects for invoices against an organization. Only live invoices and credits are returned, i.e those not voiced, paid, or posted.

#### Input

```
<ul>
  {% for invoice in member.live_invoices %}
    <li>{{ invoice.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Divorce Party
```

## `live_opportunities` 

Returns opportunity objects for opportunities against an organization. Only live opportunities are returned, i.e those that are open or active.

#### Input

```
<ul>
  {% for order in member.live_opportunities %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Divorce Party
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `live_purchase_orders` 

Returns purchase order objects for purchase orders against an organization. Only live purchase orders are returned.

#### Input

```
<ul>
  {% for purchase_order in member.live_purchase_orders %}
    <li>{{ purchase_order.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Sub-rental
• Sub-contract service
```

## `mobile` 

Returns an orgnaization's cell phone number. The first telephone number with the type “cell” or “mobile” is returned.

#### Input

```
{{ member.mobile }}
```

#### Output

```
(756) 555 1939
```

## `name` 

Returns the name of an organization.

#### Input

```
{{ member.name }}
```

#### Output

```
Bluth Company, Inc.
```

## `number` 

Returns the account number for an organization.

#### Input

```
{{ member.number }}
```

#### Output

```
111-222-333
```

## `on_stop?` 

Returns `true` if the “On Stop” toggle is set to YES against this customer; `false` otherwise.

#### Input

```
{{ member.on_stop? }}
```

#### Output

```
false
```

## `opportunities` 

Returns opportunity objects for opportunities against an organization. All opportunities are returned, regardless of state or status.

#### Input

```
<ul>
  {% for order in member.opportunities %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Engagement Dinner
• Wedding
• Baby Shower
• Divorce Party
```

See: [Opportunity](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md)

## `phones` 

Returns telephone objects for telephone numbers listed against the organization.

#### Input <a href="#input-7" id="input-7"></a>

```
{% for telephone in member.phones %}
  {{ telephone.number }}
{% endfor %}
```

#### Output <a href="#output-7" id="output-7"></a>

```
(636) 555 0113
```

See: [Phones](https://current-rms.gitbook.io/liquid-syntax/general/telephone.md)

## `price_category_name` 

Returns the price category against the organization.

#### Input

```
{{ member.price_category_name }}
```

#### Output

```
Gold
```

## purchase\_orders 

Returns purchase order objects for purchase orders against an organization. All purchase orders are returned.

#### Input

```markup
<ul>
  {% for purchase_order in member.purchase_orders %}
    <li>{{ purchase_order.name }}</li>
  {% endfor %}
</ul> 
```

#### Output

```
• Sub-rental
• Sub-contract service
```

## `purchase_tax_class_name`

Returns the purchase tax class name against an organization.

#### Input

```
{{ member.purchase_tax_class_name }}
```

#### Output

```
Default
```

## `rating` 

Returns a number 0-5 for the star rating against an organization. Typically used to print a star rating. 

#### Input

```markup
Member rating: {{ member.rating }}<br>
{% for i in (1..member.rating) %}
  ⭑
{% endfor %}
```

#### Output

```
Member rating: 4
⭑ ⭑ ⭑ ⭑
```

## `sale_tax_class_name`

Returns the sale tax class name against an organization.

#### Input

```
{{ member.sale_tax_class_name }}
```

#### Output

```
Default
```

## `tax_class_name`

> **Important:**
> **Depreciated.** Support may be withdrawn in future.

See: [`sale_tax_class_name`](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md#sale_tax_class_name) .

## `tax_number` 

Returns the tax number against an organization.

#### Input

```
{{ member.tax_number }} 
```

#### Output

```
GB123456
```

## `telephone`

Returns an orgnaization's telephone. The first telephone number with the type “work” is returned.

#### Input

```
{{ member.telephone }}
```

#### Output

```
(636) 555 0113
```

## `thumbnail_icon_url` 

Returns a URL pointing at the organization's picture. A thumbnail size image is returned.

#### Input

```
{{ member.thumbnail_icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `transactions` 

Returns invoice transaction objects for transactions against invoices for an organization.

#### Input

```
{% for transaction in member.transactions %}
  {{ transaction.amount }}<br>
{% endfor %}
```

#### Output

```
100
20
```

---
*Source: [Organization — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)*
