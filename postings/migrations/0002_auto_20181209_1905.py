# Generated by Django 2.1.2 on 2018-12-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department_courses', '0003_auto_20181209_1905'),
        ('postings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='course_abbrv',
        ),
        migrations.RemoveField(
            model_name='post',
            name='course_num',
        ),
        migrations.AddField(
            model_name='post',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='department_courses.Class'),
        ),
    ]
