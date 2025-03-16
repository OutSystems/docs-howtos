---
summary: Explore solutions for importing Excel data with blank cells into OutSystems 11 (O11) by defining numeric fields as text and using data type conversion.
guid: f7980805-52f4-442b-9c7a-6952f39e583a
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=147:325
tags: data import, excel integration, data conversion, error handling, data bootstrapping
audience:
  - full stack developers
  - frontend developers
  - backend developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - bootstrap-test-data-excel
---

# How to bootstrap numeric data from Excel with blank cells

## Question

I am trying to bootstrap data from an Excel spreadsheet with blank cells. However, I get an error from blank cells defined as numeric fields. How can I import data from an Excel file with blank cells?

![Screenshot of an Excel spreadsheet showing employee names, countries, and sales with a highlighted blank cell in the sales column.](images/How-to-bootstrap-numeric-data-from-Excel-with-blank-cells_0.png "Excel Spreadsheet with Blank Cell")

## Answer

Blank cells cannot be interpreted as numeric, either integer or decimal. You have two options:

* Change the spreadsheet. Change blank cells defined as numeric fields to 0.

* Change the import process. Define the numeric fields as Text. Then, use a [Data Type Conversion](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Logic/Built-in_Functions/Data_Conversion) function such as **TextToDecimal** to convert the text to Decimal or Integer.

