---
tags: version-11; favicon;
summary: OutSystems 11 (O11) guide on changing the default favicon in Service Studio for Reactive Web Apps.
guid: 784794a5-90a4-4cae-83df-1fcaf6d68507
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/kY6LwaHBP6HdTslYHlSadB/Front-End?node-id=844:84
---

# How to change a favicon

This document explains how to change the default icon and replace it by your favicon. OutSystems apps use the OutSystems logo as the default favicon from Service Studio > **Data** > **Resources** > **favicon.png**.

![OutSystems default favicon image displayed in the Service Studio Resources tab.](images/default-favicon.png "Default Favicon")

<div class="info" markdown="1">

When changing the favicon, keep in mind that you need to:

* Change the favicon file in **all modules** that expose screens in your app
* Reload the app data, to ensure the app loads the new favicon. If you are using Chrome, right-click the tab with your app and select **Reload**. You can also clear the entire browser cache.
* Make sure your icon [follows the guidelines](https://developers.google.com/search/docs/appearance/favicon-in-search) if you want the favicon to show on Google search results.

</div>

## Use a PNG image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **PNG image**.

1. In Service Studio, go to the **Data** tab > **Resources**, right-click **favicon.png** and select **Change Resource**. A file dialog opens.

    ![Service Studio interface showing the context menu with 'Change Resource...' option highlighted for favicon.png.](images/change-favicon-ss.png "Change Favicon in Service Studio")

1. In the **Change Resource** file dialog, select a PNG image to set it as a new favicon. 

    <div class="info" markdown="1">
        Service Studio resizes the image to the favicon standard dimensions.</div>

1. Publish your module and open it in the browser. You should see a new icon in the browser tab.

## Use an ICO image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **ICO image**:

1. In Service Studio, go to the **Data** tab > **Resources**, select **favicon.png** and change its **Name** to `favicon.ico`.

    ![Service Studio interface with the favicon.png resource selected and the 'Name' field highlighted, ready to be changed to favicon.ico.](images/change-favicon-to-ico-ss.png "Change Favicon to ICO in Service Studio")

1. Right-click **favicon.ico** and select **Change Resource**.

1. In **Change Resource**, select an ICO image with the new favicon.

1. Check if some elements in the module use the old icon and update them if needed. Press **Ctrl+F** or click the search icon, enter `favicon.png` and select **Search in this Module**.

    <div class="info" markdown="1">
    
    If you have just created your app, the **'favicon.png' occurrences in Module** search tab shows four occurrences of **favicon.png**, all in different **AddFavicon** actions.  
    <ins>Note</ins>: **AddFavicon** client action is **only** compatible with Chrome, Firefox and Edge.
   
    
    </div>

1. In the **'favicon.png' occurrences in Module** search tab, select **REPLACE ALL OCCURRENCES**.

1. Enter `favicon.ico` and select **OK**.

1. Publish your app and open it in the browser. You should see a new icon in the browser tab.
