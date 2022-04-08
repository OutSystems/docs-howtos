---
summary: Reference information about migrating Module elements from Traditional App to Reactive App.
tags:
locale: en-us
guid: edb1d08a-8c4f-49bf-9373-855a24a370d5
---

# Module elements

This section provides you with an overview of the elements that are relevant to the Module (eSpace) level of migration, with details on how to approach creating new logic in Reactive App.

## Entity { #entity }

When migrating logic that deals with Entities to the Reactive Web App, pay attention to those which you need to make public or set **Expose Read-Only** to false.

Creating a new Entity in your Reactive Web App creates a new physical table. With this in mind, the suggestion is to change the Entity to be public, then add a reference to it in the Reactive Web Module.

You can also use the [accelerators for migrating Entities](reference.md#accelerators) (copy and paste them).

## Multilingual Locales { #multilingual }

Starting with the Platform Server release 11.10, OutSystems has an integrated translations mechanism for adding and managing translations in Reactive Web and Mobile apps directly in Service Studio. Refer to [Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Multilingual_Reactive_Web_and_Mobile_Apps) for more information about this feature.

If you used the [Multilingual Forge component](https://www.outsystems.com/forge/component-overview/1784/multilingual-component) to translate your app to several languages, you need to migrate your translations to Service Studio. Read the [How to reuse translations from Multilingual Forge component in Service Studio](https://success.outsystems.com/Documentation/How-to_Guides/Front-End/How_to_reuse_translations_from_Multilingual_Forge_component_in_Service_Studio) document to learn about this process.

## On session start

<div class="info" markdown="1">

Use the On Application Ready Event in Reactive App to set the initial values of Client Variables as the configuration parameters in the app.

</div>

When you use **On Session Start** in the Traditional Web App to initialize the **Session Variables**, migrate the logic in the Reactive Web App in a place where you read the variables, and protect it by checking if you defined the variable. For example, if you're using Cookies, add the logic before calling GetCookie, so it runs only if the Cookie wasn't set before.

If you use **On Session Start** otherwise in the Traditional Web App, you need to evaluate case-by-case. Take into consideration that this logic runs on the first server request and when a user logs in and on the first request after having logged out.

## Process

Change the **Process** to be public in the original Module and reference the **Process**, to avoid losing data.

## Role { #roles }

To avoid losing data, change the **Role** to be public in the original Module and reference the **Role**. Afterward, confirm that all the Screen permissions are the same.

## Server Action

The way you migrate a **Server Action** to the Reactive Web App depends on whether the Action is public, its use on the Screens, and whether you can use it on the client side in the new Reactive Web App. Check the [accelerators section](reference.md#accelerators) to learn how you can use copy and paste with these Actions.

### Not used as a function

You can migrate it directly to a **Server Action** in the Reactive Web App.

### Used as a function with input parameters

Migrate this Action so that it's called after the calculation of the input parameters, typically at the end of a data action. Create a **Data Action** with an output for each Action. The **Data Action** should call the server Actions in the same order used in the Traditional Web App screen.

### Used as a function with a constant number of times in a Screen

The screen uses the **Server Action** for a constant number of times (not in a List). Migrate the Action to **Server Action** in the Reactive Web Module while creating a local variable for each function call.

### Used as a function with a variable number of times in a Screen

The screen uses the **Server Action** for a variable number of times on the Screen (in a List). Migrate the Action to **Server Action** in the Reactive Web Module. Then, add a calculated attribute in an Aggregate that creates the list that calls the function.

## Session Variable { #session-variable }

<div class="info" markdown="1">

Client Variables in Reactive Web Apps are in many ways similar to the Session Variables. Use them with the On Application Ready Event to initialize global configurations for the apps, like instantiating username, locale, filters. 

Keep in mind:

* The value of Client Variables clears when the user signs out
* On Application Ready System Event triggers every time you run the app in a new tab/browser

</div>

The migration of a Session Variable depends on whether it ties to a browser session or user preference, its data type, and whether it contains confidential information.

Traditional Web Apps use [Session Variables](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Session_Variable) to store data on the server side in a key-value format. In Reactive Web Apps, [Client Variables](https://success.outsystems.com/Documentation/11/Reference/OutSystems_Language/Data/Handling_Data/Client_Variable) are in the **Data** tab. Create them here, and set their default value.

Use Client Variables to cache user information that you don't want to fetch multiple times from the server or to store interface state information. Following the [Reactive Web Best Practices](https://www.outsystems.com/nextstep/2019/?wchannelid=lxt52ix89e&wmediaid=r85tt3f3hm), it isn't possible to use Client Variables of type: List, Record, Structure, and Entity.

Share Client Variables in a Module by wrapping with public Client Actions.
Initialize the interface state information on the server side through cookie settings, and then load it to Client Variables during the screen initialization.

<div class="warning" markdown="1">

Be aware of security best practices, such as not exposing table identifiers which can be exploited by malicious server-side calls. Check the user roles on the server-side calls only. For more information about security in Reactive Web Apps, see the [Reactive Web security best practices](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices).

</div>

### Site Property { #site-property }

To preserve their current values, copy the values from the original Traditional Web Module to the new Reactive Web Module via Service Center.

### Tied to a browser session

If the Session Variable ties to the browser session and the data type is simple, migrate it to a browser-session-lived cookie using some name convention (for example, `SessionVariable_NAME`). Keep in mind that the values aren't cleared on log out.

Replace reads and writes by the `GetCookie` and `SetCookie` methods of `HTTPRequestHandler`.

Alternatively, for better client-side read performance, use a JavaScript Node to get the cookie value from `document.cookie`.

If there are Widgets bound to the variable, create a Local Variable to bind them to and then sync the value with the cookie.

Note that the data type distinction is important because cookies have limits, and storing complex types there can be extremely inefficient.

### Used for storing a user preference

If you use the variable to store a user preference (meaning it ties to the user, not the browser session):

* If it's only used in the UI/client-side logic store the value in a client variable
* If the server side uses session variables, migrate the variable so the logic uses a row in a database Entity, associated with a User Id.

You might need additional work for variables of List and Record data types (for example, you may need to devise an encoding, use a separate table, or other).

### Other

If you don't find the session variable use case described in this section, then you need to evaluate the migration case-by-case.

## Theme

Copy the CSS you need from the Traditional Web App into the Theme of the Reactive Web App.

Be aware that you may need to adapt your CSS to work with OutSystems UI. If you're migrating from Silk UI, check [Migrating UI of the Silk Web applications to OutSystems UI Framework](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Migrating_UI_of_the_Silk_Web_applications_to_OutSystems_UI_Framework) for more information.

## UI flow

The new UI flows of the Reactive Web App should point to the new Theme. You can't migrate the advanced properties HTTP Security, Integrated Authentication, and Internal Access Only.

For reference information about migrating the Traditional Web Apps Front-end to Reactive Web continue to [Front-end](<ref-frontend-intro.md>).

---

Documents in this section:

* [Introduction to migrating Traditional Web to Reactive Web Apps](intro.md)
* [Differences to consider between Traditional and Reactive Web Apps](differences.md)
* [Suggested stages of Traditional to Reactive Web App migration](stages.md)
* [Traditional to Reactive Web App migration reference](reference.md)
    * [Module elements](ref-module-elements.md)
    * [Front-end](ref-frontend-intro.md)
        * [User Interface](ref-frontend-ui.md)
        * [UI Flow elements](ref-frontend-ui-flows.md)
        * [Screen and Block logic](ref-frontend-screen-and-block.md)
        * [System Actions](ref-system-actions.md)
    * [Core Widgets](ref-core-widgets.md)
