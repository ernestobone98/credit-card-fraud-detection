# Credit card fraud detection

With this project, we are trying to implement software to detect everyday common credit card fraud. 

There is also a GUI part:
    - when launching the project : there is an animation
    - once the animation is finished, a first interface is displayed on your screen in order to give access to the expert accounts and to the boss' one
        * for experts there are 2 accounts:
            - Marco's one with the identifier gm801217
            - Ernesto's one with the identifier be816425
        * for the boss:
            - Benjamin's one with the identifier bb809906

Passwords change at each execution.

**DEBUGGING** The goal is to improve customer security. For this, we will implement machine learning algorithms.

## How does it work:

#---- Fraud detection ----#

We've worked with an imbalanced dataset from kaggle (we all know that frauds are not common, so that's why)
To manage this problem we've implemented the Over-Sampling technique, specifically, the Random Over Sampler method from sklearn.

With the data already balanced we've used a Random Forest to classify and get information from data
we got a f1-score precision of 96% .

Same with a Neural Network, but this time with a worst f1-score precision of 91%.

DEBUGGING --> The goal in a near future is to merge both solutions to get a better one.

#---- For GUI ----#

Experts on their GUI can:
    - Send a message to the boss
    - Generate report and prevent victims
    - View data
The boss can:
    - Open messages
    - Open reports
    - Write down information using the 'To do list'
    - See the evolution of 5 cryptocurrencies in real time
    - Easily access to a calendar (to see today's date and help planning)


### Run projet:
We advise you if you are on Ubuntu to download Xlunch, then type:
    *python3 -m venv env* (to create a virtual environment. If you don't have the venv module installed just install it with pip)
    *source env/bin/activate*
    *export DISPLAY=:0*
this will link the display to the app.

Make sure to install all the librairies needed in your virtual environment:
    *pip install -r controllers/requirements.txt*

Once done, you can simply run the project using:
    **python3 main.py**

Your terminal will display passwords to log in wherever you want. Note that:
    - if you want one of the two expert accounts you have to choose between gm801217 and be816425
    - if you want the boss account then bb809906

For latex to compile, you must install (if you haven't already) the following packages:
- texlive
- texlive-lang-french
- texlive-latex-extra

If you have a problem watch the requirements.txt or see the error message which (must be an ImportError)

##### Matches and aliases

Here is a list of different usernames for each group member:
- Benjamin Bernaud = benj-b / bbernaud
- Ernesto Bone Bravo = ernestobone98
(the others seem unchanged)

Also, when whe programmed together we put the initials of each name on the commit description (ex : BBG = Bernaud / Bone / Gazzera)
