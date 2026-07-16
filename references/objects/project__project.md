# Project

Projects are like a folder for opportunities. They're useful for things like festivals, roadshows, and jobs with multiple areas.

### Project quotation

The standard project document that comes with Current RMS is a project quotation. This returns projects in the opportunity that are quotations. It won’t return inquiries, drafts, or orders.

This is because the document uses the `project.quotations` drop. If you like, you can change this to:

* `project.enquiries`, to return inquiries;
* `project.drafts`, to return drafts;
* `project.orders`, to return orders;
* `project.opportunities`, to return all opportunities.

When using `project.opportunities`, you may wish to filter by opportunity [`status`](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity.md#status) to exclude lost, dead, postponed, or canceled opportunities.

### Opportunity ordering

Opportunities on a project document are returned in no particular order. They're displayed in the order that they're returned from our servers.

You may use [the sort filter](https://current-rms.gitbook.io/liquid-syntax/introduction/liquid-filters.md) to sort an array that returns opportunities by an opportunity attribute. For example, to sort by start date:

```
{% assign sorted_opportunities = project.quotations | sort:"starts_at" %}
<ul>
  {% for order in sorted_opportunities %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

> **Warning:**
> If you try to filter by an attribute that's optional and that attribute is blank, you may get an error message.

### Project totals

Total objects against a project return totals for all opportunities on the project:

* `charge_excluding_tax_total`
* `charge_including_tax_total`
* `charge_total`
* `tax_total`
* `sale_charge_tax_total`
* `rental_charge_total`
* `service_charge_total`
* `surcharge_total`

Project documents tend not to return all opportunities on the project. They'll usually return just quotations or just orders. In this case, printing totals for all opportunities in the project isn't useful.

Use variables to sum the total of opportunities printed on a document. For example, from our standard project document: 

```markup
<!-- Setup total variables -->
{% assign rental_charge_total = 0 %}
{% assign sale_charge_total = 0 %}
{% assign service_charge_total = 0 %}
{% assign charge_excluding_tax_total = 0 %}
{% assign tax_total = 0 %}
{% assign charge_including_tax_total = 0 %}
{% assign deal_exists = false %}

<!-- Accumulate order totals -->
{% for order in project.quotations %}
  {% assign rental_charge_total = rental_charge_total | plus:order.rental_charge_total | plus:order.surcharge_total %}
  {% assign sale_charge_total = sale_charge_total | plus:order.sale_charge_total %}
  {% assign service_charge_total = service_charge_total | plus:order.service_charge_total %}
  {% assign charge_excluding_tax_total = charge_excluding_tax_total | plus:order.charge_excluding_tax_total %}
  {% assign tax_total = tax_total | plus:order.tax_total %}
  {% assign charge_including_tax_total = charge_including_tax_total | plus:order.charge_including_tax_total %}
  {% if order.deal_exists? == true %}
    {% assign deal_exists = true %}
  {% endif %}
{% endfor %}

<!-- Print order totals -->
<table class="table closing-totals">
  <tbody>
    <tr>
      <td class="fixed-col">
        {% if deal_exists == false %}
          <p><strong>Rental charges</strong><br></p>
          <p><strong>Sale charges</strong><br></p>
          <p><strong>Service charges</strong><br></p>
        {% endif %}
      </td>
      <td class="align-right" style="padding-right: 30px;">
        {% if deal_exists == false %}
          <p><strong>{{ rental_charge_total | currency }}</strong><br></p>
          <p><strong>{{ sale_charge_total | currency }}</strong><br></p>
          <p><strong>{{ service_charge_total | currency }}</strong><br></p>
        {% endif %}
      </td>
      <td class="fixed-col" style="padding-left: 30px;">
        <p><strong>Charge total</strong><br></p>
        <p><strong>Tax total</strong><br></p>
        <p><strong>Charge and tax total</strong><br></p>
      </td>
      <td class="align-right">
        <p><strong>{{ charge_excluding_tax_total | currency }}</strong><br></p>
        <p><strong>{{ tax_total | currency }}</strong><br></p>
        <p><strong>{{ charge_including_tax_total | currency }}</strong><br></p>
      </td>
    </tr>
  </tbody>
</table>
```

### Document layouts

The `project` object can be accessed in document layouts created against the following modules:

#### Project

```
{{ project.name }}
```

#### Opportunity

```
{{ order.project.name }}
```

### Discussion templates

The `project` object can be accessed in discussion templates created against the following modules:

#### Project

```
{{ project.name }}
```

#### Opportunity

```
{{ opportunity.project.name }}
```

## `attachments`

Returns attachment objects for attachments stored against a project.

#### Input

```
{% for attachment in project.attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `billing_address`

Returns the project billing address.

#### Input

```
{{ project.billing_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `billing_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/general/address) for the billing address against the project.

#### Input  <a href="#input-5" id="input-5"></a>

```
{{ project.billing_address_detail.state }}
```

#### Output  <a href="#output-5" id="output-5"></a>

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `billing_address_name`

Returns the name of the billing address against the project.

#### Input

```
{{ project.delivery_address_name }}
```

#### Output

```
Omni Consumer Products
```

## `charge_excluding_tax_total`

Returns the project charge total excluding tax.

#### Input

```
{{ project.charge_excluding_tax_total }}
```

#### Output

```
4500.0
```

## `charge_including_tax_total`

Returns the project charge total including tax.

#### Input

```
{{ project.charge_including_tax_total }}
```

#### Output

```
5500.0
```

## `charge_total`

Returns the project charge total.

This may be including or excluding tax depending on the value of the “Catalog Prices” setting in System Preferences.

#### Input

```
{{ project.charge_total }}
```

#### Output

```
4500.0
```

## `consolidated_items`

Returns a list of consolidated opportunity items for all opportunities in the project

See: [Consolidated opportunity items](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunity-items.md)

## `consolidated_opportunities`

Returns a list of opportunities in a project with the same start and end date and time. 

See: [Consolidated opportunities](https://current-rms.gitbook.io/liquid-syntax/opportunities/consolidated-opportunities.md)

## `customer`

Returns organization objects for the organization against the project.

#### Input

```
{{ customer.name }}
```

#### Output

```
Bluth Company
```

See: [Organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md)

## `delivery_address`

Returns the project delivery address.

#### Input

```
{{ project.delivery_address }}
```

#### Output

```
0470 Conn Throughway North Meda MN 03899-1584
```

## `delivery_address_detail`

Returns [address objects](https://current-rms.gitbook.io/liquid-syntax/general/address.md) for the delivery address against the project.

#### Input 

```
{{ project.delivery_address_detail.state }}
```

#### Output 

```
QLD
```

See: [Address detail](https://current-rms.gitbook.io/liquid-syntax/general/address.md)

## `delivery_address_name`

Returns the name of the delivery address against the project.

#### Input

```
{{ project.delivery_address_name }}
```

#### Output

```
Seaview Convention Center
```

## `description`

Returns the project description.&#x9;

#### Input

```
{{ project.description }}
```

#### Output

```
Every event is special, so we're here to make sure that it all runs smoothly.
```

## `drafts`

Returns opportunity objects for opportunities in the project that are drafts.

#### Input

```
<ul>
  {% for order in project.drafts %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Omni Consumer Products Launch
• Demo Space
```

## `ends_at`

Returns the end date and time for the project.

#### Input

```
{{ project.ends_at }}
```

#### Output

```
2021-04-12 16:00:00 +0000 
```

## `enquiries`

Returns opportunity objects for opportunities in the project that are inquiries.

#### Input

```
<ul>
  {% for order in project.enquiries %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Omni Consumer Products Launch
• Demo Space
```

## `icon_url`

Returns a URL pointing at the project's image.

#### Input

```
<img src="{{ project.icon_url }}">
```

#### Output

```
<img src="https://s3.amazonaws.com/cobra-ca9a7ac0-2539-0131-ba41-0050569ba36f/icons/233/original/icon.png">
```

## `id`

Returns the project ID.

> **Warning:**
> The ID is an internal reference for a record. It's not exposed in our web interface. Projects don't have an order number.

#### Input

```
{{ project.id }}
```

#### Output

```
1
```

## `image_attachments`

Returns attachment objects for attachments stored against a project where the attachment file type is an image.

#### Input  <a href="#input" id="input"></a>

```
{% for attachment in project.image_attachments %}
  {{ attachment.name }}
{% endfor %}
```

#### Output  <a href="#ouput" id="ouput"></a>

```
Ann Veal
```

See: [Attachments](https://current-rms.gitbook.io/liquid-syntax/general/attachments.md)

## `name`

Returns the project subject.

#### Input

```
{{ project.name }}
```

#### Output

```
V-Blast Music Festival
```

## `opportunities`

Returns opportunity objects for opportunities in the project.

> **Note:**
> All opportunities are returned, regardless of state or status.

#### Input

```
<ul>
  {% for order in project.opportunities %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Omni Consumer Products Launch
• Demo Space
```

## `orders`

Returns opportunity objects for opportunities in the project that are orders.

#### Input

```
<ul>
  {% for order in project.orders %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Omni Consumer Products Launch
• Demo Space
```

## `owner`

Returns [user objects](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md) with information about the user who owns the project.

#### Input

```
{{ project.owner.name }}
```

#### Output

```
Michael McGovern
```

See: [User](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md)

## `participants`

Returns [contact](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/contact.md), [organization](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/organization.md), [user](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/user.md), [vehicle](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/vehicle.md), or [venue](https://current-rms.gitbook.io/liquid-syntax/people-and-organizations/venue.md) objects for participants on the opportunity.

#### Input

```
{% for participant in order.participants %}
  {{ participant.name }} - {{ participant.type }}
{% endfor %}
```

#### Output

```
Michael McGovern - Contact
```

## `project_invoicing`

Returns `true` if Project Invoicing is enabled; `false` otherwise.

#### Input

```
{{ project.project_invoicing }}
```

#### Output

```
true
```

## `quotations`

Returns opportunity objects for opportunities in the project that are quotations.

#### Input

```
<ul>
  {% for order in project.quotations %}
    <li>{{ order.name }}</li>
  {% endfor %}
</ul>
```

#### Output

```
• Omni Consumer Products Launch
• Demo Space
```

## `reference`

Returns the value of the project customer reference.

#### Input

```
{{ project.reference }}
```

#### Output

```
PO-1099
```

## `rental_charge_total`

Returns the rental charge total for a project.

> **Warning:**
> [Opportunity item](https://current-rms.gitbook.io/liquid-syntax/opportunities/opportunity-items.md) charge totals include surcharges, but the project and opportunity rental charge total object does not. You may wish to add the surcharge total object (below) to the rental charge total.

#### Input

```
{{ project.rental_charge_total }}
```

#### Output

```
803.39
```

## `sale_charge_total`

Returns the sale charge total for a project.

#### Input

```
{{ project.sale_charge_total }}
```

#### Output

```
213.99
```

## `service_charge_total`

Returns the service charge total for a project.

#### Input

```
{{ project.service_charge_total }}
```

#### Output

```
10290.4
```

## `starts_at`

Returns the start date and time for the project. 

#### Input

```
{{ project.starts_at }}
```

#### Output

```
2021-04-12 10:00:00 +0000
```

## `store`

Returns [store objects](https://current-rms.gitbook.io/liquid-syntax/-LbblMS9-6hRM3IRplGC/general/store) for the store against the project.

#### Input <a href="#input-27" id="input-27"></a>

```
{{ project.store.name }}
```

#### Output <a href="#output-26" id="output-26"></a>

```
The Banana Stand
```

See: [Store](https://current-rms.gitbook.io/liquid-syntax/general/store.md)

## `surcharge_total`

Returns the surcharge total for a project. 

This isn't returned in the rental charge total object.

#### Input

```
{{ order.surcharge_charge_total }}
```

#### Output

```
803.39
```

## `tax_class_name`

Returns the project tax class.

This may differ from the organization tax class.

#### Input

```
{{ project.tax_class_name }}
```

#### Output

```
Default
```

## `tax_total`

Returns the project tax total.

#### Input

```
{{ project.tax_total }}
```

#### Output

```
100.0
```

## `venue`

Returns venue objects for the venue against the project.

> **Warning:**
> A project delivery address can be a venue, but a venue might not always be a project's delivery address. If you don't choose a venue when creating an project, using `{{ project.venue.name }}` won't return the same as `{{ project.delivery_address_name }}`.

#### Input

```
{{ order.venue.name }}
```

#### Output

```
Seaview Conference Center
```

---
*Source: [Project — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/project/project.md)*
