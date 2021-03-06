# Generated by Django 2.1.2 on 2019-07-31 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department_courses', '0009_department_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='abbreviation',
            field=models.CharField(max_length=5, unique=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
