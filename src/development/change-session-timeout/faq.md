---
tags: version-10; 
summary: 
---

# How to change the timeout of a session in a Web Application at runtime

How can I change the session timeout in a Web Application at runtime?

## Answer

To change a module's session timeout at runtime (whenever a session starts) follow these steps:

1. In Service Studio create a .NET Extension module. When Integration Studio opens create an action, **SetSessionTimeout**, with one Integer Input, `Minutes`, and one Boolean Output, `Success`.

1. Click **Edit Source Code .NET** and add the following snippet to the Action:

        ssSuccess = false; 
        try
        {
            HttpContext.Current.Session.Timeout = ssMinutes;
            ssSuccess = true;
        }
        catch (Exception e)
        {
        ssSuccess = false;
        }

1. 1-Click Publish the Extension. 

1. Inside Service Studio reference the **SetSessionTimeout** Action in the module where you want to change the session timeout.

1. In the Logic Tab right-click the Server Actions Folder and select **Add System Event**, **On Session Start**.

1. Add the **SetSessionTimeout** Action to the **On Session Start** flow.

    This sets the new session timeout when a session starts.   

<div class="info" markdown="1">
You can customize your **On Session Start** flow and use the `Success` Boolean Output to get feedback from the Action.
%%You can set a Site Property as the `Minutes` Input Parameter from **SetSessionTimeout** to be able to change your session timeout without republishing your module (with every change to the session timeout duration).
%%You can also call your **SetSessionTimeout** from other actions and modify your session timeout dynamically at runtime.
</div>
