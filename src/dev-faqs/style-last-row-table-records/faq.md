---
tags: version-10; css; table record;
summary: 
---

# How to style the last row of a Table Records

How do I make the last row of a Table Records Widget look visually distinct?

For example: I want the last row of my **LocationTable** to have bold text and a line height of 50px.

## Answer

To make the last row of the **LocationTable** Table Records Widget look visually distinct follow these steps:

1. Add the following CSS snippet to the Style Sheet of the Screen/Block containing the Table Records Widget: 

        .lastrowtrec {
            font-weight: bold; 
            line-height: 50px;
        }

    This defines the style of a new class named `lastrowtrec`.

1. Define the following code snippet as a `class` in the `Extended Properties` of the Table Record's data **Row**:

    ![data Row of the LocationTable](images/style-last-row-tr-00.png)

        If( LocationTable.List.CurrentRowNumber = LocationTable.List.Length - 1 , "lastrowtrec" , "" )

    This code snippet sets the class as `"lastrowtrec"` for the last row which is the row which row number is equal to the length of the list minus 1 ( to account for the zero based row number). 

    If the Table Records uses pagination define the `class` as:

        If( 
            LocationTable.List.CurrentRowNumber - LocationTable.StartIndex = Min(
                LocationTable.LineCount , LocationTable.List.Length - LocationTable.StartIndex 
            ) - 1 , "lastrowtrec" , "" 
        )

    This generalized version of the previous code will apply the `"lastrowtrec"` class to the last row of each page of the Table Records.
