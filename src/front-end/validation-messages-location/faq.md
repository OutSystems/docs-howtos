---
tags: css customization, ui design, form customization, user experience, error handling
summary: Explore how to customize the display of input validation messages in OutSystems 11 (O11) by relocating them from their default positions.
guid: 10da9d4f-5807-4aa0-9d63-6d31e8e78aaa
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:99
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
content-type:
  - procedure
---

# How to display input validation messages in a custom location

By default, input validation messages are shown next or below the corresponding inputs.

![Screenshot showing default input validation messages next to form fields.](images/validation-messages-00.png "Default Input Validation Messages")

How can I show these messages in another location to meet business or design requirements?

## Answer

To display input validation messages in a custom location, we must hide the default messages and display the `.ValidationMessage` runtime properties of the invalid inputs in the custom location.

Follow the steps below to display input validation messages in a custom location:

1. Depending on the type of application add one of the following CSS snippets to the Style Sheet of the Screen/Block: 

    For **Web Applications**:
    
        span.ValidationMessage {
            display: none;
        }

    For **Mobile Apps**: 

        span.validation-message {
            display: none; 
        }

    This will hide the default validation messages.

1. Assign `<input_name>.ValidationMessage` to the Value of an **Expression** Widget to display the validation message of the `<input_name>` Input in a custom location. 

    ![Interface showing how to set a custom location for input validation messages using Expression Widget.](images/validation-messages-01.png "Setting Custom Location for Validation Messages")

    You may modify the look of the custom location validation messages by modifying the style of the **Expression** Widget.

    Note for **Web Applications**: If you are using the `Ajax Submit` Method to submit your Form don't forget to **Ajax Refresh** the Expression Widget.

After these steps the input validation messages will appear in a custom location at runtime:

![Screenshot of a form displaying input validation messages in a custom location below the input fields.](images/validation-messages-02.png "Custom Location Input Validation Messages Display")