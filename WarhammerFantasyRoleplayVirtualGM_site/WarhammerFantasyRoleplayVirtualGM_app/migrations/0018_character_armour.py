# Generated by Django 3.2.19 on 2023-09-01 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0017_improvementxpcosts'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='armour',
            field=models.ManyToManyField(to='WarhammerFantasyRoleplayVirtualGM_app.Armour', verbose_name='Armour'),
        ),
    ]
