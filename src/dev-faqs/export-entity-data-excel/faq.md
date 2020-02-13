---
summary: Learn how to export entity data to an Excel file.
tags: OutSystems_How_To; OutSystems_Export_Entity_Data; OutSystems_Export_Entity_Data_Excel
---

# How to Export Entity Data to Excel

## Question

How can I export the data entered into an entity?

## Answer

Use the **Record List To Excel** action to generate an Excel worksheet for the user to download.

Note: The **Record List To Excel** action is only available in the server actions.

​For example, add a link or button to a typical page showing data in a list. Set the Method to Submit.

![Export Entity to Excel](images\export_entity_data_to_excel1.png)

In the screen action:

  1. Add the Record List To Excel widget to the logic;
  2. Select the data to send. In this case, the data from the Table Records widget on the page;
  3. Select the attributes to send to the Excel file.

![Export Entity to Excel](images\export_entity_data_to_excel2.png)

Finally, add a Download widget:

  * Refer to the binary content coming from the Record List To Excel widget;
  * Give the file a good name. If the user will download the file several times, you may want to concatenate the name with CurrDateTime().

![Export Entity to Excel](images\export_entity_data_to_excel3.png)