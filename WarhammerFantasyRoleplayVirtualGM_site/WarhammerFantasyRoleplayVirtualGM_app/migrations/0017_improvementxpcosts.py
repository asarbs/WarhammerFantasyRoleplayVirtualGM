# Generated by Django 3.2.19 on 2023-09-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0016_meleeweapons_rangedweapon_weapon'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImprovementXPCosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advances_interval_start', models.IntegerField(default='0', verbose_name='Advances Interval Start')),
                ('advances_interval_end', models.IntegerField(default='0', verbose_name='Advances Interval End')),
                ('characteristics_xp_cost', models.IntegerField(default='0', verbose_name='Characteristics xp cost')),
                ('skills_xp_cost', models.IntegerField(default='0', verbose_name='Skills Xp Cost')),
            ],
        ),
    ]