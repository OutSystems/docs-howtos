---
tags: version-10; support-Application _Lifecycle; support-Application_Lifecycle; support-Security; roles; User;
summary: 
---

# How to grant and revoke granular permissions

How can I give end users the ability to assign fine-grained permissions?

For example: I want to implement permissions to View, Print, Edit and Delete and I want these roles to be granted and revoked by certain end users of the Application and not the development team.

![](images/fine-permissions-00.png)

## Answer

To give end users the ability to grant and revoke fine-grained permissions follow these steps:

1. Create a role for each granular permission in a Module of your Application.

    ![](images/fine-permissions-01.png)

1. Use the role functions to restrict or allow access on your screens and logic:

    * **CheckViewRole()**
    * **CheckPrintRole()**
    * **CheckEditRole()**
    * **CheckDeleteRole()**

1. Create a back-office screen and use the related role actions to manage the permissions:

    * **GrantViewRole()**, **RevokeViewRole()**
    * **GrantPrintRole()**, **RevokePrintRole()**
    * **GrantEditRole()**, **RevokeEditRole()**
    * **GrantDeleteRole()**, **RevokeDeleteRole()**