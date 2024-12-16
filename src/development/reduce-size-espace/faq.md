---
summary: Discover methods to minimize module size in OutSystems 11 (O11) by optimizing architecture, image sizes, resources, and icon usage.
guid: ca1ebd84-459e-4a57-875c-ec6bbf2a3cda
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: application optimization, application architecture, image optimization, resource management, icon management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - architecture dashboard
coverage-type:
  - apply
---

# How to reduce the size of my modules

## Question

Why is my module so large?

## Answer

Our experience tells us that whenever a module has a large size, one of four things is usually involved:

* You use a **single module approach** which is against the recommended architecture. Check [OutSystems architecture canvas](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_the_Architecture_of_Your_OutSystems_Applications/The_Architecture_Canvas) to help you promote the correct abstraction of reusable services and the correct isolation of distinct functional modules.

* You have **large images**. Sometimes people include MB large jpg or png files with high resolution even if then they are re-sizing the images to smaller sizes in screens. This can also have a large impact when running the application because the browsers will fetch the entire image thus using more bandwidth. Check  
[Control image size](https://success.outsystems.com/Documentation/Architecture_Dashboard/Code_Patterns/Best_practices/Control_image_size) for more tips regarding this topic.

* You have **large resources**. Sometimes when using the Excel bootstrap approach people include it in the module by dragging and dropping the Excel to have everything together. Our recommendation in these cases is to change the bootstrap action to receive the binary instead of going to the resources and have a screen with a file upload field that calls the bootstrap action with the uploaded file.

* You have **numerous custom icons** for Actions and Integrations. The usage of high-resolution icons, or even many small-sized icons, may increase the module size. In this case, we recommend switching to the default icon.

While the first one is slightly harder to correct because it involves re-factoring of the code, the latest three are quite easy to spot and fix and will prevent such errors.
