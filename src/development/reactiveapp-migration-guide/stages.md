---
summary: An overview of the stages for migrating a Traditional App to a Reactive App. Adapt it to your requirements.
tags:
locale: en-us
guid: b00bd152-2bc4-4dc9-9200-1de2bdbd26da
---

# Suggested stages of Traditional to Reactive App migration

<div class="info" markdown="1">

We've been working on these documents. Please let us know how useful this new version is by voting.

</div>

The stages for migration Traditional Web Apps to Reactive Web Apps depend on the:

* type of Traditional Web app you want to migrate
* logic used
* design
* architecture
* resources
* your availability

Find below an overview that focuses on the steps that might be common in the migration projects. Check the document [Traditional to Reactive migration reference](reference.md) for a more detailed technical overview.

1. Refactor the app to centralize the server calls
    
    Make some preparatory work before you migrate your app to the new runtime. The first step involves inspecting the logic for server calls and optimizing them by grouping them into a common logic. If your app has complex Server Actions used by Screen, consider extracting some logic to Server Actions and reusing them where needed.
    
    Traditional App renders most of the UI on the server side, so the server calls bound to UI weren't an issue. This isn't true for Reactive apps, where forcing UI to wait for a response from the server makes an app appear slow.

1. Recreate the Screens using new Widgets and OutSystems UI
    
    Reactive apps use the new UI framework, OutSystems UI, and it's not compatible with the OutSystems Silk UI, Web UI, or older UIs. One of the first tasks should be selecting the Layout that fits your app best. Then you need to recreate your Screens in new Modules with new Widgets and Patterns. This implies adapting the existing user experience to the new UI and improving it through it.
 
    If the Screens of your app use the OutSystems 11 Screen Templates, you can recreate those Screens using similar Screen Templates in Reactive. You can also use scaffolding to speed up some UI creation.
    
    Recreate the screens with higher complexity if your old apps are using OutSystems UI Web, Silk UI, or Rich Widgets.
    
    When migrating Themes, you can copy and paste parts of the CSS. However, not all the CSS classes are the same.

    Read [UI migration considerations](ref-frontend-ui.md) for detailed information about the migration of the UI.
 
1. Update the front-end logic

    Once the UI is in place, you need to make it fully functional. For the most part, this entails focusing on the logic that now runs in the client. Check which data you bring to the client-side of the app, making sure you never expose confidential information.

    Read [Front-end migration](ref-frontend-intro.md) for detailed information about the migrating Front-end.

1. Fix the performance warnings

    Check if your app is running smoothly for the users. You should fix the performance warnings in Service Studio, particularly the ones related to using the server-side logic from UI.

Go to the [Traditional to Reactive App migration reference](reference.md) to proceed.

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
