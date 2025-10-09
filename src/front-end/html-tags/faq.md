---
tags: html, accessibility, semantic web, web development, outsystems platform
summary: Learn how to generate semantic HTML tags in OutSystems 11 (O11) applications for enhanced accessibility using HTML Element and Container Widgets.
guid: 67cc20af-ffe8-4897-b817-28460ed3bd48
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:34
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to generate HTML tags

How can I generate HTML tags around elements of my Application?

For example: I am concerned with the accessibility of my Application and I want to apply heading styles in a way that provides semantic markup.

When I apply a heading style in Service Studio, the following HTML is generated:

    <span class="Heading1">Hello</span>

But I want to ensure semantic markup and use HTML heading tags instead:

    <h1>Hello</h1>
    
## Answer

To generate HTML tags around elements of your **Mobile App** and **Reactive Web App** use the **HTML Element** Widget and define the `Tag` Property. Note that the `Tag` Property must be a constant value.  Use the `Attributes` fields to define HTML attributes.

![Screenshot showing the HTML Element Widget with the Tag property set to 'h1' in Service Studio.](images/html-tags-00.png "HTML Element Widget in Service Studio")

To generate HTML tags around elements of your **Traditional Web Application** use a **Container** or **Placeholder** Widget and add `OSTagName` = `"<html_tag>"` as an `Extended Property`, where `<html_tag>` is the HTML tag you want to use. Note that the `OSTagName` `Extended Property` can be a constant or dynamic value. Use the `Extended Properties` fields to define HTML attributes.

![Screenshot displaying the Container Widget properties with the OSTagName Extended Property set to 'h1' in Service Studio.](images/html-tags-01.png "Container Widget with OSTagName Extended Property")

Note: When using `OSTagName` it is possible to preview (at design time) the effects of the following HTML tags:

    fieldset section pre nav
    h1 h2 h3 h4 h5 h6
    ol ul li p
    button footer header hr small strong
