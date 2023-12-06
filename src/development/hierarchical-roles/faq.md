---
summary: Learn how to create several hierarchy roles using the default OutSystems user roles
tags: article-page; app-development; OutSystems-roles; user-roles; hierarchical-roles; 
guid: f39c1e48-d9a9-443a-ba1e-6f345a350ab8
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?node-id=742:276
---

# How to leverage OutSystems roles with hierarchy levels

OutSystems Roles are very useful and easy to use. You can create authorization mechanisms in a matter of minutes with the out-of-the-box roles. 

When developing an application you must secure it, allowing or restricting end-user access to specific screens of your application. Roles are often used for:

* Authorization mechanisms at screen level: who accesses what screens

* Controlling displayed information: who sees what inside a screen

* Controlling available actions: who can update/insert/delete what

It's not uncommon for development teams to face business requirements to implement more sophisticated access control and complex authorization mechanisms. Frequently, those requirements translate into an authorization model organized as a hierarchy.

Consider a factory and its different roles: they're organized hierarchically:

![factory roles example](images/factory-roles-example.png)

The scenario above requires you, a developer, to implement a hierarchy of roles. OutSystems Roles, as you know them, don’t allow the creation of a similar structure with built-in capabilities. However, you can implement this hierarchical structure by extending the OutSystems Roles. In this set of articles, you are going to learn how to do so.

Disclaimer: To implement Hierarchical Roles, you need a custom implementation that depends on the use case; there is no ‘one size fits all’ solution. Depending on the use case, you can implement different solutions. In this set of articles, you are going to find a possible solution for a concrete use case.

To understand the advantages of creating hierarchical roles, go to [Hierarchical and static roles comparison](hierarchical-and-static-roles.md).