# Generated by Django 5.0.1 on 2024-01-28 07:36

import django.core.validators
import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='tel',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='UZ', validators=[django.core.validators.RegexValidator('^\\d{3}-\\d{3}-\\d{4}$')]),
        ),
    ]
