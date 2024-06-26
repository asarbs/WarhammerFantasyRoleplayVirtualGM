# Generated by Django 5.0.6 on 2024-05-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0057_alter_character_current_wounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='notes',
            field=models.ManyToManyField(blank=True, to='WarhammerFantasyRoleplayVirtualGM_app.note', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='character',
            name='notes',
            field=models.ManyToManyField(blank=True, to='WarhammerFantasyRoleplayVirtualGM_app.note', verbose_name='Notes'),
        ),
        migrations.AlterField(
            model_name='character',
            name='spells',
            field=models.ManyToManyField(blank=True, to='WarhammerFantasyRoleplayVirtualGM_app.spells', verbose_name='Spells'),
        ),
    ]
