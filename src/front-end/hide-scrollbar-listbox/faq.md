---
tags: version-11; css; list box; runtime-traditionalweb;
summary: How to hide the scroll bar of a List Box.
guid: f7777240-9826-476e-9eab-8415771fbc79
locale: en-us
app_type: traditional web apps
---

# How to hide the scroll bar of a List Box

How do I hide the vertical scroll bar in a List Box widget?

For example: I set the Layout **Height** property to **100px** so all values are visible at runtime, and now I want to hide the unnecessary scroll bar.

## Answer

1. Drag the **List Box** widget into the **Main Content** area of your screen.

    ![Drag widget onto screen](images/hide-scrollbar-listbox-2-ss.png)

1. Select the **Styles** tab, and add the following style properties to the **Style Properties Applied** text box:

        overflow-y: hidden;
        background-image: none;

    `overflow-y: hidden` disables the scroll bar and  `background-image: none` removes the down arrow.

    ![Style Properties Applied](images/hide-scrollbar-listbox-1-ss.png)

    **Note**: Height is already set to 100px.

## Result

**Before**

![List Box with scroll bar](images/hide-scrollbar-listbox-3-ss.png)

**After**

![List Box without scroll bar](images/hide-scrollbar-listbox-4-ss.png)
