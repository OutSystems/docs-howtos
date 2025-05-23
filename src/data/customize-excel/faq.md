---
tags: data mapping, server actions, excel export, data customization, structured data
summary: Learn how to customize Excel exports in OutSystems 11 (O11) by renaming and reordering columns using structured data mapping and server actions.
guid: d1470acf-fb13-42b7-9a3d-0d4a67ddc689
locale: en-us
app_type: traditional web apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=942:245
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
topic:
  - bootstrap-test-data-excel
---

# How to customize the export to Excel

How can I customize the name and order of columns/Attributes when exporting to an Excel file?

For example: I want to export a list of receipts to an Excel file.
The original list of receipts (`ReciptTable.List`) is fed by the following Aggregate:

![Screenshot of the Aggregate configuration showing the original list of receipts with columns for Id, DateTime, ClientName, Name, and Total.](images/customize-excel-00.png "Aggregate Configuration for Receipts")

I want my Excel file to have "Store" (originally "Name"), "Date and Time" (originally "DateTime"), "Customer" (originally "ClientName") and "Order Total" (originally "Total") columns.

## Answer

To customize the name and order of columns/Attributes when exporting a List to an Excel file follow these steps:

1. In the **Data** tab, create a Structure (`ReceiptsExport`) and add the following Attributes:

    * **Store**: set the **Data Type** to **Text**.
    * **DateandTime**: set the **Label** to `Date and Time` and the **Data Type** to **Date Time**.
    * **Customer**: set the **Data Type** to **Text**.
    * **OrderTotal**: set the **Label** to `Order Total` and the **Data Type** to **Decimal**.

    This Structure defines the final labels and order of the columns in the Excel file.

1. In the **Logic** tab, create an **ExportReceiptsToExcel** Server Action and add a `ListToExport` Local Variable and set the `Data Type` to `ReceiptsExport List` by selecting `Other`>`List...` and then `ReceiptsExport`. 

1. Add an **Assign** element with the assignment `ListToExport` = `ReceiptTable.List` and set the Mapping to ReceiptsExport as:

    * **Store**: `Name`
    * **DateandTime**: `DateTime`
    * **Customer**: `ClientName`
    * **OrderTotal**: `Total`

    This defines the relation between the original List Attributes and the Structure Attributes.

1. After the **Assign** node add a **Record List To Excel** element (`ListToExcel`), set the source `Record List` as the `ListToExport` Structure and in `Attribute Selection` tick the `(All Attributes)` check box.

1. Create an Output Parameter (`ReceiptsExcelFile`) and set the **Data Type** to **Binary**.

1. After the **Record List To Excel** element, add an **Assign** element and assign the output of the **Record List To Excel** to the Output Parameter with the assignment `ReceiptsExcelFile` = `ListToExcel`.

After these steps, calling the **ExportReceiptsToExcel** Action will generate an Excel file with the desired column names and order:

![Example of an Excel file with customized column names: Store, Date and Time, Customer, and Order Total.](images/customize-excel-02.png "Customized Excel Export Example")

To enable the download of the Excel file follow this step:

* In a screen action, add the **ExportReceiptsToExcel** Server Action, replace the **End** node with a **Download** node and define the following properties:

    * **File Content**: `ExportReceiptsToExcel.ReceiptsExcelFile`
    * **File Name**: `"Receipts.xlsx"`
    * (Only for Traditional Web) **Mime-Type**: `"application/x-msexcel"`

![Screenshot of the Download action configuration in the development environment, showing the setup for exporting receipts to an Excel file.](images/customize-excel-03-ss.png "Download Action Configuration")