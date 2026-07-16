# Activity

[Activities](https://help.current-rms.com/activities-and-calendars/whats-an-activity) are created regarding records in Current RMS, for example regarding an organization in People & Organizations or regarding an opportunity. Use the activity object to access activities related to a record on a document layout or discussion template.

Current automatically creates activities for contacts, users, vehicles, and venues when they are [allocated to a service booking](https://intercom.help/current-rms/opportunities/labor-management-the-services-view/what-is-the-services-view) on an opportunity. These activities are created with the type “Task” and are regarding the opportunity that the service booking is on. 

### Objects that return activities

Activity objects are always accessed within a forloop that iterates for each activity. You may use:

#### `activities`

Returns all activities. For example, from a member document layout:

```
{% for activity in member.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### `pending_activities`

Returns activities that are pending, i.e. not completed. For example, from a member document layout:

```
{% for activity in member.pending_activities %}
  {{ activity.subject }}
{% endfor %}
```

#### `service_activities`

Returns automatically created service booking activities. For example, from a member document layout:

```
{% for activity in member.service_activities %}
  {{ activity.subject }}
{% endfor %}
```

Service booking activities are only created for contacts, users, vehicles, and venues so the `service_activities` forloop will only return activities for document layouts or discussion templates created against these modules.

### Document layouts

The `activity` object can be accessed in document layouts created against the following modules:

#### Member

```
{% for activity in member.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### Opportunity

```
{% for activity in order.activities %}
  {{ activity.subject }}  
{% endfor %}
```

#### Quarantine

```
{% for activity in quarantine.activities %}
  {{ activity.subject }}
{% endfor %}
```

### Discussion templates

The `activity` object can be accessed discussion templates created against the following modules:

#### Organization

```
{% for activity in organisation.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### Contact

```
{% for activity in contact.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### User account

```
{% for activity in user.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### Venue

```
{% for activity in venue.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### Opportunity

```
{% for activity in opportunity.activities %}
  {{ activity.subject }}
{% endfor %}
```

#### Quarantine

```
{% for activity in quarantine.activities %}
  {{ activity.subject %}
{% endfor %}
```

## `activity_status_name` 

Returns the activity status name. 

* Canceled
* Concluded
* Postponed
* Scheduled

#### Input

```
{{ activity.activity_status_name }}
```

#### Output

```
Scheduled
```

## `activity_type_name`

Returns the activity type name.

* Call
* Email
* Fax
* Holiday
* Letter
* Meeting
* Task

#### Input

```
{{ activity.activity_type_name }}
```

#### Output

```
Call
```

## `completed?`

Returns true if the activity is completed; false otherwise.

#### Input

```
{{ activity.completed? }}
```

#### Output

```
false
```

## `completed_at`

Returns the date and time that the activity was completed.

#### Input

```
{{ activity.completed_at }}
```

#### Output

```
2021-02-07 16:00:00 +0000
```

## `description`

Returns the activity description. 

For service booking activities, the order description and the related opportunity item description are pulled through.

#### Input

```
{{ activity.description }}
```

#### Output

```
Please give this lovely customer a call to collect feedback on the their last booking.
```

## `ends_at`

Returns the date and time that the activity ends.

#### Input

```
{{ activity.ends_at }}
```

#### Output

```
2021-04-24 16:00:00 +0100
```

## `for_service?`

Returns true if the activity is for a service booking; false otherwise.

#### Input

```
{{ activity.for_service? }}
```

#### Output

```
false
```

## `location` 

Returns the value of the activity’s “location” field.

For service booking activities, the opportunity delivery address is set as the location.

#### Input

```
{{ activity.location }}
```

#### Output

```
Conference Room B
```

## `opportunity_item` 

Returns opportunity item objects for activities that are automatically created for service bookings. The objects relate to the opportunity item for the service booking. 

#### Input

```
{{ activity.opportunity_item.description }}
```

#### Output

```
Setup of the kit.
```

See: [Opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md)

## `opportunity_item_asset`

Returns opportunity item asset objects for activities that are automatically created for service bookings. The objects relate to the opportunity item asset for the service booking. 

#### Input

```
{{ activity.opportunity_item_asset.status_name }}
```

#### Output

```
Confirmed
```

See: [Opportunity item assets](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-item-assets.md)

## `owner`

Returns [user objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md) with information about the user who owns the purchase order.

#### Input

```
{{ activity.owner.name }}
```

#### Output

```
Michael McGovern
```

See: [User](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md)

## `participants`

Returns [contact](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md), [organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md), [user](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md), [vehicle](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/vehicle.md), or [venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md) objects for participants of the activity.

#### Input

```
{% for participant in activity.participants %}
  {{ participant.name }} - {{ participant.type }}
{% endfor %}
```

#### Output

```
Michael McGovern - Contact
```

See: [People & Organizations](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md)

## `priority`

Returns a number 1-5 for the activity’s priority. 1 is one star; 5 is five stars.

#### Input

```
Priority: {{ activity.priority }}<br>
{% for i in (1..activity.priority) %}
  ⭑
{% endfor %}
```

#### Output

```
3
⭑ ⭑ ⭑
```

## `regarding`

Returns objects for the record that the activity is regarding. This may be:

* Organization
* Contact
* User
* Venue
* Vehicle
* Product
* Service
* Quarantine
* Purchase order 

#### Input

```
{{ activity.regarding.name }}
```

#### Output

```
Happy Ever After Wedding Planners
```

## `starts_at`

Returns the date and time that the activity starts.

#### Input

```
{{ activity.starts_at }}
```

#### Output

```
2021-04-24 14:00:00 +0100
```

## `subject`

Returns the activity subject.

#### Input

```
{{ activity.subject }}
```

#### Output

```
Feedback call
```

## `time_status_name`

Returns the activity time status.

* Free
* Busy

#### Input

```
{{ activity.time_status_name }}
```

#### Output

```
Free
```

---
*Source: [Activity — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/activity/activity.md)*
