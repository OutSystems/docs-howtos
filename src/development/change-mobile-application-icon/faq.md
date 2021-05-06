---
summary: Steps to change mobile application icon by environment
tags: 

---

# Title 

How to change a mobile application icon by environment

## Issue

Having a mobile application with different icons in all environments to able to know which one to test


## Resolution

1. Create a zip with your icons, this one for demonstration purposes is called "Resources.zip" but you can name however you desire.
    
    ![Resource with all the icons](images/zipimage.png)

1. Add the zip file to the Mobile App module
    
    ![Add zip to resources](images/Resources.png)

1. Add the JSON as shown in the image below, with the format as per the specification in the documentation presented in the top of this communication.
    
    ![Write extensability configurations](images/extensabilityconfigurations.png)

1. Publish and generate app
    
    Once you install the app it will show in the device with the icon you chose.

    For version 10 of the OutSystems Platform, the code either needs to be deployed and the JSON changed to QA icons or repeat the whole process directly in QA environment.

    In version 11 of the Platform, you only need to add the resources zip to the module. After having the file in both environments you can change the extensibility configurations through LifeTime in the application settings.

    ![Apply advanced configurations](images/applysettings.png)

    In both versions of the platform, after changing these configurations, a new build needs to be generated to display the icons correctly.

    Hope this helps your developments. If you have any further questions don't hesitate to contact us.

    If you run into any issues while doing this configuration, please, contact me by email directly and we can schedule a session to go over the process.
