# CSC-32200-Software-Engineering
CSC-32200-Software-Engineering Spring 2020 @ The City College of New York 

Okay listen up team! Read these instructions very carefully:

# Development Enviornment Set up:
To clone this repository enter the following command: 

    $ git clone https://github.com/rehman000/CSC-32200-Software-Engineering/

Once the repository is created, you can navigate to the current working/project directory and 
in order to create a python virtual enviornment you may need to install it first, you can do so by entering the following command:

    $ pip3 install virtualenv

Now in order to create a Python Virtual Enviornment, enter the following command:

    $ virtualenv Virtual_Env_Folder_Name

The Convention is to name the directory as such:

    $ virtualenv env

Now that the Python Virtual Enviornment has been created you can activate it by entering the following command:

(For Unix/Linux Systems):

    $ source env/bin/activate

(For Windows Systems):

    $ \env\Scripts\activate.bat

You will know that the Python Virtual Enviornment is working correctly when you see (env) next to your bash $ directory name, as seen in the image below:

![Python_Virtual_Enviornment](/docs/Python_Virtual_Enviornment.jpg)

# Installing Dependencies: 

Now that we are in the Python Virtual Enviornment we can install all the necessary dependencies by entering the following command:

    $ pip3 install flask flask-sqlalchemy

Note that this is temporary if I end up installing more Python modules, I will place them all in a requirements.txt file and you could install all the dependencies inisde the virtual enviornment by entering the following command: 
(This has not yet happened, but it's good to be future proof)

    $ pip3 install -r requirements.txt
    
# Running the Application:

Now that we have everything set up properly to run the application enter the following command:

    $ python3 app.py

# Deployment: 

The test application has been deployed to Heroku:
    
    https://flask-tutorial-crud-app.herokuapp.com/
