---
tags: runtime-reactiveweb;
summary: View, explore, and edit large amounts of data in a familiar spreadsheet interface with the Data Grid component for Reactive Web apps.
---

#  How to use the Data Grid component

This example This example does not define any column structure. 

1. In Service Studio, in the Toolbox, search for Grid.

    The Grid widget is displayed.

    ![Grid widget](images/grid-widget-ss.png)

1. From the Toolbox, drag the Grid widget into the Main Content area of your application's screen.

    ![Drag widget to screen](images/grid-widget-drag-ss.png)

    By default, the Grid widget contains the following placeholders:

    * ContextMenu
    * Loading (displayed while data is being fetched from teh server)
    * NoResults (displayed when no results are returned)
    * GridColumns

    ![Grid widget placeholders](images/grid-placeholders-ss.png)

    You can change the content of these placeholders as required.

1. Create an Action to fetch the data you want to display in the grid.

    ![Create fetch data action](images/grid-fetch-data-ss.png)

1. Enter a name for the Action's output parameter (for example, Data) and ensure the **Data Type** is **Text**.

    ![Name output parameter](images/grid-output-par-ss.png)

1. On the **Data** tab, drag the data source entity onto the flow.

    ![Drag data source entity to the flow](images/grid-drag-entity-ss.png)

    An aggregate (in this example, GetProducts) is automatically created. 

1. On the **Logic** tab, drag the **ArrangeData** Server Action onto the flow.

    ![Drag ArrangeData server action onto the flow](images/grid-arrange-data-ss.png)

1. Set the **Data** property to the aggregate result. 

    **Note:** The **ArrangeData** Server Action action can receive any data structure so you must use the **ToObject** function. 

    ![Set Data property to the aggregate result ](images/grid-aggregate-result-ss.png)

1. Click on the flow and add a **Set Data** data action.

    ![Add a Set Data action to the flow ](images/grid-set-data-ss.png)

1. Assign the **Set Data** property to the **ArrangeData** Server Action output.

    ![Assign the Set Data to the server action output ](images/grid-set-data-assign-ss.png)

1. Return to the main screen and select the Grid. On the **Properties** tab, set the **Data** property to the output of the Data Action you created earlier (step. 3).

    ![Set Grid's Data property](images/grid-data-prop-ss.png)

1. Bind the **IsDataFetched** property to the Data Action property **IsDataFetched**.

    ![Set Grid's IsDataFetched property](images/grid-isdata-fetched-ss.png)
