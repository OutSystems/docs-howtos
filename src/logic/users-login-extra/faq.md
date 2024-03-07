---
tags: version-11; Users; Authentication; Login
summary: Extend the Users' login flow to perform extra and custom validations
guid: 111f0e26-2847-4d05-b234-2064053a3b26
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/3YpPKdo5QwN0z6up61eKe5/Logic?node-id=842:240
---

# How to add extra logic to Users' login

In some scenarios, there may be the need to extend the default built-in login mechanism for end-users.
Some common scenarios that require such extension are:

* Validate if the user is active on an external system
* Captcha validation
* Validate extra login data (besides username and password)

To successfully extend the existing end-users login logic you need to perform three steps:

1. Extend the Users' data model
1. Create the server-side validation logic
1. Extend the default Login action

## Extend the Users' data model

The existing Users data model can be extend but not modified, since it's a core component of OutSystems.
However, extending it allows for customizations while still relying on the core authentication mechanisms.

Extending the Users' data model requires creating a new Entity with a [1-to-1 relationship](https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Data/Data_Modeling/Entity_Relationships/Create_a_One-to-One_Relationship) to the User entity.

You can apply the following steps in Reactive Web, Mobile, and Traditional Web applications.

1. Inside your module that contains the Login screen, switch to the **Data** tab.
You should have a reference to the User entity, located under _(System_).

    ![Screenshot of the Data tab in OutSystems with the User entity highlighted.](images/users-login-extra-data-tab-user-entity.png "Data Tab Showing User Entity")

1. Add a new Entity, named **UserExtended**.

1. Change the **Id** attribute Data Type to _User Identifier_.
This creates a 1-to-1 relationship between the User entity and your UserExtension entity.

    ![Screenshot showing the UserExtended entity with the Id attribute set to User Identifier data type.](images/users-login-extra-user-extension-id.png "UserExtended Entity with User Identifier")

1. Add the attributes needed for your particular use case.
For instance, add an attribute named **ExpirationDate** with the _Date_ data type.

    ![Screenshot displaying the ExpirationDate attribute added to the UserExtended entity.](images/users-login-extra-expiration-date.png "UserExtended Entity with ExpirationDate Attribute")

    The attribute used here is an example.
    [Later on](#create-the-server-side-validation-logic), you will check the expiration date.
    If the expiration date is later than the current date, the user will be able to login.
    Otherwise, the user can't log in.
    Note that you aren't implementing the functionality to fill the attribute with data.
    For that, you would need to create a back office or automate the creation of the records in the UserExtension entity.

## Create the server-side validation logic

For security reasons, all validations related to authentication should be done at the server-side (that is, inside a Server Action).

The following steps describe the creation of a Server Action that validates if the Expiration Date is in the future.
In the opposite scenario, if the expiration date is in the past, an Exception is raised.

1. In the Logic tab, create a new Server Action named **ValidateUserExpirationDate**.

1. Inside the flow of the _ValidateUserExpirationDate_ server action, add an Aggregate that fetches the data from the UserExtension entity.
Use the following filter `UserExtension.Id = GetUserId()` to fetch only the data for the current user.

    As best practice, you may also set the Max. Records property of the Aggregate to 1.

1. Add an If after the Aggregate with the following Condition `GetUserExtensionById.List.Current.UserExtension.ExpirationDate >= CurrDate()` where _GetUserExtensionById_ is the name of the Aggregate created in the previous step.

1. Connect the True branch of the If to an End.

1. Connect the False branch of the If to a Raise Exception.

    You may need to create a new Exception if you don't have one created already.

1. The flow should be similar to:

    ![Flowchart of the ValidateUserExpirationDate server action with logic to check user's expiration date.](images/users-login-extra-validateuserexpirationdate-flow.png "Server Action ValidateUserExpirationDate Flow")

    Depending on your specific use case, you can define more complex validations.
    To do that, adapt the server action to match your specific requirements.

## Change the default Login action

The actual login logic is different depending on the type of application you are working on.

If your application is Traditional Web, skip the following section.

### In Reactive Web and Mobile

The default logic for the login is implemented in multiple places.
You have the Login screen (located in the Interface tab, under the Common UI Flow).
Upon login, the Login client action of the screen is executed.
This client action submits the login information to the server by executing the DoLogin Server Action.

<div class="info" markdown="1">

You can find this Server Action in the Logic tab under the Server Actions > Authentication folders.
</div>

![Screenshot of the DoLogin server action in the Logic tab of OutSystems.](images/users-login-extra-dologin.png "DoLogin Server Action")

Extending the login logic should be done at the server side, namely inside the _DoLogin_ action.

After the existing User_Login, add another **Run Server Action** to the **ValidateUserExpirationDate** server action created in the previous section.

![Flowchart showing the extended DoLogin server action including the ValidateUserExpirationDate action.](images/users-login-extra-dologin-extended.png "Extended DoLogin Server Action")

<div class="info" markdown="1">

Due to the way the **ValidateUserExpirationDate** is defined, the actual login will be aborted (due to the raised exception) if the Expiration Date is in the past.
</div>

### In Traditional Web

The default login logic is implemented inside the Login screen (located in the Interface tab, under the Common UI Flow).

Add a **Run Server Action** immediately after the User_Login to the **ValidateUserExpirationDate** server action created before.

![Flowchart of the Traditional Web application login flow with the ValidateUserExpirationDate action.](images/users-login-extra-login-traditional.png "Traditional Web Login Flow")

<div class="info" markdown="1">

Note that if the Expiration Date is in the past, an Exception is raised inside the **ValidateUserExpirationDate**.
That will cause the login to be aborted.
</div>
