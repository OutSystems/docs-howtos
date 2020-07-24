---
tags: version-10; favicon;
summary: 
---

# How to set a favicon tag

A big thanks to Jorge Almeida, a community member, for contributing to this how-to.

In OutSystems, by default, the OutSystems logo is the favicon that is displayed for Web Applications. How do I change and set a custom favicon for my Web Application?

## Answer

If your Web Application **uses a SILK UI Template** go to the Resources folder inside the Data Tab, right click `favicon.ico`, click Replace Resource... and select your custom favicon. Don't forget to republish your application.

![Change Resource](images/silk-01.png)

If your Web Application **does not use a SILK UI Template** follow these steps to use a custom favicon:

1. Add the **AddFaviconTag** action from the **HTTPRequestHandler** extension, as a dependency of your application. 

    ![Manage Dependencies](images/no-silk-00.png)

1. Go to the Interface Tab, right click the Images folder, click Import Image... and select your custom favicon.

    ![Import Images](images/no-silk-01.png)

    <div class="info" markdown="1">

    If you are using .ico images they will not be listed in the Import Image... window. As a workaround navigate to where your image is placed, manually input/paste the file name (for example `favicon.ico`) in the File name field and press Open.

    </div>

1. To use the same favicon across all the screens of your application include the **AddFaviconTag** action inside the Preparation of the Menu Web Block. Set the `IconFilename` to `"/<menu_module>/img/<your_favicon>.<file_type>"`. 

    ![](images/no-silk-03.png)

    Where `<menu_module>` is the Module where the Menu Web Block is contained, `<your_favicon>.<file_type>` is the custom favicon filename and extension. In this case since the Menu Module is `Test`and the custom favicon is named `customfavicon.png`the `IconFilename`is `"/Test/img/customfavicon.png"`

    Calling the **AddFaviconTag** action inside the Preparation of the Menu Web Block will change the favicon in all the Web Screens where the Menu Web Block is used. If you only want to use the custom favicon in certain screens call the **AddFaviconTag** action only inside the Preparation of those screens.

After these steps your Web Application should have a new favicon.

![](images/no-silk-04.png)
