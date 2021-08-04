---
tags: version-11; runtime-reactiveweb;
summary: Enable the dynamic sorting of a Table widget that has a SQL query as the data source.
---

# How to use dynamic sorting in a Table fed by a SQL query

You can enable dynamic sorting for a Table by selecting **(New On Sort Client Action)** on the **On Sort** event. Service Studio creates an action with the sorting logic that uses the **Sort Attribute** of each **Header Cell**. The format of the **Sort Attribute** is optimized for Aggregates and the **Sort Attribute** needs to be encoded before using it in a SQL query.

To enable the dynamic sorting in a Table that has a SQL query as the data source follow these steps:

1. To create a new action to handle the On Sort event of the Table, select the **Table** and add a **(New On Sort Client Action)** to the **On Sort** event.

    ![](images/add-on-sort-event-ss.png)

    Selecting **(New On Sort Client Action)** on the **On Sort** event also adds two Local Variables, **TableSort** and **StartIndex**.

1. To define the default sort attribute, select the **TableSort** variable, and set the **Default Value** property to `"<Sort Attribute>"`, where `<Sort Attribute>` is the value of the **Sort Attribute** of a **Header Cell**.

    For example, setting the **Default Value** to `"User.Name"` sets the **Name** attribute of the User entity as the default sort attribute.

1. In the new **OnSort** action flow, set the **Data Source** of the **Refresh Data** element to the **Data Action** that contains the **SQL** query that feeds data to your Table.

    ![](images/set-refresh-data-source-ss.png)

1. Add a **Query Parameter** to the **SQL** query, set the **Name** to `SortForSQL` and set the **Expand Inline** property to **Yes**.

    Setting the `Expand Inline` property to `Yes` allows the use of the Query Parameter as part of the SQL code that's sent to the database at runtime without first being evaluated and turned into a literal by the SQL engine.

1. Add the SQL snippet `ORDER BY @SortForSQL` to your **SQL** query.

    ![](images/order-by-query-parameter-ss.png)

1. Create a new **Function**, `EncodingSortForSQL`, to encode the TableSort variable used by the OnSort action to a format that's usable by a SQL query.

    ![](images/encoding-function-ss.png)
    
    1. In the **Logic** tab, create a new **Server Action** and add the following Variables:
        
        * `SortForAggregate` Input Parameter.
        * `SortForSQL` Output Parameter.
        * `Entity` Local variable.
        * `Attribute` Local variable.

    1. Set the **Name** of the new action to `EncodingSortForSQL` and set the **Function** property to **Yes**.

    1. Add **Text.Regex_Replace** server action (probably you have to add the dependency to the **Text** extension and **Regex_replace** server action) between the **Start** and **End** elements, and set the following properties:
        
        * `Text` = `SortForAggregate`
        * `Pattern` = `"[^\w. ]"`
        * `Replace` = `""`
    
    1. Add an **Assign** between the **Text.Regex_Replace** and **End** elements. Add the following assignment:
    
        * `SortForAggregate` = `Regex_Replace.Result`

    1. Add an **If** between the **Assign** and **End** elements, and set the **Condition** to the following expression:

            Index(SortForAggregate,".") <> -1

    1. Add an **Assign** to the **False** branch of the previous **If**. Add the following assignment:

        * `SortForSQL` = `SortForAggregate`

    1. Add an **Assign** and connect it to the **True** branch of the **If**. Add the following assignment:

        * `Entity` = `"{" + Substr(SortForAggregate,0,Index(SortForAggregate,".")) + "}"`

    1. Add and connect an **If** to the right of the **Assign** created on the previous step. Set the **Condition** to the following expression:

            Index(SortForAggregate,"DESC",ignoreCase: True) <> -1
    
    1. Add and connect an **Assign** to the **True** branch of the **If**. Add the following assignments:
        *  `Attribute` = `"[" + Substr(SortForAggregate,Index(SortForAggregate,".")+1,Index(SortForAggregate," ")-Index(SortForAggregate,".")-1) + "]"`

        *  `SortForSQL` = `Entity + "." + Attribute + " DESC"`

    1. Add and connect an **End** element to the right of the **Assign**.

    1. Add and connect an **Assign** to the **False** branch of the **If**. Add the following assignments:
        *  `Attribute` = `"[" + Substr(SortForAggregate,Index(SortForAggregate,".")+1,Length(SortForAggregate)) + "]"`

        *  `SortForSQL` = `Entity + "." + Attribute`

    1. Add and connect an **End** element to the bottom of the previous **Assign**.

1. Set the **SortForSQL** parameter of your **SQL** query to `EncodingSortforSQL(TableSort)`.

    ![](images/set-sql-parameter-ss.png)
