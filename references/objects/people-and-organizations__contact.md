# Contact

[Contacts](https://help.current-rms.com/en/articles/448900-create-a-contact) in Current RMS are generally used for storing information about people who work at an organization or venue.

They're also commonly bookable resources for freelancers or staff members.

You may raise purchase orders with contacts whose location type is "External". You can't raise invoices against contacts.

### Members

Contacts, organizations, vehicles, venues, and users are all known as members in the database. Members have some shared attributes, along with attributes that are specific to that particular member type.

When you're checking a list of members, you can use the type object to determine what type of member you're working with. 

For example, the participants object against an opportunity returns participant objects for any members who are participants on the opportunity. To print only contacts:

```
<ul>
  {% for participant in order.participants %}
    {% if participant.type == "Contact" %}
      <li>{{ participant.name }}</li>
    {% endif %}
  {% endfor %}
</ul>
```

### Document layouts

The `contact` object can be accessed in document layouts created against the following modules:

#### Member

From a contact record:

```
{{ member.name }}
```

From an organization record:

```
{% for contact in member.contacts %}
  {{ contact.name }}
{% endfor %}
```

From a venue record:

```
{% for contact in member.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Opportunity

To print contacts who are a participant against an opportunity: 

```
{% for participant in order.participants %}
  {% if participant.type == "Contact" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print contacts against an opportunity's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

To print contacts who are are bookable resources for service items:

```
{% for item in order.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Contact" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print contacts who are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "Contact" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print contacts against a project's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Purchase order

Where the supplier is a contact:

```
{{ supplier.name }}
```

To print contacts against a purchase order's related organization: 

```
{% for contact in supplier.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Invoice

To print contacts against an invoice's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Activity

To print information about contacts that are participants against an activity:

```
{% for participant in activity.participants %}
  {% if participant.type == "Contact" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

### Discussion templates

The `contact` object can be accessed in discussion templates created against the following modules:

#### Member

From a contact record:

```
{{ contact.name }}
```

From an organization record:

```
{% for contact in organisation.contacts %}
  {{ contact.name }}
{% endfor %}
```

From a venue record:

```
{% for contact in venue.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Opportunity

To print contacts who are a participant against an opportunity: 

```
{% for participant in opportunity.participants %}
  {% if participant.type == "Contact" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print contacts against an opportunity's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

To print contacts who are are bookable resources for service items:

```
{% for item in opportunity.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Contact" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print contacts who are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "Contact" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print contacts against a project's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Purchase order

Where the supplier is a contact:

```
{{ supplier.name }}
```

To print contacts against a purchase order's related organization: 

```
{% for contact in supplier.contacts %}
  {{ contact.name }}
{% endfor %}
```

#### Invoice

To print contacts against an invoice's related organization: 

```
{% for contact in customer.contacts %}
  {{ contact.name }}
{% endfor %}
```

## `activities`

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to a contact.

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

Returns a contact's primary address.

#### Input

```
{{ member.address }}
```

#### Output

```
882 Broderick Flats Lake Erlingchester MA 67553-4548
```

## `address_detail`

Returns address objects for a contact's primary address.

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

Returns attachment objects for attachments stored against a contact.

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

## `department`

Returns a contact's department.

#### Input

```
{{ member.department }}
```

#### Output

```
Procurement
```

## `description`

Returns a contact's description.

#### Input

```
{{ member.description }}
```

#### Output

```
I mean it's one banana Michael. What could it cost, $10?
```

## `email`

Returns the first work email address stored against a contact.

#### Input

```
{{ member.email }}
```

#### Output

```
gob@bluthcompany.com
```

## `emails`

Returns email objects for email addresses stored against a contact.

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

Returns a URL pointing at the contact's picture. The full size image is returned.

#### Input

```
{{ member.icon_url }}
```

#### Output

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `image_attachments`

Returns attachment objects for attachments stored against a contact. Only returns those that have a file type of image.

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

Returns a contact's ID.

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

## `lawful_basis_type_id` 

Returns the legal basis type ID for a contact.

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

Returns a contact's legal basis type name.

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

## `live_purchase_orders` 

Returns purchase order objects for purchase orders against a contact. Only live purchase orders are returned.

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
• Sub-contract service
```

## `location_type` 

Returns a contact's location type ID.

| Type | Location type |
| ---- | ------------- |
| `0`  | Internal      |
| `1`  | External      |

#### Input

```
{{ member.location_type }}
```

#### Output

```
0
```

## `location_type_name`

Returns a contact's location type name.

* Internal
* External

#### Input

```
{{ member.location_type_name }}
```

#### Output

```
Internal
```

## `mobile`

Returns a contact's cell phone number. The first telephone number with the type “cell” or “mobile” is returned.

#### Input

```
{{ member.mobile }}
```

#### Output

```
(756) 555 1939
```

## `name`

Returns a contact's name.

#### Input

```
{{ member.name }}
```

#### Output

```
George Michael Bluth
```

## `organisations`

Returns organization objects for linked organizations against a contact.

#### Input

```
{% for organization in member.organisations %}
  {{ organization.name }}
{% endfor %}
```

#### Output

```
Bluth Company, Inc.
```

See: [Organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)

## `phones`

Returns telephone objects for telephone numbers stored against a contact.

#### Input <a href="#input-7-1" id="input-7-1"></a>

```
{% for telephone in member.phones %}
  {{ telephone.number }}
{% endfor %}
```

#### Output <a href="#output-7-1" id="output-7-1"></a>

```
(636) 555 0113
```

See: [Phones](https://current-rms.gitbook.io/liquid-syntax/general/telephone.md)

## `purchase_tax_class_name`

Returns the purchase tax class name against a contact.

#### Input

```
{{ member.purchase_tax_class_name }}
```

#### Output

```
Default
```

## `telephone`

Returns a contact's telephone. The first telephone number with the type “work” is returned. 

#### Input

```
{{ member.telephone }}
```

#### Output

```
(636) 555 0113
```

## `title`

Returns a contact's title.

#### Input

```
{{ member.title }}
```

#### Output

```
Head of Sales
```

## `venue`

Returns venue objects for linked venues against a contact.

#### Input

```
{% for venue in member.organisations %}
  {{ venue.name }}
{% endfor %}
```

#### Output

```
Peter Miller Manor
```

See: [Venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md)

---
*Source: [Contact — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)*
