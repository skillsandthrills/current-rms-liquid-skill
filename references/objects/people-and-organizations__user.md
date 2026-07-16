# User

All users have member records in People & Organizations. You may set contact information and add other details to user records -- useful for pulling contact details through to documents.

### Members

Contacts, organizations, vehicles, venues, and users are all known as members in the database. Members have some shared attributes, along with attributes that are specific to that particular member type.

When you're checking a list of members, you can use the type object to determine what type of member you're working with. 

For example, the participants object against an opportunity returns participant objects for any members who are participants on the opportunity. To print only users:

```
<ul>
  {% for participant in order.participants %}
    {% if participant.type == "User" %}
      <li>{{ participant.name }}</li>
    {% endif %}
  {% endfor %}
</ul>
```

### Objects that return users

In most documents and discussion templates, you may use:

#### `current_user`

Returns information about the logged-in user.

```
{{ current_user.name }}
```

#### `owner_user`

Returns information about the owner user of a record:

```
{{ owner_user.name }}
```

### Document layouts

The `user` object can be accessed in document layouts created against the following modules:

#### Member

From a user record:

```
{{ member.name }}
```

#### Opportunity

To print users that are a participant against an opportunity: 

```
{% for participant in order.participants %}
  {% if participant.type == "User" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print users that are sub-contract suppliers for service bookings:

```
{% for item in order.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "User" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print users that are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "User" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

To print information about the user who authorized a purchase order:

```
{{ authoriser.name }}
```

### Discussion templates

The `user` object can be accessed in discussion templates created against the following modules:

#### Member

From a venue record:

```
{{ user.name }}
```

#### Opportunity

To print users that are a participant against an opportunity: 

```
{% for participant in opportunity.participants %}
  {% if participant.type == "User" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

To print users that are sub-contract suppliers for service bookings:

```
{% for item in opportunity.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "User" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

#### Project

To print users that are a participant against a project: 

```
{% for participant in project.participants %}
  {% if participant.type == "User" %}
    {{ participant.name }}
  {% endif %}
{% endfor %}
```

#### Purchase order

To print information about the user who authorized a purchase order:

```
{{ authoriser.name }}
```

## `activities` <a href="#activities" id="activities"></a>

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to a user.

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

## `address` <a href="#address" id="address"></a>

Returns a user's primary address.

#### Input <a href="#input-1" id="input-1"></a>

```
{{ member.address }}
```

#### Output <a href="#output" id="output"></a>

```
882 Broderick Flats Lake Erlingchester MA 67553-4548
```

## `address_detail` <a href="#address_detail" id="address_detail"></a>

Returns address objects for a user's primary address.

#### Input <a href="#input-2" id="input-2"></a>

```
{{ member.address_detail.state }}
```

#### Output <a href="#output-1" id="output-1"></a>

```
MA
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `attachments` <a href="#attachments" id="attachments"></a>

Returns attachment objects for attachments stored against a user.

#### Input <a href="#input-2-1" id="input-2-1"></a>

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

## `description` <a href="#description" id="description"></a>

Returns a user's description.

#### Input <a href="#input-4" id="input-4"></a>

```
{{ member.description }}
```

#### Output <a href="#output-4" id="output-4"></a>

```
I mean it's one banana Michael. What could it cost, $10?
```

## `email` <a href="#email" id="email"></a>

Returns the first work email address stored against a user.

#### Input <a href="#input-5" id="input-5"></a>

```
{{ member.email }}
```

#### Output <a href="#output-5" id="output-5"></a>

```
dennis@wolfcola.com
```

## `emails` <a href="#emails" id="emails"></a>

Returns email objects for email addresses stored against a user.

#### Input <a href="#input-6" id="input-6"></a>

```
{% for email in member.emails %}
  {{ email.address }}
{% endfor %}
```

#### Output <a href="#output-6" id="output-6"></a>

```
help@current-rms.com
```

See: [Emails](https://current-rms.gitbook.io/liquid-syntax/general/email.md)

## `icon_url` <a href="#icon_url" id="icon_url"></a>

Returns a URL pointing at the user's picture. The full size image is returned.

#### Input <a href="#input-7" id="input-7"></a>

```
{{ member.icon_url }}
```

#### Output <a href="#output-7" id="output-7"></a>

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `image_attachments` <a href="#image_attachments" id="image_attachments"></a>

Returns attachment objects for attachments stored against a user. Only returns those that have a file type of image.

#### Input <a href="#input-2-2" id="input-2-2"></a>

```
{% for attachment in member.attachments %}
  {{ attachment.attachment_url }}
{% endfor %}
```

#### Output <a href="#output-2-1" id="output-2-1"></a>

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `id` <a href="#id" id="id"></a>

Returns a user's ID.

The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input <a href="#input-8" id="input-8"></a>

```
{{ member.id }}
```

#### Output <a href="#output-8" id="output-8"></a>

```
10
```

## `lawful_basis_type_id`  <a href="#lawful_basis_type_id" id="lawful_basis_type_id"></a>

Returns the legal basis type ID for a user.

| Type    | Legal basis type                        |
| ------- | --------------------------------------- |
| `11001` | Legitimate interest - prospect          |
| `11002` | Legitimate interest - existing customer |
| `11003` | Performance of a contract               |
| `11004` | Freely given consent                    |
| `11005` | Employee                                |
| `11006` | Unknown                                 |

#### Input <a href="#input-9" id="input-9"></a>

```
{{ member.lawful_basis_type_id }}
```

#### Output <a href="#output-9" id="output-9"></a>

```
11005
```

## `lawful_basis_type_name` <a href="#lawful_basis_type_name" id="lawful_basis_type_name"></a>

Returns a user's legal basis type name.

You may add legal basis types in System Setup > List of Values.

*  Legitimate interest - prospect
* Legitimate interest - existing customer
* Performance of a contract
* Freely given consent
* Employee
* Unknown

#### Input <a href="#input-10" id="input-10"></a>

```
{{ member.lawful_basis_type_name }}
```

#### Output <a href="#output-10" id="output-10"></a>

```
Employee
```

## `live_purchase_orders`  <a href="#live_purchase_orders" id="live_purchase_orders"></a>

Returns purchase order objects for purchase orders against a user. Only live purchase orders are returned.

#### Input <a href="#input-11" id="input-11"></a>

```
<ul>
  {% for purchase_order in member.live_purchase_orders %}
    <li>{{ purchase_order.name }}</li>
  {% endfor %}
</ul> 
```

#### Output <a href="#output-11" id="output-11"></a>

```
• Sub-contract service
```

## `mobile` <a href="#mobile" id="mobile"></a>

Returns a user's cell phone number. The first telephone number with the type “cell” or “mobile” is returned.

#### Input <a href="#input-14" id="input-14"></a>

```
{{ member.mobile }}
```

#### Output <a href="#output-14" id="output-14"></a>

```
(756) 555 1939
```

## `name` <a href="#name" id="name"></a>

Returns a user's name.

#### Input <a href="#input-15" id="input-15"></a>

```
{{ member.name }}
```

#### Output <a href="#output-15" id="output-15"></a>

```
Dennis Reynolds
```

## `phones` <a href="#phones" id="phones"></a>

Returns telephone objects for telephone numbers stored against a user.

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

## `telephone` <a href="#telephone" id="telephone"></a>

Returns a user's telephone. The first telephone number with the type “work” is returned.

#### Input <a href="#input-18" id="input-18"></a>

```
{{ member.telephone }}
```

#### Output <a href="#output-18" id="output-18"></a>

```
(636) 555 0113
```

## `title` <a href="#title" id="title"></a>

Returns a user's title.

#### Input <a href="#input-19" id="input-19"></a>

```
{{ member.title }}
```

#### Output <a href="#output-19" id="output-19"></a>

```
Executive Vice President of Worldwide Distribution
```

---
*Source: [User — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md)*
