# Generated by Django 5.0.6 on 2024-06-18 10:30

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_alter_director_options_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
