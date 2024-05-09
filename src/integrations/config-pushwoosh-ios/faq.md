---
tags: version-10; support-Integrations_Extensions; support-Mobile_Apps; support-webapps; Pushwoosh; iOS;
summary: Learn how to configure Pushwoosh for iOS, including creating an App ID and APNS certificate, and setting up in OutSystems 11 (O11).
guid: c299ba80-55f5-4102-89ea-ab2ea0b23315
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/gKoXqtZTY2IJjyMWschrRB/Integrations?node-id=1242:234
---

# How to Configure Pushwoosh for iOS

To configure Pushwoosh for iOS, follow these steps. 

<div class="info" markdown="1">

You will need a Mac computer for this process.
</div>

## Creating an Application Identifier (App ID)

For an application, Apple Push Notification Service (APNS) requires a unique application identifier (App ID) configured with “Push Notifications” enabled. To create one, access your Apple developer account at: [https://developer.apple.com/membercenter/](https://developer.apple.com/membercenter/ "https://developer.apple.com/membercenter/") and enter **Certificates, Identifiers & Profiles**.

![Screenshot of the Apple Developer account overview highlighting the 'Certificates, IDs & Profiles' section.](images/image02.png "Apple Developer Account Overview")

Select **App IDs** and the “+” on the right side of the page to create a new identifier:

![Screenshot showing the 'App IDs' section with the '+' button to create a new identifier in the Apple Developer account.](images/image08.png "App IDs Section in Apple Developer Account")

Complete the form and select **Push Notifications** from “App Services”.

![Screenshot of the form to register a new App ID with 'Push Notifications' service selected.](images/image05.png "Registering an App ID")

## Create an APNS Certificate

APNS Certificates are bound to one application ID. There are two application service configurations for each application ID:

* Development 
* Distribution 

Development APNS Certificates enable a developer to set up push notifications for an application in development. 

<div class="info" markdown="1">

Push notifications do not work in the simulator.
</div>

Access **iOS App IDs** from the Apple Developer Member Center and locate the application identifier you wish to configure. Click the **Edit** button.

![Screenshot of the 'iOS App IDs' page with an 'Edit' button to modify an existing App ID.](images/image11.png "Edit App ID Configuration")

Scroll down to “Push Notifications” and click **Create certificate** for either Development or Distribution.

![Screenshot showing the option to create a new APNS certificate for Development or Distribution.](images/image00.png "Creating an APNS Certificate")

Follow the steps on the page to generate a certificate signing request.

![Screenshot with instructions on how to generate a Certificate Signing Request (CSR) for an APNS certificate.](images/image06.png "Generating a Certificate Signing Request")

<div class="info" markdown="1">

If you don't have access to a Mac [here](<https://success.outsystems.com/Documentation/10/Delivering_Mobile_Apps/Generate_and_Distribute_Your_Mobile_App/More_Information_on_Generating_and_Distributing_Mobile_Apps#create-a-certificate>) is how you can generate a certificate signing request on a Windows machine.
</div>

Upload the newly created certificate signing request file and click the **Generate** button. Once that is done, download the created certificate and add it to your keychain.

![Screenshot of the interface to upload a CSR file and generate an APNS certificate.](images/image04.png "Uploading a CSR File")

## Export Certificates from Keychain

When configuring the iOS settings for an application in Pushwoosh, you must upload the public APNS certificate and its private key for a specific application ID. In step 2, we generated a certificate; now we will export it from the keychain.

Open Keychain, locate the desired certificate and export the public certificate. Usually APNS certificates have a “Apple Development IOS Push Services” prefix or “Apple Production IOS Push Services” prefix followed by the application identifier. Export it as “.cer”.

![Screenshot of the Keychain Access application with an APNS certificate selected for export.](images/image12.png "Exporting a Public Certificate from Keychain")

![Screenshot of the save dialog in Keychain Access for exporting a public certificate as a '.cer' file.](images/image03.png "Saving Exported Certificate")

Export the associated private key. 

<div class="info" markdown="1">

Remember the password you choose when exporting, because it’ll be needed later when setting up iOS on Pushwoosh.
</div>

![Screenshot of the Keychain Access application with a private key selected for export.](images/image13.png "Exporting a Private Key from Keychain")

## Create an Application in Pushwoosh

Access your Pushwoosh account at: [https://cp.pushwoosh.com/applications](https://cp.pushwoosh.com/applications "https://cp.pushwoosh.com/applications"). Create a new application by clicking the **Add new** button.

Pushwoosh recommends the setup of two applications: one for development and one for distribution.

In this example, we’ll create and configure an application using a development APNS certificate. The process is exactly the same for distribution.

![Screenshot of the Pushwoosh dashboard with the 'Add new' button to create a new application.](images/image07.png "Pushwoosh Add New Application")

Give the new application a name, an icon and choose **Pushwoosh** under iOS SDK and Android SDK. Click **Save application**.

![Screenshot of the form to create a new application in Pushwoosh with fields for application title and icon.](images/image01.png "Creating a New Application in Pushwoosh")

## Configure iOS

In the screen that opens, you’ll see an application code. This code is unique to each Pushwoosh application and is used by your application. In the iOS ribbon on this screen, click **Configure**.

![Screenshot showing the unique application code in Pushwoosh for a newly created application.](images/image09.png "Pushwoosh Application Code")

On the **Manual** tab, complete the required information. **Certificate file (.cer)** is the public certificate exported earlier. **Push Certificate (.p12)** is the private key that was exported. **Private key password** is the password picked in the export process for the private key. **Framework** should be set to Native.

![Screenshot of the manual configuration tab for iOS notifications in Pushwoosh with fields for certificate file, push certificate, and private key password.](images/image10.png "Configuring iOS Notifications in Pushwoosh")

Click **Save**. You've now configured Pushwoosh for iOS.
