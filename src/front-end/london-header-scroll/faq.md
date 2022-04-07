---
tags: version-10; css; header; london
summary: 
guid: b80fd8bd-01dd-475a-9fd1-50709e60ab86
locale: en-us
---

# How to make the header scroll with the page in the London theme

In the London theme, the header is fixed at the top of the page. How can I make the header scroll with the page?

## Answer

The London CSS style sheet defines the header style as follows:

    .Header {
        background-color: #393939;   
        color: #D1D1D1;
        position: fixed;
        top: 0;
        width: 100%;
        z-index: 10;
        box-shadow: 0px 1px 3px #111;
    }

In lines 4 and 5, the CSS properties `position` and `top` fix the header area in the top of the screen.

To change the behavior of the header in Web Applications using the London Theme add the following CSS snippet to your Application's style sheet:

    .Header {
        position: static;
    }
    .Content {
        padding-top: 0;
    }

This CSS snippet resets the property `position` and removes the top padding for the content area (which was used to compensate for the fixed header). 