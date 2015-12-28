===============================
Running the example application
===============================

Assuming you use virtualenv, follow these steps to download and run the
django-knowledgebase example application in this directory:

::

    $ git clone git://github.com/bazzite/django-knowledgebase.git
    $ cd django-knowledgebase/example
    $ virtualenv venv
    $ . venv/bin/activate
    $ pip install -r requirements.txt

Now we need to create the database tables and an admin user.

::

    $ python manage.py migrate
    $ python manage.py createsuperuser

Now you need to run the Django development server:

::

    $ python manage.py runserver

You should then be able to open your browser on http://127.0.0.1:8000.
