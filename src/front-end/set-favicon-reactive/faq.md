---
tags: version-11; favicon;
summary: Instructions on how to set the favicon in Reactive Web Apps.
---

# How to set a favicon in Reactive Web Apps

<div class="info" markdown="1">

This FAQ applies to the Reactive Web Apps only.

</div>

Follow these steps to set the favicon in your Reactive Web Apps. You need to do two things in Service Studio:

* Add the favicon to the app resources
* Load the favicon when the Module loads

In this example we're using favicon.ico. You should edit the Java Script if you're using a different file name.

![Service Studio and adding favicon image](<images/favicon-example.png?width=500>)

1. Go to the **Data** tab > **Resources** > **Import resource** and select your favicon.ico file. A dialog shows.
1. In the **Add Resource** dialog window click **Add as resource**. The image is added as a resource and you can set other options. 
1. Set the **Deploy Action** property of the favicon resource to **Deploy to Target Directory**.
1. Go to the **Logic** tab > right-click the **Client Action** folder >  open the **Add System Event** menu > click **On Application Ready**. The logic of this new Action opens.
1. Drag a **JavaScript Tool** to the Flow. Name it AddFavicon.
1. Double-click AddFavicon JavaScript Tool to open the JS editor. Add the following code:

        var link = document.createElement('link');
        link.rel = 'icon';
        link.href = 'favicon.ico';
        var head = document.querySelector('head');
        head.appendChild(link);

1. Publish and open your app in a browser.

