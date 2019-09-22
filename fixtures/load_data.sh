#!/bin/bash
python manage.py loaddata fixtures/Departments.json 
python manage.py loaddata fixtures/Courses.json 
python manage.py loaddata fixtures/Teacher_profiles.json 
python manage.py loaddata fixtures/Posts.json 

