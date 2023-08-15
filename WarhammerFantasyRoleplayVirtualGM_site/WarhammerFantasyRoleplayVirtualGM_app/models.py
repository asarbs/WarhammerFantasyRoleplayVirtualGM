from django.db import models
from django.contrib.auth.models import User
from WarhammerFantasyRoleplayVirtualGM_app.validators import validator_sex

# Create your models here.

class RefBook(models.Model):
    name = models.CharField(max_length= 250)
    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Reference(models.Model):
    refBook = models.ForeignKey(RefBook, on_delete=models.CASCADE, verbose_name="Reference Book")
    page = models.IntegerField(default=0, verbose_name="Page")
    def __str__(self):
        return u"{0}, {1}".format(self.refBook.name, self.page)

    def __unicode__(self):
        return u"{0}, {1}".format(self.refBook.name, self.page)

class Campaign(models.Model):
    name = models.CharField(max_length= 250)
    party_name = models.CharField(max_length= 250, default="")
    ambitions_shortterm = models.TextField(verbose_name="Shortterm", default="")
    ambitions_longterm = models.TextField(verbose_name="Longterm", default="")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)


class Player(models.Model):
    user = models.OneToOneField(User, verbose_name='Player', on_delete=models.CASCADE)

    def __str__(self):
        return u"{0} \"{1}\" {2}".format(self.user.first_name, self.user.username, self.user.last_name)

    def __unicode__(self):
        return u"{0} \"{1}\" {2}".format(self.user.first_name, self.user.username, self.user.last_name)

