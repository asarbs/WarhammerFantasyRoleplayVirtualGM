# Generated by Django 3.2.19 on 2023-09-02 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0020_auto_20230902_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spells',
            name='effect',
            field=models.TextField(default='', verbose_name='Effect'),
        ),
    ]