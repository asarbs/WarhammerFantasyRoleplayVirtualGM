from django.db import models
from django.contrib.auth.models import User
from WarhammerFantasyRoleplayVirtualGM_app.validators import validator_sex
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RefBook(models.Model):
    name = models.CharField(max_length= 250)
    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Reference(models.Model):
    class Meta:
        ordering = ['refBook', 'page']

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
    max =  models.CharField(max_length= 50, default="")
    tests = models.CharField(max_length= 50, default="", blank=True, null=True)
    description = models.TextField(verbose_name="Description", default="")
    ref = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    @property
    def my_talent_id(self):
        return self.id

class Trapping(models.Model):
    name = models.CharField(max_length= 50, unique=True)
    description = models.TextField(verbose_name="Description", default="")

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
    random_interal_end = models.IntegerField(default=0, verbose_name="random_interal_end")
    skills = models.ManyToManyField(Skils)
    talents = models.ManyToManyField(Talent)

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

class CareerPath(models.Model):
    name = models.CharField(max_length= 50)
    skills = models.ManyToManyField(Skils)
    talents = models.ManyToManyField(Talent)
    trappings = models.ManyToManyField(Trapping)
    earning_money = models.CharField(max_length= 50, verbose_name="Earning Money", default="default")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)


class CareersAdvanceScheme(models.Model):
    class Marked(models.TextChoices):
        NONE = "NO", _('NONE')
        CROSS = 'CR', _('CROSS')
        HALBERD = 'HA', _('HALBERD')
        SKULL = 'SK', _('SKULL')
        SHIELD = 'SH', _('SHIELD')
    class Meta:
        ordering = ['career']
    career = models.ForeignKey(Career, verbose_name="Career", on_delete=models.CASCADE)
    characteristics_ws_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_bs_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_s_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_t_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_i_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_ag_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_dex_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_int_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_wp_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    characteristics_fel_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE)
    advances_level_1 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_1')
    advances_level_2 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_2')
    advances_level_3 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_3')
    advances_level_4 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_4')

    def __str__(self):
        return u"{0} Advance Scheme".format(self.career.name)

    def __unicode__(self):
        return u"{0} Advance Scheme".format(self.career.name)

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
    class SkillType(models.TextChoices):
        BASIC_SKILL = 'BS', _('BASIC SKILL')
        NORMAL_SKILL = 'NS', _('NORMAL SKILL')
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skils, on_delete=models.CASCADE)
    adv = models.IntegerField(default="0", verbose_name="adv")
    type = models.CharField(max_length=2, choices=SkillType.choices, default=SkillType.BASIC_SKILL)
    class Meta:
        unique_together = ('characters', 'skills',)

class Character2Talent(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    taken = models.IntegerField(default="0", verbose_name="adv")
    class Meta:
        unique_together = ('characters', 'talent',)


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

class RandomTalentsTable(models.Model):
    talent = models.ForeignKey(Talent, verbose_name="Talent", on_delete=models.CASCADE, null=True)
    random_interal_start = models.IntegerField(default=0, verbose_name="random_interal_start")
    random_interal_end = models.IntegerField(default=0, verbose_name="random_interal_end")
    any = models.BooleanField(default=False, verbose_name="Any")

    def __str__(self):
        return u"{0}".format(self.talent.name)

    def __unicode__(self):
        return u"{0}".format(self.talent.name)

    @property
    def name(self):
        return self.talent.name

    @property
    def max(self):
        return self.talent.max

    @property
    def tests(self):
        return self.talent.tests

    @property
    def description(self):
        return self.talent.description

    @property
    def ref(self):
        return self.talent.ref

    @property
    def my_talent_id(self):
        return self.talent.id