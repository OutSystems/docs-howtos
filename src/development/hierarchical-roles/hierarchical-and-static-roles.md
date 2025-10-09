---
summary: Explore the comparison between hierarchical and default roles in OutSystems 11 (O11), highlighting advantages and implementation considerations.
tags: outsystems security, role-based access control, application security, web application development, outsystems best practices
guid: 7c2103e0-79cb-43a7-a430-92ca71e0f8f4
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Hierarchical and static roles comparison

This section shows a comparison between hierarchical roles and the default roles in OutSystems apps.

## Advantages of hierarchical roles

The following bullets show the advantages of defining hierarchical roles:

* Accommodates hierarchical authorization

* Accommodates potential explosion of application roles

* Allows runtime configuration of roles (for example, renaming, screen mapping)

## What you should take into consideration

Consider the following when defining hierarchical roles:

* Effective runtime configuration depends on implementation. Plan the delivery of incremental functionality instead of unnecessary blocks.
* Configuration overhead for setting up the security model to each scheme flow: plan for end-user training and assistance, or improved UX (for example, contextual help).
* Performance penalty due to database query on every screen access: load the user’s authorization model into session upon login. This may bring additional challenges to data structure mapping and size.
* Security risk due to manual inclusion of authorization checks: consider using authorization actions inside a web block present in the base layout.
* Lack of built-in product support: plan for extensive unit and component testing. Create the necessary support elements enumeration needs (static entities, actions, etc.).

To learn how to implement hierarchical roles, go to [How to implement hierarchical roles](hands-on.md).
