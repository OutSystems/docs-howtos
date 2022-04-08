---
summary: Reference information about migrating Traditional App to Reactive App. Use it while you're migrating your app to Reactive Web or to assess the effort you might need for migration.
tags: migration-traditional-web; migration-reactive-web; traditional-to-reactive-migration; reference-migration
locale: en-us
guid: 010044c5-0729-43e3-adea-d864e57c8843
---

# Traditional to Reactive App migration reference

<div class="info" markdown="1">

We've been working on these documents. Please let us know how useful this new version is by voting.

</div>

This reference document is a collection of notes about the differences between Traditional and Reactive App. The purpose is to help developers in migrating an existing Traditional app to a Reactive runtime.

## Initial planning and preparation

These are the considerations relevant in the preparatory steps of the Traditional Web App migration.

* URLs should be working for new Screens, Resources, Images. If you use hardcoded URLs, you need to update them on your new Screens. 
* Migrate Entities while preserving the data
* Handling Site Properties
* Migrating Roles
* Impact of Timers and Processes

Once you start migrating your app to the Reactive Web App, consider following this order for each Module:

1. Theme
2. UI Flows
3. External sites
4. Web Screens
5. Web Blocks, starting by the Web Blocks with no dependencies.

## Customize or redirect the application URL

To manage the site and page rules in your Reactive Web Apps see [Technical Preview - SEO in Reactive Web Apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Technical_Preview_-_SEO_in_Reactive_Web_Apps).

## Accelerators

There are several accelerators that can help you migrate your app faster.

### Elements you can copy and paste

You can copy the following elements from your Traditional App to Reactive App directly:

* [Aggregates](ref-frontend-screen-and-block.md#aggreg) without dependencies from other Aggregates and logic. Paste Aggregates to a Screen to create a Screen Aggregate.
* Database content
* [Entities](ref-module-elements.md#entity)
* Processes
* Timers
* [Roles](ref-module-elements.md#roles)
* Server Actions
* [Site Properties](ref-module-elements.md#site-property)
* Structures

Additionally, you can paste a Server Action to a Screen Client Action, but never paste server Actions containing sensitive information that you could expose. For more information about security in Reactive Web Apps, see the [Reactive Web security best practices](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices).

  
### Scaffolding and Screen Templates

If your Screens base on scaffolding or Screen Templates, it's faster to recreate them the same way. Make sure you're using the latest version of the [OutSystems UI Templates Reactive](https://www.outsystems.com/forge/component-overview/6335/outsystems-ui-templates-reactive).

Continue to [Module elements](ref-module-elements.md).

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
