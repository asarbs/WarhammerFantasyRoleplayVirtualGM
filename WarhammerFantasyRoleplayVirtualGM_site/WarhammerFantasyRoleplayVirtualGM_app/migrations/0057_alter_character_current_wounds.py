# Generated by Django 3.2.19 on 2024-05-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0056_rename_wounds_character_current_wounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='current_wounds',
            field=models.IntegerField(default='0', verbose_name='Current Wounds'),
        ),
    ]