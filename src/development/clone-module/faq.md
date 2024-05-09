---
summary: Explore how to clone and relocate a module between applications using OutSystems 11 (O11) in Service Studio.
guid: 27e7e1ed-437a-46ba-941d-a31ec6f0c5ac
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/ZqxffTIAhYyQg8Q2KbSFbb/Development?node-id=1747:45
---

# How to Clone a Module into Another Application

## Question

How do I clone a module into another application in Service Studio?

## Clone the module

1. Open the module you wish to clone in Service Studio

1. Click the 'Module' menu at the top of your screen and click 'Clone':

    ![Dropdown menu in Service Studio with 'Clone' option highlighted.](images/clone-module-menu-clone.png "Service Studio Module Menu")

A clone of the module has now been created.

![Confirmation dialogue box indicating the module was successfully cloned.](images/clone-module-confirmation-dialogue.png "Module Cloned Confirmation Dialogue")
    
Press the 1-Click Publish button to publish it to your environment:

![The '1-Click Publish' button in Service Studio.](images/clone-module-publish-button.png "1-Click Publish Button")

The published module will reside in the 'Independent Modules' Application.

## Move the module to new application

1. Open the 'Independent Modules' Application in Service Studio:

    ![Independent Modules application icon in Service Studio.](images/clone-module-independent_modules.png "Independent Modules Application")

1. Press the arrow button on the right of the cloned module:

    ![List of modules in the Independent Modules application with an arrow button.](images/clone-module-independent_modules_list.png "List of Independent Modules")
    
1. Select the application you would like to move the cloned module to and press the 'Move' button:

    ![Dialogue box for moving a cloned module to another application.](images/clone-module-move-dialogue.png "Move Module Dialogue")

You have now successfully cloned a module from one application to another.

![Destination Application showing the moved module within its development environment.](images/clone-module-move-complete.png "Module Moved to Destination Application")
