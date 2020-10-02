# CC_Redact_Iter3

This is the third iteration of my CC_Redact website, a fresh attempt at my previous Fake Chuck E Cheese Neptune Membership Card Redactor App. 

The main purpose of this project is to accept the web site visitor's fake membership card number and redact it.

What distinguishes this iteration of this poject from previous iterations is that this time around I intend on using only a single template (the home page / landing page) to present all the functionality, rather than distribute each feature in their separate disparate templates. 

## BUILD INSTRUCTIONS

For *nix:
```
$ virtualenv --python=python3.8 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```
To get your test server running, you'll also need to create superuser and login to the Admin Dashboard and create a blog post by entering Lorem Ipsum placeholder content. Be sure to upload a small .jpg for the blog post in the Admin Dashboard. You also may need to create a superuser.  Then migrate and make migrations.

Those instructions are for Linux. I believe macOS is similar. No idea for Windows.

## CURRENT FEATURE LIST

This project includes four core apps:
* <strong>redactors</strong>: This app accepts the user's 12 digit card number as input and then processes (redacts) it.
* <strong>blogs</strong>: This app enables the author of the website to share blog  post. In the production environment I intend on invoking this app only once to create a single blog post which will contain my 'post-mortem' which I will use to document everything I learned while writing this Django site.
* <strong>wordcounters</strong>: This app counts all the words used in a blog post and presents top 10 most frequently used words (and filters out common words such as 'the', 'this', 'you', 'me'). It also counts and ranks the most common words in a text file of the public domain work Alice and Wonderland and even the Holy Bible.
* <strong>converters</strong>: This app is a basic HTML input form which enables web visitors to convert miles to kilometers and kilometers to miles.

## TO DO

After the above features are implemeneted, later I plan on adding these four minor additional features:
* When the usr clicks the 'Redact' button, the results 'gently' animate into existence.  I believe this can be achieved using AJAX. This will take some future reasarch on my part.
* ~~A page view hit counter~~ **IMPLEMENTED** 2 October 2020
* ~~Show current time and date at bottom of landing webpage~~ **IMPLEMENTED** 2 October 2020
* ~~Public domain copyright note with dynamic year value~~ **IMPLEMENTED** 2 October 2020
* ~~Refactor *posts* app to *blogs*~~ **IMPLEMENTED** 2 October 2020
* Stylize table
* Stylize basic header + basic footer using Bootstrap?
* ~~Stylize redactors box to match previous iteration of this project, including:~~ **IMPLEMENTED** 2 October 2020
    - ~~white text glow~~
    - ~~sleek dark gray bg color~~
    - ~~slight skeumorphic green button~~
    - ~~beveled edges for input boxes~~
    - ~~re-implement basic, subtle CSS animation~~
* ~~For redactors input form, reformat numeric requirements into bullet list, and perhaps be more specific with more explicit instructions about what is acceptable input~~ **IMPLEMENTED** 2 October 2020
* Start working on using "[Crayon Syntax Highlighter](https://github.com/aramk/crayon-syntax-highlighter )" to prepare for writing my post mortem