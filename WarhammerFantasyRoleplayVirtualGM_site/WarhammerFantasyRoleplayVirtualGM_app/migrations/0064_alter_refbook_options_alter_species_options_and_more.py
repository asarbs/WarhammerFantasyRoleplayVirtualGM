# Generated by Django 5.1.3 on 2025-05-19 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0063_character_coruption_and_mutation_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='refbook',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='species',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='talent',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='trapping',
            options={'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='Character2Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_app.character')),
                ('weapon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_app.weapon')),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='weapons_with_quantity',
            field=models.ManyToManyField(related_name='characters_with_quantity', through='WarhammerFantasyRoleplayVirtualGM_app.Character2Weapon', to='WarhammerFantasyRoleplayVirtualGM_app.weapon', verbose_name='Weapons (with quantity)'),
        ),
    ]
