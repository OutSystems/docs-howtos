---
guid: 89c5c9a1-308d-416a-b917-9080a9ddb42d
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:37
---

# How to improve list slowness on low-end devices

## Question

How to improve list slowness on low-end devices and provide good scroll experience, preventing some blank spaces from appearing?

## Answer

Create an image to a be the preview for list items without data.

Then, do the following:

1. Import the image to your application.

    ![](images/How-to-improve-list-slowness-on-low-end-devices_0.png)

1. Open the CSS Editor and create a new class to use the image as background.
 
        .task-list > script {                               
            background: url(...) !important;
            /* Drag and drop the image to set the URL of the image */
        }

    ![](images/How-to-improve-list-slowness-on-low-end-devices_1.png)  

1. Add the new CSS class to the **Style Classes** of the List widget.

    ![](images/How-to-improve-list-slowness-on-low-end-devices_2.png)
