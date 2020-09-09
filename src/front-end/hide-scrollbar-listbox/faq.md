---
tags: version-10; css; list box;
summary: How to hide the scrollbar of a list box
---

# How to hide the scrollbar of a List Box

How do I hide the vertical scrollbar in a List Box widget? 

For example: I set the Layout **Height** property to 100px so all values are visible at runtime, and now I want to hide the unnecessary scrollbar.

## Answer

To hide the vertical scrollbar of a List Box, select the **Styles** tab, and add the following style properties to the **Style Properties Applied** text box:
    
    overflow-y: hidden;
    background-image: none;

`overflow-y: hidden` disables the scroll bar and `background-image: none` removes the down arrow. 

![Style Properties Applied](images/hide-scrollbar-listbox-1-ss.png)
