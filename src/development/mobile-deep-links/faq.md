---
tags: version-11; support-mobile; support-Mobile_Apps; deep link; Intent;
summary: 
---

# How to define Mobile App deep links

To define a deep link to a Screen (`<screen>`) of a Module (`<module>`) of a Mobile App use the following syntax:

    <app-identifier>://<module>/<screen>

Where `<app-identifier>` is the [App identifier you defined when generating your Mobile App Package](<https://success.outsystems.com/Documentation/10/Delivering_Mobile_Apps/Generate_and_Distribute_Your_Mobile_App>) in **lowercase**.

<div class="info" markdown="1">
As a best practice the App identifier of your Mobile App should be lowercase. 
%%In deep links the `<app-identifier>` scheme must be lowercase, even if your App identifier has uppercase characters.
</div>

To include values for Input Parameters in your deep link use the following syntax:

    <app-identifier>://<module>/<screen>?<Parameter1>=<Value1>&<Parameter2>=<Value2>

<div class="info" markdown="1">

If you use a **RedirectToURL** destination to open a external website, you can't call a deep link back to the mobile app from the external website in iOS devices. 
Instead if you need to open an external website, use the **Open** client action from the [InAppBrowser Plugin](https://www.outsystems.com/forge/component-overview/1558/inappbrowser-plugin) with the **Target** set as `Entities.Target.SYSTEM`and the **Url** set as the external website url.

</div>

## Android Intents

For Android end users with Chrome you can use [Android Intents](https://developer.chrome.com/multidevice/android/intents).
Android Intents allow the redirection of end users that do not have your App available on their device to your App page in the Google Play Store or to another URL specified by you. 

<div class= "info" markdown= "1">
When you generate an Android App in OutSystems 10 it already includes a `BROWSABLE` Intent filter.
</div>

To define an Android Intent use the following syntax:

    intent://<module>/<screen>#Intent;scheme=<app-identifier>;package=<app-identifier>;end;

To specify a custom fallback URL (`<URL>`) add a string extra `S.browser_fallback_url=<URL>;` to the Intent:

    intent://<module>/<screen>#Intent;scheme=<app-identifier>;package=<app-identifier>;S.browser_fallback_url=<URL>;end;

## Additional considerations

* Don't pass critical information on the URL of deep links, as deep links aren't secure by design.

* The main use case of deep links in OutSystems apps is allowing navigation to specific parts of the target app. 

* Ensure that actions available through deep links don’t risk users' data. For example, don’t allow other apps to directly delete content nor access sensitive information about users.

