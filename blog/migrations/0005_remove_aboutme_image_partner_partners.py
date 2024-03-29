# Generated by Django 5.0.1 on 2024-01-28 09:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_aboutme_image_my_alter_aboutme_image_partner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='image_partner',
        ),
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('AboutMe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.aboutme')),
            ],
        ),
    ]
