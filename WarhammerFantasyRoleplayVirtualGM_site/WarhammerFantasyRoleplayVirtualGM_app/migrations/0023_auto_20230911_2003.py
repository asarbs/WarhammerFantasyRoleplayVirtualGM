# Generated by Django 3.2.19 on 2023-09-11 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0022_remove_character_experience_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='weapon',
            name='reference',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=models.SET(None), to='WarhammerFantasyRoleplayVirtualGM_app.reference'),
        ),
        migrations.AlterField(
            model_name='character2talent',
            name='taken',
            field=models.IntegerField(default='0', verbose_name='Taken'),
        ),
    ]
