---
summary: Explore system actions and migration strategies in OutSystems 11 (O11) for enhancing mobile and reactive apps.
tags: migration strategies, system actions, javascript in outsystems, outsystems forge, ui patterns
locale: en-us
guid: 89d99597-4385-4748-9aac-3b72a112a9bd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - forge
coverage-type:
  - apply
---

# Systems Actions

If there's no equivalent Client Action to the Server Action you want to use, consider the following:

* Wrapping a System Action into a Server Action, keeping in mind the performance implications.

* Creating a [custom JavaScript implementation](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/JavaScript/Extend_Your_Mobile_and_Reactive_Apps_Using_JavaScript).

For more ideas and examples, check the [Reactive Utilities](https://www.outsystems.com/forge/component-overview/1730/reactive-utilities) Forge component by the OutSystems community.

## Notify

Check out the [Web Block](ref-frontend-ui-flows.md#webblock) section.

## Notify get message

Check out the [Web Block](ref-frontend-ui-flows.md#webblock) section.

Continue to the [Core Widgets](ref-core-widgets.md) section.

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
