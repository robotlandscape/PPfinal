Acceptance Testing
==================

## Spell Check
No change needed 

## Capitalization Check
No change needed 

## Punctuation Check (parentheses, quotes, etc.)
Cleared punctuation in a comment but otherwise good

## Spacing and Indentation Check
Made the main menu a bit nicer

Usability Testing
=================

## User Input Check (i.e. running your program using a variety of user input responses)
Output was as expected, it brought the user back and asked them to try again. Doing control-c could be nicer, because at the moment it just throws an error, but it exits the program fine. 

## Peer Review (i.e. receiving feedback from another person)
My dad suggested that I wrote a way to dynamically find the number of lines in the file instead of just using the "58" that I had. 

Post Mortem Review Questions
============================

## What was the purpose of your program?
The purpose of the program was to sort a dataset of real-life information in a useful way to advise decisions on which countries an organization can make the greatest impact in. 

## How could your program be useful in the real world?
My program could definitely be useful in the real world, not just in the other two scenarios. Any time there is data that needs to be sorted, or organized in a relevant manner (like a search engine!), these same methods are used in the same manner.

## What is a problem you ran into, and how did you fix it?
I could not figure out some of the variable type translations initially. I could transfer the data from CSV to a json-like format, similar to Python dictionaries. Unfortunately, it also converted integers to strings. I had to write an additional function which reversed this. 

## Describe one thing you would do differently the next time you write a program.
I switched to using VS Code near the end of the project and actually enjoyed it quite a bit. Is love to experiment with that further in the future.

## How could your program be generalized and useful in other areas?
Besides the other two scenarios, this could be generalized to any other situation which data needs to be analyzed to make informed decisions. 

Security Measure
================

## Authentication
If the data are sensitive, like if the program is generalized for, say, job interviews, then asking the user for a username and password before continuing would be important. 

## Digital Signature
Digital Signatures in this program could be employed to verify the authenticity of data collected, to make sure that it comes from the source that it does. 

## Encryption
If authentication is used, then credentials should be encrypted so that the only people that have access are the users who are intended to have access, even if the database itself leaks