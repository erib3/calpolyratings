#!/bin/bash

python manage.py dumpdata --format json department_courses.Department > fixtures2/Departments.json
python manage.py dumpdata --format json department_courses.Course > fixtures2/Courses.json
python manage.py dumpdata --format json teacher_profile > fixtures2/Teacher_profiles.json
python manage.py dumpdata --format json postings > fixtures2/Posts.json

