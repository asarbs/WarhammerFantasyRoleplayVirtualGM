# Generated by Django 5.0.7 on 2024-08-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_news2tag_news_tagss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='contents',
            field=models.TextField(blank=True, default='', null=True, verbose_name='lead'),
        ),
    ]
