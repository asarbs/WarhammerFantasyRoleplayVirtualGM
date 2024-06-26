# Generated by Django 5.0.6 on 2024-05-25 18:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_NPC', '0003_npc_characteristics_ag_npc_characteristics_bs_and_more'),
        ('WarhammerFantasyRoleplayVirtualGM_app', '0057_alter_character_current_wounds'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='portrait',
            field=models.ImageField(null=True, upload_to='static/page_images/'),
        ),
        migrations.CreateModel(
            name='NPC2Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default='0', verbose_name='Value')),
                ('npc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_NPC.npc')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_app.skils')),
            ],
        ),
        migrations.AddField(
            model_name='npc',
            name='skills',
            field=models.ManyToManyField(through='WarhammerFantasyRoleplayVirtualGM_NPC.NPC2Skill', to='WarhammerFantasyRoleplayVirtualGM_app.skils'),
        ),
    ]
