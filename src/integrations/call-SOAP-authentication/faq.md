---
summary: Learn how to handle SOAP web service authentication in OutSystems 11 (O11) by saving WSDL locally and using EnhancedWebReferences for credentials.
guid: bace3ad4-c605-4a40-bb54-b78a7a2830c5
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/gKoXqtZTY2IJjyMWschrRB/Integrations?node-id=147:325
tags: soap, web services, authentication, wsdl, enhancedwebreferences
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - enhancedwebreferences
content-type:
  - procedure
---

# How to call a SOAP web service with authentication

## Question

I am having some issues with a Soap Web Service I am trying to import to OutSystems.

After trying to use the option "Consume Soap Web Service…" I am getting the following error. The Web Service that I try to connect to has an authentication, but I don’t know where to add the user and password.

Can you please help me with this?

![Error dialog showing 'WSDL Load Error' with a message 'Couldn't access resource at [URL] The remote server returned an error: (401) Unauthorized.'](images/How-to-call-a-SOAP-web-service-with-authentication_0.png "WSDL Load Error Dialog")

## Answer

if your web service requires authentication then what you need to do is first fetch the WSDL from your browser and save it locally on your disk. Then instead of pointing to the URL you have to put the path to the file in the filesystem (e.g `c:\\mysoap.wsdl`) and this should allow you to import the web service.

Also if your WS requires authentication when invoking you might have to set the proper credentials. For that you can use the **SetWebReferenceCredentials** from the **EnhancedWebReferences** extension to set the username and password.

![Screenshot of the EnhancedWebReferences extension in OutSystems showing the 'SetWebReferenceCredentials' action selected.](images/How-to-call-a-SOAP-web-service-with-authentication_1.png "SetWebReferenceCredentials Action in OutSystems")

