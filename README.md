# Login Authentication using Python and Django
Login authentication application using Python and Django with PostgreSQL

## Description
This authentication application, built with Python, Django, and PostgreSQL, was developed on Windows 10 using VSCode and has been tested on both Windows 10 and Mac OS Ventura. It gathers registration details from new users and saves this information in a PostgreSQL database. Upon successful login, users are directed to a homepage. The application enforces the following:

* Registering with existing credentials triggers an error message.
* Mismatched passwords during registration result in an error.
* Attempting to log in with non-existent credentials also raises an error.



## Prior to Execution
Before running the project, you must install all necessary components on your machine: python3, Django, PostgreSQL15, and psycopg2. The following instructions describe how to prepare the environment on Windows 10 or Mac.

Begin by installing PostgreSQL15. You can follow the instructions from the [PostgreSQL website](https://www.postgresql.org/download/). However, if you're on a mac, you can simply enter `brew install postgresql@15`. I recommend using PGAdmin 4 - you can find the installer [here](https://www.pgadmin.org/download/pgadmin-4-macos/). I chose to use PGAdmin 4 and will reference it in the following instructions. 

Clone the project repository. After doing so, create a virtual environment adjacent to the project folder, then activate the virtual environment. To activate the virtual environment on mac, navigate to the "bin" directory and enter `scource activate`. On windows, navigate to the "Scripts" directory and enter `.\activate`.

Now, configure a postgresql server with a database. To do so, open PGAdmin 4 and register a new server. Expand the new server, right-click on 'Databases,' create a new database called "loginauth" and save. 

Having activated the virtual environment and configured postgresql, the project must be connected to postgresql. To do so, open the project and navigate to settings.py in the "loginauth" folder. Find the following section and enter your postgresql database information. If your database is named "loginauth" under the user "postgres" running on localhost and port 5432, replace only the password:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'loginauth',
        'USER': 'postgres',
        'PASSWORD' : 'Enter your password here...',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}
```
Install Django in the folder containing the project and virtual environment folders. To do so, enter `pip install django`.

Ensure you have downloaded `psycopg2`, a necessary package for using django with postgresql. You can do so by using `pip install psycopg2` or `pip3 install psycopg2-binary` in the project folder.

Finally, after installing all necessary components, migrate to your database by entering `python manage.py migrate` in the project directory. 

Optionally, you can create a super user by using `python manage.py createsuperuser`.



## Execution
To run the project, first launch the virtual environment, then navigate to the project folder. In the project folder, enter `python manage.py runserver`. If the environment was properly configured, you should see the following output in the terminal:
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 01, 2023 - 20:43:35
Django version 4.2.4, using settings 'loginauth.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Copy the address where the development server is at and enter it in your browser. 



## Walkthrough
After entering the address in your browser, you will see a 404 error:

![404 error](https://github.com/BrickFrisbee/login-authentication/blob/main/images/local.PNG "local")

The 404 error appears because you must enter a path with the address. The path for the signup page is `signup/`, which should be appended to the to address. You should now see the signup page:

![Create an Account](https://github.com/BrickFrisbee/login-authentication/blob/main/images/Signup_Blank.PNG "signup")

Enter credentials to create a new account. After hitting the "Sign Up" button, the credentials will be added to the database. The following is an image of the `auth_user` table in the database. Having created a user with the first name "firsttest1," last name "lasttest1," email "test1@test.me," username "test1," and password "test," the information is visible in the first row of the table and can be used to login:

![Database](https://github.com/BrickFrisbee/login-authentication/blob/main/images/database.png "database")

After creating a new user and hitting the signup button, you will be redirected to the `login/` page:

![Login](https://github.com/BrickFrisbee/login-authentication/blob/main/images/Login_Blank.PNG "login")

Having successfully logged in with your credentials, you will be redirected to the `success/` page. You can choose to return to the `signup/` page or `login/` page:

![Successful Login](https://github.com/BrickFrisbee/login-authentication/blob/main/images/Success.PNG "success")







