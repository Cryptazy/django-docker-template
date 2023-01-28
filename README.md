# Deploying a Scalable Django App with Docker, Celery, Redis, Nginx, and PostgreSQL
Streamlining Development and Production with a Containerized Django Stack

Deploying a Django application with multiple components such as Celery, Redis, Nginx, and PostgreSQL can be a daunting task, 
especially when trying to do it on a home Linux server. Each component requires specific configurations and dependencies, 
and if not set up correctly, can lead to conflicts and errors. Additionally, maintaining and scaling the application can become 
increasingly difficult as the traffic and complexity of the app grows. However, by containerizing the components with Docker, 
it becomes much easier to manage and deploy the application.

### django-docker-template
An example of a django project wih celery, postgresql, redis, gunicorn and nginw contenarized with Docker

### Copy the files to a new folder

### In the django directory 
- add : .env file to store the credential of your database

### in the django folder: run the following command to create virtual environement:
python -m venv venv

## Activate the virtual environement
venv\Scripts\activate

## Install the requirements:
pip install -r requirements.txt

Note:
- the .env file will have your database credential on the production server
- the -env_dev will have your credential on the developmenent server

the .en file should be as follows:

DATABASE_URL=postgres://user:password@db:5432/db_name

POSTGRES_PORT=5432

POSTGRES_HOST=db

POSTGRES_USER=user

POSTGRES_PASSWORD=password

POSTGRES_DB=db_name

