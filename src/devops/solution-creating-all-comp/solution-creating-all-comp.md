---
summary: Explore how OutSystems 11 (O11) facilitates the creation and management of solutions for efficient application deployment and troubleshooting.
tags:
guid: 065b4d9d-5b4a-4892-9e82-bdfc77ea98d3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/XbkdagtFJ9kxan8pAx0Qsz/DevOps?node-id=1542:366
---
# Creating and using a solution

It's a common practice in OutSystems Factory management to create and use a solution. This is either a Factory solution containing all the components, a solution for a specific module or an application with all its dependencies. It's used to:

* Refresh references in environments used for development purposes.
* Republish application modules after an update or upgrade.
* Troubleshoot some tasks.

For feature availability in different environments check [here]( https://success.outsystems.com/Documentation/11/Setup_and_maintain_your_OutSystems_infrastructure/Setting_Up_OutSystems/Configure_your_OutSystems_environment#feature-availability-for-different-purposes).

A solution can also be used to publish a version of a specific application in another environment as an alternative to a LifeTime staging. For example, an "All Components" solution will publish and deploy all associated components.

## Creating an "All Components" solution

If you don't have an "All Components" solution yet:

1. Go to Service Center (`https://<YOUR_ENVIRONMENT>/ServiceCenter`).

1. Under **Factory** -> **Solutions**, click the **New Solution** link.

    ![Screenshot of the Service Center interface highlighting the 'New Solution' button.](images/servicecenter-new-solution.png "Service Center New Solution Button")

1. Name the solution "All_Components" and click the **Save** button.

    ![Screenshot showing the 'Create Solution' form with the 'All_Components' name entered and the 'Save' button highlighted.](images/servicecenter-create-solution.png "Service Center Create Solution Form")

### Adding the components

On the "All Components" solution screen:

1. Go to the **Components** tab.

1. Click the **Associate All Modules/Extensions** button.

    ![Screenshot of the 'All Components' solution screen with the 'Associate All Modules/Extensions' button highlighted.](images/servicecenter-solution-associate-modules.png "Service Center Associate All Modules Button")

    For previous versions of Service Center, type "*" and click the **Associate** button:

    ![Screenshot of the Service Center's previous version interface for associating components with a solution, showing an input field and the 'Associate' button highlighted.](images/servicecenter-solution-associate-modules-previous-version.png "Service Center Associate Components with Solution")

## Creating a solution for a module and all its dependencies

1. Go to Service Center (`https://<YOUR_ENVIRONMENT>/ServiceCenter`).
1. Under **Factory** > **Solutions**, click the **New Solution** link

    ![Screenshot of the Service Center interface highlighting the 'New Solution' button.](images/servicecenter-new-solution.png "Service Center New Solution Button")

1. Name the solution and click the **Save** button.

    ![Screenshot showing the 'Create Solution' form for a module with all dependencies, with the 'Save' button highlighted.](images/servicecenter-create-solution-all-dependencies.png "Service Center Create Solution for Module with Dependencies")

### Adding the components

1. Go to the **Components** tab.
1. Search for the module name, tick the **include dependencies as component** checkbox.
1. Click the **Associate** button.

    ![Screenshot of the 'Associate Components with Solution' section where a specific module is entered and the 'Associate' button is highlighted.](images/serviceceneter-solution-module.png "Service Center Associate Module with Solution")

### How to use

* Whenever you want to **republish your whole factory**, click the **Publish** button for the "Current Running Version".

    ![Screenshot of the 'Versions' tab in Service Center with the 'Publish' button for the 'Current Running Version' highlighted.](images/servicecenter-solution-publish.png "Service Center Publish Solution Button")

* If you want to **deploy the whole solution to another environment** or just download the solution for **troubleshooting** purposes, you can click the **Download** button for the "Current Running Version", or any other version you have created (you can then save the .osp file in your file system).

    ![Screenshot of the 'Versions' tab in Service Center with the 'Download' button for the 'Current Running Version' highlighted.](images/servicecenter-solution-download.png "Service Center Download Solution Button")  

The publishing operation by itself doesn't impact application availability at runtime. However, you should consider any possible breaking changes (for example, after an upgrade or update) or broken references as not to impact the applications' behavior.

<div class="info" markdown="1">

There is generally no need to create versions for this solution. If you do, remember that publishing a solution version may revert some applications to the version they were in when the solution version was created.
</div>
