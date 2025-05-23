---
summary: Learn how to build and evolve front-end architecture using OutSystems 11 (O11) with practical examples and use cases.
tags: front-end development, ui/ux design, outsystems best practices, app development process
guid: e9051244-8de6-4d2f-8aa2-3b51afe8a83c
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:22
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - front-end-architecture
---

# How to Build a Front-End Architecture in OutSystems

This article provides you insights about how to build a front-end architecture in OutSystems, based in the OutSystems UI, and shows examples and use cases of how to evolve this architecture.

## Simple Project Architecture

This section explains the structure of the architecture of a simple project.

![Diagram illustrating the structure of a simple project architecture in OutSystems, showing the relationship between OutSystems UI, Project Theme, Project Style Guide, and Project Application.](images/architecture-structure-diag.png "Simple Project Architecture Diagram")

The OutSystems UI is the base application. Based on this, we build the Project Theme (you can add other Project Patterns based on the OutSystems patterns only) and finally the Project Application.
The Project style guide is also based on the project theme.
The Template Project is the template for your application.

## Patterns in Front-End Architecture

The following graphic shows how to structure the Front-end architecture at OutSystems UI.

![Graphic representation of the front-end architecture in OutSystems UI, highlighting the OutSystems UI patterns, Corporate Styles, and themes for different types of applications.](images/front-end-architecture-outsystems-ui-diag.png "OutSystems UI Front-End Architecture Diagram")

The OutSystems UI is the base application, containing all the UI patterns and screen templates ready to use.

The red squares represent the **OutSystems UI** patterns.
The yellow squares represent the changed styles that have the rules to customize your **Corporate Styles**. These are based on the **OutSystems UI**.
The yellow triangles represent new **Corporate Styles** patterns.
These square and triangle patterns defined at **Corporate Styles** are used in all your applications and can be changed at specific Themes. For example, the **Apps** theme on the left side has a new circle pattern, the **Internal Apps** theme has a new pentagon pattern, and the **Partners Apps** theme has a new diamond pattern.

You can have several applications based on these themes. At the current example, you have external apps that share the same properties defined in the **Apps** theme, internal apps that share the same **Internal Apps** theme, and partner apps that share the **Partner Apps** theme, all these based on the **Corporate Styles**.

## Front-End Use Case Architecture

The following diagram shows how to structure your Front-End architecture:

![Diagram showing the structure of front-end architecture based on OutSystems UI, with layers for branding, style definitions, and core stylesheets.](images/front-end-architecture-diag.png "Front-End Use Case Architecture Diagram")

Based on the OutSystems UI, you can set your institution branding and broad style definitions. These contain the common patterns and widgets, based on a Core Stylesheet.
The OutSystems UI contains evolved code optimized with the last best practices, usable in a large range of tested devices and browsers.

## Client Case Study

The following diagram shows an example of an architecture for a company that built a B2C custom application for a partner with an OutSystems UI-based theme, and wants to grow and build more B2C applications, and create also B2B and Corporate applications with different themes.

Existing B2C Flow → Business to Consumer (for example, a security agency website)
New B2B Flow → Business to Business (for example, security agency website only for partners)
New Corporate Flow → (for example, security agency intranet applications)

![Example architecture diagram for a company's B2C, B2B, and Corporate applications, illustrating the use of different themes and style guides based on OutSystems UI.](images/company-architecture-diag.png "Client Case Study Architecture Diagram")

Based on the **OutSystems UI**, this company built two different themes: one for **B2C** applications, and other for **corporate applications**. They built a **Partner Theme** with specific styles and layouts and used it to create a **Custom Theme Style Guide** for a partner, where all branding of their partner (layouts, colors, fonts, and so on)  is set. They built a custom application for a final customer, using the styles and themes defined in this style guide.
On the other hand, they built a different **Corporate Theme** that defines their company’s styles and layouts and a **Store Theme** Style guide specific for their store.

The company now wants to build applications for its customers, using a particular style guide for this kind of application: the **B2C Theme 1**. This style guide defines all the styles and layouts to use for every B2C App they build (in this example: **B2C App 1** and **B2C App 2**).
They want to start developing B2B applications, for example, a website for their partners only, and for this, they need to build a specific **B2B Theme** and a B2B Style Guide, which defines all the styles and patterns to use in the new **B2B Apps**.
Also, based on their existing **Corporate Theme**, they plan to build a **Store App** that uses the existing **Store Theme** style guide and create a new one for their internal corporate applications: the **Corp Theme 2** style guide.

## Store Application Front-End Architecture

The diagram below focus on the architecture of the store application of the previous example:

![Detailed architecture diagram of a store application, showing the consumption of patterns and templates from the Store Style Guide and Corporate Base Style.](images/store-application-architecture-diag.png "Store Application Front-End Architecture Diagram")

The new store application consumes patterns and templates that were previously defined at the **Store Style Guide**, and also the corporate patterns and resources define at the **Corporate Base** Style.

## Partner Application Front-End Architecture

The diagram below focus on the architecture of the partner application of the previous example:

![Architecture diagram for a partner application, depicting the use of custom resources, B2C Style Guides, and partner and B2C base patterns and resources.](images/partner-application-architecture-diag.png "Partner Application Front-End Architecture Diagram")

The partner’s B2C applications consume custom resources, the **B2C Style Guides**, partner patterns and resources defined at the **Partner Base**, and B2C patterns and resources defined at the **B2C Base** style.

