---
guid: f7980805-52f4-442b-9c7a-6952f39e583a
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to bootstrap numeric data from Excel with blank cells

## Question

I am trying to bootstrap data from an Excel spreadsheet with blank cells. However, I get an error from blank cells defined as numeric fields. How can I import data from an Excel file with blank cells?

![image alt text](images/How-to-bootstrap-numeric-data-from-Excel-with-blank-cells_0.png)

## Answer

Blank cells cannot be interpreted as numeric, either integer or decimal. You have two options:

* Change the spreadsheet. Change blank cells defined as numeric fields to 0.

* Change the import process. Define the numeric fields as Text. Then, use a [Data Type Conversion](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Logic/Built-in_Functions/Data_Conversion) function such as **TextToDecimal** to convert the text to Decimal or Integer.

