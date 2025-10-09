---
tags: ui patterns, web development, autocomplete functionality, performance optimization, outsystems ui
summary: Learn how to implement a server-side filtered autocomplete search field in a Traditional Web App using OutSystems 11 (O11).
guid: 5aad9f1a-b906-4e68-a058-3b34646444b7
locale: en-us
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:5
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to create a search field with autocomplete in a Traditional Web App

If you have a long list of results to filter, using the [Dropdown Select](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Patterns/Using_Traditional_Web_Patterns/Controls/Dropdown_Select) pattern may impact the performance of your app since it returns the unfiltered results before filtering them in the client side.

To filter the results in the server side and send the filtered list to your app you can use the **Input_AutoComplete** rich widget.

To use **Input_AutoComplete** with an input widget follow these steps:

1. In the module which contains the input widget to which you want to add the auto complete to, open **Manage Dependencies** and add the following dependencies:

    * Add the **Input_AutoComplete** rich widget and the **Input\_AutoComplete\_ShowList** action from the **RichWidgets** producer.

1. Set the **Name** and **Variable** properties of the search field input widget to a **Local Variable** (in this case `UserSearch` and `Name_Search`).

    ![Screenshot showing how to set the Name and Variable properties of the search field input widget.](images/autocomplete01.png "Setting Name and Variable Properties")

    ![Image displaying the configuration of a local variable for the search field in a web application.](images/autocomplete03.png "Local Variable Configuration")

1. Add an **Input_AutoComplete** RichWidget next to the input widget and set the **InputWidgetId** property to the Id of the input.

    ![Screenshot of the Input_AutoComplete RichWidget being added next to the input widget.](images/autocomplete00.png "Adding Input_AutoComplete Widget")

    ![Image showing the setting of the InputWidgetId property for the Input_AutoComplete widget.](images/autocomplete06.png "InputWidgetId Property Setting")

1. Set the **On Notify**>**Destination** property of Input_AutoComplete to a newly created Screen Action, in this case **UsersAutoComplete**.

    ![Screenshot illustrating how to set the On Notify Destination property of the Input_AutoComplete widget.](images/autocomplete07.png "On Notify Destination Configuration")

1. Add an Aggregate to the Screen Action and create a Filter using the Local Variable to limit the query results according to what's typed in the Input Widget.

    ![Image depicting the addition of an Aggregate to the Screen Action for filtering query results.](images/autocomplete11.png "Filtering with Aggregate in Screen Action")

    In this case the Filter `Users.Name like Name_Search+"%"` only retrieves users whose `Name` Attribute starts with what's typed in the Input Widget.

1. Add an **Input\_AutoComplete\_ShowList** Server Action after the Aggregate.

1. Set the **Action**>**InputWidgetId** property to the Id of the Input and the **Action**>**List** to the Aggregate's List, in this case `GetUsersforAutoComplete.List`.

    ![Screenshot showing the configuration of the Input_AutoComplete_ShowList server action.](images/autocomplete10.png "Configuring Input_AutoComplete_ShowList")

    Be sure to map the **Label** and **Identifier** properties. The **Label** holds the value displayed in the autocomplete list, and the **Identifier** holds the Identifier of those values.

    The Screen Action should look similar to the following image.

    ![Image providing an overview of the Screen Action setup for the autocomplete functionality.](images/autocomplete09.png "Screen Action Overview")

    The action queries the database for the **autocomplete** suggestions that appear below the Input field.

1. Publish the module by selecting **1-Click Publish**.

After these steps the search field in your app shows a list of suggestions that changes as you type.

![Screenshot demonstrating the autocomplete suggestions appearing below the search field as a user types.](images/autocomplete13.png "Autocomplete Suggestions Display")

<div class="info" markdown="1">

To access the Identifier of the selected user use the **Input\_AutoComplete\_GetIdentifier** Server Action from the **RichWidgets** module. Before using this action you have to add it as a dependency to your module.
</div>
