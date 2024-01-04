# EdLight Interview Application
## Sections
* [Project Structure](#project)
* [Tech Overview](#tech)
* [API Summary](#api)
* [Database Schema](#database)
* [Required Setup](#setup)
* [Running the Application](#run)
* [Testing the Application](#test)
* [Logging Levels](#logging)
* [Other Information](#other)
## <a name="project" id="project"></a> Project Structure
This project follows the <a href="https://docs.djangoproject.com/en/5.0/intro/tutorial01/">default structure</a> for a Django application.

The root application configuration is in the `worksheet` folder and the `comments` and `images` folders contain the two Django apps. All urls are contained in the root worksheet `urls.py` (more on that in the API summary section). The `images` app contains all the static content and templates for the application; the `comments` app contains neither of these. Both `comments` and `images` map to database tables (more on that in the database schema section). The `media` folder contains all the images uploaded by users.

## <a name="tech" id="tech"></a> Tech Overview
In addition to the required Django modules and standard Python libraries that form the base of the application, the following additional technologies were used:
* **Google Image AI API**: This is the API used to analyze uploaded images and extract test from them. For more information on it, go <a href="https://cloud.google.com/vision/docs/ocr#vision_text_detection-python">here</a>.
* **Bootstrap**: This is the base UI framework for the application so that everything has consistent colors and styling. For more information on it, go <a href="https://getbootstrap.com/docs/5.3/getting-started/introduction/">here</a>. 
* **jQuery**: This is the extremely minimal JavaScript framework used for most of the required JavaScript functionality in the app. For more information on it, go <a href="https://jquery.com/">here</a>.
* **Waypoints**: This is a JavaScript library used to enable infinite scrolling behavior. For more information on it, go <a href="http://imakewebthings.com/waypoints/guides/getting-started/">here</a>.

## <a name="api" id="api"></a> API Summary
There are four API endpoints in the application:
* `/analyze-image` (`POST` only): Receives a request to upload an image from the user. Image is analyzed by the Google Image AI API. Text found by the API and the image are uploaded to the database.
* `/images` (`GET` only): Loads all the images uploaded to the site on the home page.
* `/image/<id>` (`GET` only): Loads all the comments and other details associated with an image on the image detail page.
* `/image/<id>/comment` (`POST` only): Receives a request to add a comment under an image from a user. Requires the user to be logged in to access, and uses their username in the data associated with the comment.

There are also the `admin` and `login` links for the purposes of application administration and authenticaiton, respectively

## <a name="database" id="database"></a> Database Schema
There are two custom tables in the application:
* comments: Represent comments under each processed image (In application as Comment)
* images: Represent each processed image (in application as ImageUpload)

There is also the standard users table provided by Django

The columns for the two custom tables are represented as follows:
* comments:
    * id: Primary key
    * text: the content of the comment
    * author: a foreign key to the users table (represents the person who wrote the comment)
    * image: a foreign key to the images table (represents the image the comment is under)
* images:
    * id: Primary key
    * image: the actual uploaded image file
    * text: the text that has been extracted from each image

The images and comments have a one to many relationship, where every image can have any number of comments.

## <a name="setup" id="setup"></a> Required Setup
Each of the following steps only needs to be done once.

### 0. Basic Requirements
Make sure all the project files are in some local location on your computer. You should also have the latest version of <a href="https://www.python.org/downloads/">Python</a> with pip installed as a command line on your system.

### 1. Virtual Environment
If you don't already have the <a href="https://docs.python.org/3/library/venv.html">virtual environment</a> module installed globally on your system, install it.

Next, create a virtual environment with the following command:

`python -m venv ./.venv`

Next, run the <a href="https://docs.python.org/3/library/venv.html#how-venvs-work">appropriate command</a> to activate a virtual environment based on your operating system.

Finally, install all the Python modules for the project using the following command:

`pip install -r requirements.txt`

### 2. ENV file configuration

In the root directory on the project is a `default.env` file. Rename this file to simply `.env`.

Next, in the invitation to collaborate on the Google Drive, there should have been a "secret word". Go to <a href="https://1drv.ms/u/s!AktASkXGXSHv3FpCHowewUpmcJyO">this file</a> and use the "secret word" as the password.

Download that file and place it in the root directory for the project. 

Lastly, change the value in the env file for `GOOGLE_APPLICATION_CREDENTIALS` to match the name of the file. Save the env file.

### 3. Initialize the application

To create a starting database for the application, run the following two commands in order:

`python manage.py makemigrations`

`python manage.py migrate`

The application begind with an empty database

To create a user account, run the following command:

`python manage.py createsuperuser`

Then, answer the prompts that follow. Email can be left blank. The password will not appear as you type it. 

## <a name="run" id="run"></a> Running the Application
To start the application, run the following command:

`python manage.py runserver`

To manage the administrative aspects of the application, go to <a href="http://localhost:8000/admin">this link</a> while the application is running

## <a name="test" id="test"></a> Testing the Application
All tests in the application are in same directories as the files they test.

To run the tests for the application, run the following command line in the root project directory:

`python manage.py test`

To run all the tests in a folder, run:

`python manage.py test folderName`

To run all the tests in a particular module, run:

`python manage.py test moduleName.tests`

To run just one test case class, run:

`python manage.py test moduleName.tests.TestCaseName`

To run just one test case function, run:

`python manage.py test moduleName.tests.TestCaseName.test_name`

For more information on running tests, go <a href="https://docs.djangoproject.com/en/5.0/topics/testing/overview/">here</a>

## <a name="logging" id="logging"></a> Logging Levels
There are five logging levels in the application, from least to most detailed:
* `DEBUG`: The most detailed level. All potential log messages will appear
* `INFO`: Messages will appear about the most important bits regarding application data and flow
* `WARNING`: Only warning messages, exceptions, and errors will appear in the logs
* `ERROR`: Only exceptions and errors will appear in the logs
* `CRITICAL`: Only exceptions or errors that stop the application from functioning will appear in the logs

By default, only output from the `WARNING` level and above will be displayed.

To change the level of logging, replace `WARNING` in line 30 of `./worksheet/settings.py` to your desired logging level from the list above.

Changing other logging configuration details can be found <a href="https://docs.djangoproject.com/en/5.0/topics/logging/">here</a>.

## <a name="other" id="other"></a> Other Information
The applicant who created this project is Natalie Euley.

The start time for the project in Central Time was 8AM on 1/1/24 and the end time for the project was 8AM on 1/4/24.

The requirements of the project are <a href="https://docs.google.com/document/d/1Mo7GnUfcQ8p--IuXcLoRKxI40dhkBrn3wXblukrZ5N0/edit">here</a>.

And the terms of the project are <a href="https://na2.documents.adobe.com/public/agreements/view/CBJCHBCAABAAhm9rLa3kposOtcznKgcdNWcJAC7n4H7r?type=esign&tsid=CBFCIBAACBSCTBABDUAAABACAABAAs0BjSex2KLx8CFxAvOSftghKm-BBmO0gIQgANSfdRcYu49Cfi1oSvFl3lNqt49AyDp7YFLM8L7hwbClrRcPpWHLA7XzN0x61vsSXHGY9MRvdzIP9UG9GgZ6fzSh1iFn4">here</a>.