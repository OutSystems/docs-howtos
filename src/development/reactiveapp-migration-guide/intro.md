---
summary: Reactive is a type of app that has many improvements when compared to Traditional App. This document provides introductory notes for developers and leads who are considering migrating old Traditional Apps to Reactive.
tags: article-page; migration-traditional-web; migration-reactive-web
locale: en-us
guid: 6fd52b69-653d-4384-b9fe-7e30b698609b
---

# Introduction to migrating Traditional Web to Reactive Web Apps

<div class="info" markdown="1">

We've been working on these documents. Please let us know how useful this new version is by voting.

</div>

<div class="info" markdown="1">

This document addresses experienced developers and Tech Leads planning to migrate Traditional Web Apps to Reactive Web Apps. The migration requires good knowledge of the Reactive Web front-end features and application architecture. Check the guided path [Becoming a Reactive Web Developer](https://www.outsystems.com/learn/paths/18/becoming-a-reactive-web-developer/) in OutSystems training to get into Reactive Web development.

</div>

The objective of these documents is to guide developers on the end-to-end process of migrating Traditional Web apps to Reactive Web.

## About Reactive Web Apps

In October 2019, OutSystems released Reactive Web, enabling the developers to create the next generation of Web Apps. Due to significant changes to the Reactive App, OutSystems doesn't provide a tool for automatic migration of the Traditional Web Apps.

Developing Reactive Web Apps is a highly performant and scalable way to build apps for web and mobile. It boosts the development journey to build apps that run on every device. By having separated server-side and client-side logic, asynchronous data fetching, and reactive client-side rendering, supported by a future-proof architecture, the overall performance of Reactive Web Apps lets you improve both your development and your users' experience.

## Why migrating your apps to Reactive Web

Migrating your apps to Reactive Web lets you to boost their performance, and make them more secure by letting you have all sensitive data processed on the server side only. It's also an opportunity to refactor your apps, offering your users a modern UI and a smooth experience while using your apps. 

The migration process is manual. The effort might be significant, depending on the size and complexity of the applications, particularly in the front end. If you have a solid architecture supporting your apps, you can reuse a lot of server-side logic and speed up the migration.

Migration, for the most part, implies creating a new UI with the new framework and then creating logic using a new development paradigm. In the process, you may rethink and improve your user experience, especially if your app has an outdated look and feel.

The developers already familiar with the development of Mobile Apps find in the Reactive App many concepts they already know, due to the similarities in the development tools. The developers who develop primarily in the older Traditional Web App technology may need to learn more about [Becoming a mobile developer](https://www.outsystems.com/learn/paths/1/becoming-a-mobile-developer/), [Becoming a Reactive Web developer](https://www.outsystems.com/learn/paths/18/becoming-a-reactive-web-developer), and the client-side development paradigm. 

## Migration journey overview

The recommended approach for migrating Traditional apps to Reactive Web is to start from bottom-up. This means the first thing to address is the Front-end, creating the UI structure first with the layouts where you're going to build your logic, and then start the migration one Block at a time. The new Reactive Web layouts need to be identical to the old Traditional Web layouts.

After creating the Themes, Layouts, images, and other, it's time to build the Core Widgets reused by several Modules, meaning that now you have the UI plus the new logic, which differs from the traditional one (Events, Aggregates, and others).

The final step is to migrate the pages the users see, one by one.

## Effort estimation and team requirements

To estimate how long your project can take, start with a proof of concept and migrate simple Screens, and then move to more complex Screens. The effort you invest should be a good indication of how fast your team can migrate the app to the new runtime. The higher the complexity of a Screen, the longer it takes to migrate all its components used.

Consider also using a gradual release strategy where you migrate only some Screens or sets of Screens and deploy them side by side with the old Screens. In the process, you should test how the Screens work on devices with different display sizes. 

Before initiating a migration project, make sure that:

* There is a real value in migration. For example, you plan to continue developing the app actively, have the need to reuse elements between Mobile and Web apps, the improvements in end-user experience justify the investment, and similar.

* Your team has experience and training in building Reactive Apps or Mobile Apps. Reactive Web Apps builds on top of modern client-side logic that's powered by a well-designed server side. The development team must be familiar with both. If you aren't confident that the team is ready for the task, OutSystems advises working with partners or developers experienced in migrating projects.

* You acknowledge the developers' effort needed to perform a migration.

## Documents about migrating Traditional Web Apps to Reactive Web
 
To help you on the migration of your Traditional Web Apps, these are the available documents:

* [Introduction to migrating Traditional Web to Reactive Web Apps](intro.md) - this document.
* [Differences to consider between Traditional and Reactive Web Apps](differences.md) - refers to the main differences between both technologies.
* [Suggested stages of Traditional to Reactive Web App migration](stages.md) - the suggested approach to the migration.
* [Traditional to Reactive Web App migration reference](reference.md) - a set of reference documents with information about migrating from Traditional to Reactive Web.
    * [Module elements](ref-module-elements.md) - reference document about Modules.
    * [Front-end](ref-frontend-intro.md) - a set of documents about migrating Front-end.
        * [User Interface](ref-frontend-ui.md) - reference document about UI migration.
        * [UI Flow elements](ref-frontend-ui-flows.md) - reference document about UI Flows migration.
        * [Screen and Block logic](ref-frontend-screen-and-block.md) - reference document about Screens and Block logic migration.
        * [System Actions](ref-system-actions.md) - reference document about System Actions
    * [Core Widgets](ref-core-widgets.md) - reference document about the Core Widgets.
 
Proceed to the [Differences to consider between Traditional and Reactive](differences.md) document to continue reading about the migration.
