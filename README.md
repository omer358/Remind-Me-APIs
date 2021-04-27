# Remind-Me-APIs
  A REST-APIs service for my previous personal Mobile app [Remind Me](http://github.com/omer358/Remind-Me).

# Installation
  * Clone the project.
  * Create a virtual evnirnoment.
  * Activate your virtual environment. 
  * Run: ```pip install -r requirement.txt``` to install  all the required packages
  * Create a Postgres database under the name **Remind-Me** and update the `DATABASE` dictanory in  `settings.py` to your own database configrations.
  * Run ```python manage.py makemigrations``` & ```python manage.py migrate```.
  * Create some users.
  * Create a token for each user by runing ```manage.py drf_create_token <username>```
  * Add some people to the database.
  * In your request add the token as ```query_params``` like this:
    - ```http://127.0.0.1:8000/people/?token=```
  

 That's it! you're ready to go.

# Technologies
  * [Django Framework](https://djangoproject.com).
  * [Django REST framework](https://www.django-rest-framework.org).
