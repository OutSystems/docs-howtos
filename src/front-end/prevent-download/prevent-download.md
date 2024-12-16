---
summary: Explore various methods to prevent content copying in OutSystems 11 (O11), including CSS and JavaScript techniques.
guid: c0bda1f0-88a2-4879-8c95-1eac2a7b3cdf
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: content protection, css, javascript, user experience, security
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# How do you prevent users from copying text or images?

You can use a variety of methods to prevent users from copying text or images. Let's take a look at them.

## Disable selection
Any content inside a container or other element with the “basic-protect” class is generally not selectable by users.

You accomplish this by adding CSS code in the **[Style Sheet Editor](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Cascading_Style_Sheets_(CSS))**.


	.basic-protect * {
	    /* Selection */
	    -webkit-touch-callout: none;
	    -webkit-user-select: none;
	    -khtml-user-select: none;
	    -moz-user-select: none;
	    -ms-user-select: none;
	    user-select: none;
	}

## Disable printing (with notification message)

Any content inside a container or other element with the “basic-protect” isn't displayed when printed and show a message instead.

You accomplished this by adding CSS code in the **[Style Sheet Editor](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Cascading_Style_Sheets_(CSS))**.


	@media print {
	    .basic-protect::before {
	        content: "Not available for printing. "
	    }
    
	    .basic-protect * {
	      display: none;
	  }
	}

## Disable right-click menu

Prevent access to cut/copy commands from the browser’s context menu.

You accomplished this by **[adding JavaScript code](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/JavaScript/Extend_Your_Web_Application_Using_JavaScript/Define_and_Run_JavaScript_Code)** in the property in question:


	/* Disable right-click menu on page */
	document.addEventListener('contextmenu', function(event) { 
	    event.preventDefault()
	});

## Disable print screen screenshots

Prevent the “print screen” button from taking a screenshot of the page when the page has focus. 

Caveat: This only works if the page is in focus AND the user isn’t using a special screenshot tool. In other words, this one is pretty weak. 

You accomplished this by **[adding JavaScript code](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/JavaScript/Extend_Your_Web_Application_Using_JavaScript/Define_and_Run_JavaScript_Code)** in the property in question:


	/* Disable print screen button */
	document.addEventListener("keyup", function (event) {
	    var keyCode = event.keyCode ? event.keyCode : event.which;
	    if (keyCode == 44) {
	        stopPrntScr();
	    }
	});

	function stopPrntScr() {
	    var inpFld = document.createElement("input");
	    inpFld.setAttribute("value", ".");
	    inpFld.setAttribute("width", "0");
	    inpFld.style.height = "0px";
	    inpFld.style.width = "0px";
	    inpFld.style.border = "0px";
	    document.body.appendChild(inpFld);
	    inpFld.select();
	    document.execCommand("copy");
	    inpFld.remove(inpFld);
	}
