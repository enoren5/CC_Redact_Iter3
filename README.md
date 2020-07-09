# CC_Redact_Iter3
This is the third iteration of my CC_Redact website, a fresh attempt at my previous Fake Chuckee Cheese Neptune Credit Card Redactor App. This time around I intend on using ultimately only a single template (the home/landing page) to handle all the functionality. 

This project includes four apps:
* redactors: This app accepts the user's 16 digit card number as input and then processes (redacts) it
* mortems: This app is kinda like for a blog post, but in my production environment I only intend on invoking this app once to create a single blog post which will contain my 'postmortem' (documenting everything I learned while writing this Django site)
* counters: This app counts all the words used in the postmortem and presents the data to the user (which includes some advanced features (very basic and rudimentary data analysis) that I have worked on for a previous CLI Python script I wrote earlier in 2019)

I plan on adding these three features laster:
* A page view hit counter
* Show current time and date at bottom of landing webpage
* Public domain copyright note with dynamic year value
