---
tags: version-10; 
summary: 
guid: 42ccc03c-d5c3-47b9-a4cc-36c576058d42
locale: en-us
---

# How to find out if a string is contained in another string

How do I check if a certain text string contains another text string?  
Is there an equivalent to the C# String.Contains function?    

## Answer

To know if one text string is contained in another text string use the Text Built-in Function [**Index**](<https://success.outsystems.com/Documentation/10/Reference/Logic/Built-in_Functions/Text_Built-in_Functions#Index>).  
The **Index** Function returns an integer with the zero-base position of a `keyword` string inside another `text` string and returns `-1` if `keyword` is not found.

To get a Boolean Output similar to the C# String.Contains use the following Expression:

        Index(text,keyword) > -1

To make your search case insensitive set the `ignoreCase` parameter to `True`:

        Index(text,keyword,ignoreCase:True) > -1