class Campaign2Player(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return u"{0} -> {1}".format(self.player, self.campaign)

    def __unicode__(self):
        return u"{0} -> {1}".format(self.player, self.campaign)

class Species(models.Model):
    name = models.CharField(max_length= 50)
    random_interal_start = models.IntegerField(default=0, verbose_name="random_interal_start")
    random_interal_end = models.IntegerField(default=0, verbose_name="random_interal_start")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class ExampleName(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE)
    name = models.CharField(max_length= 50, unique=True)
    sex = models.CharField(validators = [validator_sex], max_length=1, default="f")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class CareerPath(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Class(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Career(models.Model):
    name = models.CharField(max_length= 50)
    ch_class = models.ForeignKey(Class, verbose_name="Class", default="1", on_delete=models.CASCADE)
    random_table_human_start = models.IntegerField(default="0", verbose_name="random_table_human_start")
    random_table_human_end = models.IntegerField(default="0", verbose_name="random_table_human_end")
    random_table_dwarf_start = models.IntegerField(default="0", verbose_name="random_table_dwarf_start")
    random_table_dwarf_end = models.IntegerField(default="0", verbose_name="random_table_dwarf_end")
    random_table_halfling_start = models.IntegerField(default="0", verbose_name="random_table_halfling_start")
    random_table_halfling_end = models.IntegerField(default="0", verbose_name="random_table_halfling_end")
    random_table_high_elf_start = models.IntegerField(default="0", verbose_name="random_table_high_elf_start")
    random_table_high_elf_end = models.IntegerField(default="0", verbose_name="random_table_high_elf_end")
    random_table_wood_elf_start = models.IntegerField(default="0", verbose_name="random_table_wood_elf_start")
    random_table_wood_elf_end = models.IntegerField(default="0", verbose_name="random_table_wood_elf_end")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Status(models.Model):
    name = models.CharField(max_length= 50)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Hair(models.Model):
    name = models.CharField(max_length= 50)
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    random_table_start = models.IntegerField(default="0", verbose_name="random_table_human_start")
    random_table_end = models.IntegerField(default="0", verbose_name="random_table_human_end")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Eyes(models.Model):
    name = models.CharField(max_length= 50)
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    random_table_start = models.IntegerField(default="0", verbose_name="random_table_human_start")
    random_table_end = models.IntegerField(default="0", verbose_name="random_table_human_end")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Skils(models.Model):
    name = models.CharField(max_length= 50, unique=True)
    characteristics = models.CharField(max_length= 3, default="")
    description = models.TextField(verbose_name="Description", default="")
    ref = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Talent(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField(verbose_name="Description", default="")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Character(models.Model):
    player = models.ForeignKey(Player, verbose_name="Player", on_delete=models.CASCADE)
    name = models.CharField(max_length= 50, verbose_name="Character name")
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    ch_class = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE, null=True)
    career = models.ForeignKey(Career, verbose_name="Career", on_delete=models.CASCADE, null=True)
    career_level = models.IntegerField(default="1", verbose_name="Career  Level")
    career_path = models.ForeignKey(CareerPath, verbose_name="CareerPath", on_delete=models.CASCADE, null=True)
    status = models.ForeignKey(Status, verbose_name="Status", on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default="1", verbose_name="Age")
    height = models.IntegerField(default="1", verbose_name="Age")
    hair = models.ForeignKey(Hair, verbose_name="Hair", on_delete=models.CASCADE, null=True)
    eyes = models.ForeignKey(Eyes, verbose_name="Eyes", on_delete=models.CASCADE, null=True)
    characteristics_ws_initial = models.IntegerField(default="0", verbose_name="ws_initial")
    characteristics_bs_initial = models.IntegerField(default="0", verbose_name="bs_initial")
    characteristics_s_initial = models.IntegerField(default="0", verbose_name="s_initial")
    characteristics_t_initial = models.IntegerField(default="0", verbose_name="t_initial")
    characteristics_i_initial = models.IntegerField(default="0", verbose_name="i_initial")
    characteristics_ag_initial = models.IntegerField(default="0", verbose_name="ag_initial")
    characteristics_dex_initial = models.IntegerField(default="0", verbose_name="dex_initial")
    characteristics_int_initial = models.IntegerField(default="0", verbose_name="int_initial")
    characteristics_wp_initial = models.IntegerField(default="0", verbose_name="wp_initial")
    characteristics_fel_initial = models.IntegerField(default="0", verbose_name="fel_initial")
    characteristics_ws_advances = models.IntegerField(default="0", verbose_name="ws_advances")
    characteristics_bs_advances = models.IntegerField(default="0", verbose_name="bs_advances")
    characteristics_s_advances = models.IntegerField(default="0", verbose_name="s_advances")
    characteristics_t_advances = models.IntegerField(default="0", verbose_name="t_advances")
    characteristics_i_advances = models.IntegerField(default="0", verbose_name="i_advances")
    characteristics_ag_advances = models.IntegerField(default="0", verbose_name="ag_advances")
    characteristics_dex_advances = models.IntegerField(default="0", verbose_name="dex_advances")
    characteristics_int_advances = models.IntegerField(default="0", verbose_name="int_advances")
    characteristics_wp_advances = models.IntegerField(default="0", verbose_name="wp_advances")
    characteristics_fel_advances = models.IntegerField(default="0", verbose_name="fel_advances")
    wounds = models.IntegerField(default="0", verbose_name="wounds")
    fate_fate = models.IntegerField(default="0", verbose_name="fate_fate")
    fate_fortune = models.IntegerField(default="0", verbose_name="fate_fortune")
    resilience_resilience = models.IntegerField(default="0", verbose_name="resilience_resilience")
    resilience_resolve = models.IntegerField(default="0", verbose_name="resilience_resolve")
    resilience_motivation = models.CharField(max_length= 50, verbose_name="Character Motivation")
    experience_current = models.IntegerField(default="0", verbose_name="experience_current")
    experience_spent = models.IntegerField(default="0", verbose_name="experience_spent")
    experience_total = models.IntegerField(default="0", verbose_name="experience_total")
    movement_movement = models.IntegerField(default="0", verbose_name="movement_movement")
    movement_walk = models.IntegerField(default="0", verbose_name="movement_walk")
    movement_run = models.IntegerField(default="0", verbose_name="movement_run")
    ambitions_shortterm = models.TextField(verbose_name="Shortterm", default="")
    ambitions_longterm = models.TextField(verbose_name="Longterm", default="")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Character2Skill(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skils, on_delete=models.CASCADE)
    adv = models.IntegerField(default="0", verbose_name="adv")

class RandomAttributesTable(models.Model):
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    weapon_skill = models.IntegerField(default="0", verbose_name="weapon_skill")
    ballistic_skill = models.IntegerField(default="0", verbose_name="ballistic_skill")
    strength = models.IntegerField(default="0", verbose_name="strength")
    toughness = models.IntegerField(default="0", verbose_name="toughness")
    initiative = models.IntegerField(default="0", verbose_name="initiative")
    agility = models.IntegerField(default="0", verbose_name="agility")
    dexterity = models.IntegerField(default="0", verbose_name="dexterity")
    intelligence = models.IntegerField(default="0", verbose_name="intelligence")
    willpower = models.IntegerField(default="0", verbose_name="willpower")
    fellowship = models.IntegerField(default="0", verbose_name="fellowship")
    fate = models.IntegerField(default="0", verbose_name="fate")
    resilience = models.IntegerField(default="0", verbose_name="resilience")
    extra_points = models.IntegerField(default="0", verbose_name="extra_points")
    movement = models.IntegerField(default="0", verbose_name="movement")

    def __str__(self):
        return u"{0}".format(self.species.name)

    def __unicode__(self):
        return u"{0}".format(self.species.name)