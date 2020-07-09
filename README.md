# <center>CC_Redact_Iter3</center>

This is the third iteration of my CC_Redact website, a fresh attempt at my previous Fake Chuckee Cheese Neptune Credit Card Redactor App. 

The main purpose of this project is to accept the web site visitor's fake credit card number and redact it.

What distinguishes this iteration of this poject from previous iterations is that this time around I intend on using only a single template (the home page / landing page) to handle all the functionality. 

This project includes three core apps:
* <strong>redactors</strong>: This app accepts the user's 16 digit card number as input and then processes (redacts) it
* <strong>mortems</strong>: This app is kinda like a blog post, but in my production environment I only intend on invoking this app once to create a single blog post which will contain my 'postmortem' to (document everything I learned while writing this Django site)
* <strong>counters</strong>: This app will eventually count all the words used in the postmortem and present the data to the user. But for now it just counts the most common words in Alice and Wonderland - - which was a project that I have worked on for a previous Python shell script that I wrote in 2019

After the above features are implemeneted, later I plan on adding these three minor additional features:
* A page view hit counter
* Show current time and date at bottom of landing webpage
* Public domain copyright note with dynamic year value
