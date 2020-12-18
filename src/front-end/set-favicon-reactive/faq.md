---
tags: version-11; favicon;
summary: Instructions on how to update the favicon in Reactive Web Apps.
---

# How to change a favicon in Reactive Web Apps

This document explains how to change the default icon and replace it by your favicon. OutSystems Reactive Apps use the OutSystems logo as the default favicon from Service Studio > **Data** > **Resources** > **favicon.png**.

![The default favicon](images/default-favicon.png?width=600)

<div class="info" markdown="1">

You need to change the favicon file in **all modules** that expose screens in your app.

</div>


## Use a PNG image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **PNG image**.

1. In Service Studio, go to the **Data** tab > **Resources**, right-click **favicon.png** and select **Change Resource**. A file dialog opens.

    ![Help menu to edit resource, favicon](images/change-favicon-ss.png?width=500)

1. In the **Change Resource** file dialog, select a PNG image to set it as a new favicon. 

    <div class="info" markdown="1">
    
    Service Studio resizes the image to the favicon standard dimensions.

    </div>

1. Publish your module and open it in the browser. You should see a new icon in the browser tab.

## Use an ICO image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **ICO image**:

1. In Service Studio, go to the **Data** tab > **Resources**, select **favicon.png** and change its **Name** to `favicon.ico`.

    ![Properties showing favicon with ICO extension](images/change-favicon-to-ico-ss.png?width=500)

1. Right-click **favicon.ico** and select **Change Resource**.

1. In **Change Resource**, select an ICO image with the new favicon.

1. Check if some elements in the module use the old icon and update them if needed. Press **Ctrl+F** or click the search icon, enter `favicon.png` and select **Search in this Module**.

    <div class="info" markdown="1">

    If you have just created your app, the **'favicon.png' occurrences in Module** search tab shows four occurrences of **favicon.png**, all in different **AddFavicon** actions.

    </div>

1. In the **'favicon.png' occurrences in Module** search tab, select **REPLACE ALL OCCURRENCES**.

1. Enter `favicon.ico` and select **OK**.

1. Publish your app and open it in the browser. You should see a new icon in the browser tab.

## Troubleshooting

If your new favicon isn't showing, it may be because the old favicon is still in the browser cache. If you are using Chrome, right-click the tab with your app and select **Reload**.
