# Generated by Django 5.0.1 on 2024-01-30 10:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_alter_results_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.comments'),
        ),
        migrations.AddField(
            model_name='comments',
            name='top_level_comment_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='results',
            name='created_time',
            field=models.DateTimeField(),
        ),
    ]
