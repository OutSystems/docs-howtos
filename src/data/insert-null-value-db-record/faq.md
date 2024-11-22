---
summary: Learn to insert null values in a database with OutSystems 11 (O11) using SQL nodes to handle null inputs.
guid: ba5cba5e-31eb-447e-a9d6-6e766a62aebf
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=942:258
tags: database operations, sql, data types, default values, null handling
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
content-type:
  - procedure
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

![Screenshot of an OutSystems SQL node configuration showing parameters and query setup.](images/How-to-insert-a-null-value-into-a-database-record_0.png "SQL Node Configuration")

To pass data to the query parameter ActivityNodes, check if the value:

* If empty, pass the string "null".

* Otherwise, pass the value encoded as SQL.

<div class="warning" markdown="1">
Use EncodeSql() to avoid SQL injection on query parameters with Expand Inline.
</div>

![Code snippet for handling null values in an SQL query parameter in OutSystems.](images/How-to-insert-a-null-value-into-a-database-record_1.png "SQL Query Parameter Code")

This way you can build the code generic enough for different DBMS, and you are avoiding business logic inside the query.

More information:

[**Available data types**](https://success.outsystems.com/documentation/11/reference/outsystems_language/data/data_types/available_data_types/)

Defines the default values for each type.

