---
tags: version-10; support-Database; support-Front_end_Development; support-webapps;
summary: 
---

# How to use the List Sort Column Widget with a SQL query

How can I dynamically sort a Table Records fed by a **SQL** query using the List Sort Column Rich Widget?

## Answer

To to use the List Sort Column widget with a **SQL** query follow these steps:

1. Add a query Parameter to the **SQL** query define the `Name` as `SORT`, the `Data Type` as `Text` and the `Expand Inline` Property to `Yes`.

    Setting the `Expand Inline` Property to `Yes` allows the use of the Query Parameter as part of the SQL code that will be sent to the database at runtime.

1. Add the SQL snippet `ORDER BY @SORT` to your **SQL** query.

1. Define the `SORT` Parameter of your **SQL** query as `List_SortColumn_GetOrderBy(LocationTable.Id,DefaultOrder:"{<Entity>}.[<Attribute>]")`, where `DefaultOrder:"{<Entity>}.[<Attribute>]"` defines that by default the **SQL** query will be sorted ascendantly by Attribute `<Attribute>` (of the Entity `<Entity>`)

    ![SORT query Parameter](images/list-sort-sql-02.png?width=800)

    The `List_SortColumn_GetOrderBy()` Function returns the column to sort by.

1. Implement List Sort Column Rich Widgets in your Table Records Widget as you would do if you were using an Aggregate: 

    ![](images/list-sort-sql-05.png?800)

    * Drag a List Sort Column to each of the columns that will be used to sort the **SQL** query.
    * Set the `Column` and `OnNotify` > `Destination` Properties for each List Sort Column.
    * Add a **Refresh Data** node (with the **SQL** query as the `Data Source` to be fetched) and an **Ajax Refresh** node (with the Table Records Widget as the `Widget or Web Block` to refresh).