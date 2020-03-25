# How to have multiline inputs in Editable Table

## Question

How can I accept new lines in Editable Table with a textarea (input with >= 2 lines)?

When I press "Enter", the row is automatically saved.

## Answer

Editable Table does not support inputs with new lines. However, you can use Javascript to work around the limitation.

1. Make sure the textarea input has the **Name** property set (e.g. **myTextArea**).

2. Right after this input, add an expression with property **Escape Content **set to** No**.

3. Change the expression's **Example** property to something more meaningful, such as "`<Script: Allow Enter>`".

4. In the Expression value, enter the following Javascript, replacing **myTextArea** with the name of your input:
```
<script language='javascript'>  
$('#" + myTextArea.Id + "').keyup(function <br>(e) { 
    if <br>(e.keyCode == 13) {
        var <br>ta = this;  
        var <br>caretPos = ta.selectionStart;   
        var <br>textAreaTxt = $('#'+this.id).val();   
        var <br>txtToAdd = '\n';  
        ta.selectionStart = caretPos + txtToAdd.length;   
        $('#'+this.id).val(textAreaTxt.substring(0, caretPos) + txtToAdd + textAreaTxt.substring(caretPos));
        ta.selectionStart = caretPos + txtToAdd.length;   
        ta.selectionEnd = caretPos + txtToAdd.length;   
        e.stopPropagation();  
    }   
})  
</script>"  
```
The script monitors the keys that the user presses in the input. If the script detects an "Enter", it inserts a newline, and stops the propagation of the event. Therefore, the Editable Table won't see the key press.

In the end, you should have something similar to the example below:

![image alt text](images/How-to-have-multiline-inputs-in-Editable-Table-0.png)

