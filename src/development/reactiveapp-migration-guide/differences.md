---
summary: Overview of differences between Traditional Web Apps and Reactive Web Apps, from the perspective of migrating to the new Reactive runtime.  
tags:
locale: en-us
guid: 013992fc-35b0-485d-9097-68a0d1b1afc8
---

# Differences to consider between Traditional and Reactive Web Apps

<div class="info" markdown="1">

We've been working on these documents. Please let us know how useful this new version is by voting.

</div>

This document presents some differences between the Traditional Web and Reactive Web Apps, in the context of migrating to the newer Reactive runtime. Refer to your Traditional apps and check how you implemented user experience and logic related to these new features, and assess what you need to change in the new runtime.

## Traditional Web App elements not available for Reactive Web Apps

<div class="info" markdown="1">

Check the document [Traditional to Reactive migration reference](reference.md) for a detailed technical overview.

</div>

These are the elements commonly used in the Traditional Web that aren't available for Reactive Web Apps. These documents also provide some helpful tips on how you can get similar functionality in the new app.

### Ajax Refresh

Ajax Refresh in Traditional Web Apps refreshes parts of the interface. The UI elements in Reactive App refresh automatically on data change, so you don't need to use Ajax Refresh.

### Entry

The Entry node in Traditional Web Apps defines the default page that loads in the UI Flow. It points to the index Screen of the flow.

Go to [Entry Point](ref-frontend-ui-flows.md#entry-point) to learn more about migrating Screen entry points.

### Notify

**Notify** and **NotifyGetMessage** enable Widgets in the Traditional Web to exchange data, and they're not available in Reactive Web.

In Reactive Web Apps, use Events and corresponding handler Actions. Check how to do that in [Use Events to Propagate Changes From a Block to the Parent](<https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Reuse_UI/Use_Events_to_Propagate_Changes_From_a_Block_to_the_Parent>). 

### Exception handler

You can catch exceptions on both the client and server side. Read more about is the [flow exception handler reference](ref-frontend-ui-flows.md#flow-exception-handler).

### Preparation

Preparation, a dedicated server-side Action that loads initial data for Screens, doesn't exist in the client-side Reactive interface. The absence of the Preparation Action is an important difference between Traditional Web Apps and Reactive Web Apps. You need to recreate the data fetched on the client side. Refer to the [Preparation](ref-frontend-screen-and-block.md#screen-prep) section to read about the process.

### Session Variable

Session Variables are a server-side feature of Traditional Web Apps to store session information that you can access across the app. In Reactive Web Apps, store information in [Client Variables](<https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Client_Variable>), which you can initialize the On Application Ready System Event.

For details on how to migrate this element to Reactive, check the notes on migration [Session Variables](ref-module-elements.md#session-variable).

### Date Time in Reactive

Reactive Web Apps treat date and time values like Mobile Apps. The Date and Time values are always UTC, even when requested from the server.
When you use them in the app UI, there's a value conversion to the local time of the device. Read more about this in the [Date Time documentation](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Data_Types/Available_Data_Types#date-time-notes).

## Improved practices in Reactive 

This section provides general notes about the changes in how you approach development in the Reactive Web Apps when compared to Traditional Apps.

### More Client Actions, less custom JavaScript

The focus of Reactive Apps is the Front-end, driven by the client-side logic. This should enable you to use less custom JavaScript, replacing it with Client Actions. Use Client Actions instead of custom JavaScript code whenever possible.

### Optimize data fetching on the client side

Design how Aggregates of a Reactive Web App should fetch data, by setting Aggregate **Fetch** property to `At Start` or `Only On Demand`. This provides a lot of flexibility for designing UI Patterns and speeds up the responsiveness of the UI. Check [Implement asynchronous data fetching using Aggregates](<https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Data/Query_Data/Implement_asynchronous_data_fetching_using_Aggregates>) for an example.

### Use Libraries for solid architecture

You can use Libraries to optimize the number of dependencies in the environment where the apps are running. You can also convert an existing Mobile or Reactive Module to a Library. Check the [Libraries documentation](https://success.outsystems.com/Documentation/11/Developing_an_Application/Reuse_and_Refactor/Libraries) to verify if this type of Module fits your use case.

### Use client-side validation for quick feedback about values

Reactive Web Apps provides an efficient way to validate data on the client side. There's an example in [Validate Form Inputs](<https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Forms/Validate_Form_Inputs>). The client-side validation is there for a quick feedback to your users about the values they're submitting. However, you should implement your server-side validation to make sure that the correct data gets saved in the database.

Continue to the [Suggested stages of Traditional to Reactive App migration](<stages.md>).

---

Documents in this section:

* [Introduction into migrating Traditional Web to Reactive Web Apps](<intro.md>)
* [Differences to consider between Traditional and Reactive](<differences.md>)
* [Suggested stages of Traditional to Reactive App migration](<stages.md>)
* [Traditional to Reactive App migration reference](<reference.md>)
	* [Module elements](<ref-module-elements.md>)
	* [Front-end](<ref-frontend-intro.md>)
	    * [User Interface](<ref-frontend-ui.md>)
	    * [UI Flow elements](<ref-frontend-ui-flows.md>)
	    * [Screen and Block logic](<ref-frontend-screen-and-block.md>)
	    * [System Actions](<ref-system-actions.md>)
	* [Core Widgets](<ref-core-widgets.md>)