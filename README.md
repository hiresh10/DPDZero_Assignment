# DPDZero_Assignment
Table of Contents
Getting Started
Installation
Authentication
Endpoints
User Registration
Token Obtain
Token Refresh
Other Endpoints...
Error Handling

Installation
Clone this repository:
git clone https://github.com/hiresh10/DPDZero_Assignment/your-api.git
cd your-api

Prerequisites
Before you begin, make sure you have the following installed:

Python 3.x: https://www.python.org/downloads/
Django 3.x: Install using pip
pip install django
Clone the Repository
First, clone the repository to your local machine using the following command:

bash
git clone https://github.com/your-username/tender-proposal-app.git
Setup Virtual Environment (Optional, but Recommended)
It's a good practice to create a virtual environment to manage project dependencies.

Install virtualenv (if you don't have it installed):

pip install virtualenv
Create a virtual environment:

virtualenv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate
On macOS and Linux:
bash
source venv/bin/activate
Install Dependencies
Change into the project directory and install the required dependencies using pip:

bash
cd tender-proposal-app
Database Setup
By default, the app is configured to use SQLite as the database. You can change this in the settings if needed. To set up the initial database, run the following commands:

python manage.py makemigrations
python manage.py migrate
Create Superuser
To access the Django admin interface, create a superuser using the following command:

python manage.py createsuperuser
Run the Development Server
Start the development server using the following command:

python manage.py runserver
The app will now be accessible at http://127.0.0.1:8000/

Access Admin Interface
To access the Django admin interface, go to http://127.0.0.1:8000/admin/ and log in using the superuser credentials created earlier.
