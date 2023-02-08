---
tags: saving_changes; javascript;
summary: Preventing users from losing unsaved changes
guid: 0a798086-ce2a-40f6-b476-7ba81c974b6d
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---


# How can you prevent users from losing unsaved changes?

When you want to prevent the loss of unsaved changes in a Reactive Web application, you need to add some additional logic and JavaScript. 

To do it, you need to track whether the user has modified in the data and prevents the page from navigating. To do it:

1. Add a new local variable to store whether the data in the form is modified.

1. Add a checkbox to the form tied to the above variable and hide it with CSS

1. In the screen’s initialize event, add the following JS to handle click, close, and navigate events. 
    
    You’ll need to pass the form ID and the checkbox ID to the JavaScript as parameters. 

    	var confirmationMessage = "You have unsaved changes. Are you sure you want to leave?";

    	var isModified = function () {
	        return document.getElementById($parameters.FormIsModifiedId).checked;
    	}

	    // Handle normal button and link clicks on the page
	    document.body.addEventListener(
	      "click",
	        function(event){
	         if (event.target.tagName === "BUTTON" || event.target.tagName === "A") {
	            var associatedWithForm = event.target.form
	            var isInProtectedForm = associatedWithForm && event.target.form.id === 	$parameters.FormId
	            if(!isInProtectedForm && isModified()) {
	                if(!confirm(confirmationMessage)) {
	                    event.stopPropagation();
	                    event.preventDefault()
	                    return false;
	                 }
	              }
	            }
	      }   
	    )

	    // Catch navigating back
	    window.onpopstate = function(event) {
	      if(isModified()) {
	            if(!confirm(confirmationMessage)) {
	              history.pushState(null, document.title, location.href);
	            }
	        }
	    }   
	
	    function confirmExit (event) {
	       if(isModified()) {
	           (event || window.event).returnValue = confirmationMessage; //Gecko + IE
	           return confirmationMessage; //Gecko + Webkit, Safari, Chrome etc.
	        }
	    }
	
	    // Catch window close
	    window.onbeforeunload = confirmExit;


