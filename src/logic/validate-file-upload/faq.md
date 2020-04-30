---
tags: version-11; deployment; upload; runtime-traditionalweb
summary: 
---

# How to validate file input on a File Upload Widget in a Traditional Web App

* How do I verify if the end user chose a file in the  **Upload Widget** before submitting?
* How do I verify if the file the end user chose is empty?
* How do I validate the file type?

## Answer

Unlike other Widgets, in Traditional Web Apps the File Upload Widget doesn't have `Valid` or `Validation Message` properties. You have to create your own custom validation.

The following screenshot includes a simple snippet of three different custom validations using the runtime properties of the Upload Widget (named **UploadFile** in this case):

![](images/file-up-00.png)

1. Check if the end user did not select a file to upload
:  Add an If with the Condition set to `UploadFile.Filename = ""` and make the True Branch show an error message and end the Action.

2. Check if the end user did not select an empty file to upload
:  Add an If with the Condition set to `UploadFile.Content = NullBinary()` and make the True Branch show an error message and end the Action.

3. Check if the end user selected a valid file type (PDF in this case)
:  Add an If with the Condition set to `UploadFile.Type = "application/pdf"` and make the False Branch show an error message and end the Action.
