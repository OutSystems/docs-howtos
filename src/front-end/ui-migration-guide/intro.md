---
summary: An overview about migrating the user interface (UI) framework of the Silk Web UI applications to the OutSystems UI Web.
tags: article-page
en_title: Migrating UI of the Silk Web applications to OutSystems UI Framework
locale: en-us
guid: 9842b593-ee78-466b-9fdd-a8f6e21f44b1
---

# Migrating UI of the Silk Web applications to OutSystems UI Framework

This document introduces the migration paths to upgrade the user interface (UI) framework of the Silk Web UI applications to the new OutSystems 11 UI Web Framework. It applies to applications based on Silk UI Web Framework, but also to migrating previous UI solutions, such as the London Theme or any custom theme. The migration is a manual process.

<div class="info" markdown="1">

The documents in this section:

* [Migrating UI of the Silk Web applications to OutSystems UI Framework](intro.md)
* [Migrating the patterns of the Silk web applications to OutSystems UI](migrate-patterns.md)
* [Migrating the structure of the Silk web applications to OutSystems UI](migrate-structure.md)
* [Migration reference tables for Silk and OutSystems Web UI](migration-reference-tables.md)

</div>

The document is intended for OutSystems developers with intermediate to advanced knowledge of the OutSystems Web platform. There are several paths the developers can approach the migration:

* To remove each Silk UI pattern, one at a time, and replace it with the pattern from OutSystems Web UI. This is the most contained and focused migration path.
* To migrate patterns screen by screen, changing the 'Source Web Block' attribute of each pattern in the same screen.
* Remove the reference to Silk UI altogether, rename UI Flows and/or patterns from OutSystems UI so the 'Source Web Block' attribute is the same, but the patterns are updated.

The procedure is supported by the following documents:

* Migrating UI of the Silk Web applications to OutSystems UI Framework (this document)
* Migrating the structure of web applications
* Migrating the patterns of web applications
* Migration reference tables

The specific instructions for the migration path where you upgrade the application UI framework by first modifying the structure and then changing the patterns are outlined in _Migrating web application structure_ and _Migrating Patterns_.

## Rationale

In OutSystems 11 we improved the UI web framework and brought it closer to the Web Runtime and the platform itself. To use the new features of OutSystems 11 for the web application you need to migrate the UI framework of your OutSystems 10 applications to OutSystems Web UI Framework. This will enable you to use Screen Templates which, for the time being, work only with the new Application Templates that inherit the new UI features by default.

In OutSystems 11 the new OutSystems Web UI Framework supersedes Silk Web UI Framework. Therefore:

* If you want to use OutSystems Web UI Framework for the web applications created in Silk UI Web, you need to manually migrate your web applications to the new UI framework.
* The built-in Screen Templates in OutSystems 11 are designed for OutSystems Mobile UI Framework and OutSystems Web UI Framework. If you try to instantiate a Screen Template with an application based on the Silk UI frameworks, you will see a compatibility warning. For best experience use Screen Templates with new applications based on one of the OutSystems 11 built-in Application Templates.
* You can continue developing apps created in Silk UI Mobile with OutSystems Mobile UI Framework without any changes to the apps.

## Considerations about time and complexity

You should estimate the time and effort for the migration to the new UI framework. Replacing the actual patterns is not complicated, but some replacements require changes of the related placeholders, parameters or logic. This means the migration can become a challenging task when dealing with complex pattern uses. A top-level migration, with replacing only patterns and correcting errors, may take less time than a low-level migration.

You should familiarize yourself with the new CSS classes and structure of the OutSystems Web UI framework before you start migrating the applications. Achieving an identical visual outcome in OutSystems UI Web, if wanted, is possible - but requires high attention to detail.

The migration path and the estimation for the related tasks depends on whether your web applications use a style guide:

* Applications that inherit the built-in main theme and layout. You can migrate these applications by following the instructions from the documents referred in this text.
* Applications that inherit the style guide with a main theme and layout. You can migrate these applications by first migrating the style guide and then the applications.
