---
summary: Explore how to integrate Auth0 with OutSystems 11 (O11) for streamlined user authentication and single sign-on capabilities.
tags:
guid: f42b952f-3f83-4a46-b15f-bc96a6080bfb
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?node-id=742:262
---

# How to integrate Auth0 with OutSystems

<div class="info" markdown="1">

This article was written by [Justin James](https://www.outsystems.com/profile/5685/justin-james/), OutSystems MVP.
</div>

[Auth0](https://auth0.com/) is an authentication and authorization service that lets you easily provide single sign-on services. This way, your application can use other services, such as Azure and Dropbox, as the source of the user accounts. 
Integrating them into your OutSystems application makes it much faster for your users to log in to your application because they will have fewer accounts to manage and do not need to go through a lengthy signup process with your application.

## Integrating Auth0 with OutSystems

Auth0 supports the SAML protocol and the IdP component in the OutSystems Forge implements this protocol, so we will leverage that component for this guide. The only work needed is the configuration of IdP and the modification of your application so it can use it. Here are the steps:

1. [Get IdP from the Forge](https://www.outsystems.com/forge/component-overview/599/idp) and publish it to your server. You can install it directly through Service Studio.
1. Modify your application to use IdP as per the instructions in IdP, found at `https://hostname/IdP/Instructions.aspx` (use your hostname) after installation on the server.
1. [Sign up for an Auth0 account](https://auth0.com/signup).
1. [Turn on and configure SAML in your Auth0 account](https://auth0.com/docs/protocols/saml/saml-configuration/auth0-as-identity-provider).
1. [Set up the generic SAML IdP connection in Auth0](https://auth0.com/docs/protocols/saml/saml-idp-generic). For the `Application Callback URL` parameter, use the value `https://hostname/IdP/SSO.aspx` (filling in the correct hostname for your server).

    ![Screenshot of the Auth0 SAML configuration settings with fields for callback URL and various options.](images/setting-up-auth0-authentication-01.png "Auth0 SAML Configuration Settings")

1. Go to the Usage tab of Auth0’s SAML configuration to get the information needed for your IdP Configuration page (`https://hostname/IdP/Configuration.aspx`). Fill out the Configuration parameters according to the picture below:

    ![Screenshot showing the process of configuring IdP settings in OutSystems with fields mapped to Auth0 settings.](images/setting-up-auth0-authentication-02.png "IdP Configuration in OutSystems")

1. Configure your users in Auth0.
1. Test!

One thing that you will note, is that when someone logs in via IdP, it will create a user account for them in OutSystems, but it will also not bring over user information such as name into the OutSystems User record. Your workflow should likely drive people to provide their details after login until they complete enough information for your application to work as expected.
