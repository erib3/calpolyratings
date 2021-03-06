# Generated by Django 2.1.2 on 2018-12-24 04:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_profile', '0006_auto_20181220_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
