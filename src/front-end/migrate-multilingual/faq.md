---
summary: Learn how to reuse translations from the Multilingual Forge component in Service Studio translation management. This feature is in Technical Preview.
tags: support-application_development; multilingual; migration-multilingual-translations; multilingual-service-studio
---

# How to reuse translations from Multilingual Forge component in Service Studio

Starting with the Platform Server release 11.10, OutSystems has an built-in translation mechanism for adding and managing translations in Reactive Web and Mobile apps directly in Service Studio. You don't need to install the Multilingual Forge component as in previous versions.

<div class="info" markdown="1">

OutSystems will discontinue the [Multilingual Forge component](https://www.outsystems.com/forge/component-overview/1784/multilingual-component) on July 5th, 2021.

</div>

OutSystems designed Multilingual to allow you to manage your translations fast and to have the possibility to change your app language while offline.

This document explains how to migrate translations from the Multilingual Forge component to the new Multilingual on Service Studio.

Before proceeding, ensure you fill all the prerequisites. Refer to the [Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Technical_Preview_-_Multilingual_Reactive_Web_and_Mobile_Apps) documentation.

You need to perform the following steps to migrate your app translations:

1. [Activate the Multilingual Technical Preview](#technical-preview)
1. [Migrate the translations to the Translations Editor](#translations-editor)
1. [Delete the unnecessary logic](#delete-unnecessary-logic)
1. [Remove the dependency on the Multilingual module](#remove-dependencies)

Find below the instructions to migrate your translations.

## Activating the Multilingual Technical Preview { #technical-preview }

The first step to proceed with the migration is to activate the Multilingual Technical Preview for your environment in the LifeTime console. Read the [Technical Preview features](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features) for more information.


## Migrating the translations to the Translations Editor { #translations-editor }

You have two ways to migrate the existing translations, depending on how you keep them: on a local resource or a list.

* If you are using a local resource see [Using a local resource file](#localresource).
* If you are using a list go to [Using a list](#migrateusinglist) (for example, an Entity).

### Translations on a local resource file { #localresource }

If you are using a local resource, follow the steps below. You only need to migrate locales and the translations. You don't need the translation IDs and the `isRightToLeft` locale property.

1. Open the resource file created when you used the Multilingual Forge component, for example:

        [{
            "locale": "pl",
            "isRightToLeft": false,
            "translations": {
                "08e142ce-dc09-4cbc-ad": "Nie masz zadań do wykonania. Możesz iść na kawę.",
                "0c0875e4-dba7-4a9e-a9": "Dodaj nowe zadanie", ...
            } 
        }, ... ]

1. Add locales to your app according to the [Add a new language and translate the text](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Technical_Preview_-_Multilingual_Reactive_Web_and_Mobile_Apps/Translate_your_app#add-new-language) section of the [Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Technical_Preview_-_Multilingual_Reactive_Web_and_Mobile_Apps) documentation.

1. Copy the translations from your resource file (for example, an Excel sheet) to the correspondent language on the **translations editor** that opened when you created the locales in the previous step.

1. Delete the old **data-trans** IDs of the translations, as you don't need them anymore. The figure below shows an example of one of these IDs.

    ![Translation IDs to delete](images/multilingual-ids-to-delete.png?width=750)

### Migrating translations using a list { #migrateusinglist }

If you are using a list, check the translations on your list and manually copy the translations to the new Multilingual.

You have two ways to view the translated data on an entity:

* On Service Studio, by right-clicking the **AppTranslations** entity and selecting **View Data**.

    ![View data list](images/multilingual-migration-data-list.png)

* On an exported Excel file containing the translations. To export the translations to Excel follow the [How to export entity data to Excel](../../data/export-entity-data-excel/faq.md) document.

## Deleting the unnecessary logic { #delete-unnecessary-logic }

When using the Multilingual Forge component, you used the plugin to translate your apps, and added extra logic for loading the translations and to translate the elements. With the Multilingual for Reactive and Mobile apps, the OutSystems platform handles this for you.

To clean up your app's logic, delete all usages of the following Client Actions from your app:

* **GetLocale**
* **SetLocale**
* **GetTranslation**
* **AddTranslations**
* **AddTranslationsFromResource**

<div class="info" markdown="1">

Before deleting the **GetLocale** and **SetLocale** Client Actions, ensure you placed the new **GetCurrentLocale** and **SetCurrentLocale** Client Actions, respectively, in your logic. 

</div>

You can also delete the **data-trans** attribute from the text widgets, as you don't need it anymore.

### Finding where the used actions are

To find where the used actions are, do the following steps:	

1. Go to the **Logic** tab and expand the **Client Actions** folder.

1. Click on the **MultiLingual** reference, and expand it.

1. Select a client action and click the F12 key on your keyboard. A search area appears with the usages of that client action on your application.

    ![Multilingual client actions](images/multilingual-client-actions.png)

### Switching locales using the new Multilingual

For switching locales in your logic using the new Multilingual, use the new **SetCurrentLocale** client action available in your system module. See the [Create a language switcher](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Technical_Preview_-_Multilingual_Reactive_Web_and_Mobile_Apps/Translate_your_app#add-language-switcher) section of the [Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Technical_Preview_-_Multilingual_Reactive_Web_and_Mobile_Apps) documentation for more information.

## Removing the dependency on the Multilingual module { #remove-dependencies }

The final procedure is to remove the Multilingual plugin reference from your app.

1. Click on the **Manage Dependencies** icon. The dependencies window opens.

1. Uncheck the Multilingual dependency.

    ![Removing the Multilingual dependency](images/multilingual-remove-dependency.png)

1. Click **APPLY** to remove the Multilingual dependency.

