# Generated by Django 5.0.6 on 2024-06-17 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='label_text',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
