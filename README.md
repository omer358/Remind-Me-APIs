# Remind-Me-APIs
  A REST-APIs service for my previous personal Mobile app [Remind Me](http://github.com/omer358/Remind-Me).

# Installation
  * Clone the project.
  * Create a virtual evnirnoment.
  * Activate your virtual environment. 
  * Run: ```pip install -r requirement.txt``` to install  all the required packages
  * Create a Postgres database under the name **Remind-Me** and update the `DATABASE` dictanory in  `settings.py` to your own database configrations.
  * Run ```python manage.py makemigrations``` & ```python manage.py migrate```. 

And that's it! you're ready to go.

# Technologies
  * [Django Framework](https://djangoproject.com).
  * [Django REST framework](https://www.django-rest-framework.org).
