# Generated by Django 5.0.6 on 2024-06-17 12:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0002_topic_label_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue_message',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
