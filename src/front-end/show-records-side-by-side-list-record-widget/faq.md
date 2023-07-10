---
summary: In the standard table grid layout each record is on a separate line. Here, we'll show how to achive other record arrangements, such as diplaying records side by side.
guid: 955219bb-026a-4fd4-a24a-0fc5da6a0a1e
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
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

![](images/How-to-show-records-side-by-side-in-a-List-Record-widget_0.png)

After you select the **List Records widget** to use in your Web Screen you just need to go to the properties of the widget and set the **Line Separator** property to **None** so the records can be displayed side-by-side.

![](images/How-to-show-records-side-by-side-in-a-List-Record-widget_1.png)

After you performed these configurations your layout may look similar to the following image. You can see more useful UI patterns by looking into  [OutSystems UI](https://www.outsystems.com/forge/component-overview/1385/outsystems-ui) component available on Forge.

![](images/How-to-show-records-side-by-side-in-a-List-Record-widget_2.png)
