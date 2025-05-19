from django.db import migrations


def migrate_weapons(apps, schema_editor):
    Character = apps.get_model('WarhammerFantasyRoleplayVirtualGM_app', 'Character')
    Character2Weapon = apps.get_model('WarhammerFantasyRoleplayVirtualGM_app', 'Character2Weapon')

    for character in Character.objects.all():
        # Zakładamy, że istnieje pole character.weapon jako ManyToManyField
        for weapon in character.weapon.all():
            Character2Weapon.objects.create(character=character, weapon=weapon, quantity=20)


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0064_alter_refbook_options_alter_species_options_and_more'),
    ]

    operations = [
        migrations.RunPython(migrate_weapons),
    ]
