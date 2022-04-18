---
guid: 52dd517e-798e-481e-8528-a656972ec0d0
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# How to configure OutSystems to use identity providers using SAML

## Federated SSO Authentication using SAML

To set up a Federated Authentication in your OutSystems applications, using the SAML protocol to connect to external identity providers you can take advantage of the [IdP Forge component](https://www.outsystems.com/forge/component-overview/599/idp), a generic federated identity provider (IdP) connector. IdP allows your OutSystems applications to integrate with Single Sign-On (SSO) provided by most of the commercial Identity Provider companies.

<div class="info" markdown="1">

Since [Platform Server Release Jul.2019 CP2](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) (August 23rd, 2019) you can configure a SAML 2.0 authentication for the whole environment directly in the Users application. Check the documentation on how to [Configure SAML 2.0 Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/End_Users_Authentication/Configure_SAML_2.0_Authentication).

</div>

With this integration, when the users access an OutSystems application (Service Provider - SP), they are redirected to a web page (known as the enterprise's login manager) where they are prompted to enter their enterprise user name and password. Upon verification of the user’s login, the enterprise identity provider informs OutSystems application of the verified identity for the user who is logging in, and the user is redirected back to the portal website.

![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_0.png)

To successfully establish the connection between the IdP component and the Identity providers you'll need to change the authentication flow and configure both parties to redirect the user to the Login of the Identity Provider. In this article, we'll guide you through the needed setup.

## Configure your application to use IdP connector

### Login Flow

* Change **NoPermission** screen on Common Flow.

In a standard OutSystems application there is a Common Flow responsible for handling authentication and exception.

One of the scenarios is when a user tries to access a resource that requires the user is authenticated, and the user is not authenticated yet.

In that case, the application raises a Security exception that will be handled in Common flow and then redirects the user to the login screen.

So, the first step to integrate an OutSystems application to change this behavior, and instead of redirect the user to the Login screen, redirect it to the Identity Provider.

* Change **Preparation** of the **NoPermission** screen to redirect the user to the URL provided by **IdP_SSO_URL** action.

_Note:_ if the system contains multiple tenants, the tenant switch has to have been done before calling IdP_SSO_URL.

![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_1.png)

### Logout Flow

* Change **LoginInfo** web block on Common Flow (Optional: Single-logout).

In a standard OutSystems application the Common Flow is also responsible for handling Logout operation.

By default, the Logout will invalidate the session on the OutSystems application server, but with an IdP SSO scenario many times the logout must be also performed on IdP Server, redirecting the browser to a specific URL on IdP SSO server.

So, to achieve that, it's necessary to change the Logout default behavior.

If your IdP Server allows a Logout initiated by the SP (IdP Connector), configure the field **IdP server Single Logout URL** which should be provided by your IdP Server (the IdP Connector will generate the SAML messages to perform a Single-Logout).

Note: Your application shouldn't call the User_Logout or Logout system actions. The IdP connector is the one responsible for that call.

* Change **Preparation** of the **LoginInfo** to redirect the user to the URL provided by IdP Server

* If your IdP Server allows a Logout initiated by the SP through SAML messages: call the action **IdP_SingleLogout_URL** and call the **Common\ExternalURL** with its output.

![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_2.png)

## Configure IdP connector

To configure the SAML Single Sign-On in the IdP component you must set up the values according to your Identity Provider.

* **IdP Server Issuer/Entity ID**: A URL that uniquely identifies your SAML identity provider (IdP Server). SAML messages sent from IdP server must match this value exactly in the `<saml:Issuer>` attribute of SAML message.

* **IdP server Single Sign-On URL**: The URL that IdP Connector should redirect to allow a user to sign in.

* **Certificate**: The X.509 public certificate issued by your identity provider. Used to check the signature of SAML messages from the IdPServer.

* **SP Issuer/Entity ID**: SAML Service Provider Issuer (SP Entity ID) sent in SAML messages from the IdP connector.

Optional (when required):

* **IdP server Single Logout URL**: Identity Provider Server Single Logout URL. Used when the server allows SingleLogout initiated by the SP.

* **IdPConnector (SP) Keystore**: The keystore that contains the private key and the public certificate that IdP connector uses to sign SAML messages sent to IdPServer (also to decrypt assertions if encrypted by IdP server). PFX/PKCS12 is the supported format.

* **KeyStore password**: Keystore password to protect the keys in it.

* **Session_Cookie** (site property): Variable that holds the cookie name that has the SessionId of the IdP connector (usually 'ASP.NET_SessionId')

_Note:_ When updating the certificate, make sure you update it on both ends, in your Identity Provider and in OutSystems, in the IdP component.

## Configure Identity Provider - Examples

### Azure AD / ADFS

<div class="info" markdown="1">

Since [Platform Server Release Jul.2019 CP2](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) (August 23rd, 2019) Azure AD (Azure Active Directory) authentication mode is directly available in the Users application, having the "Claims" settings already filled in with Azure AD default values. Check the documentation on how to [Configure Azure AD Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/End_Users_Authentication/Configure_Azure_AD_Authentication).

</div> 

1. Sign in to the [Azure Active Directory portal](https://aad.portal.azure.com/) and add the **OutSystems Azure AD** application from the gallery.

    * Navigate to **Enterprise applications**

    * Click **New application**.

    * Search for **OutSystems Azure AD**.

    * Select the application and click **Add**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_3.png)

1. Select **SAML** as the single sign-on method.

    * In the OutSystems Azure AD application dashboard click the **Single sign-on** entry.

    * Select **SAML**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_4.png)

1. Set up Single Sign-On with SAML.

    * Click the Edit icon on the **Basic SAML Configuration** section.

    * Set the required values accordingly.

        * **Identifier (Entity ID)**: `http://YOUR_SERVER/IdP/`

        * **Reply URL (Assertion Consumer Service URL)**: `https://YOUR_SERVER/IdP/SSO.aspx`

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_5.png)

    * Alternatively, you can upload the metadata file from the IdP connector.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_6.png)

