---
tags: runtime-reactiveweb;
summary: View, explore, and edit large amounts of data in a familiar spreadsheet interface with the OutSystems Data Grid component for Reactive Web apps.
guid: cca0de21-e1fb-452f-9ff7-c73b55b3c287
locale: en-us
---

#  How to use the OutSystems Data Grid

**Prerequisites** 

* Download and install the [OutSystems Data Grid](https://www.outsystems.com/forge/component-overview/9764/data-grid-reactive) component from Forge.

This example fetches data from a database and displays it in the grid. (This examples does not define any column structure.) 

1. In Service Studio, in the Toolbox, search for Grid.

    The Grid widget is displayed.

    ![Grid widget](images/grid-widget-ss.png)

1. From the Toolbox, drag the Grid widget into the Main Content area of your application's screen.

    ![Drag widget to screen](images/grid-widget-drag-ss.png)

    By default, the Grid widget contains the following placeholders:

    * ContextMenu
    * Loading (displayed while data is being fetched from the server)
    * NoResults (displayed when no results are returned)
    * GridColumns

    ![Grid widget placeholders](images/grid-placeholders-ss.png)

    You can change the content of these placeholders as required.

1. Create a Data Action to fetch the data you want to display in the grid.

    ![Create fetch data action](images/grid-fetch-data-ss.png)

1. Enter a name for the Action's output parameter (for example, Data) and ensure the **Data Type** is **Text**.

    This output parameter is used to receive the data fetched from the database.

    ![Name output parameter](images/grid-output-par-ss.png)

1. On the **Data** tab, drag the data source entity onto the flow.

    ![Drag data source entity to the flow](images/grid-drag-entity-ss.png)

    An aggregate (in this example, GetProducts) is automatically created. 

1. On the **Logic** tab, drag the **ArrangeData** Server Action onto the flow.

    The **Grid** block receives data in JSON format. The **ArrangeData** Server Action analyzes this data, serializes it, and retrieves the information from each column, whether it be in, for example, string, number, boolean format.

    ![Drag ArrangeData server action onto the flow](images/grid-arrange-data-ss.png)

1. Set the **Data Action** property to the aggregate result. 

    All of the aggregate data is passed to the action.

    **Note:** Because the **ArrangeData** Server Action action can receive any data structure, you must use the **ToObject** function. 

    ![Set Data property to the aggregate result ](images/grid-aggregate-result-ss.png)

1. Drag an **Assign** onto the flow and set the **Data** action output parameter to the **ArrangeData.DataJSON** property.

    ![Set Assign Data output parameter ](images/grid-set-assign-ss.png)

1. Return to the main screen and select the Grid. On the **Properties** tab, set the **Data** property to the output of the Data Action you created earlier (step. 3).

    ![Set Grid's Data property](images/grid-data-prop-ss.png)

1. Bind the Grid's **IsDataFetched** property to the Data Action property **IsDataFetched**.

    ![Set Grid's IsDataFetched property](images/grid-isdata-fetched-ss.png)

After following these steps and publishing the module, you can test the component in your app.

**Result**

![Grid result](images/grid-result-ss.png)

## Properties

| **Properties** | **Description** |
|---|---|
| Data (Text): Mandatory  | The data displayed in the Grid.  |
| IsDataFetched (Boolean): Mandatory | Defines what is displayed while data is loading. | 
| GridHeight (Integer): Optional  |  Sets the Grid's height in pixels. Default height is 400 pixels. |  
| HasGroupPanel (Boolean): Optional  | Enables the group panel to allow dragging columns and apply the grouping by the fields corresponding to the dragged columns. Default value is True. |  
| AllowColumnEdit (Boolean): Optional  | Allows columns to be edited. Default value is False.  |   
| AllowColumnReorder (Boolean): Optional  | Allows columns to be reordered. Default value is True. | 
| AllowColumnResize (Boolean): Optional  | Allows column width to be resized. Default value is True. |  
| AllowColumnSort (Boolean): Optional  | Allows sorting data by column. Default value is True. | 
| RowHeight (Integer): Optional  | Sets the row height in pixels. Default height is 48 pixels. | 
| RowsPerPage (Integer): Optional  | Sets the number of rows displayed per page. Default value is 50.| 

