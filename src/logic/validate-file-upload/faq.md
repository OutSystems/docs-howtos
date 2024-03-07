---
tags: version-11; deployment; upload; runtime-traditionalweb
summary: Create custom validations for the upload widget
guid: 33e8fc48-2034-4ae4-844e-d6d0fdaaeb55
locale: en-us
app_type: Web apps
platform-version: o11
figma: https://www.figma.com/file/3YpPKdo5QwN0z6up61eKe5/Logic?node-id=842:251
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
  