---
summary: Explore how to integrate OneSignal for push notifications in OutSystems 11 (O11) and OutSystems Developer Cloud (ODC) applications using the OneSignal plugin.
tags: push notifications, onesignal integration, notification configuration, mobile app development, platform-specific setup
guid: d7d5445d-d28d-4acb-b158-b6d85b7f2ace
locale: en-us
app_type: mobile apps
platform-version: o11, odc
figma: https://www.figma.com/file/gKoXqtZTY2IJjyMWschrRB/Integrations?node-id=1242:340
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
---

# How to use push notifications with OneSignal

OneSignal is a service that enables push notifications, abstracting details such as the platform the device is running on. With the OneSignal plugin, OutSystems applications can send and receive push notifications.

The image below shows a push notification in an Android smartphone.

![Example of a push notification on an Android smartphone screen with the message 'Hello from OutSystems!'](images/One-Signal-0.png "Android Push Notification Example")

## Configuring OneSignal

You need to configure OneSignal for each of the mobile platforms it works on. Once your configuration is done, you have an Application ID and a REST API KEY from OneSignal.

You can configure OneSignal for iOS and Android.

* [Initial setup of your OneSignal App](https://documentation.onesignal.com/docs/mobile-sdk-setup#step-by-step-instructions-for-configuring-your-onesignal-app)
* [Configure for iOS](https://documentation.onesignal.com/docs/ios-p12-generate-certificates)
* [Configure for Android](https://documentation.onesignal.com/docs/android-firebase-credentials "https://documentation.onesignal.com/docs/en/android-firebase-credentials")

<div class="info" markdown="1">

From Android 15 onwards, users can install an app in the [Private space](https://developer.android.com/about/versions/15/features#private-space). Users can lock their private space at any time. This means that push notifications are not shown until the user unlocks it.

You cannot detect if an app is installed in the private space. If you use the OneSignal plugin for delivering critical notifications, inform your users to avoid installing your app in the private space.

For more information about the behavior changes of your app related to the private space, refer to [Android documentation](https://developer.android.com/about/versions/15/behavior-changes-all#private-space-changes).

</div>

## Installing the OneSignal plugin

Start by installing the OneSignal plugin (available for both [O11 OutSystems Forge](http://www.outsystems.com/forge/component/2119/onesignal-plugin/ "http://www.outsystems.com/forge/component/2119/onesignal-plugin/") and ODC Forge).

![Screenshot of the OneSignal Plugin page on the OutSystems Forge website (O11)](images/image.png "OneSignal Plugin on OutSystems Forge")

## Receiving notifications

For your app to receive notifications, you need to implement client-side logic to register the device in OneSignal.

Start by adding the OneSignal plugin to the mobile app in the **Manage Dependencies** menu option. This plugin contains the client-side actions to register the device.

![OutSystems Service Studio interface showing the OneSignal Plugin selected in the Manage Dependencies window](images/One-Signal-1.png "OneSignal Plugin in Manage Dependencies")

In case you want to add logic to run on events over notifications, do the following:

1. Add the OneSignal block to the Layout block of your application.

    ![Service Studio interface highlighting the OneSignal block added to the Layout block of an application](images/Layout.png "OneSignal Block in Layout")

1. Add your logic to the event handlers of the OneSignal block:

    * **OnNotificationReceived**: a Client Action that runs when the app receives a notification.
    * **OnNotificationOpened**: a Client Action that runs when the user opens a notification.

### Receiving notifications with deep links for Android

If your app is deployed to Android devices and you intend to use deep links in your notifications, you need to set a `AndroidLaunchMode` preference in your Extensibility Configurations.

This preference changes how a new [activity](https://developer.android.com/guide/components/activities/intro-activities) from your Mobile App is launched. For more information about the activity launch mode, refer to [Activity element documentation](https://developer.android.com/guide/topics/manifest/activity-element#lmode).

This extra step ensures that Android end users will be redirected to specific Screens when they click the OneSignal notification. No additional configuration is needed for iOS devices.

#### O11

Add the following to your module's Extensibility Configurations.

```json
    {
        "preferences": {
            "android": [
                {
                    "name": "AndroidLaunchMode",
                    "value": "singleTask"
                }
            ]
        }   
    }
```

#### ODC

Add the `AndroidLaunchMode` preference to your application's Extensibility Configuratons.

(Recommended) Using the universal extensibility configurations schema:

```json
{
  "appConfigurations": {
    "cordova": {
      "preferences": {
        "android": {
          "AndroidLaunchMode": "singleTask"
        }
      }
    }
  }
}
```

Using the Cordova-based extensibiility configurations schema (for MABS versions lower than 12):

```json
    {
        "preferences": {
            "android": [
                {
                    "name": "AndroidLaunchMode",
                    "value": "singleTask"
                }
            ]
        }   
    }
```

Note that you can only use the Cordova-based extensibility for MABS versions lower than 12. It won't work on MABS 12.

### Registering a device with a user

If your users need to login to use the application, the device can be registered with that user.

One place to do it can be the “Login” screen.

![OutSystems Service Studio interface showing the Login screen in the UI Flows section](images/One-Signal-2.png "Login Screen in Service Studio")

Use the RegisterWithUser action to register the user along with the device.

Put it after the “DoLogin” action and it should look like this:

![Flowchart in Service Studio depicting the RegisterWithUser action after the DoLogin action](images/one-signal-03.png "Register With User Logic Flow")

To set the AppId value, use the **OneSignal App ID** value from the OneSignal console.

By default, the registration action is performed asynchronously. It sends the action to register the device in OneSignal service and continues the logic execution without waiting for the registration action response. To change this behavior, set AsyncRegister parameter to `false`. This blocks the code execution and waits until the device is registered in OneSignal service before proceeding.

Save the **OneSignal App ID** and **REST API Key** values because you need them later.

![OneSignal console showing the App Settings with fields for OneSignal App ID and REST API Key](images/One-Signal-4.png "OneSignal App Settings")

By default, notifications won’t be displayed when the application is already running in the foreground. To always display notifications, set property InFocusDisplayOptions to `Entities.InFocusDisplayOption.NOTIFICATION`.

### Registering a device without a user

If your application does not have a login, the device can be registered without a user.

One place to do it can be the “On Application Ready” action.

![Service Studio interface showing the On Application Ready action in the MainFlow of a HomeScreen](images/One-Signal-5.png "On Application Ready Action")

Use the Register action to register the device. It should look like in the image below:

![Flowchart in Service Studio depicting the Register action in the OnApplicationReady client action](images/one-signal-06.png "Register Device Logic Flow")

By default, the registration action is performed asynchronously. It sends the action to register the device in OneSignal service and continues the logic execution, without waiting for the registration action response. To change this behavior, set AsyncRegister parameter to `false`. This blocks the code execution and waits until the device is registered in OneSignal service before proceeding.

Furthermore by default, notifications aren't displayed when the application is already running in the foreground. To always display notifications, set property InFocusDisplayOptions to `Entities.InFocusDisplayOption.NOTIFICATION`.

## Sending notifications (O11 only)

To send notifications, you need to implement server-side logic. Add the OneSignalAPI in the Manage Dependencies… menu option. This API contains the server-side actions to send notifications.

![OutSystems Service Studio interface showing the OneSignalAPI selected in the Manage Dependencies window](images/One-Signal-7.png "OneSignalAPI in Manage Dependencies")

Add the server-side logic to send the notification like in the image below:

![Flowchart in Service Studio depicting the logic to send a push notification using OneSignalAPI](images/One-Signal-8.png "Send Notification Logic Flow")

To set the OneSignalRestAPIKey and OneSignalAppId values, use the values you saved earlier in this document.

By default, Android notifications are displayed using the bell icon. To replace this icon with the application icon, set the SmallIcon property to `"icon"` if you are generating your app using MABS 4 or below. Else, set the SmallIcon property to `"ic_launcher"`.

![Service Studio interface showing the configuration for the notification icon in the SendPushNotification server action](images/One-Signal-9.png "Notification Icon Configuration")

### Defining the notification message(s)

To define the text of the notifications to send, set the Message input parameter to a list of "Content" structures (the "Content" structure is defined in OneSignalAPI), containing each notification message and its respective language/locale.

In the following example, two local variables were defined in the SendReminder server action where the notifications are sent: a local variable Message of data type "Content" and a local variable MessageList of data type "Content List".

![Service Studio interface showing the structure of the SendReminder server action with MessageList and Message variables](images/One-Signal-Flow-action.png "SendReminder Server Action Structure")

To send a notification with a simple message in English, do the following in the server action flow:

![Flowchart in Service Studio showing the steps to send a notification with Assign, ListAppend, and SendPushNotificationToUserId actions](images/One-Signal-SendNotification-flow-steps.png "Send Notification Flow Steps")

1. **Assign** the message text and the English language code `"en"` to the Message local variable of data type "Content";

    ![Service Studio interface showing the Assign action with Message.Lang set to 'en' and Message.Value set to a notification text](images/One-Signal-Flow-assign-element.png "Assign Action in Send Notification Flow")

1. **Append** this local variable to the list of notifications to send which is kept in the MessageList local variable of data type "Content List";

    ![Service Studio interface showing the ListAppend action appending a Message to the MessageList](images/One-Signal-Flow-listappend-element.png "ListAppend Action in Send Notification Flow")

1. **Send** the notification supplying the MessageList variable as the Message input parameter.

## Remarks

This article provides a simple example of implementing push notifications. However, OneSignalPlugin and OneSignalAPI (on O11) provide further client and server-side functionality to implement other ways of pushing notifications. For example, on the client-side, add logic to take an action when the user opens the notification or, on the server-side, push a notification only to some specific users.

For more information about **OneSignalPlugin** and **OneSignalAPI**, use the tooltips by hovering over the elements in the Service Studio.

To know more about **OneSignal**, check [this documentation](https://documentation.onesignal.com/docs).
