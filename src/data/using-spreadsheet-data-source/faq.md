---
summary: Explore how OutSystems 11 (O11) integrates Google Sheets as a data source for read and write operations using specific connectors and components.
tags: google sheets, data integration, connectors, components, outsystems integrate google sheets
guid: efffdbcf-fb3d-44ea-81f1-6f167b236883
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=942:270
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
topic:
  - bootstrap-test-data-excel
---

# How to Use a Spreadsheet as Your Data Source

This guide shows how you can use a spreadsheet as data source in an OutSystems App.

OutSystems provides a [Google Sheet Connector](https://www.outsystems.com/forge/component-overview/3058/google-sheets-connector) that allows you to use a Google Spreadsheet as a data source, by allowing users to execute Read and Write operations on it.

To retrieve data, you can use the **GetValue** or **GetValues** actions to read data from a single cell or from a range of cells, respectively.

For instance, you can add a [Data Grid component](https://www.outsystems.com/forge/component-overview/5554/data-grid) to your screen, and populate it with the data from the Data Sheet.

![Screenshot of an OutSystems Data Grid component showing spreadsheet data integration.](images/outsystems-spreadsheet-data-source-read-example.png "OutSystems Data Grid Component Populated with Spreadsheet Data")

In the **RestURL** defined in the data grid:

1. Set the cell, or cell range you want to retrieve, the Spreadsheet ID and Spreadsheet Name
1. Call the GetValue or GetValues action
1. Populate the output list with the information retrieved, so it can be mapped into the Data Grid

![Flowchart demonstrating the logic to read data from a spreadsheet in OutSystems.](images/reading-spreadsheet-as-data-source-outsystems-logic-example.png "OutSystems Logic for Reading Data from a Spreadsheet")

To save data back into the spreadsheet, use the **SetValue** or **SetValues** actions to write data into a single cell, or into a range of cells, respectively.

For instance, using the previous scenario, you can add a button to write all the changes performed in the Data Grid.

![OutSystems interface with a Data Grid and an 'Update Changes' button for writing data to a spreadsheet.](images/outsystems-spreadsheet-data-source-write-example.png "OutSystems Data Grid with Update Button")

In the RestURL defined to save the data:

Deserialize the received JSON
Iterate the generated Record List
Set the Spreadsheet ID, Spreadsheet Name and Range, and use the SetValues function to store the information

![Flowchart showing the process of writing data back to a spreadsheet in OutSystems.](images/writing-spreadsheet-as-data-source-outsystems-logic-example.png "OutSystems Logic for Writing Data to a Spreadsheet")

For Excel files, OutSystems provides a similar component that leverages the Microsoft Graph API to use an Excel File as a data source, the [Microsoft Graph Connector](https://www.outsystems.com/forge/component-overview/5552/microsoft-graph-connector).
