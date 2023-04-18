---
tags: version-10; email; timestamp;
summary: 
guid: 7ec5da67-8fb3-4c37-b20f-e8759abea401
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to find when the last email was sent

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

How can I get the timestamp of the last sent email?

## Answer

To check the timestamp of sent emails at runtime in your Application reference the **Systems** Entities **Sent\_Email** and **Email\_Status** and use the **Sent** Date Time Attribute from the **Email\_Status** Entity. 

![](images/email-sent-00.png)

You can also check the timestamp of sent emails in Service Center in the **Email Log** screen of the **Monitoring** Tab.
