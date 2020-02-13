---
tags: version-10; css; list box;
summary: 
---

# How to hide the scrollbar of a List Box

How do I hide the vertical scrollbar in a List Box Widget? 

For example: I set the `Heigth` Property of the List Box so all values are visible at runtime and I want to hide the now unneeded scrollbar.

## Answer

To hide the vertical scrollbar in a List Box add the following `Style Properties` to the List Box:
    
    overflow-y: hidden;
    background-image: none;

`overflow-y: hidden` disables the scroll bar and  `background-image: none` removes the down arrow. 

![Style Properties](images/hide-scrollbar-listbox-00.png)