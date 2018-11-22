# playWithDjango
I just want to play with Django


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
To install this project you need the following framework and tools
```
- Python3
- Postgres
```

### Installing
These Steps would help you install the project dependent packages and run the application.

#### Primary steps
* Clone the repository and CD into the repository directory
* Ensure that you have created a database for this project
* Create a file called `env.sh`
* Copy the content of the file `env.sample.sh` to the `env.sh` file and add the appropriate value to the variables
* Run the shell script to export the environment variable `. env.sh`
* create and activate a virtual environment. Here is an example using Virtualenv: run `virtualenv env` to create the environment then run `activate env/bin/activate` to activate the virtual environment
* Install the base dependencies `pip install -r requirements/base.txt` and test dependencies `pip install -r requirements/test.txt`
* Run migration `python manage.py migrate`
* Start the app via Django `python manage.py runserver`  or Gunicorn `gunicorn config.wsgi`


## List of Features that I have played with
* [Rss](https://docs.djangoproject.com/en/2.1/ref/contrib/syndication/): used in the `rss` app
