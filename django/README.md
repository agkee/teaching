# Tutorial Guide

## Basic setup 
- Must have Python installed
```
pip install Django
django-admin startproject PROJECT_NAME
```

## Structure
- One project has multiple applicatons
- Define all the urls from this big file 
- Specify urls within each applications under urls.py file 
- Handle these urls from the views.py file 

### Managing Files
1. manage.py
    - Generally won't change this file

2. settings.py
    - settings of the project 

3. urls.py 
    - table of contents that all my application is going to visit 

Running server
```
python manage.py runserver
```

Create a new app 
```
python manage.py startapp hello
```
Add hello under installed apps in settings.py inside django_basics

Migrate tables 
```
python manage.py migrate
```

### Managing applications
1. views.py
    - File where the user will see
2. urls.py
    - Create urls.py where it will keep track of all the urls of this project 
    - Try adding more paths 
