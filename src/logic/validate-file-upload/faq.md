---
tags: file upload validation, custom validation logic, user experience enhancement, error handling
summary: Explore custom file validation techniques for the Upload Widget in OutSystems 11 (O11) to enhance web app functionality.
guid: 33e8fc48-2034-4ae4-844e-d6d0fdaaeb55
locale: en-us
app_type: traditional web apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/3YpPKdo5QwN0z6up61eKe5/Logic?node-id=842:251
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
content-type:
  - procedure
---

# How to validate file input on a File Upload Widget in a Web App

The Upload Widget enables your users to browse and select a file that they want to upload into an app.

This widget doesn't include built-in validations  such as if a file uploaded or if the size or type of file is valid. Therefore, to have validation, you can create a custom validation.

Adding validation properties helps solve simple issues, such as an empty file. This helps to make your apps more user-friendly.

The following example, shows a snippet of three different custom validations. This snippet uses the runtime properties of the Upload Widget, named **UploadFile**.

![Flowchart showing three custom validation scenarios for a file upload widget: checking if a file is selected, if the file is empty, and if the file is a PDF.](images/file-up-00.png "Custom Validation Logic for File Upload")

* **Row 1**: Use to verify the end user chose a file in the **Upload widget** before submitting.
    * Add an **If** with the Condition set to `UploadFile.Filename = ""`
    * Make the True Branch show an error message and end the Action.
* **Row 2**: Use to verify that the end user didn't select an empty file to upload.
    * Add an **If** with the Condition set to `UploadFile.Content = NullBinary()`
    * Make the True Branch show an error message and end the Action.
* **Row 3** Use to verify the end user selected a valid file type (PDF in this example).
    * Add an **If** with the Condition set to `UploadFile.Type = "application/pdf"`
    * Make the False Branch show an error message and end the Action.
  