# Generated by Django 5.1 on 2024-09-09 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_alter_news_datetime_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='datetime_create',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 9, 20, 56, 21, 235743), verbose_name='Create Time'),
        ),
    ]