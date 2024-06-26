# Generated by Django 5.0.6 on 2024-06-14 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_remove_decade_label_alter_movie_decade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Decade',
        ),
        migrations.AddField(
            model_name='movie',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movie.country'),
        ),
    ]
