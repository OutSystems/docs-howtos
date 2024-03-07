---
tags: version-11; css; list box; runtime-traditionalweb;
summary: How to hide the scroll bar of a List Box.
guid: f7777240-9826-476e-9eab-8415771fbc79
locale: en-us
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:29
---

# How to hide the scroll bar of a List Box

How do I hide the vertical scroll bar in a List Box widget?

For example: I set the Layout **Height** property to **100px** so all values are visible at runtime, and now I want to hide the unnecessary scroll bar.

## Answer

1. Drag the **List Box** widget into the **Main Content** area of your screen.

    ![Screenshot showing the List Box widget being dragged into the Main Content area.](images/hide-scrollbar-listbox-2-ss.png "Dragging List Box Widget")

1. Select the **Styles** tab, and add the following style properties to the **Style Properties Applied** text box:

        overflow-y: hidden;
        background-image: none;

    `overflow-y: hidden` disables the scroll bar and  `background-image: none` removes the down arrow.

    ![Screenshot of the Styles tab with style properties 'overflow-y: hidden' and 'background-image: none' added to hide the scroll bar.](images/hide-scrollbar-listbox-1-ss.png "Adding Style Properties")

    **Note**: Height is already set to 100px.

## Result

**Before**

![Before screenshot displaying a List Box with a visible vertical scroll bar.](images/hide-scrollbar-listbox-3-ss.png "List Box with Scroll Bar")

**After**

![After screenshot showing a List Box with the scroll bar hidden after applying the CSS styles.](images/hide-scrollbar-listbox-4-ss.png "List Box without Scroll Bar")
