# Generated by Django 5.0.1 on 2024-01-28 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_aboutme_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutme',
            name='image_my',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='image_partner',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]