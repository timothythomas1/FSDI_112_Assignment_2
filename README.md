# FSDI_112_Assignment_2

❯ python3 -m venv venv
❯ source venv/bin/activate
❯ pip3 install django

# Check Django Commands
❯ django-admin

# (Creates a config dir and manage.py file)
❯ django-admin startproject config . 
❯ python3 manage.py

# (Run the server)
❯ python3 manage.py runserver

❯ python3 manage.py migrate

# (Creating a new user)
❯ python3 manage.py createsuperuser 

# (Creating a new "app")
❯ python3 manage.py startapp pages
❯ code .

After running server, you can go to /admin to log in.

(GitHub Open Sourced Repo)
https://github.com/django/django