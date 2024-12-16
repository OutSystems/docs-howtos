---
tags: email logging, entity relationships, runtime monitoring, technical support, service center
summary: OutSystems 11 (O11) allows users to find the timestamp of the last sent email by referencing the Sent_Email and Email_Status entities.
guid: 7ec5da67-8fb3-4c37-b20f-e8759abea401
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/3YpPKdo5QwN0z6up61eKe5/Logic?node-id=147:325
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - apply
---

# How to find when the last email was sent

How can I get the timestamp of the last sent email?

## Answer

To check the timestamp of sent emails at runtime in your Application reference the **Systems** Entities **Sent\_Email** and **Email\_Status** and use the **Sent** Date Time Attribute from the **Email\_Status** Entity. 

![Diagram showing the relationship between Email_Content, Email_Definition, Sent_Email, and Email_Status entities in the system database.](images/email-sent-00.png "Email Entities Relationship Diagram")

You can also check the timestamp of sent emails in Service Center in the **Email Log** screen of the **Monitoring** Tab.