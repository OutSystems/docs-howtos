---
guid: ba5cba5e-31eb-447e-a9d6-6e766a62aebf
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to insert a null value into a database record

## Question

How to insert a null value into a field?

When I try to insert null, I get 0.

## Answer

OutSystems Platform always assumes default values for the built-in types.

The built-in actions to create and/or update the database write values to the database, unless the attribute is a foreign key. To avoid problems with constraints, foreign keys are stored as null if not defined. But an undefined decimal is written as 0.

Use a SQL node to save nulls to the database. You can build code generic enough for different DBMS and avoid having business logic inside the query.

In the example below, a SQL node has two inputs. ActivityNotes is a text input with the property Expand Inline defined to yes. This means that the value of ActivityNotes input will be injected directly into the query.

![image alt text](images/How-to-insert-a-null-value-into-a-database-record_0.png)

To pass data to the query parameter ActivityNodes, check if the value:

* If empty, pass the string "null".

* Otherwise, pass the value encoded as SQL.

<div class="warning" markdown="1">
Use EncodeSql() to avoid SQL injection on query parameters with Expand Inline.
</div>

![image alt text](images/How-to-insert-a-null-value-into-a-database-record_1.png)

This way you can build the code generic enough for different DBMS, and you are avoiding business logic inside the query.

More information:

[**Available data types**](http://www.outsystems.com/help/servicestudio/9.0/default.htm#Language_Reference/Data_Types/Available_Data_Types.htm)

Defines the default values for each type.

