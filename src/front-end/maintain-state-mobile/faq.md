---
tags: local storage, client actions, mobile app navigation, ui state management, data persistence
summary: Learn how to maintain the state of a mobile screen across navigation in OutSystems 11 (O11) using local storage and client actions.
guid: 1ab580bd-06db-488c-bcfa-133209853697
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:44
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How to maintain the state of a mobile screen

How can I maintain the state of a screen in a mobile app while navigating across screens?

For instance, in this app, the home screen has a list of To-Do items and notes concerning each item. 

![Screenshot of the home screen in a mobile app displaying a list of To-Do items with titles and notes.](images/maintain-state-1.png "Home Screen with To-Do List")

If I click on the search icon, I am redirected to a Search screen where I can search the list of To-Dos by title and by the contents in the notes. 

![Screenshot of the search screen in a mobile app with input fields for searching To-Do items by title and notes.](images/maintain-state-2.png "Search Screen Interface")

I want to maintain the user input in the Search screen across navigation to other screens.

## Answer

Note that the state of the previous screens in a mobile app is automatically maintained if you use the back button.

To maintain the values of the fields in the Search screen after you navigate forward to other screens and come back to it:

1. In the **Data** tab, create an entity SearchFormData in the Local Storage with attributes SearchTitle and SearchNotes, both of type Text, and change the type of the Id to User Identifier.

    ![Screenshot showing the creation of a Local Storage entity named SearchFormData with attributes for search functionality.](images/maintain-state-5.png "Local Storage Entity Creation")

1. In the **Interface** tab, in the Elements Tree, right-click the screen Search, select Fetch Data from Local Storage and set the source as the SearchFormData entity. Filter the resultant GetSearchFormData aggregate by UserId.

    ![Screenshot of the process to fetch data from Local Storage by filtering the GetSearchFormData aggregate by UserId.](images/maintain-state-6.png "Fetching Data from Local Storage")

1. In the properties of the widgets, assign **Input_SearchTitle** with `GetSearchFormDataByUserId.List.Current.SearchFormData.SearchTitle` and **Input_SearchNotes** with `GetSearchFormDataByUserId.List.Current.SearchFormData.SearchNotes`.

1. In the properties of SearchForm that encloses the Input widgets, create a new **onchange** event and select **(New Client Action)** from the dropdown.

    ![Screenshot of the Search screen with an onchange event setup for the SearchForm in the mobile app interface.](images/maintain-state-7.png "Search Screen OnChange Event")

1. In the action flow of the Input_FieldOnChange, assign the current User Id as the value of the Id of that aggregate record.

1. From the Data tab, drag the CreateOrUpdateSearchFormData client action to the action flow and set the source record to `GetSearchFormDataByUserId.List.Current.SearchFormData`.

   ![Screenshot of the action flow for creating or updating SearchFormData in the mobile app.](images/maintain-state-8.png "Create or Update Data Action Flow")

At the end of the user session, clear the temporary data stored in the SearchDataForm entity.