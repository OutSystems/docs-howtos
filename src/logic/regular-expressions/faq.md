---
tags: text processing, pattern matching, server actions, guid validation, outsystems api
summary: Explore how to utilize regular expressions in OutSystems 11 (O11) for text processing and pattern matching.
guid: c7045a0e-c6ec-4db9-ae8d-d21d80731cd7
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - full stack developers
  - mobile developers
  - frontend developers
outsystems-tools:
  - service studio
content-type:
  - procedure
---

# How to use regular expressions in OutSystems

Regular expressions let you process text strings using search patterns.

OutSystems includes the following two server actions from the **Text** extension that lets you use regular expressions in your app:

* Use [**Regex\_Search**](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/Text_API#Regex_Search) to search text for a matching regular expression pattern.

* Use [**Regex\_Replace**](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/Text_API#Regex_Replace) to replace a matching regular expression pattern in text.

## Example: Check if text is a GUID

A Globally Unique IDentifier, or GUID, is a base-16 integer with 128 bits, for example `4ccdb844-bcb6-4abd-83af-6655f31ca65d`. You can use GUIDs when you need to ensure identifiers are unique across environments and systems.

The regular expression `"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"`, lets you check if a text string includes only a GUID.
Check the [RFC 4122](https://www.ietf.org/rfc/rfc4122.txt) for more information on GUIDs and their format.

The following example shows you how to use this regular expression and the **Regex\_Search** action to create a reusable server action that checks if a text input is a GUID:

1. In a module of your app, open **Manage Dependencies**, and add the **Regex\_Search** action from **Text** producer as a dependency.

1. In the **Logic** tab, create a new **Server Action**, and name it `CheckGUID`.

1. Add the following variables to the action:

    * Add an **Input Parameter**, of the **Text** data type, named `TextToCheck`.

    * Add an **Output Parameter**, of the **Boolean** data type, named `IsGuid`.

1. In the action flow, add a **Regex\_Search** action.

1. Set the following properties of the **Regex\_Search** action:

    * Set **Text** as the input parameter,`GuidToCheck`.

    * Set **Pattern** as `"^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"`.

1. After the **Regex\_Search** action, add an **Assign**, and add the assignment `IsGuid` = `Regex_Search.Found`. 

After these steps you created a server action that receives a text input, and outputs a boolean that's True if the input text is a GUID.

## Example: Extract a GUID from text

Let's expand on the previous example, by enabling the detection and output of a GUID in the middle of a text string. The regular expressions `"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"`, lets you check if a text string contains a GUID. 

Follow these steps to create a reusable server action that detects and outputs a GUID from a text input:

1. In a module of your app, open **Manage Dependencies**, and add the **Regex\_Search** action from **Text** producer as a dependency.

    <div class="info" markdown="1">
    Skip this step if you completed the previous example and are using the same module.
    </div>

1. In the Logic tab, create a new **Server Action**, and name it `ExtractGUID`.

1. Add the following variables to the action:

    * Add an **Input Parameter**, of the **Text** data type, named `GuidToCheck`.

    * Add an **Output Parameter**, of the **Boolean** data type, named `HasGuid`.

    * Add an **Output Parameter**, of the **Text** data type, named `Guid`.

1. In the action flow, add a **Regex\_Search** action.

1. Set the following properties of the **Regex\_Search** action:

    * Set **Text** as the input parameter,`TextToCheck`.

    * Set **Pattern** as `"[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}"`.

1. After the **Regex\_Search** action, add an **Assign**, and add the following assignments:

    * `HasGuid` = `Regex_Search.Found`
    * `Guid` = `Regex_Search.PatternResult`

After these steps you created a server action that receives a text input, and outputs a boolean that's True if the input text includes a GUID and outputs the extracted GUID as text.
