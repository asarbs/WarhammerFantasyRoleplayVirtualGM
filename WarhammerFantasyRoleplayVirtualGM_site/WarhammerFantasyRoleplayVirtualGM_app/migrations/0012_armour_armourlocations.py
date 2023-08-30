# Generated by Django 3.2.19 on 2023-08-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0011_auto_20230828_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArmourLocations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Armour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('armour_type', models.CharField(choices=[('NO', ' '), ('SOFT LEATHER', 'SOFT LEATHER'), ('BOILED LEATHER', 'BOILED LEATHER'), ('MAIL', 'MAIL'), ('PLATE', 'PLATE')], default='NO', max_length=14, verbose_name='Armour Type')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('encumbrance', models.IntegerField(default=0, verbose_name='Encumbrance')),
                ('availability', models.CharField(choices=[('Common', 'Common'), ('Scarce', 'Scarce'), ('Rare', 'Rare')], default='Common', max_length=6, verbose_name='Availability')),
                ('penalty', models.CharField(max_length=250, verbose_name='Penalty')),
                ('armour_points', models.IntegerField(default=1, verbose_name='Armour Points')),
                ('qualities_and_flaws', models.CharField(max_length=250, verbose_name='Qualities & Flaws')),
                ('locations', models.ManyToManyField(to='WarhammerFantasyRoleplayVirtualGM_app.ArmourLocations', verbose_name='Locations')),
            ],
        ),
    ]
