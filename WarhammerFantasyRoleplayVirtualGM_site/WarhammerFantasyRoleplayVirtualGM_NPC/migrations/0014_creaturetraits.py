# Generated by Django 5.0.6 on 2024-05-26 18:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_NPC', '0013_alter_npc_species'),
        ('WarhammerFantasyRoleplayVirtualGM_app', '0058_alter_campaign_notes_alter_character_notes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatureTraits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(default='', verbose_name='Description')),
                ('ref', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_app.reference')),
            ],
        ),
    ]
