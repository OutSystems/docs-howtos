---
summary: Learn how you can customize dialog messages in Reactive Web Apps.
tags:
guid: 34f82c63-eff4-49e6-82fb-0958e13dddf7
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to create animated and styled dialog messages

<div class="info" markdown="1">

This article was written by [Rúben Bonito](https://www.outsystems.com/profile/87379/), OutSystems MVP.

</div>

This article shows how to implement animated and styled dialog messages on **OutSystems Reactive Web Apps**.

To do it:

1. Upload the 2 JavaScript libraries ([promisepolyfill](https://www.jsdelivr.com/package/npm/promise-polyfill) and [sweetalert2_min](https://www.jsdelivr.com/package/npm/sweetalert2)) into your OutSystems application, by clicking the Scripts folder, with the opposite button and select Import Script.

    ![](images/create-styled-dialogs_0.png)

    ![](images/create-styled-dialogs_1.png)

1. Create a Block by dragging it to the editor area:

    ![](images/create-styled-dialogs_2.png)

1. Inside the block, go to the advanced properties of the block and paste the style sheet, provided by the same source as the libraries:

    ![](images/create-styled-dialogs_3.png)

1. On the event "On Render" associate a client action to execute the following JavaScript code:

        var latetoast = sessionStorage.getItem("latetoast");

        if (latetoast === "True") {
            sessionStorage.setItem("latetoast", "False");
            //
            swal({
                title: sessionStorage.getItem("IN_title"),
                text: sessionStorage.getItem("IN-text"),
                allowOutsideClick: false,
                allowEscapeKey: false,
                allowEnterKey: false;
                showConfirmButton: false,
                showCancelButton: false,
                timer: sessionStorage.getItem("IN_timeout"),
                toast: true,
                type:sessionStorage.getItem("IN_type"),
                Position: 'center'
            });
        }    

1. Drag the block to your application's layout header.

    <div class="info" markdown="1">

    To make this how-to shorter, it only describes the implementation for the most complex type of dialog messages, the confirmation dialog message. All the other types have a very similar or easier implementation process.

    </div>

1. Create a client action with all the inputs visible in the following picture:

    ![](images/create-styled-dialogs_4.png)

1. Inside the action flow, add a JS node and execute a JavaScript with the following code:

        swal({
            type: $parameters.IN_type,
            title: $parameters.IN_title,
            text: $parameters.IN_text,

            showCancelButton: true,
            reverseButtons: false,
            cancelButtonColor: '#d33',
            cancelButtonText: $parameters.IN_cancelTxt,
            cancelButtonClass: $parameters.IN_cancelClass,
            confirmButtonClass: $parameters.IN_confirmClass,
            confirmButtonColor: '#3085d6',
            confirmButtonText: $parameters.IN_confirmTxt,
            buttonsStyling: false,
        }).then(function (result) {
            if (result.value) {
                document.getElementById($parameters.IN_InputId,).value = "True";
            } else {
                document.getElementById($parameters.IN_InputId,).value = "False";
            }
            document.getElementById($parameters.IN_InputId,).change();
        });

1. Create a button in your screen that when clicked by the user executes a screen action.

    This screen action has the Confirmation Dialog client action (created on Step 6) which require that you fill in the following inputs:

    ![](images/create-styled-dialogs_5.png)

Finally, publish your application and the result, when you click on the confirmation button, is:

![](images/create-styled-dialogs_6.png)

<div class="info" markdown="1">

This implementation is [available as a reusable component in the Forge](https://www.outsystems.com/forge/component-overview/8395/animated-styled-dialogs-alerts).

</div>
