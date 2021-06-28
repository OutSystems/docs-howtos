---
tags: runtime-reactiveweb;
summary: The following example demonstrates how to edit information in the Grid using columns.
---
#  How to edit data in the Data Grid component

This example shows how to edit data in the Grid using columns.

**Prerequisites:** Complete [How to use the Data Grid component](how-to-view-data.md).

1. Select the **Grid** component, and on the **Properties** tab, expand **Optional Configs** and set the **AllowColumnEdit** property to **True**. 

    This allows the Grid values to be edited. 

   ![Set AllowColumnEdit property](images/grid-edit-true-ss.png)

1. In the Toolbox, search for Column.

    The Grid Column widgets are displayed.

   ![Search for Column widget](images/grid-edit-columns-ss.png)

1. Drag the relevant Column type to the **Grid Column** placeholder. 

    In this example, the **Text Column** is used.

   ![Drag Text Column to placeholder](images/grid-edit-textcolumn-ss.png)

1. On the Text Column **Properties** tab, enter the **Header** and **Binding** information.

    The **Header** property displays in the column’s header. In this example, **"Name"** is entered. 
 
    The **Binding** property displays the name of the entity and the attribute in the column. In this example, the entity is called Sample_Product and the Attribute is Name, so the Binding property is **"Sample_Product.Name"**.

    ![Drag Text Column to placeholder](images/grid-edit-textcolumn-ss.png)

1. Repeat steps 3 and 4 for the relevant Column widgets you want to display on your Grid. 

    This examples uses the following:

 

    Sample_Product.Stock” for Number Column,  “Sample_Product.Price” for Currency Column,  “Sample_Product.IsFavourite” for Checkbox Column

!   [Drag more columns to the placeholder](images/grid-edit-textcolumn-ss.png)

After following these steps and publishing the module, you can test the component in your app. Double-click a cell to edit it's content.
