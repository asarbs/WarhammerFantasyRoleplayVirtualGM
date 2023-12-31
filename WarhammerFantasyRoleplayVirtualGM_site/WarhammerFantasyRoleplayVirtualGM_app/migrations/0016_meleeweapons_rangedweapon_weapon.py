# Generated by Django 3.2.19 on 2023-08-29 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0015_trapping_encumbrance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('weapon_group', models.CharField(choices=[('BASIC', 'BASIC'), ('BLACKPOWDER', 'BLACKPOWDER'), ('BOW', 'BOW'), ('BRAWLING', 'BRAWLING'), ('CAVALRY', 'CAVALRY'), ('CROSSBOW', 'CROSSBOW'), ('ENGINEERING', 'ENGINEERING'), ('ENTANGLING', 'ENTANGLING'), ('EXPLOSIVES', 'EXPLOSIVES'), ('FENCING', 'FENCING'), ('FLAIL', 'FLAIL'), ('PARRY', 'PARRY'), ('POLEARM', 'POLEARM'), ('SLING', 'SLING'), ('THROWING', 'THROWING'), ('TWO-HANDED', 'TWO-HANDED')], default='BASIC', max_length=14, verbose_name='Weapon Group')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('encumbrance', models.IntegerField(default=1, verbose_name='Encumbrance')),
                ('availability', models.CharField(choices=[('Common', 'Common'), ('Scarce', 'Scarce'), ('Rare', 'Rare')], default='Common', max_length=6, verbose_name='Availability')),
                ('damage', models.IntegerField(default=0, verbose_name='Damage')),
                ('qualities_and_flaws', models.CharField(default='-', max_length=250, verbose_name='Qualities & Flaws')),
            ],
        ),
        migrations.CreateModel(
            name='MeleeWeapons',
            fields=[
                ('weapon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WarhammerFantasyRoleplayVirtualGM_app.weapon')),
                ('reach', models.CharField(choices=[('AVERAGE', 'Average'), ('LONG', 'Long'), ('MASSIVE', 'Massive'), ('MEDIUM', 'Medium'), ('PERSONAL', 'Personal'), ('VARIES', 'Varies'), ('VERY_LONG', 'Very_Long'), ('VERY_SHORT', 'Very Short')], default='VERY_SHORT', max_length=14, verbose_name='Reach')),
            ],
            bases=('WarhammerFantasyRoleplayVirtualGM_app.weapon',),
        ),
        migrations.CreateModel(
            name='RangedWeapon',
            fields=[
                ('weapon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='WarhammerFantasyRoleplayVirtualGM_app.weapon')),
                ('range', models.IntegerField(default=0, verbose_name='Range')),
            ],
            bases=('WarhammerFantasyRoleplayVirtualGM_app.weapon',),
        ),
    ]
