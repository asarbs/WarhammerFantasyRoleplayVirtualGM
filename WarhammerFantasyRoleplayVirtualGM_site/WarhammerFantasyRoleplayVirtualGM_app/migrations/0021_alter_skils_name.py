# Generated by Django 3.2.19 on 2023-08-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0020_alter_skils_ref'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skils',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]