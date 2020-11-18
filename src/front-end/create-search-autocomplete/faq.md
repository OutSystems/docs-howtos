---
tags: runtime-traditional; support-Front_end_Development; support-webapps;
summary: Learn how to use the Input_AutoComplete RichWidget to filter results in the server side while an end user types in an input field.
---

# How to create a search field with autocomplete in a Traditional Web App

1. Set the **Name** and **Variable** properties of the search field input widget to a **Local Variable** (in this case `UserSearch` and `Name_Search`).

    ![](images/autocomplete01.png)

    ![](images/autocomplete03.png)
    
1. Add an **Input_AutoComplete** RichWidget next to the input widget and set the **InputWidgetId** property to the Id of the input.

    ![](images/autocomplete00.png)

    ![](images/autocomplete06.png)

1. Set the **On Notify**>**Destination** property of Input_AutoComplete to a newly created Screen Action, in this case **UsersAutoComplete**.

    ![](images/autocomplete07.png)

1. Add an Aggregate to the Screen Action and create a Filter using the Local Variable to limit the query results according to what's typed in the Input Widget.

    ![](images/autocomplete11.png)

    In this case the Filter `Users.Name like "%"+Name_Search+"%"` only retrieves users whose `Name` Attribute includes what's typed in the Input Widget.

1. Add an **Input\_AutoComplete\_ShowList** Server Action after the Aggregate.

    Set the **Action**>**InputWidgetId** property to the Id of the Input and the **Action**>**List** to the Aggregate's List, in this case `GetUsersforAutoComplete.List`.

    ![](images/autocomplete10.png)

    Be sure to map the **Label**and **Identifier** properties; the **Label** holds the value displayed in the autocomplete list and the **Identifier** holds the Identifier of those values.

    The Screen Action should look similar to the following image.

    ![](images/autocomplete09.png)

    The action queries the database for the **autocomplete** suggestions that appear below the Input field.

After these steps the search field shows a list of suggestions that changes as you type.

![](images/autocomplete13.png)

<div class="info" markdown="1">
To access the Identifier of the selected user use the **Input\_AutoComplete\_GetIdentifier** Server Action.
</div>
