---
summary: Demo application for implementing hierarchical roles
tags: app-development; OutSystems-roles; user-roles; hierarchical-roles; 
guid: c3a3c216-5fcb-4943-b787-aa744827ad28
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?node-id=742:293
---

# Sales application demo

This page shows a sales application demo that controls access through a [predefined authorization mechanism](hands-on.md). Let’s call it **Sales**.

This application demonstrates how to use the Hierarchical Roles approach. It’s a simple application with only one end-user module. In this module, you can find several screens. Your future business applications that require a Hierarchical Roles approach are going to be similar to this application.

<div class="info" markdown="1">

[Download from the OutSystems Forge](https://www.outsystems.com/forge/Component_Overview.aspx?ProjectId=8742) the Hierarchical Roles example described in this article, and publish it in your factory environment. Use it as a reference or adapt the code to implement your business case.

</div>

In the [first article](faq.md), you learned about the roles and what they're used for:

* Authorization mechanisms at screen level: who accesses what screens

* Controlling displayed information: who sees what inside screens

* Controlling available actions: who can update/insert/delete what

Let’s see how you can cover these three scenarios with the new hierarchical roles approach.


## Authorization mechanisms at screen level

To control which role in your factory can access the sales screens, you should take advantage of the built-in Screen Roles feature.

In every screen of this application, you have to assign the unique role that you have created before: **Sales**.

![Screenshot of the screen role assignment for the Sales application.](images/sales-role-ss.png "Sales Role Screen Assignment")

## Controlling the displayed information

Simply call the **HasAccessByFunctionId** action, described previously, in screen preparations. This way you identify if a specific user/function has permission to access the entire screen or parts of the screen.

If the user doesn’t have permission to access the screen, raise an exception, and redirect the user to the Invalid Permissions screen.

The following figure shows the **HasAccessByFunctionId** action and the exceptions in the logic.

![Flowchart showing the HasAccessByFunctionId logic used to control screen access.](images/hasaccessbyfunctionId-logic-ss.png "HasAccessByFunctionId Logic Flow")

## Controlling the available actions

In screens where users can perform actions such as updating records, importing reports, etc., you may need to validate the user's permissions for each of these actions. To perform this validation, you can call **GetPermissionsByUserId** in those screens’ **Preparation**. Simply check the outputs of this action to understand if the user has permission to read/write or not.

The following figure shows the SalesDashboard screen Preparation.

![Screenshot of the SalesDashboard screen preparation logic in OutSystems.](images/sales-dashboard-screen-preparation-ss.png "Sales Dashboard Screen Preparation Logic")

The figures below depict the use of the **GetPermissionByUserId** action in the Preparation logic, and the assignments to check the permissions:

![Screenshot depicting the use of GetPermissionsByUserId action in screen preparation.](images/getpermissionbyuserid-action-preparation-ss.png "GetPermissionsByUserId Action in Preparation")

![Screenshot showing the permission checking logic wrapper in OutSystems.](images/permission-checking-wrapper.png "Permission Checking Logic Wrapper")

![Screenshot of an if condition used to check a user's permission in OutSystems.](images/if-condition-check-users-permission-ss.png "If Condition to Check User's Permission")

Here's how the **Sales** module looks like:

![Screenshot showing the overview of the Sales module in OutSystems.](images/sales-module-overview-ss.png "Sales Module Overview")

## SalesDashboard screen

Every role can access the SalesDashboard screen. It’s the homepage and it's not restricted by function.

At the preparation, calling the **GetPermissionsByUserId** action shows or hides parts of the screen, or allows or forbids operations on the screen.

Let’s consider two users and two Functions:

* Agnes Marvs, as Account Manager;

* Angela Arthur, as Agent.

At the BackOffice, the configuration of the Account Manager role allows you to have Read/Write permissions, while the Agent role has Read-Only permission.

As an Account Manager, Agnes Marvs can perform the actions "Pay Bills" and “Transfer.”, as depicted in the figure below.

![Screenshot of the SalesDashboard screen with write permissions enabled for an Account Manager.](images/write-permission-example-screen.png "Write Permission Example Screen")

As an Agent, Angela Arthur doesn’t see any actions. 

![Screenshot of the SalesDashboard screen with read-only permissions for an Agent.](images/read-only-permission-example-screen.png "Read-Only Permission Example Screen")


## Other screens

Other dashboards are function-specific. This means that only the designated function or higher functions in the hierarchy can access the dashboard screen. Two examples:

* **DashboardAgent** (Agent specific): since Agent is the lowest level in the hierarchy, every function can access it.

* **DashboardRegionalManager** (Regional Manager-specific): only Regional Manager or above roles can access it. The Account Manager and Agent functions can't enter this screen.

To implement this access, at the preparation you need to add the **HasAccessByFunctionId** action to restrict or allow access to the screen.

Let’s use the same users with the same functions to exemplify - Agnes Marvs (Account Manager) and Angela Arthur (Agent).

The Agent function accesses the Agent Dashboard:

![Screenshot showing an Agent's access to the Agent Dashboard in the Sales application.](images/agent-dashboard-access-by-agent.png "Agent Dashboard Access by Agent")

The Account Manager function, or any other function, accesses the Agent Dashboard.

![Screenshot showing an Account Manager's access to the Agent Dashboard in the Sales application.](images/agent-dashboard-access-by-account-manager.png "Agent Dashboard Access by Account Manager")

The Account Manager function accesses the Dashboard Account Manager.

![Screenshot showing an Account Manager's access to their own dashboard in the Sales application.](images/account-manager-dashboard-access-by-account-manager.png "Account Manager Dashboard Access by Account Manager")

The Agent role can't access the Dashboard Account Manager. 

![Screenshot displaying an 'Invalid Permissions' error message when access is denied.](images/invalid-permissions-access-screen.png "Invalid Permissions Access Screen")
