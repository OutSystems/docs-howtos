# How to host a big resource file in your server

## Question

How to host a large CSS stylesheet file in my server?

For example, a 800 KB fonts.css file downloaded from [typography.com](http://typography.com/)?

## Answer

Create a new eSpace to host the large CSS resource.

Since resources are uploaded each time you publish an eSpace, it's better to keep big resources outside the eSpaces that change often.

Here are the steps:

1. Create a new empty Module (e.g. **Fonts**).

2. Under tab **Data**, section **Resources**, right-click and select **Import Resource**. Select the **fonts.css** file you've downloaded.

3. In the properties of the resource, make sure you select **Deploy to Target Directory** as the Deploy Action (see screenshot below).

4. Publish the Module.

5. On your current Module, change your link tag URL to point to the new space and resource. For example: <link type="text/css" rel="stylesheet" href="**/Fonts/fonts.css**" />.

![image alt text](images/How-to-host-a-big-resource-file-in-your-server_0.png)

<div class="info" markdown="1">
The first browser request will still take some time, because it's a big file. But the browser should cache its contents in the subsequent requests.
</div>

