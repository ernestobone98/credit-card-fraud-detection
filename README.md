# Credit card fraud detection

With this project, we are trying to implement software to detect everyday common credit card fraud. 

There is also a GUI part:
    - when launching the project: there is an animation
    - once the animation is finished, a first interface is displayed on your screen in order to give access to the expert accounts and that of the boss
        * for experts there are therefore 2 accounts:
            - that of Marco with the identifier gm801217
            - that of Ernesto with the identifier be816425
        * for the boss:
            - that of Benjamin with the identifier bb809906
Passwords change with each execution.

**DEBUGGING** The goal is to improve customer security. For this, we will implement machine learning algorithms such as:
Over/under sampling;

## How it works:

#---- Dection fraud ----#
TO DO 

#---- For GUI ----#
Experts on their GUI can:
    - Send a message to the boss
    - Generate report
    - View data
The boss can:
    - Open messages
    - Open reports
    - Write down information using the To do list
    - See the curve of 5 cryptocurrencies in real time
    - Easy access to see today's date and help plan


### Run projet:
We advise you if you are on Ubuntu to download Xlunch, once that type:
    source env/bin/activate
    export DISPLAY=:0

You are therefore connected to the env of the project.

Once that run the project using:
    (on Ubuntu): python3 views/login.py
    (on Windows): python3 views\login.py

Link you guide in your terminal will display the passwords to connect where you want. Note that:
    - if you want one of the two expert accounts you have to choose gm801217 or be816425
    - if you want the boss account bb809906

For latex to compile, you must install (if you haven't already) the following packages:
- texlive
- texlive-lang-french
- texlive-latex-extra

If you have a problem watch the requirement.txt or see the error message which must be a ImportError

##### Matches and aliases

Here is a list of different usernames for each group member:
- Benjamin Bernaud = benj-b / bbernaud
- Ernesto Bone Bravo = ernestobone98
(the others seem unchanged)

Also, when whe programmed together we put the initials of each name on the commit description (ex : BBG = Bernaud / Bone / Gazzera)
