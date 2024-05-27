# Generated by Django 5.0.6 on 2024-05-26 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_NPC', '0012_alter_npc_characteristics_ag_and_more'),
        ('WarhammerFantasyRoleplayVirtualGM_app', '0058_alter_campaign_notes_alter_character_notes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npc_species', to='WarhammerFantasyRoleplayVirtualGM_app.species', verbose_name='Species'),
        ),
    ]
