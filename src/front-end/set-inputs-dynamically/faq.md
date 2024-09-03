---
tags: runtime-traditionalweb; version-11;
summary: OutSystems 11 (O11) allows dynamic updating of input values in Traditional Web apps based on other inputs.
guid: fcea5150-affd-4f27-8263-97e32b24a7a6
locale: en-us
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:88
---
# How to dynamically set the values of inputs

In your Traditional Web app, you can set the value of an input depending on the value set in another input.

For example, a form can include two date inputs ("From" and "To") and the "To" date can automatically change to one day after the "From" date.

![Screenshot of the initial state of 'From' and 'To' date input widgets before setting dynamic values.](images/dyn-input-00.png "Initial Date Input Widgets")

Both "From" and "To" dates are set using **Input** widgets (assigned to Variables `TestDate.From` and `TestDate.To`) associated with **Input Calendar** RichWidgets.

To dynamically set the "To" date to one day after the "From" date follow these steps:

1. Enclose the "To" **Input** widget and **Input Calendar** RichWidget in a **Container** and name it `ToWrapper`.

    ![Screenshot highlighting the 'To' input widget and Input Calendar RichWidget enclosed within a 'ToWrapper' container.](images/dyn-input-01.png "Container Encapsulation")

1. Set the **On Change**>**Destination** property of the "From" date **Input** widget to a newly created **Action**, in this case `UpdateToDate`.

    ![Screenshot showing the properties of the 'From' date input widget with the 'On Change' destination set to 'UpdateToDate' action.](images/dyn-input-02.png "Setting On Change Destination")

1. Add an **Assign** node to the **UpdateToDate** action with the assignment `TestDate.To=AddDays(TesDate.From,1)`.

    ![Screenshot of the 'Assign' node in the 'UpdateToDate' action with the assignment to add one day to the 'From' date.](images/dyn-input-03.png "Assign Node Configuration")

    This assignment updates the "To" date and defines it as the "From" date plus one day.

1. After the **Assign** node, in the **UpdateToDate** action, add an **Ajax Refresh** and set its **Widget** property to `ToWrapper`.

    The Screen Action should look similar to the following image:

    ![Screenshot of the 'UpdateToDate' action flow with an 'Ajax Refresh' node targeting the 'ToWrapper' widget.](images/dyn-input-04.png "Ajax Refresh Setup")

After these steps the "To" date changes to one day after the "From" date every time the end user modifies the "From" date.

<iframe src="https://player.vimeo.com/video/1005756606" width="350" height="320" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video demonstrating the dynamic update of the 'To' date input when the 'From' date is changed.</iframe>
