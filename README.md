Template for a small Website with Flask, Bootstrap and NGINX
=========
Welcome!
------------

This template provides you with a flask environment that serves three main routes: yourdomain.com,
yourdomain.com/imprint and yourdomain.com/privacy_policy. Further, flask-mail is integrated and you'll 
need to configure it with you mail provider in order to use it - the route is here yourdomain.com/send. 


## Table of Contents
1. [Overview]() 
2. [How to setup development]()
3. [How to start app locally]()
4. [How to deploy to ubuntu]()

## Overview

The python application structure is seperated in the root folder where you'll find the following files/folders:
* _.env_ - File for environment variables such as secret key, your mail provider username and password
* _app.ini_ - Init file to start the application with the application server UWSGI (only for deployment)
* _requirements.txt_ - All packages to setup your development environment to use this repo
* _nginx_ - Configuration files for web server to achieve SSL-encryption once deployed
* _app_ - Here the actual application lives

The app folder holds all the python logic and the necessary assets. The main logic is located in the
_view.py_ file; the routes / , /imprint , /privacy_policy and /send are here defined. In _controller.py_ you'll 
find the helper functions for sending mails. In the _templates_ folder all HTML files are stored, which will 
be served through view.py. You want to make your actual website? You'll have to look here. 
All other website assets such as CSS, JavaScript libraries and images can be placed under the _static_ folder.


## How to setup development

First, you create virtualenvironment so that all python dependencies for this repository are in their own environment.
Open a location on your harddrive where you would like to store the virtualenvironment. 
In the best case: A folder where you always will store virtualenvironment.

    $ python -m venv YOURENVIRONMENT
    
Now you have created a virtualenvironment in your current location. You'll need to activate it by:
    
    # For Linux:
    $ source /YOURENVIRONMENT/bin/activate
    
    # For Windows CMD line:
    $ cd YOURENVIRONMENT
    $ cd Scripts
    $ activate.bat

The next step is to go to clone this repository. 

After you have done that, you'll go with terminal to the folder where requirements.txt is located. 
Watch out that you have activated the virtualenvironment! 
Once you reached that location, you do:

    YOURENVIRONMENT$ pip install -r requirements.tx
    
Congrats! You have the virtualenvironment created and are setup to build your own website with this repository!

## How to start app locally

For starting the app, you'll need to load the environment variables.

    # For Linux:
    $ source /.env
    
    # For Windows CMD line:
    $ set FLASK_ENV="development"
    $ set FLASK_APP="app"
    $ set FLASK_DEBUG="1"
    $ set SECRET_KEY="SOMESECRETKEY"
    $ set MAIL_PASSWORD="YOURPASSWORD"
    $ set MAIL_USERNAME="YOURMAIL"

And now, finally, you can start the application by:
    
    YOURENVIRONMENT$ python run.py
    
Again, watch out that you are in the local folder of this repository!


If no error occurs, you can open 127.0.0.1:5000 in your browser and will see the template running.


## How to deploy to ubuntu

TBD