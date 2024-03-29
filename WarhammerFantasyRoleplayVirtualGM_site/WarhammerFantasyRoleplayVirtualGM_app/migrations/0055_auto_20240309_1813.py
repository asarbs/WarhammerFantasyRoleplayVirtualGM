# Generated by Django 3.2.19 on 2024-03-09 17:13

from django.db import migrations, models

import random
import string

def calculate_hash_id(apps, schema_editor):
    Character = apps.get_model('WarhammerFantasyRoleplayVirtualGM_app', 'Character')
    for character in Character.objects.filter(hash_id=""):
        hash = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(29))
        character.hash_id = hash
        character.save()

class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0054_auto_20240305_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='character2careerpath',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='character',
            name='hash_id',
            field=models.CharField(default='', max_length=29, verbose_name='Hash ID'),
        ),
        migrations.RunPython(calculate_hash_id),
    ]
