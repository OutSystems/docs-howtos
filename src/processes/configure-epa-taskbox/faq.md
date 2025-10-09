---
summary: Learn how to configure EPA Taskbox preferences in OutSystems 11 (O11) to control its visibility across different eSpaces.
guid: 32e83f65-befb-46b4-9984-d804192357a3
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/qdZmVuCDqCHvhakBTOLZcI/Processes?node-id=1042:233
tags: configuration, administration, security, user interface customization, outsystems platforms
audience:
  - platform administrators
  - full stack developers
  - frontend developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - apply
---

# How to configure EPA taskbox preferences

By default, EPA Taskbox is displayed in all screens in all applications. It is however possible to have EPA not show up in particular eSpaces by using the administration backoffice.

You can configure EPA Taskbox preferences on your server by going to `http://<server url>/EPA_Taskbox/`. There, you'll find the EPA administration web screen where you can activate the EPA administration:

![Screenshot of the EPA Taskbox activation screen with a button to activate EPA Administration.](images/How-to-configure-EPA-taskbox-preferences_0.png "EPA Taskbox Activation Screen")

After activating the EPA Administration, you'll have a configuration page where you can set the applications where you want to have EPA taskbox to be shown:

![Screenshot showing the EPA Administration configuration screen with options to hide or show EPA on selected eSpaces.](images/How-to-configure-EPA-taskbox-preferences_1.png "EPA Administration Configuration Screen")

![Screenshot displaying a success notification indicating EPA was activated for the selected eSpaces/tenants.](images/How-to-configure-EPA-taskbox-preferences_2.png "EPA Administration Success Notification")
