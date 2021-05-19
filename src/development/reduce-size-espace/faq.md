# How to reduce the size of my eSpace

## Question

Why is my eSpace so large?

## Answer

Our experience tells us that whenever a module has a large size, one of four things is usually involved:

* You use a **single module approach** which is against the 4 Layer recommend architecture.

* You have **large images**. Sometimes people include MB large jpg or png files with high resolution even if then they are re-sizing the images to smaller sizes in screens. This can also have a large impact when running the application because the browsers will fetch the entire image thus using more bandwidth.

* You have **large resources**. Sometimes when using the Excel bootstrap approach people include it in the module by dragging and dropping the Excel to have everything together. Our recommendation in these cases is to change the bootstrap action to receive the binary instead of going to the resources and have a screen with a file upload field that calls the bootstrap action with the uploaded file.

* You have **numerous custom icons** for Actions and Integrations. The usage of high-resolution icons, or even many small-sized icons, may increase the module size. In this case, we recommend switching to the default icon.

While the first one is slightly harder to correct because it involves re-factoring of the code, the latest three are quite easy to spot and fix and will prevent such errors.

