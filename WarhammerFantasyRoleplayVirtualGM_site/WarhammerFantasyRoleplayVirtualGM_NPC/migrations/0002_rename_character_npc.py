# Generated by Django 3.2.19 on 2024-05-25 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0057_alter_character_current_wounds'),
        ('WarhammerFantasyRoleplayVirtualGM_NPC', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Character',
            new_name='NPC',
        ),
    ]
