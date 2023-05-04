---
tags: 
summary: Learn how to use screen actions as callbacks in UI element events 
guid: 0872EBF9-3413-4F52-8E32-4239C888CEE3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---


# How to use screen actions as callbacks on UI element events 

Using screen actions as callbacks can be helpful when you want to run a screen action to change the UI or call server side actions after a custom event in a UI component.    

The following example showcases how you can use screen actions as callbacks. The scenario demonstrates how you can display a message to the user when a Date Picker is open.

## Prerequisites

* A screen containing the Date Picker component from OutSystems UI.
* The Date Picker must have the **OptionalConfigs** > **MinDate** property set to **CurrDate()**.

## Prepare the UI to display the message  

1. In **Service Studio**, go to the **Interface** tab and select the Date Picker component.
1. In the **Widget tree**, select **Date Picker** and enter Date Picker property **Name**, for example **DatePicker**.
1. In the **Widget tree**, right click your screen name and select **Enclose in Container**.
1. From the **Toolbox**, drag a container next to the Date Picker container and add an info-circle icon and add the message to display, for example, **Only dates in the future are accepted**.

## Create logic to show or hide the message

1. On the screen with the Date Picker, create a boolean **Local variable** and name it **PickerIsOpen**. This variable controls the message visibility.
1. In the **Widget Tree**, select both the icon and the message, then right click and select **Enclose in If**.
1. Set the **Condition** property to the **PickerIsOpen** boolean variable.
1. On the screen create a new **Client action** called **TooglePickerDateStatus**.
1. Add an **Assign** node and set **PickerIsOpen** to **not PickerIsOpen**

## Use the Date Picker event to show or hide the message

1. To create a handler for the Initialized event, go back to the screen, select the Date Picker, and from the **Handler** dropdown, select **New Client Action**. 
1. Add a JavaScript node to the client action and call it **HandleOpenAndCloseEvent**.
1. Add an input parameter in the JavaScript node called **WidgetId** of type **Text**.
1. To set the **TooglePickerDateStatus** client action as the callback for the Date Picker's open and close events, use the ollowing JavaScript code inside the JavaScript node:

    ``OutSystems.OSUI.Patterns.DatePickerAPI.SetProviderEvent($parameters.WidgetId,'onOpen', $actions.TogglePickerDateStatus);``

    ``OutSystems.OSUI.Patterns.DatePickerAPI.SetProviderEvent($parameters.WidgetId,'onClose', $actions.TogglePickerDateStatus);``

<div class="info" markdown="1">

The Date Picker component is built on top of the **flatpickr library**. For more information about the events that handle the opening and closing of the Date Picker, see [Events](https://flatpickr.js.org/events/#events)

</div>


