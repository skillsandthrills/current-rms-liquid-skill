# PDF document limitations

When you download to PDF, we use some software to convert your HTML to a PDF. Converting HTML content to PDF generally goes smoothly and most folks won’t notice any problems at all. 

There are a few limitations that more advanced web developers might encounter.

## Target the browser preview

The body of the document layout preview in the browser has an ID of `print_preview` , meaning you can create styles that only target the browser preview and not the PDF. This is handy if you use document approval more often than not.

For example, to set a custom font to show in the preview but not the PDF, use:

```
body#print_preview {
  font-family: "Open Sans", sans-serif;
}
```

The PDF doesn’t have a body ID of `print_preview`, so it’ll be safely ignored.

Use [the `:not` pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/:not) to work the other way around. For example, to set a custom font to show in the PDF but not in the preview, use:

```
body:not(#print_preview) {
  font-family: "Open Sans", sans-serif;
}
```

Use display properties to hide or show content on the PDF or browser preview.

## Custom font kerning and spacing issues

Since Current RMS is a web application, fonts used in your documents must be web fonts. [Google Fonts](https://fonts.google.com/) is a great source of web fonts. 

Our PDF rendering software doesn’t always work correctly with web fonts and you might notice issues with font kerning or spacing. 

Here’s an example of [Open Sans](https://fonts.google.com/specimen/Open+Sans), notice the letter spacing and kerning:

We’ve investigated this and we’re not too sure what the cause is. Adjusting kerning or letter spacing in CSS doesn’t make a difference. It’s likely that the problem lies with a third-party component used by our PDF rendering software.

Before selecting a font, we recommend testing fonts by adding them a document and previewing to PDF.

## Fix content to the bottom of the body section

If you’re used to creating quotations or invoices in word processors, it’s fairly straightforward to float content to the bottom of the page. This is because you’re working with known content, so you can position things exactly where you like.

Similarly, if you're a web developer then you know you can fix content to the bottom of the window. 

Documents in Current RMS use dynamically generated content, so the information on them might fit on one page or might span multiple pages. 

For this reason, there’s no way to float content to the bottom of the body section. 

Remember the header and footer are repeated on each page, so you can include information like page numbers at the bottom of each page – it’s just floating content to the bottom of one particular page that’s a problem.

## Different headers and footers on different pages

All documents in Current RMS are made up of header, body, and footer content.

* **Header**\
  Code here appears above the top margin of the document and is repeated on each page when printed to PDF.
* **Body**\
  Code here is placed between the margins of the document. This is where your main content should go.
* **Footer**\
  Code here appears below the bottom margin of the document and is repeated on each page when printed to PDF.

The header and footer content will repeat on every page. There’s no way to prevent this from happening, so it’s worth bearing in mind if you’re looking to build cover pages or would like documents with different headers across pages.

Keep in mind that PDFs that you attach to document layouts and are merged during PDF generation will not include the header or footer.

## HTML and CSS properties not supported

* CSS flexbox
* CSS columns
* CSS columns
* CSS animations (of course!)
* Embedded content like maps or iframes

If a CSS property isn't working as expected, try using vendor prefixes on the impacted CSS. Use [Autoprefixer](https://autoprefixer.github.io/) and set the filter to `Chrome >= 13`.

---
*Source: [PDF document limitations — Current RMS Liquid docs](https://current-rms.gitbook.io/liquid-syntax/pdf-renderer/pdf-generator.md)*
