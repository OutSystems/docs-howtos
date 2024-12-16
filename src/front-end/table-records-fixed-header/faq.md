---
tags: web development, ui design, css, traditional web, fixed header
summary: Explore how to create a scrollable table with a fixed header in OutSystems 11 (O11) using Table Records Widgets for Traditional Web Apps.
guid: bc28b35e-c684-4094-a937-e189a137886d
locale: en-us
app_type: traditional web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to scroll records in a table with a fixed header

<div class="info" markdown="1">

Applies only to Traditional Web Apps

</div>

How can I create a scrollable table that has a fixed header? 

For example: I am using the Table Records Widgets to show the name and location of several stores. I want my table to be vertically scrollable and I want the header row to always be visible.

## Answer

To create a scrollable table that always shows the header, follow these steps:

1. Create a Table Widget (**FixedTableHeader** in this case) above your Table Records Widget (**TableBodyScroll** in this case) with 1 row and the same number of columns as the Table Widget (`2` in this case).

    The **FixedTableHeader** will be the new table header and the next 3 steps help recreating the look of the original header.

1. Set the `Style Classes` of the **FixedTableHeader** to `TableRecords`.

1. In the **FixedTableHeader** Table, recreate the header text from the **TableBodyScroll** Record Table. In this case write `Name` in the first column and `City` in the second column.

1. For each one of the Cells in **FixedTableHeader**  set the `Style Classes` to `TableRecords_Header`. 

1. For the first Cell of the **FixedTableHeader** select the Styles Editor and add `padding: 10px 10px 10px 20px;` to the `Style Properties Applied`. Set the padding of the other Cell to `padding: 10px;`.

1. Select the **TableBodyScroll** Table Records and set the Properties `Show Header` to `No` and `Margin Top` to `0px`. 

    This will hide the original header and remove the top margin.

1. Define the width of each Cell of the **FixedTableHeader** and do the same for the content Cells of **TableBodyScroll**. In this case set the `Width` of the first Cells to `33%` and of the second Cells to `67%`.

    This sets the width of each cell and makes sure that the width will be equal for the table header and for the scrollable table body.

1. Add the following CSS snippet to the `Style Properties Applied` of the **TableBodyScroll** Record Table:

        table-layout: fixed;
        word-wrap: break-word;

    This CSS snippet makes sure that the width of the table body at runtime is always equal to the defined width and makes sure the contents don't overflow out of the table cells.

1. Enclose the **TableBodyScroll** Table Records Widget in a Container.

1. Select the Container and in the `Style Properties Applied` of the Styles Editor add the following CSS snippet:

        height: 200px;
        overflow-y: auto;
        padding-top: 0px;

    This CSS sets the height of the body of your table to `200px`, adds a vertical scroll bar to your table body in case it is needed and removes the padding on the top of the table body.
