---
summary: Considerations about migrating the UI of Traditional Web Apps that use different UI frameworks to Reactive Web Apps using OutSystems UI.
tags: migration-traditional-web; migration-reactive-web; frontend-migration 
locale: en-us
guid: f3b2a6fe-c642-4dde-b104-9f37f32bb4fa
---

# UI migration considerations

The User Interface of your app is one of the first things to consider when planning a migration from a Traditional App to a Reactive Web App.

There are different scenarios to start from.

* Traditional App using [OutSystems UI Web](#os-ui-web)
* Traditional App using  [Silk UI](#silk-ui)
* Traditional App using [London UI or older](#london-older-ui)

Find below the recommended approaches to each of these scenarios.

## OutSystems UI Web { #os-ui-web }

OutSystems UI Web uses the same styles and user interface of OutSystems UI, used in Reactive Web Apps. You need to consider the CSS customization you have created and reproduce it in the new app. This means you need to implement the styles and Theme from your style guide and recreate them using a Reactive Web style guide. The CSS classes and UI patterns are almost the same.

## Silk UI { #silk-ui }

When migrating an app created with the patterns of the Silk UI framework, you need to recreate the customizations you had, like all the styles of your personal style guide, and consider all the overridden classes.

For information about migrating from Silk UI to OutSystems UI, read [Migrating UI of the Silk Web applications to OutSystems UI Framework](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Migrating_UI_of_the_Silk_Web_applications_to_OutSystems_UI_Framework).

## London UI or older { #london-older-ui }

When you plan to migrate an app using London UI or older UIs, you need to change the layouts and the Themes used and recreate all your customizations from scratch, based on your style guide. There are two different approaches to this:

* Using a Reactive Web App, a Reactive style guide, and customize only what you need for matching your current style guide - this option grants you the opportunity to build a cleaner style guide and to get rid of what's old or not used. It offers you also the advantage of having CSS variables that let you customize your styles in a few lines of code, and these are automatically used by all the Patterns and style guide consistently.

    For more information about CSS see [Cascading Style Sheets](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Cascading_Style_Sheets_(CSS) ).

* Analyzing existing customizations, like styles, colors, fonts, and logo, and recreating them in the Reactive Web App - meaning there's a great effort involved.

Have a look at the [OutSystems UI website](https://outsystemsui.outsystems.com/outsystemsuiwebsite/) to see the single UI framework for Reactive Web Apps. You can also check the [OutSystems UI Style Guide Theme](https://www.outsystems.com/forge/component-overview/8240/outsystems-ui-style-guide-theme) component in the OutSystems Forge.

Continue to [UI Flow elements](ref-frontend-ui-flows.md).

---

Documents in this section:

* [Introduction to migrating Traditional Web to Reactive Web Apps](intro.md)
* [Differences to consider between Traditional and Reactive Web Apps](differences.md)
* [Suggested stages of Traditional to Reactive Web App migration](stages.md)
* [Traditional to Reactive Web App migration reference](reference.md)
    * [Module elements](ref-module-elements.md)
    * [Front-end](ref-frontend-intro.md)
        * [User Interface](ref-frontend-ui.md)
        * [UI Flow elements](ref-frontend-ui-flows.md)
        * [Screen and Block logic](ref-frontend-screen-and-block.md)
        * [System Actions](ref-system-actions.md)
    * [Core Widgets](ref-core-widgets.md)
