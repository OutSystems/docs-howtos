---
guid: 898aad86-1277-4840-bcbc-91db6dea61ab
locale: en-us
---

# How to save and restore the active tab on SilkUIFramework

## Question

How can I restore the active tab between visits on SilkUIFramework?

Should I use the RichWidgets "Tabs_ClientSide" component instead?

## Answer

To restore the active tab on the SilkUIFramework, use a Javascript onclick handler to:

* Save the tab number in a hidden input

* Submit it to the server with a hidden button, and set a session variable.

 

For example:

1. Add a session variable for keeping the current tab (e.g. *SelectedTab*), with data type: *Tabs Identifier*.

2. Add an Input field to the screen or web block, with properties:

    1. Style Classes = *RememberTabInput*

    2. Extended properties: name = *style*, value = "display:none;"

    3. Also set the Variable (create a new one, e.g. *TabNumber*)

3. Add a Button to the screen or web block, with properties:

    4. Style Classes = *RememberTabButton*

    5. Method = *Ajax Submit*

    6. Extended properties: name = *style*, value = "display:none;"

4. Add this script to an Expression with property Escape Content = *No*:

```
"<script language='javascript'>
 $('.Tabs__tab').click(                                                  
    function() {                                       
        var  activeTabNumber = $(this).attr('value');      
        $('.RememberTabInput')[0].value = activeTabNumber; 
        $('.RememberTabButton')[0].click(); 
    }
)             
</script>"
```                                         

5. Add a screen action as destination for the button created in step 3. The variable associated to the input will hold the tab number (1, 2, 3...). Add some logic to set the session variable created in step 1.

6. In your Tab widget, fill in parameter *ActiveTab *with the session variable created in step 1 (e.g. *Session.ActiveTab*).

 

## Improved answer

This solution will work well when navigating back to the page. However, the browser will show a cached version of the page if:

* The user reloads the page;

* The user returns to the page through the browser history.

Add a response header to avoid caching the page. For example, add the header `*Cache-Control="NO-STORE"*`.

On the Preparation of the screen with the tabs, add the action *HttpRequestHandler* > ***_AddHeader_** action, as shown below.

![image alt text](images/How-to-save-and-restore-the-active-tab-on-SilkUIFramework_0.png)

### More information

Read the following for more information on browser caching:

* [http://blog.maskalik.com/asp-net/resolving-browser-back-button-with-caching-pages/](http://blog.maskalik.com/asp-net/resolving-browser-back-button-with-caching-pages/)

* [http://www.mobify.com/blog/beginners-guide-to-http-cache-headers/](http://www.mobify.com/blog/beginners-guide-to-http-cache-headers/)

