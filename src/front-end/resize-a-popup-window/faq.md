---
tags: dynamic ui, javascript, user interface, web development, pop-up management
summary: Learn how to dynamically resize pop-up windows in OutSystems 11 (O11) by setting the AutoResize property and using JavaScript for runtime adjustments.
guid: 8aef5808-c75c-4831-ad81-f72a3fdc27d8
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:66
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to dynamically resize a pop-up window

How can I make my **pop-up** window **automatically grow** and **shrink** at **runtime**?

For example: I created a pop-up window using Popup_Editor with a TableRecords; the contents of the TableRecords can be changed from the pop-up window and I want to automatically resize the pop-up window according to the size of the TableRecords.

## Answer

To make a pop-up **automatically grow** according to its contents, set the `AutoResize` property from the Popup_Editor to `True`.

![Screenshot showing the AutoResize property of the Popup Editor set to True.](images/popup-autoresize-true.png "Popup Editor AutoResize Property Set to True")

The `AutoResize` property only affects the automatic growth of the pop-up window.
-To make the pop-up **automatically shrink** according to its contents, follow these steps:

1. Add the following **JavaScript snippet** to the `JavaScript` property of the **pop-up Web Screen**:

        function PopupEditor_ForceResize() {
            var popupDiv = window.top.$(".os-internal-ui-dialog-content");
            var popupDivOldHeight = popupDiv.height();
            // reduce iframe's div height to its contents
            popupDiv.height($(".MainPopup").innerHeight());
            // pop-up editor already auto-grows, so we just need to address auto-shrink
            if (popupDiv.height() >= popupDivOldHeight) {
                return false;
            }
            var result = window.top.RichWidgets_Popup_Editor_resize(popupDiv, -1, -1, false, {target: popupDiv});
            if (!result) {
                // something wrong happened in resize - reset iframe's div height
                popupDiv.height(popupDivOldHeight);
            }
        }

    This JavaScript snippet defines a function **PopupEditor_ForceResize()** that you will use to shrink the pop-up window during runtime.

1. Add the **RunJavaScript** action from the **HTTPRequestHandler** extension and set the `Script` property set as `"PopupEditor_ForceResize()"` to **every action** that makes your popup contents shrink.

     ![Screenshot of the RunJavaScript action with the Script property set to 'PopupEditor_ForceResize()'.](images/popup-runjavascript.png "RunJavaScript Action Configuration")

     This will call the **PopupEditor_ForceResize()** JavaScript action.
