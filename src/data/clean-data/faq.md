---
tags: version-10; support-Database
summary: Explore how to delete test data from entities in OutSystems 11 (O11) using SQL queries and back office screens.
guid: 8796fe43-091c-4613-a9ac-9babde52b7a2
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/5uD7gg1CIy1jlOE2BNFdsU/Data?node-id=942:233
---

# How to delete data from Entities

How do I erase test data from Entities? 

For example: I have two Entities (`Location` and `Store`) with test data, and I wish to clear them both. 

![Diagram showing the relationship between Location and Store entities, with Location having fields Id, City, Country and Store having fields Id, Name, LocationId.](images/sqldelete-00.png "Entity Relationship Diagram")

Note: My `Store` Entity has a Foreign Key to my `Location` Entity.

## Answer

To delete all test data from your Entities you need to create your own logic and a back office screen. Follow these steps:

1. Create a new Server Action (in this case **ClearData**) and add a SQL Query. Add a "dummy" Output Entity/Structure to the SQL Query, in this case `Location`.

1. Add the following SQL snippet to the SQL Query:

        DELETE FROM {Store};
        DELETE FROM {Location};

    This will first delete all data from the `Store` Entity and then it will delete all data from the `Location` Entity. The order of deletion is important, first delete data from the child Entity (that references another Entity) and only then delete data from the parent Entity.
    
    ![Screenshot of the ClearData SQL Query in Service Studio with DELETE statements for Store and Location entities.](images/sqldelete-01.png "SQL Query in Service Studio")

1. Create a new Web Screen (in this case **BackOffice**), add a Button to it and set the `On Click`>`Destination` to a new Screen Action, in this case **ClearTestData**.

1. Inside the **ClearTestData** Screen Action call the **ClearData** Server Action.

    ![Flowchart in Service Studio depicting the ClearTestData screen action calling the ClearData server action.](images/sqldelete-02.png "ClearTestData Screen Action Flow")
    
    
