---
summary: This article guides on how to create/update a Solution package including all the modules in the environment and how to use it. A solution with all the modules can be used to refresh references in bulk or to update a factory in non production environments.
tags:
---
# Creating and using an "all components" solution

It's a common practice in OutSystems Factory management to create and use a solution that contains all the components deployed on the environment. It's used to refresh references, republish application modules after an update/upgrade and for some troubleshooting tasks.

An all components solution will publish and deploy all of the associated components.
The main difference is that with a solution, all the references are refreshed in one take. This will ensure that consumers get their producers code updated, avoiding compilation errors.

## How to create

### Creating the solution

If you don't have an "All Components" solution yet:

1. Go to Service Center (`https://<YOUR_ENVIRONMENT>/ServiceCenter`).

1. Under **Factory** -> **Solutions**, click the **New Solution** link.

    ![](images/servicecenter-new-solution.png?width=900)

1. Name the solution "All_Components" and click the **Save** button.

    ![](images/servicecenter-create-solution.png?width=600)

### Adding the components

On the "All Components" solution screen:

1. Go to the **Components** tab.

1. Click the **Associate All Modules/Extensions** button.

    ![](images/servicecenter-solution-associate-modules.png?width=800)

    For previous versions of Service Center, type "*" and click the **Associate** button:

    ![](images/servicecenter-solution-associate-modules-previous-version.png?width=800)

## How to use

* Whenever you want to **republish your whole factory**, click the **Publish** button for the "Current Running Version".

    ![](images/servicecenter-solution-publish.png?width=800)

* If you want to **deploy the whole solution to another environment** or just download the solution for **troubleshooting** purposes, you can click the **Download** button for the "Current Running Version", or any other version you have created (you can then save the .osp file in your file system).

    ![](images/servicecenter-solution-download.png?width=800)  

The publishing operation by itself doesn't impact application availability at runtime. However, you should consider any possible breaking changes (for example, after an upgrade or update) or broken references as not to impact the applications' behavior.

<div class="info" markdown="1">

There is generally no need to create versions for this solution. If you do, remember that publishing a solution version may revert some applications to the version they were in when the solution version was created.
</div>
