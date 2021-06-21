# Data Grid Reactive APIs 

Version 2.2.0  
  
Data Grid for Reactive Web Applications is built on top of [Grape City Data Grid](https://www.grapecity.com/en/wijmo-flexgrid/), an Enterprise Grade Javascript Data Grid, that can be used for building applications, such as reporting and data analytics and business workflow.

## Summary

Widget | Description
---|---
[ActionColumn](<#ActionColumn>) | Column for your GridContainer Block to render number fields. Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[CheckboxColumn](<#CheckboxColumn>) | Column for your GridContainer Block to render boolean fields.Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[ContextMenu](<#ContextMenu>) | Add a context menu to the grid. Default options: Copy, Copy with headers, Export to CSV to Excel Freeze column(s),Unfreeze column(s)
[CurrencyColumn](<#CurrencyColumn>) | Column for your GridContainer Block to render number fields. Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[DateColumn](<#DateColumn>) | Column for your GridContainer Block to render text fields.Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[DateTimeColumn](<#DateTimeColumn>) | Column for your GridContainer Block to render text fields. Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[DropdownColumn](<#DropdownColumn>) | Column for your GridContainer Block to render fields with dropdown options.%%%%Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[Grid](<#Grid>) | Container that will show the grid. Add the Grid Block on your Screen and associate your data to it.
[MenuItem_Column_Freeze](<#MenuItem_Column_Freeze>) | Allow the user to freeze columns on grid.
[MenuItem_Column_FreezeUnfreeze](<#MenuItem_Column_FreezeUnfreeze>) | Allow the user to freeze or unfreeze columns on grid.
[MenuItem_Column_Unfreeze](<#MenuItem_Column_Unfreeze>) | Allow the user to unfreeze columns on grid.
[MenuItem_Copy](<#MenuItem_Copy>) | Allow the user to copy data from grid.
[MenuItem_Copy_WithHeaders](<#MenuItem_Copy_WithHeaders>) | Allow the user to copy data from grid, including its headers.
[MenuItem_CustomOption](<#MenuItem_CustomOption>) | Allow to set customized actions to the ContextMenu.
[MenuItem_Export](<#MenuItem_Export>) | Aggregates all the available export functions.
[MenuItem_Export_ToCSV](<#MenuItem_Export_ToCSV>) | Allow the user to export data to a .CSV file
[MenuItem_Export_ToExcel](<#MenuItem_Export_ToExcel>) | Allow the user to export data to a .XLS file
[MenuItem_Export_ToExcelWithoutStyles](<#MenuItem_Export_ToExcelWithoutStyles>) | Allow the user to export data to a .XLS file, ignoring CSS styles.
[MenuItem_Rows_Add](<#MenuItem_Rows_Add>) | Allow the user to insert as many rows as the selected.
[MenuItem_Rows_Delete](<#MenuItem_Rows_Delete>) | Allow the user to delete the selected rows.
[MenuItem_Separator](<#MenuItem_Separator>) | Insert a line separator, used to distinguish areas in a context menu
[NumberColumn](<#NumberColumn>) | Column for your GridContainer Block to render number fields.%%%%Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.
[OnFiltersChange](<#OnFiltersChange>) | This block enables to listen to the OnFiltersChange event of a given grid. When the end-user changes a filter, the event is fired with all of the currently active filters.
[SearchData](<#SearchData>) | Search for data on already loaded grid
[TextColumn](<#TextColumn>) | Column for your GridContainer Block to render text fields. Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

Action | Description
---|---
[ArrangeData](<#ArrangeData>) | Prepares your data to be used by the Data Grid.%%You should use this action in the Data Action after you fetched the data from DB.

Client Action | Description
---|---
[ActivateFilter](<#Client_ActivateFilter>) | Activate filter on a given column.
[AddClass](<#Client_AddClass>) | Add a CSS class to a specific row from the grid.
[AddNewRows](<#Client_AddNewRows>) | Add new lines to the grid depending on the number of lines that are selected.
[ClearFilter](<#Client_ClearFilter>) | Clear filter on a given column.
[ClearSort](<#Client_ClearSort>) | Clear all sorts on grid
[DeactivateFilter](<#Client_DeactivateFilter>) | Deactivate filter on a given column
[FreezeColumns](<#Client_FreezeColumns>) | Responsable to  freeze the leftmost columns from grid.
[FreezeColumnsByActiveCell](<#Client_FreezeColumnsByActiveCell>) | Responsable to freeze the leftmost columns from grid, considering the active cell.
[GetAllSelections](<#Client_GetAllSelections>) | Returns the Ranges for all selections on Grid
[GetAllSelectionsData](<#Client_GetAllSelectionsData>) | Returns the DataSource for all the ranges and rows selected on the Grid.
[GetChangedLines](<#Client_GetChangedLines>) | Gets the lines that were added/changed/removed by the user.
[GetSelectedRowsCount](<#Client_GetSelectedRowsCount>) | Returns how many rows are selected on Grid.
[GetSelectedRowsData](<#Client_GetSelectedRowsData>) | Returns the DataSource for all the rows selected on the Grid
[GetViewLayout](<#Client_GetViewLayout>) | Return the current layout of the grid.
[HasFrozenColumns](<#Client_HasFrozenColumns>) | Used to validate if grid has frozen columns.
[HasSelectedRows](<#Client_HasSelectedRows>) | Checks if there is a Row selected on the Grid
[MarkChangesAsSaved](<#Client_MarkChangesAsSaved>) | Marks the lines that were changed, as saved in the DB.
[RemoveAllClasses](<#Client_RemoveAllClasses>) | Remove all CSS classes from a specific row on the grid.
[RemoveClass](<#Client_RemoveClass>) | Remove a CSS class from a specific row on the grid.
[RemoveSelectedRows](<#Client_RemoveSelectedRows>) | Delete the lines that are selected on the grid.
[SearchData_deprecated](<#Client_SearchData_deprecated>) | Search for data on already loaded grid.
[SetValidationStatus](<#Client_SetValidationStatus>) | Responsible for defining a specific cell as valid/invalid and showing an error message to the user when the content of that same cell is invalid.
[SetViewLayout](<#Client_SetViewLayout>) | Add new lines to the grid depending on the number of lines that are selected.
[UnfreezeColumns](<#Client_UnfreezeColumns>) | Unfreezed all columns from the grid

Structure | Description
---|---
[ActionOptionalConfigs](<#Structure_ActionOptionalConfigs>) | Additional configurations that can be set in the Action Column.
[ActiveFilters](<#Structure_ActiveFilters>) | Contains the information of a given filter  of a column.
[BindingValue](<#Structure_BindingValue>) | Represents the content of a Cell
[CellRange](<#Structure_CellRange>) | Represents a range of cells.
[ChangedLines](<#Structure_ChangedLines>) | Information about the tines that were added/changed/removed by the user.
[ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>) | Additional configurations that can be set in the Column.
[CurrencyOptionalConfigs](<#Structure_CurrencyOptionalConfigs>) | Additional configurations that can be set in the Currency columns.
[DateConditionalFormatRule](<#Structure_DateConditionalFormatRule>) | Conditional format rule definition for Date column.
[DateFormatCondition](<#Structure_DateFormatCondition>) | Condition to be validated.
[DateOptionalConfigs](<#Structure_DateOptionalConfigs>) | Additional configurations that can be set in the Date columns.
[DateTimeConditionalFormatRule](<#Structure_DateTimeConditionalFormatRule>) | Conditional format rule definition for DateTime column.
[DateTimeFormatCondition](<#Structure_DateTimeFormatCondition>) | Condition to be validated.
[DateTimeOptionalConfigs](<#Structure_DateTimeOptionalConfigs>) | Additional configurations that can be set in the DateTime columns.
[DropdownOption](<#Structure_DropdownOption>) | Option to be displayed in the Dropdown column
[ErrorMessage](<#Structure_ErrorMessage>) | Error message from actions such as adding or removing rows from the grid.
[Filter_Condition](<#Structure_Filter_Condition>) | Represents a filter condition
[Mandatory](<#Structure_Mandatory>) | Set column fields as mandatory and set an error message
[MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>) | Additional configurations that can be set in the Context Menu items.
[NumberConditionalFormatRule](<#Structure_NumberConditionalFormatRule>) | Conditional format rule definition for Number column.
[NumberFormatCondition](<#Structure_NumberFormatCondition>) | Condition to be validated.
[NumberOptionalConfigs](<#Structure_NumberOptionalConfigs>) | Additional configurations that can be set in the Number columns.
[OptionalConfigs](<#Structure_OptionalConfigs>) | Additional configurations that can be set in the DataGrid.
[RangeData](<#Structure_RangeData>) | Represent a range of selected cells in a row
[RowData](<#Structure_RowData>) | Represent the data source of a Row.

Static Entity | Description
---|---
[AlignMode](<#StaticEntity_AlignMode>) | Alignment modes for the column 'Align' parameter. Has the values Center, Left and Right
[DateOperator](<#StaticEntity_DateOperator>) | Operators to be used by in Date and DateTime conditional format.
[Filter_OperatorType](<#StaticEntity_Filter_OperatorType>) | Operators supported by the filter.
[Filter_Type](<#StaticEntity_Filter_Type>) | Type of filter supported by the grid - condition and value.
[NumberOperator](<#StaticEntity_NumberOperator>) | Operators to be used by in Number and Currency conditional format.

## Widgets

### ActionColumn { #ActionColumn }

Column for your GridContainer Block to render number fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

TextFixed
:   Type: optional, Text.  
    Text to be displayed in this column links.  
    --  
    If used, field &quot;TextFromBinding&quot; will be ignored.

TextFromBinding
:   Type: optional, Text.  
    Field to be displayed as text of the link from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.Name&quot;  
    --  
    Note: Field &quot;TextFixed&quot; is dominant.

ActionOptionalConfigs
:   Type: optional, [ActionOptionalConfigs](<#Structure_ActionOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

### CheckboxColumn { #CheckboxColumn }

Column for your GridContainer Block to render boolean fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.IsFavourite&quot;

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

### ContextMenu { #ContextMenu }

Add a context menu to the grid.  
(Default options:  
Copy  
Copy with headers  
Export  
to CSV  
to Excel  
Freeze column(s)  
Unfreeze column(s)  
)

### CurrencyColumn { #CurrencyColumn }

Column for your GridContainer Block to render number fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.Price&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

CurrencyOptionalConfigs
:   Type: optional, [CurrencyOptionalConfigs](<#Structure_CurrencyOptionalConfigs>).  
    Set additional configurations that can be set in the Currency columns.

### DateColumn { #DateColumn }

Column for your GridContainer Block to render text fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.CreatedOn&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

DateOptionalConfigs
:   Type: optional, [DateOptionalConfigs](<#Structure_DateOptionalConfigs>).  
    Set additional configurations that can be set in the Date columns.

### DateTimeColumn { #DateTimeColumn }

Column for your GridContainer Block to render text fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.CreatedOn&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

DateTimeOptionalConfigs
:   Type: optional, [DateTimeOptionalConfigs](<#Structure_DateTimeOptionalConfigs>).  
    Set additional configurations that can be set in the Datetime columns.

### DropdownColumn { #DropdownColumn }

Column for your GridContainer Block to render fields with dropdown options.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.Category&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

DropdownOptionList
:   Type: mandatory, [DropdownOption](<#Structure_DropdownOption>) List.  
    List of options to appear in the dropdown.

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

### Grid { #Grid }

Container that will show the grid.  
  
Add the Grid Block on your Screen and associate your data to it.

*Inputs*

Data
:   Type: mandatory, Text.  
    The content that will be displayed in the grid. To best set data in this parameter, fetch data from your database and convert it to JSON with either the ArrangeData action or the JSON Serialize node.

IsDataFetched
:   Type: mandatory, Boolean.  
    Defines if an empty state should be displayed while data is loading.  
    E.g. DataAction.IsDataFetched

GridHeight
:   Type: optional, Integer.  
    Set the container's height in pixels (default: 400px).

HasGroupPanel
:   Type: optional, Boolean.  
    Enables the group panel to allow dragging columns and apply the grouping by the fields corresponding to the dragged columns (default: true).

OptionalConfigs
:   Type: optional, [OptionalConfigs](<#Structure_OptionalConfigs>).  
    Set additional parameters to customize the grid's behavior and functionality.

### MenuItem_Column_Freeze { #MenuItem_Column_Freeze }

Allow the user to freeze columns on grid.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Column_FreezeUnfreeze { #MenuItem_Column_FreezeUnfreeze }

Allow the user to freeze or unfreeze columns on grid.

*Inputs*

FreezeColumnsLabel
:   Type: optional, Text.  
    Menu item's label

UnfreezeColumnsLabel
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Column_Unfreeze { #MenuItem_Column_Unfreeze }

Allow the user to unfreeze columns on grid.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Copy { #MenuItem_Copy }

Allow the user to copy data from grid.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Copy_WithHeaders { #MenuItem_Copy_WithHeaders }

Allow the user to copy data from grid, including its headers.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_CustomOption { #MenuItem_CustomOption }

Allow to set customized actions to the ContextMenu.

*Inputs*

Label
:   Type: optional, Text.  
    

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Export { #MenuItem_Export }

Aggregates all the available export functions.

*Inputs*

Label
:   Type: optional, Text.  
    

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Export_ToCSV { #MenuItem_Export_ToCSV }

Allow the user to export data to a .CSV file

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Export_ToExcel { #MenuItem_Export_ToExcel }

Allow the user to export data to a .XLS file

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Export_ToExcelWithoutStyles { #MenuItem_Export_ToExcelWithoutStyles }

Allow the user to export data to a .XLS file, ignoring CSS styles.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Rows_Add { #MenuItem_Rows_Add }

Allow the user to insert as many rows as the selected.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Rows_Delete { #MenuItem_Rows_Delete }

Allow the user to delete the selected rows.

*Inputs*

Label
:   Type: optional, Text.  
    Menu item's label

MenuItemOptionalConfigs
:   Type: optional, [MenuItemOptionalConfigs](<#Structure_MenuItemOptionalConfigs>).  
    Additional configurations that can be set in the context menu items.

### MenuItem_Separator { #MenuItem_Separator }

Insert a line separator, used to distinguish areas in a context menu

### NumberColumn { #NumberColumn }

Column for your GridContainer Block to render number fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.Stock&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.

NumberOptionalConfigs
:   Type: optional, [NumberOptionalConfigs](<#Structure_NumberOptionalConfigs>).  
    Set additional configurations that can be set in the Number columns.

### OnFiltersChange { #OnFiltersChange }

This block enables to listen to the OnFiltersChange event of a given grid.  
When the end-user changes a filter, the event is fired with all of the currently active filters.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block, that the block will listen to events.

### SearchData { #SearchData }

Search for data on already loaded grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

PromptMessage
:   Type: optional, Text.  
    Message that will appear in the search input (default: &quot;Search for data in the Grid&quot;).

### TextColumn { #TextColumn }

Column for your GridContainer Block to render text fields.  
  
Drag into the GridColumnsPlaceholder in the GridContainer Block as many columns as you need.

*Inputs*

Header
:   Type: mandatory, Text.  
    Title of the column.

Binding
:   Type: mandatory, Text.  
    Field to be displayed from your data.  
    Expected format: &quot;{EntityName}.[FieldName]&quot;  
    --  
    For example: &quot;Product_Sample.Name&quot;

Mandatory
:   Type: optional, [Mandatory](<#Structure_Mandatory>).  
    Set column fields as mandatory and set an error message

ColumnOptionalConfigs
:   Type: optional, [ColumnOptionalConfigs](<#Structure_ColumnOptionalConfigs>).  
    Set additional parameters to customize the column's behavior and functionality.


## Actions

### ArrangeData { #ArrangeData }

Prepares your data to be used by the Data Grid.  
You should use this action in the Data Action after you fetched the data from DB.

*Inputs*

Data
:   Type: mandatory, Object.  
    Data to be displayed in the datagrid. Use the method ToObject() to pass your data.  
    E.g. ToObject(GetProducts.List)

*Outputs*

Success
:   Type: Boolean.  
    Result of the operation. If the result is false, the ErrorMessage output will be filled up.

DataJSON
:   Type: Text.  
    Data in JSON format to be provided to the Data Grid.

ErrorMessage
:   Type: Text.  
    Problem that as occured


## Client Actions

### ActivateFilter { #Client_ActivateFilter }

Activate filter on a given column

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

ColumnWidgetId
:   Type: mandatory, Text.  
    ID of the Column block in which the filter will be activated.

### AddClass { #Client_AddClass }

Add a CSS class to a specific row from the grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

RowNumber
:   Type: mandatory, Integer.  
    Number of the row in which the class is going to be added.

Class
:   Type: mandatory, Text.  
    CSS class to add to the row.

### AddNewRows { #Client_AddNewRows }

Add new lines to the grid depending on the number of lines that are selected.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

*Outputs*

Success
:   Type: Boolean.  
    Boolean that indicates if the action was successfully performed.

ErrorMessage
:   Type: [ErrorMessage](<#Structure_ErrorMessage>).  
    Error message from actions such as adding or removing rows from the grid. Contains a code and a message explaining the error.

### ClearFilter { #Client_ClearFilter }

Clear filter on a given column

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

ColumnWidgetId
:   Type: mandatory, Text.  
    ID of the Column block in which the filter will be cleared.

### ClearSort { #Client_ClearSort }

Clear all sorts on grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

### DeactivateFilter { #Client_DeactivateFilter }

Deactivate filter on a given column

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

ColumnWidgetId
:   Type: mandatory, Text.  
    ID of the Column block in which the filter will be deactivated.

### FreezeColumns { #Client_FreezeColumns }

Responsable tofreeze the leftmost columns from grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

ColumnsCount
:   Type: mandatory, Integer.  
    Number of mostleft columns to freeze

### FreezeColumnsByActiveCell { #Client_FreezeColumnsByActiveCell }

Responsable tofreeze the leftmost columns from grid, considering the active cell.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

### GetAllSelections { #Client_GetAllSelections }

Returns the Ranges for all selections on Grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

SelectedRanges
:   Type: [CellRange](<#Structure_CellRange>) List.  
    Returns all selections made in grid

### GetAllSelectionsData { #Client_GetAllSelectionsData }

Returns the DataSource for all the ranges and rows selected on the Grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

SelectionData
:   Type: [RangeData](<#Structure_RangeData>) List.  
    Returns the values selected in each row

### GetChangedLines { #Client_GetChangedLines }

Gets the lines that were added/changed/removed by the user.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

*Outputs*

ChangedLines
:   Type: [ChangedLines](<#Structure_ChangedLines>).  
    Lines that were added/changed/removed by the user.

### GetSelectedRowsCount { #Client_GetSelectedRowsCount }

Returns how many rows are selected on Grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

RowsCount
:   Type: Integer.  
    Returns the number of selected rows

### GetSelectedRowsData { #Client_GetSelectedRowsData }

Returns the DataSource for all the rows selected on the Grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

RowsData
:   Type: [RowData](<#Structure_RowData>) List.  
    Returns the selected rows data

### GetViewLayout { #Client_GetViewLayout }

Return the current layout of the grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

*Outputs*

Config
:   Type: Text.  
    

### HasFrozenColumns { #Client_HasFrozenColumns }

Used to validate if grid has frozen columns.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

IsFrozen
:   Type: Boolean.  
    Returns a boolean indicating if the given grid has columns frozen

### HasSelectedRows { #Client_HasSelectedRows }

Checks if there is a Row selected on the Grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

*Outputs*

HasSelectedRows
:   Type: Boolean.  
    Returns a boolean indicating if the given grid has rows selected

### MarkChangesAsSaved { #Client_MarkChangesAsSaved }

Marks the lines that were changed, as saved in the DB.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

### RemoveAllClasses { #Client_RemoveAllClasses }

Remove all CSS classes from a specific row on the grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

RowNumber
:   Type: mandatory, Integer.  
    Number of the row in which all classes are going to be removed.

### RemoveClass { #Client_RemoveClass }

Remove a CSS class from a specific row on the grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

RowNumber
:   Type: mandatory, Integer.  
    Number of the row in which all CSS classes are going to be removed.

Class
:   Type: mandatory, Text.  
    CSS class to remove from the row.

### RemoveSelectedRows { #Client_RemoveSelectedRows }

Delete the lines that are selected on the grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

*Outputs*

Success
:   Type: Boolean.  
    Boolean that indicates if the action was successfully performed.

ErrorMessage
:   Type: [ErrorMessage](<#Structure_ErrorMessage>).  
    Error message from actions such as adding or removing rows from the grid. Contains a code and a message explaining the error.

### SearchData_deprecated { #Client_SearchData_deprecated }

Search for data on already loaded grid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

SearchValue
:   Type: mandatory, Text.  
    Value to be searched in the Grid.

### SetValidationStatus { #Client_SetValidationStatus }

Responsible for defining a specific cell as valid/invalid and showing an error message to the user when the content of that same cell is invalid.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.

RowNumber
:   Type: mandatory, Integer.  
    Number of the row in which the action of validation should be triggered.

ColumnWidgetId
:   Type: mandatory, Text.  
    ID of the Column block in which the action of validation should be triggered.

IsValid
:   Type: mandatory, Boolean.  
    Boolean that indicates whether the cell value meets a validation or data type rule. True, if the value conforms to the rule. False, otherwise.

ErrorMessage
:   Type: optional, Text.  
    Message shown to the user when the value introduced is not valid. By default: &quot;Invalid [ColumnName]&quot;

### SetViewLayout { #Client_SetViewLayout }

Add new lines to the grid depending on the number of lines that are selected.

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.  
    By default: first grid on the screen.

Config
:   Type: optional, Text.  
    

### UnfreezeColumns { #Client_UnfreezeColumns }

Unfreezed all columns from the grid

*Inputs*

GridWidgetId
:   Type: mandatory, Text.  
    ID of Grid block.


## Structures

### ActionOptionalConfigs { #Structure_ActionOptionalConfigs }

Additional configurations that can be set in the Action Column.

*Attributes*

Align
:   Type: AlignMode Identifier.  
    Set the horizontal alignment of cells in the column  
    (default:  
    Text Columns - Left  
    Currency Columns - Right  
    Numeric Columns - Right  
    Dropdown Columns - Left  
    Date / DateTime Columns - Right  
    Checkbox Columns - Center).

AllowReorder
:   Type: Boolean.  
    Allows changing the column order (default: true).

AllowResize
:   Type: Boolean.  
    Allows resizing the column width (default: true).

Visible
:   Type: Boolean.  
    Allows to hide/display the column in the data grid (default: true).

Width
:   Type: Integer.  
    Set the column's default width in pixels (default: 0 -&gt; set automatically by the grid).

### ActiveFilters { #Structure_ActiveFilters }

Contains the information of a given filter  of a column.

*Attributes*

ColumnWidgetId
:   Type: Text.  
    Column Id where the filter was applied to. If not using columns, and relying in the auto-generate of columns, then this value will be empty.

Binding
:   Type: Text.  
    Binding where the filter was applied to.

FilterTypeId
:   Type: Filter_Type Identifier.  
    Type of filter applied, can be either &quot;conditon&quot; or &quot;value&quot;.

FilterConditions
:   Type: [Filter_Condition](<#Structure_Filter_Condition>) List.  
    List of conditions defined in the filter

FilterShowValues
:   Type: [Text](<#Structure_Text>) List.  
    List of values (in string format) of selected values for the filter.

### BindingValue { #Structure_BindingValue }

Represents the content of a Cell

*Attributes*

Binding
:   Type: Text.  
    Cell binding property

Value
:   Type: Text.  
    Cell's value

### CellRange { #Structure_CellRange }

Represents a range of cells.

*Attributes*

TopRowIndex
:   Type: Integer.  
    Topmost row index  
    Top row index.

LeftColumnIndex
:   Type: Integer.  
    Leftmost column index.

BottomRowIndex
:   Type: Integer.  
      
    Bottom row index.

RightColumnIndex
:   Type: Integer.  
    Rightmost column index.

### ChangedLines { #Structure_ChangedLines }

Information about the tines that were added/changed/removed by the user.

*Attributes*

HasChanges
:   Type: Boolean.  
    Tells if there was any change done by the user in the data grid.  
    If &quot;false&quot;, then no change was done in the data.

AddedLines
:   Type: Text.  
    JSON Serialization of the lines that were added by the user.

EditedLines
:   Type: Text.  
    JSON Serialization of the lines that were edited by the user.

RemovedLines
:   Type: Text.  
    JSON Serialization of the lines that were removed by the user.

HasInvalidLines
:   Type: Boolean.  
    Tells if there is any invalid lines in the data grid.

InvalidLines
:   Type: Text.  
    JSON Serialization of the lines that are invalid in the data grid.

### ColumnOptionalConfigs { #Structure_ColumnOptionalConfigs }

Additional configurations that can be set in the Column.

*Attributes*

Align
:   Type: AlignMode Identifier.  
    Set the horizontal alignment of cells in the column.  
    (Default per column type:  
    Text Columns - Left  
    Currency Columns - Right  
    Numeric Columns - Right  
    Dropdown Columns - Left  
    Date / DateTime Columns - Right  
    Checkbox Columns - Center  
    )

AllowEdit
:   Type: Boolean.  
    Allows to make the column editable (default: true).

AllowReorder
:   Type: Boolean.  
    Allows changing the column order (default: true).

AllowResize
:   Type: Boolean.  
    Allows resizing the column width (default: true).

AllowSort
:   Type: Boolean.  
    Allows sorting data by column (default: true).

Visible
:   Type: Boolean.  
    Allows to hide/display the column in the data grid (default: true).

Width
:   Type: Integer.  
    Set the column's default width in pixels (default: 0 -&gt; set automatically by the grid).

### CurrencyOptionalConfigs { #Structure_CurrencyOptionalConfigs }

Additional configurations that can be set in the Currency columns.

*Attributes*

NumberConditionalFormatRules
:   Type: [NumberConditionalFormatRule](<#Structure_NumberConditionalFormatRule>) List.  
    List of conditional format rules  to be applied to the Currency column.

DecimalPlaces
:   Type: Integer.  
    Set the column's default decimal places (default: 2).  
    Decimal places should be defined between 0 and 11.

Symbol
:   Type: Text.  
    Set the column's default currency symbol (default: $).

### DateConditionalFormatRule { #Structure_DateConditionalFormatRule }

Conditional format rule definition for Date column.

*Attributes*

DateFormatConditions
:   Type: [DateFormatCondition](<#Structure_DateFormatCondition>) List.  
    List of Conditions to be validated in order to apply the css class in the cell and/or row.

CellClass
:   Type: Text.  
    CSS class to be applied in the cell.

RowClass
:   Type: Text.  
    CSS class to be applied in the row.

### DateFormatCondition { #Structure_DateFormatCondition }

Condition to be validated.

*Attributes*

DateOperatorId
:   Type: DateOperator Identifier.  
    Operator to used to compare the value field with the cell value.

Value
:   Type: Date.  
    Value to be compared to.

### DateOptionalConfigs { #Structure_DateOptionalConfigs }

Additional configurations that can be set in the Date columns.

*Attributes*

DateConditionalFormatRules
:   Type: [DateConditionalFormatRule](<#Structure_DateConditionalFormatRule>) List.  
    List of conditional format rules  to be applied to the Date column.

### DateTimeConditionalFormatRule { #Structure_DateTimeConditionalFormatRule }

Conditional format rule definition for DateTime column.

*Attributes*

DateTimeFormatConditions
:   Type: [DateTimeFormatCondition](<#Structure_DateTimeFormatCondition>) List.  
    List of Conditions to be validated in order to apply the css class in the cell and/or row.

CellClass
:   Type: Text.  
    CSS class to be applied in the cell.

RowClass
:   Type: Text.  
    CSS class to be applied in the row.

### DateTimeFormatCondition { #Structure_DateTimeFormatCondition }

Condition to be validated.

*Attributes*

DateOperatorId
:   Type: DateOperator Identifier.  
    Operator to used to compare the value field with the cell value.

Value
:   Type: Date Time.  
    Value to be compared to.

### DateTimeOptionalConfigs { #Structure_DateTimeOptionalConfigs }

Additional configurations that can be set in the DateTime columns.

*Attributes*

DateTimeConditionalFormatRules
:   Type: [DateTimeConditionalFormatRule](<#Structure_DateTimeConditionalFormatRule>) List.  
    List of conditional format rules  to be applied to the DateTime column.

### DropdownOption { #Structure_DropdownOption }

Option to be displayed in the Dropdown column

*Attributes*

Text
:   Type: Text.  
    Text to be displayed.  
    --  
    For example: Sample_ProductCategory.Label

Value
:   Type: Text.  
    ID of this option.  
    --  
    For example: Sample_ProductCategory.Id

### ErrorMessage { #Structure_ErrorMessage }

Error message from actions such as adding or removing rows from the grid.

*Attributes*

Code
:   Type: Long Integer.  
    Code that tells if there was any success or error resulting from the actions such as adding or removing lines from the grid.

Message
:   Type: Text.  
    Message that explains the resulting code from the actions such as adding or removing lines from the grid.

### Filter_Condition { #Structure_Filter_Condition }

Represents a filter condition

*Attributes*

And
:   Type: Boolean.  
    Operator to be used between conditions. If true &quot;and&quot;, else &quot;or&quot;.

OperatorTypeId
:   Type: Filter_OperatorType Identifier.  
    Filter operator to be used in the condition (e.g. &quot;Is Greater than&quot;, ...)

Value
:   Type: Text.  
    Condition value against which the to cell value will be match against - string format.

### Mandatory { #Structure_Mandatory }

Set column fields as mandatory and set an error message

*Attributes*

IsMandatory
:   Type: Boolean.  
    Boolean that tells if this column will be mandatory or not.  
    If you wish to have another type of validation, you can use the SetValidationStatus client action.

ErrorMessage
:   Type: Text.  
    Message that will be displayed if the cell is not filled with any value

### MenuItemOptionalConfigs { #Structure_MenuItemOptionalConfigs }

Additional configurations that can be set in the Context Menu items.

*Attributes*

Enabled
:   Type: Boolean.  
    Boolean literal or expression that defines if the Context Menu item is enabled. The menu item will not be clickable if this configuration is set to False.

### NumberConditionalFormatRule { #Structure_NumberConditionalFormatRule }

Conditional format rule definition for Number column.

*Attributes*

NumberFormatConditions
:   Type: [NumberFormatCondition](<#Structure_NumberFormatCondition>) List.  
    List of Conditions to be validated in order to apply the css class in the cell and/or row.

CellClass
:   Type: Text.  
    CSS class to be applied in the cell.

RowClass
:   Type: Text.  
    CSS class to be applied in the row.

### NumberFormatCondition { #Structure_NumberFormatCondition }

Condition to be validated.

*Attributes*

NumberOperatorId
:   Type: NumberOperator Identifier.  
    Operator to used to compare the value field with the cell value.

Value
:   Type: Decimal (0, 0).  
    Value to be compared to.

### NumberOptionalConfigs { #Structure_NumberOptionalConfigs }

Additional configurations that can be set in the Number columns.

*Attributes*

NumberConditionalFormatRules
:   Type: [NumberConditionalFormatRule](<#Structure_NumberConditionalFormatRule>) List.  
    List of conditional format rules  to be applied to the Number column.

DecimalPlaces
:   Type: Integer.  
    Set the column's default decimal places (default: 0).  
    Decimal places should be defined between 0 and 11.

MaxValue
:   Type: Decimal (0, 0).  
    Set the maximum value accepted by the column.  
    When the cell is in edit mode and it is changed to a value higher than Max Value, the cell value will become Max Value.  
    If Max Value is 0, then no maximum value will be defined.

MinValue
:   Type: Decimal (0, 0).  
    Set the minimum value accepted by the column.  
    When the cell is in edit mode and it is changed to a value lower than Min Value, the cell value will become Min Value.  
    If Min Value is 0, then no minimum value will be defined.

Step
:   Type: Decimal (0, 0).  
    Set the step value in the increments in column.  
    When step value is defined and the cell is in edit mode, the input will show two buttons, a plus (+) that will increase the cell value with the step value and a minus (-) that will decrease the cell value.  
    If step value is 0, then no buttons will be displayed.

### OptionalConfigs { #Structure_OptionalConfigs }

Additional configurations that can be set in the DataGrid.

*Attributes*

AllowColumnEdit
:   Type: Boolean.  
    Allows to make the columns editable (default: false).

AllowColumnReorder
:   Type: Boolean.  
    Allows changing the column order (default: true).

AllowColumnResize
:   Type: Boolean.  
    Allows resizing the column width (default: true).

AllowColumnSort
:   Type: Boolean.  
    Allows sorting data by column (default: true).

RowHeight
:   Type: Integer.  
    Set the row height in pixels (default: 48px).

RowsPerPage
:   Type: Integer.  
    Set the number of rows per page (default: 50).

### RangeData { #Structure_RangeData }

Represent a range of selected cells in a row

*Attributes*

RowIndex
:   Type: Integer.  
    Row Index

Selected
:   Type: [BindingValue](<#Structure_BindingValue>) List.  
    List of selected cells

### RowData { #Structure_RowData }

Represent the data source of a Row.

*Attributes*

DataItem
:   Type: Text.  
    Data source serialized to string

RowIndex
:   Type: Integer.  
    Row Index.


## Static Entities

### AlignMode { #StaticEntity_AlignMode }

Alignment modes for the column 'Align' parameter. Has the values Center, Left and Right

*Attributes*

Id
:   Type: Text (50).  
    

*Records*

* Center
* Left
* Right

### DateOperator { #StaticEntity_DateOperator }

Operators to be used by in Date and DateTime conditional format.

*Attributes*

Label
:   Type: Text (50).  
    

*Records*

* LessOrEqualsTo
* GreaterThan
* LessThan
* Equals
* GreaterOrEqualsTo

### Filter_OperatorType { #StaticEntity_Filter_OperatorType }

Operators supported by the filter.

*Attributes*

Id
:   Type: Text (50).  
    

Label
:   Type: Text (50).  
    

Order
:   Type: Integer.  
    

*Records*

* Contains
* EndsWith
* BeginsWith
* IsGreaterThanOrEqualTo
* DoesNotContain
* DoesNotEquals
* IsLessThanOrEqualTo
* Equals
* IsGreaterThan
* IsLessThan

### Filter_Type { #StaticEntity_Filter_Type }

Type of filter supported by the grid - condition and value.

*Attributes*

Id
:   Type: Text (50).  
    

*Records*

* Condition
* Value

### NumberOperator { #StaticEntity_NumberOperator }

Operators to be used by in Number and Currency conditional format.

*Attributes*

Label
:   Type: Text (50).  
    

*Records*

* GreaterOrEqualsTo
* GreaterThan
* NotEquals
* Equals
* LessThan
* LessOrEqualsTo


