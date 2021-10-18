---
tags: runtime-traditionalweb; version-11;
summary: Learn how to set the value of an input depending on the value set in another input in your Traditional Web app.
---
# How to dynamically set the values of inputs

In your Traditional Web app, you can set the value of an input depending on the value set in another input.

For example, a form can include two date inputs ("From" and "To") and the "To" date can automatically change to one day after the "From" date.

!["From" and "To" Inputs](images/dyn-input-00.png)

Both "From" and "To" dates are set using **Input** widgets (assigned to Variables `TestDate.From` and `TestDate.To`) associated with **Input Calendar** RichWidgets.

To dynamically set the "To" date to one day after the "From" date follow these steps:

1. Enclose the "To" **Input** widget and **Input Calendar** RichWidget in a **Container** and name it `ToWrapper`.

    ![ToWrapper](images/dyn-input-01.png)

1. Set the **On Change**>**Destination** property of the "From" date **Input** widget to a newly created **Action**, in this case `UpdateToDate`.

    ![On Change Handler](images/dyn-input-02.png)

1. Add an **Assign** node to the **UpdateToDate** action with the assignment `TestDate.To=AddDays(TesDate.From,1)`.

    ![Assign](images/dyn-input-03.png)

    This assignment updates the "To" date and defines it as the "From" date plus one day.

1. After the **Assign** node, in the **UpdateToDate** action, add an **Ajax Refresh** and set its **Widget** property to `ToWrapper`.

    The Screen Action should look similar to the following image:

    ![UpdateToDate Action](images/dyn-input-04.png)

After these steps the "To" date changes to one day after the "From" date every time the end user modifies the "From" date.

![Dynamic Inputs GIF](images/dyn-input-05.gif)
