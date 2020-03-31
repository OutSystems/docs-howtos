---
tags: version-11; favicon;
summary: Instructions on how to set the favicon in Reactive Web Apps.
---

# How to set a favicon in Reactive Web Apps

<div class="info" markdown="1">

This how-to applies to the Reactive Web Apps only.

</div>

By default, OutSystems Reactive apps use the OutSystems logo as the favicon. The name of the default favicon is **favicon.png**, and it's in **Resources**, in the **Data** tab.

## Use a PNG image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **PNG image**:

1. In the **Data** tab > **Resources**, right-click **favicon.png** and select **Change Resource**.

1. In **Change Resource**, select a PNG image with the new favicon.

After publishing your Module, test your app and make sure the new favicon is shown.

## Use a ICO image as a favicon

Follow these steps to change the favicon in your Reactive Web App to a different **ICO image**:

1. In the **Data** tab > **Resources**, select **favicon.png** and change its **Name** to `favicon.ico`.

1. Right-click **favicon.ico** and select **Change Resource**.

1. In **Change Resource**, select an ICO image with the new favicon.

1. In **Search**, enter `favicon.png` and select **Search in this Module**.

        <div class="info" markdown="1"> 

        If you have just created your app, the **'favicon.png' occurrences in Module** search tab shows four occurrences of favicon.png, all in different **AddFavicon** actions.

        </div>

1. In the **'favicon.png' occurrences in Module** search tab, select **REPLACE ALL OCCURRENCES**.

1. Enter `favicon.ico` and select **OK**.

After publishing your Module, test your app and make sure the new favicon is shown.

## Troubleshooting

If you are testing your app and your new favicon is not appearing, it may be because the old favicon is still in cache. If you are using Chrome to test your app, right-click the tab with your app and select **Reload**. 
