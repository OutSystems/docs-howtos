---
summary: Learn how to install the OutSystems 11 (O11) trial on Microsoft Azure, including VM setup and app creation.
tags: cloud deployment, azure services, virtual machines, infrastructure as a service, platform as a service
locale: en-us
guid: e0085624-ca0d-42cf-91ae-f259280dc67b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/o7Rkyuxm89D6KrjD7AOYCU/Infrastructure?node-id=1242:781
audience:
  - full stack developers
  - platform administrators
  - infrastructure managers
outsystems-tools:
  - none
content-type:
  - procedure
---

# Install OutSystems Trial on Azure

Are you ready to discover the joy that's developing with OutSystems on Microsoft Azure? Then let's get you started with the Trial. This article explains how to:

* [Launch the installation wizard](#launch)
* [Start your VM](#start-vm)
* [Create your OutSystems apps](#create-apps)

## Launch the installation wizard {#launch}

The first part of installing your trial is to launch the installation wizard:

1. Log in to the Azure portal with your Azure account and search for **OutSystems 11 Standalone Trial**.

1. Click **Create**. The Azure Portal starts a standard VM creation wizard.

    ![Screenshot of the 'Create' button for OutSystems 11 Standalone Trial on Microsoft Azure portal.](images/azure-trial-create.png "Create OutSystems Trial on Azure")

1. The creation wizard starts on the **Basics** blade fill in the details:
    * On the **Resource group** choose **Create new** and name your resource.
    * Select your desired Azure region under **Region**.

        ![Screenshot of the 'Basics' tab in the Azure portal showing fields for subscription, resource group, and region during OutSystems trial setup.](images/azure-trial-basics.png "OutSystems Trial Basic Setup")

1. Click **Next: OutSystems Trial Setup**.

1. On the **OutSystems Trial Setup** blade fill in the **Username** and **Password**. These will be the credentials:
    * to connect to the VM via remote desktop using the **Username** and **Password**;
    * to connect to the SQL server with the username `admin`and the **Password** you defined in this step;
    * to connect to your OutSystems trial using Service Studio and Service Center with the username `admin`and the **Password** defined.

1. Click **Next: Virtual Machine Setup**.

1. On the **Virtual Machine Setup** blade, accept the suggested VM size or change it to your preference.

    ![Screenshot of the 'Virtual Machine Setup' tab in the Azure portal with the default VM size selected for the OutSystems trial.](images/azure-trial-vm.png "Virtual Machine Size Selection")

1. You're almost done, click **Next: Review + create**.

1. Click **Create**. 

Your OutSystems trial starts to deploy. A complete OutSystems platform will be deployed and it can take a while, but you can check its progress:

![Screenshot showing the deployment progress of OutSystems trial on Azure with various resources listed and their status.](images/azure-trial-deployment.png "OutSystems Trial Deployment Progress")


Deployment completed, you can now access your new VM.

![Screenshot indicating the completion of the OutSystems trial deployment on Azure with a 'Go to resource group' button.](images/azure-trial-complete.png "OutSystems Trial Deployment Complete")

## Start your VM {#start-vm}

Next, make sure the new VM is started. First you'll need to locate the recently created VM. The Azure Portal offers several filtering options for your resources. 

1. You can, for example, click **Go to resource group** once the deployment has finished and look for the **OS11Trial** virtual machine.

1. Click **Start**.

    ![Screenshot of the 'Start' button in the Azure portal to initiate the OutSystems trial virtual machine.](images/azure-trial-start.png "Starting the Virtual Machine")


    If the **Start** button is disabled your VM is already started and you can proceed.


## Create your OutSystems apps {#create-apps}

You OutSystems Azure Trial is ready to use, so go ahead and take it for a spin! But let's ensure you have all the necessary components first.

1. [Download and install the Development Environment 11](https://www.outsystems.com/downloads/) on your local computer. 

1. Connect [Service Studio](https://success.outsystems.com/Documentation/11/Getting_started/Service_Studio_Overview)  to your environment. 

    * You'll need the address of you VM to connect. It's the address associated with the **OS11Trial Application gateway** that can be found on the Azure Portal:

        ![Screenshot of the Azure portal showing the 'OS11Trial Application gateway' in the resource group for the OutSystems trial.](images/azure-trial-gateway.png "OutSystems Trial Application Gateway")

    * Click on the **OS11Trial Application gateway** to see the **Frontend public IP address**. You can use either the IP or the `<my_trial>.cloudapp.azure.com` address.

    * Launch Service Studio on your local computer. A **Connect to Environment** dialog box will appear. On the top right corner click **Sign in with environment URL**. The login box will look like this:

        ![Screenshot of the Service Studio login dialog box with fields for environment, username, and password.](images/azure-trial-ss.png "Service Studio Login Dialog")

        Your Service Studio may already launch with this login box. No worries, you're in the right place, just follow to the next steps.
    
    * On the **Environment** field, fill in the address of the **OS11Trial Application gateway**. Use the username `admin`and the password you defined on **step 5** of the [installation wizard](#launch}).

    * Click **LOG IN**. This warning will appear:

        ![Screenshot of a warning dialog in Service Studio indicating an insecure connection due to a missing SSL certificate.](images/azure-trial-warning-ss.png "Service Studio Insecure Connection Warning")



        You'll see this warning because by default, the OutSystems 11 Standalone Trial doesn't have an SSL certificate installed. You can [add a valid certificate](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_on_Microsoft_Azure/Set_Up_OutSystems_on_Microsoft_Azure#add-a-valid-certificate-to-the-environments) or click **CONNECT ANYWAY**.

1. You're almost ready to start creating OutSystems apps! One final step, let's [install the extended product components](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_on_Microsoft_Azure/Set_Up_OutSystems_on_Microsoft_Azure#Install_the_extended_product_components).


### Need a hand?

If you want to learn more before creating your first OutSystems apps, we have a lot of available resources:

* Visit [OutSystems training](https://www.outsystems.com/training/).
* Check the guided introductions to [create your first Reactive Web app](https://success.outsystems.com/Documentation/11/Getting_started/Create_Your_First_Reactive_Web_App) and to [create your first mobile app](https://success.outsystems.com/Documentation/11/Getting_started/Create_Your_First_Mobile_App).
