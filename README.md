# Improved-UNCGenie
A web app improving some of the features for registration. CSC-490 Project

## Setting up Enviroment
### Windows
To set up the enviroment for the website we need: Python with Flask (backend), Nodejs with React (frontend), PostgreSQL (database server), and dbeaver. Do a git pull or git pull origin main to get the up to date github repository. Skip each one you have installed.

#### I. Installing Nodejs with React
    1. Go here: https://nodejs.org/en/download and install the windows .msi 64-bit installer, then run it.

    2. Go through installer, leaving all the defaults.

    3. Run Command prompt as administrator (cmd in start search bar, right click and run as administrator)

    4. Enter:    Node --version
       It should return Nodejs version if installed  

    5. If installed, go to the front-end folder in the ImprovedUNCGenie folder and enter:    npm install

    6. The react app can be started with (in front-end folder) :   npm start

#### II. Installing Python with Flask
    1. Go here: https://www.python.org/downloads/windows/ and install Python 3.11.8 64-bit under stable releases, run it.

    2. During Installer, check Add python.exe to PATH, then install.

    3. Run Command Prompt as administrator

    4. Enter:   py -0      
       It should return python version if installed

    5. If installed, go to the backend folder in the ImprovedUNCGenie folder and enter:    pip install virtualenv
       This installs virtual enviroment package

    6. Create a virtual enviroment with:     py -m venv venv/
       This creates a virtual enviroment for the flask app (without virtual enviroment the modules would be installed in the python folder)

    7. Activate the virtual enviroment with:    .\venv\Scripts\activate.bat
       You should see (venv) next to the prompt showing you have activated the virtual enviroment

    8. Install the packages needed for the flask app with requirements.txt:    pip install -r requirements.txt

    9. The flask app can be started with (in backend folder with venv active):    py app.py
       If py command doesn't work try replacing it with python or python3

#### III. Installing Postgres
    1. Go here: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads  and install the latest postgres version for Windows x86-64

    2. During installer, uncheck pgAdmin 4 and StackBuilder, enter 1234 as password for database superuser, default port (should be 5432), default locale, then install

    3. Run Command Prompt as administrator and enter:    psql --version
       It should return version if installed

    4. To connect to postgres enter:    psql -U postgres
       Enter password (1234)

    5. when in postgres enter:    CREATE DATABASE webregistrationapp;
       This creates the database

    6. Enter \l to list the databases. You should see 4, one being webregistrationapp (with owner postgres)

    7. \q to quit postgresql

    8. to check the status of the postgres server enter:   pg_ctl -D "C:\Program Files\PostgreSQL\16\data" status 
       It should say the server is running, if not you can replace status with start to start it (or stop to stop it)

#### IV. Installing Dbeaver
    1. Go here: https://dbeaver.io/download/  and install dbeaver with windows installer.

    2. Install for everyone or yourself, include java if you don't have java installed on your computer.

    3. start dbeaver 

    4. On menu bar go to Database > New Database Connection.

    5. Choose Postgresql, under connection settings the port should be 5432, password is 1234, user postgres, database webregistrationapp. test connection in bottom left. (download drivers if you need to) click finish if no error.

    6. Open all the sqlfiles in the backend/databaseSQL folder.

    7. In schemaSQL.spl tab right click in the text editing area and do execute > execute SQL script
       This create the database schema and tables
       (if you get a "no active connection" error go to SQL Editor in menu bar then set active connection)
       (Refresh webregistrationapp on left side to see changes, right click and refresh)

    8. In addRecords.sql tab execute the script to add records to the table

    9. queries.sql has queries that can be executed. Execute sql query for 1 at a time or execute sql script for all.

    10. RegistrationDropSchema drops the schema and tables.

#### Check If Enviroment is set up
    1. In app.py file in backend folder, make sure the psycopg connect parameters are the same as what was used in dbeaver to connect to postgresql (for each endpoint)

    2. start react, flask, and make sure server is running (it should be)

    3. In the browser that react app opened test the communication between backend and frontend by testing the login page. First with incorrect credentials, you should get "Wrong pin or password alert". Second with correct credentials (ex.  98513241  and 327914) it should redirect you to homepage.

    (JSON parse error means something is wrong)
