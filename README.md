#Rate 1 Day Stock Prediction Websites

Ever wonder how accurate different stock prediction websites are?  
Are certain websites better at predicting different stocks than others?
Different industries?
Do all the websites have similar predictions?
Which websites have been the most accurate overall this month?  Year?  Last 5 years?

This app scrapes daily stock prediction websites, stores the data, and allows you to view the statistics of a few chosen websites.

This application was written in Python (with a little SQLite3) using Model-View-Controller architectural pattern.  


### Setup:

In directory you'd like to run the program, first clone the depository:

`git clone https://github.com/himleyb85/prediction_rater`

Then, you need to set a cron job (Linux only, a daemon that runs in the background of your computer, no input neccessary) to regularly collect the information from the websites into your database.

`crontab -e` 

to open your crontab for editing, then add this line *with your actual filepath*:

`0 8 * * 1-6 <filepath to>/python3 <filepath to>/prediction_rater/dailyrun.py`

A few days after you've set your chron job, see the results so far in the user dashboard by running 

`python3 controller.py`

Enjoy!