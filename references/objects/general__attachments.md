# Attachments

You can upload attachments against nearly all records in Current RMS. They're generally used for files that are associated with a record, for example:

* PowerPoint presentations, configuration files, or information sheets related to an opportunity.
* Floor plans or photographs associated with a venue
* Photographs of damaged goods for a quarantine.

Remember that when using the `attachments` object, you can include images but you can't embed other kinds of files into a document layout or discussion template. Instead, you can hyperlink to link to them.

> **Important:**
> Attachments may contain commercially sensitive information, so be sure that you’re not inadvertently sharing attachments that you don't mean to on a document layout or discussion template.

### Example

Here’s an example document that prints attachments for an opportunity.

{% file src="/files/-Lk91hPOwwo7EitEahvB" %}
Example opportunity attachments
{% endfile %}

### Objects that return attachments

Attachments can be accessed for the following objects:

* Activity
* Invoice
* Contact
* Opportunity
* Opportunity cost
* Product
* Project
* Purchase order 
* Quarantine
* Service
* Stock level 
* User
* Vehicle
* Venue

Attachment objects are always accessed within a forloop that iterates for each attachment. You may use:

#### `attachments`

Returns all attachments. For example, from an opportunity document layout:

```
{% for attachment in order.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### `image_attachments`

Returns attachments that are images, useful for printing pictures associated with an opportunity For example, from an opportunity document layout:

```
{% for attachment in order.image_attachments %}
  {{ attachment.name }}
{% endfor %}
```

### Document layouts 

The `attachments` object can be accessed in document layouts created against the following modules:

* Invoice
* Opportunity
* Project
* Product
* Quarantine
* Member
* Purchase order

### Discussion templates

The `attachments` object can be accessed discussion templates created against the following modules:

* Organization
* Contact
* User account
* Venue
* Activity
* Invoice
* Opportunity
* Project
* Product
* Service
* Quarantine
* Purchase order

## `attachment_content_type`

Returns the content type for an attachment.

#### Input

```
{{ attachment.attachment_content_type }}
```

#### Output

```
image/jpeg
```

## `attachment_file_name`

Returns the file name for an attachment. This is the original name of the file uploaded, including the extension. 

#### Input

```
{{ attachment.attachment_file_name }}
```

#### Output

```
Ann_Veal.jpg
```

## `attachment_file_size`

Returns the file size for an attachment. The output is in bytes.

#### Input

```
{{ attachment.attachment_file_size }}
```

#### Output

```
656873
```

> **Note:**
> Use a [math filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md#maths-filters) to convert to kilobytes or megabytes.

## `attachment_thumb_url`

Returns the thumbnail URL for an attachment that's an image; blank otherwise. 

Thumbnails are square images, 64x64px.

#### Input

```
{{ attachment.attachment_thumb_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/thumb/Ann_Veal.jpg
```

## `attachment_url`

Returns the full URL for an attachment.

#### Input

```
{{ attachment.attachment_url }}
```

#### Output

```
https://s3.amazonaws.com/current-rms/f7b92d60-1421-0132-8004-0401207f6801/attachments/473/original/Ann_Veal.jpg
```

## `description`

Returns the value of the description field against an attachment. You can specify this when creating or editing an attachment in the web interface.

#### Input

```
{{ attachment.description }}
```

#### Output

```
Third place winner of the Miss Inner Beauty pageant.
```

## `name`

Returns the name of an attachment. This is the name entered in the "Name" field in the web interface, not the file name.

#### Input

```
{{ attachment.name }}
```

#### Output

```
Egg
```

---
*Source: [Attachments — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)*
