# How to Call a Block Action in a Mobile Screen

## Question

When working with big forms, I need to split them into several Blocks. In the mobile screen containing those Blocks, how can I trigger the validation actions of each Block?

![image alt text](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_0.png)

### Answer

To trigger a Block action in a mobile screen, you need to:

1. Create a top Container in the Block. This will allow you to access the Block as the parent element of the Container. In this example, the name of the top Container is **Root**;
 

2. In the **OnReady** action of the Block, use a JavaScript node to define a JavaScript function that will expose the Block actions. In this example, **validatePhone** function exposes **ValidatePhoneNumber** Block action, using the top Container **rootId** to access the Block parent element:

```
var wbElement = document.getElementById($parameters.rootId).parentElement;
wbElement.validatePhone = $actions.ValidatePhoneNumber;
```

![image alt text](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_1.png)
 

3. Pass the Id of the top Container as a parameter to the JavaScript node:

![image alt text](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_2.png)
 

4. In the consumer screen, use a JavaScript node to access the JavaScript function defined in the Block DOM element, passing the Block Id as a parameter. In this example, we use the **BlockId** to get Block DOM element and call its **validatePhone** function:

```
var wbElement = document.getElementById($parameters.BlockId);
wbElement.validatePhone();
```

![image alt text](images/How-to-Call-a-Block-Action-in-a-Mobile-Screen_3.png)

<div class="info" markdown="1">
**You can only select a block "Id" runtime property in the Expression Editor if you have given the block a name.** In the example above, the source block name is "PhoneNumber", but after dragging it into the consumer screen (creating a block instance) it was named "PhoneNumberBlock" in the properties editor.
</div>
