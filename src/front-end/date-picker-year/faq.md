# How to have a date picker with year selection

## Question

I want an input_calendar widget to enter a date of birth, which could easily be many years ago.

The standard input_calendar widget doesn't allow the direct selection of the year.

## Answer

Use the component [DatePicker](http://www.outsystems.com/forge/component/351/datepicker/) from the OutSystems Forge.

The component uses the jQuery plugin [DatePicker](http://jqueryui.com/datepicker/#dropdown-month-year), which has options to select the month and the year through drop down menus.

By default the year dropdown will contain the last 10 years as options to select. As you want to enter a date of birth, it is possible to extend the range of year options in the dropdown.

You must modify the plugin to add the options changeMonth, changeYear and yearRange as shown below:

![image alt text](images/How-to-have-a-date-picker-with-year-selection_0.png)

The widget should appear as follows:

![image alt text](images/How-to-have-a-date-picker-with-year-selection_1.png)
