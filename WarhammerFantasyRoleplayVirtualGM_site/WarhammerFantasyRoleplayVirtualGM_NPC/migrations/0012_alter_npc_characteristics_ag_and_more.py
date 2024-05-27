# Generated by Django 5.0.6 on 2024-05-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarhammerFantasyRoleplayVirtualGM_NPC', '0011_npc_characteristics_m_npc_characteristics_w_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='npc',
            name='characteristics_ag',
            field=models.IntegerField(default='0', verbose_name='Agility'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_bs',
            field=models.IntegerField(default='0', verbose_name='Ballistic Skill'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_dex',
            field=models.IntegerField(default='0', verbose_name='Dexterity'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_fel',
            field=models.IntegerField(default='0', verbose_name='Fellowship'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_i',
            field=models.IntegerField(default='0', verbose_name='Initiative'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_int',
            field=models.IntegerField(default='0', verbose_name='Intelligence'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_s',
            field=models.IntegerField(default='0', verbose_name='Strength'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_t',
            field=models.IntegerField(default='0', verbose_name='Toughness'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_w',
            field=models.IntegerField(default='0', verbose_name='Wounds'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='characteristics_wp',
            field=models.IntegerField(default='0', verbose_name='Willpower'),
        ),
    ]
