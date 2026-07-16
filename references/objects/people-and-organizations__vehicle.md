# Vehicle

[Vehicles](https://help.current-rms.com/en/articles/457935-add-vehicles) are typically bookable resources for services. They live in Resources > Vehicles, but under the hood they're member records so share attributes with other objects in People & Organizations.

Vehicles have contact information against them because newer smart trucks for business have cell phone numbers and email addresses built into their trip computers. Some customers email PDFs or send messages with information about jobs to trucks.

### Members

Contacts, organizations, vehicles, venues, and users are all known as members in the database. Members have some shared attributes, along with attributes that are specific to that particular member type.

When you're checking a list of members, you can use the type object to determine what type of member you're working with. 

For example, the participants object against an opportunity returns participant objects for any members who are participants on the opportunity. To print only users:

```
<ul>
  {% for participant in order.participants %}
    {% if participant.type == "Vehicle" %}
      <li>{{ participant.name }}</li>
    {% endif %}
  {% endfor %}
</ul>
```

### Document layouts

The `vehicle` object can be accessed in document layouts created against the following modules:

#### Member

From a vehicle record:

```
{{ member.name }}
```

#### Opportunity

To print vehicles that are are bookable resources for service items:

```
{% for item in order.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Vehicle" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

### Discussion templates

The `vehicle` object can be accessed in discussion templates created against the following modules:

#### Member

From a vehicle record:

```
{{ vehicle.name }}
```

#### Opportunity

To print vehicles that are are bookable resources for service items:

```
{% for item in opportunity.services %}
  {% if item.is_item? %}
    {% for asset in item.assets %}
      {% if asset.is_resource_stock? %}
        {% if asset.resource.type == "Vehicle" %}
          {{ asset.resource.name }}
        {% endif %}
      {% endif %}
    {% endfor %}
  {% endif %}
{% endfor %}
```

## `activities` <a href="#activities" id="activities"></a>

Returns [activity objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/activity/activity) for the activities relating to a vehicle.

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

## `attachments` <a href="#attachments" id="attachments"></a>

Returns attachment objects for attachments stored against a vehicle.

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

Returns a vehicle's description.

#### Input <a href="#input-4" id="input-4"></a>

```
{{ member.description }}
```

#### Output <a href="#output-4" id="output-4"></a>

```
Our little nipper, perfect for small gear.
```

## `email` <a href="#email" id="email"></a>

Returns the first work email address stored against a vehicle.

#### Input <a href="#input-5" id="input-5"></a>

```
{{ member.email }}
```

#### Output <a href="#output-5" id="output-5"></a>

```
dennis@wolfcola.com
```

## `emails` <a href="#emails" id="emails"></a>

Returns email objects for email addresses stored against a vehicle.

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

## `height` <a href="#icon_url" id="icon_url"></a>

Returns a vehicle's height.

#### Input

```
{{ member.height }}
```

#### Output

```
100.0
```

## `icon_url` <a href="#icon_url" id="icon_url"></a>

Returns a URL pointing at the vehicle's picture. The full size image is returned.

#### Input <a href="#input-7" id="input-7"></a>

```
{{ member.icon_url }}
```

#### Output <a href="#output-7" id="output-7"></a>

```
https://s3.amazonaws.com/cobra-4934606a-294f-4fc2-bca1-2fd55ba5019c/icons/449/original/abigail.jpeg
```

## `image_attachments` <a href="#image_attachments" id="image_attachments"></a>

Returns attachment objects for attachments stored against a vehicle. Only returns those that have a file type of image.

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

Returns a vehicle ID.

> **Note:**
> The ID is an internal reference for a record. It's not exposed in our web interface.

#### Input <a href="#input-8" id="input-8"></a>

```
{{ member.id }}
```

#### Output <a href="#output-8" id="output-8"></a>

```
10
```

## `length`

Returns a vehicle's length.

#### Input

```
{{ member.length }}
```

#### Output

```
30.0
```

## `location_type` 

Returns a vehicle's location type ID.

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

Returns a vehicle's location type name.

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

## `mobile` <a href="#mobile" id="mobile"></a>

Returns a vehicle's cell phone number. The first telephone number with the type “cell” or “mobile” is returned.

#### Input <a href="#input-14" id="input-14"></a>

```
{{ member.mobile }}
```

#### Output <a href="#output-14" id="output-14"></a>

```
(756) 555 1939
```

## `name` <a href="#name" id="name"></a>

Returns a vehicle's name.

#### Input <a href="#input-15" id="input-15"></a>

```
{{ member.name }}
```

#### Output <a href="#output-15" id="output-15"></a>

```
Ford Pickup
```

## `payload` <a href="#phones" id="phones"></a>

Returns a vehicle's maximum payload.

#### Input

```
{{ member.payload }}
```

#### Output

```
700
```

> **Note:**
> Use `weight_unit` against [the company object](https://current-rms.gitbook.io/liquid-syntax/general/company.md) to print your system weight unit.

## `phones` <a href="#phones" id="phones"></a>

Returns telephone objects for telephone numbers stored against a vehicle.

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

## `plate` <a href="#telephone" id="telephone"></a>

Returns a vehicle's licence plate.

#### Input

```
{{ member.plate }}
```

#### Output

```
EXY-7946
```

## `telephone` <a href="#telephone" id="telephone"></a>

Returns a vehicle's telephone. The first telephone number with the type “work” is returned.

#### Input <a href="#input-18" id="input-18"></a>

```
{{ member.telephone }}
```

#### Output <a href="#output-18" id="output-18"></a>

```
(636) 555 0113
```

## `volume`

Returns a vehicle's volume.

#### Input

```
{{ member.volume }}
```

#### Output

```
36.0
```

## `width`

Returns a vehicle's width.

#### Input

```
{{ member.width }}
```

#### Output

```
100.0
```

---
*Source: [Vehicle — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/vehicle.md)*
