# Generated by Django 5.0.1 on 2024-01-29 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_categories_tags_blog_subblog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=123)),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField()),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog')),
            ],
        ),
    ]
