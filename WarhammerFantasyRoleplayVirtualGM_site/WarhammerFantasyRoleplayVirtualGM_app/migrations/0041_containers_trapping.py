# Generated by Django 3.2.19 on 2023-12-30 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_app', '0040_auto_20231211_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='containers',
            name='trapping',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='WarhammerFantasyRoleplayVirtualGM_app.trapping'),
            preserve_default=False,
        ),
    ]
