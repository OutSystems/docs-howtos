---
summary: Explore the migration process from unsupported to supported Firebase-based mobile plugins in OutSystems 11 (O11) for enhanced app performance and support.
tags:
locale: en-us
guid: 0999bb9f-af58-4fc6-ba6d-9c411958eedc
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/XbkdagtFJ9kxan8pAx0Qsz/DevOps?node-id=1542:374
---

# Migrating to the supported Firebase-based mobile plugins

You can use two types of Firebase-based plugins in your apps: **supported plugins** and **unsupported plugins**. This document provides guidance on how to migrate from older unsupported Firebase-based plugins (namely **Firebase Mobile**), to the newer and supported plugins. To migrate from an unsupported plugin to a supported one, refactor your apps by replacing actions in your logic. This is a straightforward process as plugins behave the same way, adopt the same parameters, and follow similar naming conventions. 

Firebase-based plugins offer an integration with Firebase. Firebase is a Google mobile development platform. It speeds up many of the common development patterns for mobile apps. OutSystems recommends that you use the **supported plugins**, as that's in the best interest of both end users and developers of the apps. By using OutSystems supported plugins you can count on the following advantages:

* Dedicated plugin for each feature with own release cycle
* OutSystems support teams to assist you
* Regular updates and visibility over changes
* Compatibility at day zero with new versions of MABS
* New features, particularly in the Performance and Crash Reporting plugins
* [Dynamic Links](https://www.outsystems.com/forge/component-overview/10988/dynamic-links-plugin-firebase), a new Firebase-based plugin 

| Supported plugin                                                                                   | Description                                                                            |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| [Analytics](https://www.outsystems.com/forge/component-overview/10704/firebase-analytics-plugin)   | Understand user behavior by viewing live usage data with real-time reporting.          |
| [Performance Monitoring](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10706) | Gain insight into the performance of your mobile apps.                                 |
| [Crash Reporting](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10705)        | Get real-time crash reporting to help you track, prioritize, and fix stability issues. |
| [Cloud Messaging](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=12174)        | Send, receive and manage notifications. |

This document refers to the OutSystems plugins as **supported plugins**. Forge also contains **unsupported plugins**, which are mostly the plugins contributed by partners and community.

<div class="info" markdown="1">

The Analytics, Performance, and Crash Reporting plugins by OutSystems cover all the features with the matching components of the unsupported Firebase-based plugin.

</div>

## Setting up the plugins

To function properly, you need to set up the plugin in both the Google console and your app. See the instructions in [Firebase Plugins](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/Mobile_Plugins/Firebase_Plugins) to set up your plugin.

## Sample app

Install [Firebase Sample App](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=10707&ProjectName=firebase-mobile-sample-app) from Forge and open the app in Service Studio. The sample app contains logic for common use cases, which you can examine and recreate in your apps. For example, the sample app shows how to:

* Log app custom events (for example, user signs in)
* Set the UserId property
* Set user properties (for example, user language)
* Set the current screen name, to specify the app visual context
* Set the parameters that the plugin sends with every event logged from the device, including automatic events
* Receive and handle push notifications from Firebase Cloud Messaging

![Screenshot of the Firebase Sample App interface showing options for Analytics, Crashlytics, Performance, and Cloud Messaging.](images/migrate-to-firebase-sample-app.png "Firebase Sample App Interface")

## Example of migrating a logging event with the Analytics Plugin

If you are using the **LogEvent** of the unsupported plugin, follow these steps to migrate to the supported Analytics plugin. You can log events anywhere inside a logic flow. To log an event, drag the **LogEvent** action provided by the Analytics Plugin to the logic inside of the part of the app where you want to create a log event.

<div class="info" markdown="1">

See [Reference of the plugin actions](#reference-of-the-plugin-actions) for more information.

</div>

1. Delete the **LogEvent** action of the unsupported plugin.

    ![Service Studio screenshot showing the legacy LogEvent action in a logic flow.](images/migrate-to-firebase-legacy-ss.png "Legacy LogEvent Action in Service Studio")

1. Solve the errors Service Studio highlighted after you deleted  the former LogEvent action. Start by dragging LogEvent action from the supported Analytics plugin folder. Service Studio automatically renames the action to **LogEvent2** in logic flows where the module references both plugins.

    ![Service Studio screenshot highlighting the process of fixing errors after deleting the legacy LogEvent action.](images/migrate-to-firebase-fix-errors-ss.png "Fixing Errors in Service Studio")

1. Substitute all parameters from the old **LogEvent** action with equivalent parameters from the new **LogEvent2** action.

    ![Screenshot showing the substitution of parameters from the old LogEvent action to the new LogEvent2 action in Service Studio.](images/migrate-to-firebase-params-ss.png "Migrating Parameters to New LogEvent Action")

1. Optionally, set any other parameters to capture additional information and get metrics from the Google Console dashboard.
  
    ![Screenshot of Service Studio where additional parameters are being set for the new LogEvent2 action.](images/migrate-to-firebase-additional-values-ss.png "Adding Additional Parameters in Service Studio")
    
## Example of sending and receiving a notification with the Cloud Messaging Plugin

If you want to subscribe to a topic and receive notifications for it, follow these steps:

<div class="info" markdown="1">

See [Reference of the plugin actions](#reference-of-the-plugin-actions) for more information.

</div>

1. Call the **Subscribe** client action of the supported plugin.

    ![Screenshot showing the Subscribe client action in a logic flow within Service Studio.](images/migrate-to-firebase-subscribe-topic.png "Subscribing to a Topic in Service Studio")

1. Include the **NotificationsHandler** block in the screen on which you want to handle the notifications. If you want to see these as in-app notifications, you can use the **NotificationDialog** block as a placeholder, or implement your own logic.

    ![Screenshot of Service Studio displaying the NotificationsHandler block used for handling notifications.](images/migrate-to-firebase-cloud-block.png "Cloud Messaging Notification Handler Block")

1. Send a POST request to endpoint `baseURL/notification/topics` of the Cloud Messaging Configurator's REST API.

    ![Screenshot of a REST API request setup for sending notifications to a topic in Cloud Messaging Configurator.](images/migrate-to-firebase-rest-api.png "Cloud Messaging REST API Request")

1. See notifications in the device, whether in the notification center or inside your app as in-app notifications.
  
    ![Screenshot showing a notification from Firebase Cloud Messaging on a mobile device's screen.](images/migrate-to-firebase-notifications.png "Notifications on a Device")


## Reference of the plugin actions

This section contains the comparison of the relevant actions between supported and unsupported plugins. To migrate to a supported plugin, refactor your apps by replacing the actions in the logic. The input and output parameters of these actions behave in the same way.

### Analytics

The list of relevant actions in the two plugins.

| Firebase Mobile (unsupported) | Analytics Plugin (supported) |
| ----------------------------- | ---------------------------- |
| LogEvent                      | LogEvent                     |
| SetAnalyticsCollectionEnabled | SetEnabled                   |
| SetScreenName                 | SetCurrentScreen             |
| SetUserProperty               | SetUserProperty              |

Check out the [sample app](#sample-app) to see how to:

* Log an application custom event (for example, the user signs in)
* Set the UserId property
* Set a user property (for example, the user's language)
* Set the current screen name
* Set the parameters that the apps sends with every event logged from the device, including automatic events

### Cloud Messaging

The list of relevant actions in the two plugins.

Firebase Mobile (unsupported) && Firebase CM Compat R&D (unsupported) | Cloud Messaging Plugin (supported) |
| --------------------------------------------------------------------| ---------------------------------- |
| ClearAllNotifications                                               | ClearNotifications                 |
| GetBadgeNumber                                                      | GetBadgeNumber                     |
| GetToken                                                            | GetToken                           |
| GrantsPermission                                                    | -                                  |
| HasPermission                                                       | -                                  |
| InitCloudMessaging                                                  | -                                  |
| RegisterDevice                                                      | RegisterDevice                     |
| SetBadgeNumber                                                      | SetBadgeNumber                     |
| SubscribeToTopic                                                    | Subscribe                          |
| UnsubscribeToTopic                                                  | Unsusbscribe                       |
| UnregisterDevice                                                    | UnregisterDevice                   |
| -                                                                   | GetPendingNotitications            |
| -                                                                   | SendLocalNotification              |

While the unsupported plugin has only one block, **FirebaseCloudMessaging**, the supported plugin has two: **NotificationsHandler** and **NotificationDialog**.

The NotificationsHandler block is the equivalent to the FirebaseCloudMessaging block. Learn more about the NotificationDialog block in the [plugin's documentation page](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/Mobile_Plugins/Firebase_Plugins/Firebase_Cloud_Messaging_plugin). 

The following table lists each of the block’s client actions and events, as well as how they relate to each other.

Firebase Mobile (unsupported) | Firebase CM Compat R&D (unsupported) | Cloud Messaging Plugin (supported) |
| --------------------------- | ------------------------------------ | ---------------------------------- |
| NotificationHandler         | Handler_OnMessage                    | OnDefaultNotificationReceived      |
| -                           | -                                    | OnSilentNotificationReceived       |
| -                           | Handler_OnBackgroundMessage          | -                                  |
| ErrorHandler                | ErrorHandler                         | -                                  |
| NewNotification             | OnMessage                            | DefaultNotificationReceived        |
| -                           | -                                    | SilentNotificationReceived         |
| -                           | OnBackgroundMessage                  | -                                  |
| ErrorEvent                  | ErrorEvent                           | -                                  |

While the unsupported plugin had a module, **Middleware**, the supported plugin has a different component, **Cloud Messaging Configurator**, which is Reactive Web app, that offers a REST API.

The following table lists the REST API methods that are equivalent to the Middleware's server actions.

| Firebase Mobile (unsupported) <br/> Firebase CM Compat R&D (unsupported) | Cloud Messaging Configurator (supported) |
| --------------------------------------------------------------------- | ---------------------------------------- |
| SendNotificationToTopic                                               | SendNotifcationToTopics                  |
| SendNotificationToUser                                                | SendNotifcationToUsers                   |
| SendSilentNotificationToTopic                                         | SendSilentNotificationToTopics           |
| SendSilentNotificationToUser                                          | SendSilentNotificationToUsers            |


Check out the [sample app](#sample-app) to see how to:

* Receive and handle notifications sent through Firebase Cloud Messaging
* Use the NotificationsHandler block to handle notifications inside your app (e.g. for in-app notifications)
* Get pending silent notifications
* Clear all notifications from the notification central of a device

### Crash Reporting

The list of relevant actions in the two plugins.

| Firebase Mobile (unsupported) | Crash Reporting Plugin (supported) |
| ----------------------------- | ---------------------------------- |
| LogError                      | LogError                           |
| SetCrashlyticsUserId          | SetUserId                          |
| -                             | SetEnabled                         |
| -                             | Log                                |

Check out the [sample app](#sample-app) to see how to:

* Log a Message
* Log an Error
* Force an app crash

### Performance

The list of relevant actions in the two plugins.

| Firebase Mobile (unsupported)   | Performance (supported) |
| ------------------------------- | ----------------------- |
| AddTraceAttribute               | AddTraceAttribute       |
| IncrementCounter                | IncrementMetric         |
| SetPerformanceCollectionEnabled | SetEnabled              |
| StartTrace                      | StartTrace              |
| StopTrace                       | StopTrace               |
| -                               | RemoveTraceAttribute    |

Check out the [sample app](#sample-app) to see how to:

* Start or stop a trace
* Add or remove a trace attribute
* Increment a specific metric
