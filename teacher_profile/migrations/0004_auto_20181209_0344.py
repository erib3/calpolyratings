# Generated by Django 2.1.2 on 2018-12-09 03:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_profile', '0003_auto_20181209_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_profile',
            name='first_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='teacher_profile',
            name='last_name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
