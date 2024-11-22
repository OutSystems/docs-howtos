---
summary: Learn how to display records side-by-side using the List Records widget in OutSystems 11 (O11).
guid: 955219bb-026a-4fd4-a24a-0fc5da6a0a1e
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:95
tags: ide usage, reactive web apps, list records widget, ui patterns, outsystems ui framework
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
content-type:
  - procedure
---

# How to show records side by side in a List Record widget

## Question

Is it possible to customize the layout to show records side-by-side, as follows?

| Record1 | Record3 | Record5 |
|---------|---------|---------|
| Record2 | Record4 |         |

In the standard table grid layout each record is on a separate line, as follows:

| Record1 |
|---------|
| Record2 |
| Record3 |
| Record4 |
| …       |

## Answer

Use the **List Records widget** to manipulate how information is displayed on your Web Screen.

![Example of a standard table grid layout where each record is displayed on a separate line.](images/How-to-show-records-side-by-side-in-a-List-Record-widget_0.png "Standard table grid layout with records on separate lines")

After you select the **List Records widget** to use in your Web Screen you just need to go to the properties of the widget and set the **Line Separator** property to **None** so the records can be displayed side-by-side.

![Screenshot showing the List Records widget properties with the Line Separator set to None.](images/How-to-show-records-side-by-side-in-a-List-Record-widget_1.png "List Records widget properties")

After you performed these configurations your layout may look similar to the following image. You can see more useful UI patterns by looking into  [OutSystems UI](https://www.outsystems.com/forge/component-overview/1385/outsystems-ui) component available on Forge.

![Customized layout displaying records side by side in a List Records widget, with computer names under state headings.](images/How-to-show-records-side-by-side-in-a-List-Record-widget_2.png "Customized layout with records side by side")
