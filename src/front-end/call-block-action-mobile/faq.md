---
summary: OutSystems 11 (O11) enables triggering block actions in mobile screens through JavaScript integration.
guid: afc5fd88-c84d-4ea3-9ebb-d50b7b86dca3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:0
tags: javascript integration, mobile development, ui components, validation, event handling
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - service studio
content-type:
  - procedure
---

# How to Call a Block Action in a Mobile Screen

## Question

When working with big forms, I need to split them into several Blocks. In the mobile screen containing those Blocks, how can I trigger the validation actions of each Block?

![Illustration showing a puzzle piece connecting to a mobile screen interface with a 'Save' button, indicating the trigger of block validation.](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_0.png "Triggering Block Validation")

### Answer

To trigger a Block action in a mobile screen, you need to:

1. Create a top Container in the Block. This will allow you to access the Block as the parent element of the Container. In this example, the name of the top Container is **Root**.

1. In the **OnReady** action of the Block, use a JavaScript node to define a JavaScript function that will expose the Block actions. In this example, **validatePhone** function exposes **ValidatePhoneNumber** Block action, using the top Container **rootId** to access the Block parent element:

        var wbElement = document.getElementById($parameters.rootId).parentElement;
        wbElement.validatePhone = $actions.ValidatePhoneNumber;

    ![Screenshot of a JavaScript function definition in a mobile app development environment, exposing a block action for phone number validation.](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_1.png "JavaScript Function Definition in Block")

1. Pass the Id of the top Container as a parameter to the JavaScript node:

    ![Screenshot showing the process of passing the ID of a top container to a JavaScript node within a mobile app development platform.](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_2.png "Passing Container ID to JavaScript")

1. In the consumer screen, use a JavaScript node to access the JavaScript function defined in the Block DOM element, passing the Block Id as a parameter. In this example, we use the **BlockId** to get Block DOM element and call its **validatePhone** function:

        var wbElement = document.getElementById($parameters.BlockId);
        wbElement.validatePhone();

    ![Screenshot depicting the use of JavaScript to call a block action from a consumer screen by accessing the block's DOM element.](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_3.png "Calling Block Action from Consumer Screen")

An improved approach is to put this second piece of JavaScript code inside a global Client Action (for example, **PhoneNumberValidate(PhoneNumberBlockId)**), so the caller Screen runs low code.

<div class="info" markdown="1">

**You can only select a block "Id" runtime property in the Expression Editor if you have given the block a name.** In the example above, the source block name is "PhoneNumber", but after dragging it into the consumer screen (creating a block instance) it was named "PhoneNumberBlock" in the properties editor.

</div>