1. You can then [configure the IdP connector](#configure-idp-connector) with the provided information on sections 3 and 4, or upload the **Federation Metadata XML** file downloaded in the Azure AD application.

![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_7.png)

### Okta

<div class="info" markdown="1">

Since [Platform Server Release Oct.2019](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) (October 3rd, 2019) the Users application includes specific configurations for OKTA authentication. Check the documentation on how to [Configure OKTA Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/End_Users_Authentication/Configure_SAML_2.0_Authentication).

</div>

1. Create an Okta trial account.

    * Go the [Okta website](https://www.okta.com/free-trial/) and sign up to create a trial account using your company email address.

    * You should then receive an email with your account details.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_8.png)

1. Sign-in to your Okta domain.

    * Access your Okta domain homepage, as described in the email.

    * Input your username and password and click **Sign In**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_9.png)

1. Add a SAML application to your Okta domain.

    * Access the Admin Dashboard and click to **Add Application**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_10.png)

    * Click on the **Create New App** button.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_11.png)

    * Select Web and SAML 2.0 because we are creating a SAML integration for web applications. Click **Create** to continue.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_12.png)

    * Define the **App Name** (for example, `OutSystems Okta`) and click **Next**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_13.png)

1. Configure the SAML settings for the integration.

    * Set the **Single sign on URL** (URL in the OutSystems environment to handle the SAML response):  
    `http://YOUR_SERVER/IdP/SSO.aspx`

    * Set the **Audience URI (SP Entity ID)**:  
    `http://YOUR_SERVER/IdP/SSO.aspx`

    ![image alt text](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_14.png)

    * Click on the **Show Advanced Settings** link and set the remaining values

    * **Digest Algorithm**: SHA1

    * **Signature Algorithm**: RSA-SHA1

    * **Assertion Signature**: Unsigned

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_15.png)

    * Click **Next** and you'll be asked for some information for feedback purposes. Select the option **I'm a software vendor. I'd like to integrate my app with Okta** and click **Finish** to complete the configuration.

    * Finally, click **View Setup Instructions** to get the data needed to [configure the IdP connector](#configure-idp-connector).

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_16.png)

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_17.png)

### OneLogin

<div class="info" markdown="1">

Since [Platform Server Release Jul.2019 CP2](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) (August 23rd, 2019) you can configure a SAML 2.0 authentication directly in the Users application. Check the documentation on how to [Configure SAML 2.0 Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/End_Users_Authentication/Configure_SAML_2.0_Authentication).

</div>

1. Create a [free OneLogin account](https://www.onelogin.com/signup).

1. Log in to the admin console.

1. Click on **Apps** tab then click on **Add App** button.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_18.png)

1. Search for **SAML** and select **SAML Test Connector (IdP)** option.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_19.png)

1. Configure **Display Name** of your application and then click on **Save** button.

1. Click on the **Configuration** tab and configure the following properties.

    * **ACS (Consumer) URL Validator**: URL of the OutSystems environment to handle the SAML response (`http://YOUR_SERVER/IdP/SSO.aspx`)

    * **ACS (Consumer) URL**: URL of the OutSystems environment to handle the SAML response (`http://YOUR_SERVER/IdP/SSO.aspx`)

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_20.png)

1. Click on **SSO** tab and configure the following properties

    * **SAML Signature Algorithm**: SHA-1

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_21.png)

1. Finally, [configure the IdP connector](#configure-idp-connector) with the provided information.

### PingOne

<div class="info" markdown="1">

Since [Platform Server Release Jul.2019 CP2](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) (August 23rd, 2019) you can configure a SAML 2.0 authentication directly in the Users application. Check the documentation on how to [Configure SAML 2.0 Authentication](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/End_Users_Authentication/Configure_SAML_2.0_Authentication).

</div>

1. Create a [free Ping Identity account](https://www.pingidentity.com/).

1. Log in to the [admin console](https://admin.pingone.com/web-portal/login).

1. Click on the **Applications** tab then click on **Add Application** button.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_22.png)

1. Select **New SAML Application** option.

1. Configure application name, description, category and click on **Continue to Next Step**.

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_23.png)

1. On **Application Configuration** configure the following properties

    * **Assertion Consumer Service (ACS)**: URL of the OutSystems environment to handle the SAML response (`http://YOUR_SERVER/IdP/SSO.aspx`)

    * **Entity ID**: URL of the OutSystems environment to handle the SAML response (`http://YOUR_SERVER/IdP/SSO.aspx`)

    * **Signing Algorithm**: RSA_SHA1

    ![](images/How-to-configure-OutSystems-to-use-identity-providers-using-SAML_24.png)

1. Click on **Continue to Next Step** and then **Save & Publish**.

1. Finally, [configure the IdP connector](#configure-idp-connector) with the provided information.
