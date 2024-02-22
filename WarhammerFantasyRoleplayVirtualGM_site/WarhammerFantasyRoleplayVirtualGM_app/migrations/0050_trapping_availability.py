# Generated by Django 3.2.19 on 2024-02-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0049_trapping_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='trapping',
            name='availability',
            field=models.CharField(choices=[('Common', 'Common'), ('Scarce', 'Scarce'), ('Rare', 'Rare'), ('Exotic', 'Exotic')], default='Common', max_length=6, verbose_name='Availability'),
        ),
    ]
