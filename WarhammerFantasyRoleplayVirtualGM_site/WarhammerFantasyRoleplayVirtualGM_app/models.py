from django.db import models
from django.contrib.auth.models import User
from WarhammerFantasyRoleplayVirtualGM_app.validators import validator_sex
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

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
    skils_parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

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
    talent_parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

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
    encumbrance = models.IntegerField(default=1, verbose_name="Encumbrance")

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

class Status(models.Model):
    class Tier(models.TextChoices):
        NONE= "NONE", _("NONE")
        BRASS = "Brass", _("Brass")
        SILVER = "Silver", _("Silver")
        GOLD = "Gold", _("Gold")
    tier = models.CharField(max_length=6, choices=Tier.choices, default=Tier.NONE, verbose_name="Tier")
    level = models.IntegerField(default="0", verbose_name="Status Level")

    class Meta:
        unique_together = ('tier', 'level',)

    def __str__(self):
        return u"{0} {1}".format(self.tier, self.level)

    def __unicode__(self):
        return u"{0} {1}".format(self.tier, self.level)

class CareerPath(models.Model):
    name = models.CharField(max_length= 50)
    skills = models.ManyToManyField(Skils)
    talents = models.ManyToManyField(Talent)
    trappings = models.ManyToManyField(Trapping)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Status', null=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def serialize(self):
        out = {
            'name': self.name,
            'skills': [],
            'talents': [],
            'trappings': [],
            'status': {
                'tier': self.status.tier,
                'level': self.status.level,
            }
        }
        for s in self.skills.all():
            out['skills'].append(s.id)
        for s in self.talents.all():
            out['talents'].append(s.id)
        for s in self.trappings.all():
            out['trappings'].append(s.id)
        return out

class CareersAdvanceScheme(models.Model):
    class Marked(models.TextChoices):
        NONE = "NO", _(' ')
        CROSS = 'CR', _('CROSS')
        HALBERD = 'HA', _('HALBERD')
        SKULL = 'SK', _('SKULL')
        SHIELD = 'SH', _('SHIELD')
    class Meta:
        ordering = ['career']
    career = models.ForeignKey(Career, verbose_name="Career", on_delete=models.CASCADE)
    characteristics_ws_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Weapon Skill")
    characteristics_bs_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Ballistic Skill")
    characteristics_s_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Strength")
    characteristics_t_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Toughness")
    characteristics_i_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Initiative")
    characteristics_ag_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Agility")
    characteristics_dex_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Dexterity")
    characteristics_int_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Intelligence")
    characteristics_wp_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Willpower")
    characteristics_fel_initial = models.CharField(max_length=2, choices=Marked.choices, default=Marked.NONE, verbose_name="Fellowship")
    advances_level_1 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_1')
    advances_level_2 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_2')
    advances_level_3 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_3')
    advances_level_4 = models.ForeignKey(CareerPath, on_delete=models.CASCADE, related_name='advances_level_4')

    def __str__(self):
        return u"{0} Advance Scheme".format(self.career.name)

    def __unicode__(self):
        return u"{0} Advance Scheme".format(self.career.name)

    def serialize(self):
        out = {
            'characteristics_ws_initial': self.characteristics_ws_initial,
            'characteristics_bs_initial': self.characteristics_bs_initial,
            'characteristics_s_initial': self.characteristics_s_initial,
            'characteristics_t_initial': self.characteristics_t_initial,
            'characteristics_i_initial': self.characteristics_i_initial,
            'characteristics_ag_initial': self.characteristics_ag_initial,
            'characteristics_dex_initial': self.characteristics_dex_initial,
            'characteristics_int_initial': self.characteristics_int_initial,
            'characteristics_wp_initial': self.characteristics_wp_initial,
            'characteristics_fel_initial': self.characteristics_fel_initial,
            'advances_level' : { '1': self.advances_level_1.serialize(),
                                 '2': self.advances_level_2.serialize(),
                                 '3': self.advances_level_3.serialize(),
                                 '4': self.advances_level_4.serialize(),
            }
        }
        return out

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

class Availability(models.TextChoices):
    COMMON = "Common", _('Common')
    SCARCE = "Scarce", _('Scarce')
    RARE = "Rare", _('Rare')

class ArmourLocations(models.Model):
    name = models.CharField(max_length= 50, verbose_name="Name")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Armour(models.Model):
    class ArmourType(models.TextChoices):
        SOFT_LEATHER = 'SOFT LEATHER', _('SOFT LEATHER')
        BOILED_LEATHER = 'BOILED LEATHER', _('BOILED LEATHER')
        MAIL = 'MAIL', _('MAIL')
        PLATE = 'PLATE', _('PLATE')
    name = models.CharField(max_length= 50, verbose_name="Name")
    armour_type = models.CharField(max_length=14, choices=ArmourType.choices, default=ArmourType.SOFT_LEATHER, verbose_name="Armour Type")
    price = models.IntegerField(default=0, verbose_name="Price")
    encumbrance = models.IntegerField(default=1, verbose_name="Encumbrance")
    availability = models.CharField(max_length=6, choices=Availability.choices, default=Availability.COMMON, verbose_name="Availability")
    penalty = models.CharField(max_length= 250, default="-", verbose_name="Penalty")
    locations = models.ManyToManyField(ArmourLocations, verbose_name="Locations")
    armour_points = models.IntegerField(default=1, verbose_name="Armour Points")
    qualities_and_flaws = models.CharField(max_length= 250, default="-", verbose_name="Qualities & Flaws")
    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        loc = []
        for l in self.locations.all():
            loc.append(l)
        data['locations'] = self.armour_locations
        return data

    @property
    def armour_locations(self):
        loc = []
        for l in self.locations.all():
            loc.append(str(l))
        out = ", ".join(loc)
        return out

class Weapon(models.Model):
    class WeaponGroup(models.TextChoices):
        BASIC = 'BASIC', _('BASIC')
        BLACKPOWDER = 'BLACKPOWDER', _('BLACKPOWDER')
        BOW = 'BOW', _('BOW')
        BRAWLING = 'BRAWLING', _('BRAWLING')
        CAVALRY = 'CAVALRY', _('CAVALRY')
        CROSSBOW = 'CROSSBOW', _('CROSSBOW')
        ENGINEERING = 'ENGINEERING', _('ENGINEERING')
        ENTANGLING = 'ENTANGLING', _('ENTANGLING')
        EXPLOSIVES = 'EXPLOSIVES', _('EXPLOSIVES')
        FENCING = 'FENCING', _('FENCING')
        FLAIL = 'FLAIL', _('FLAIL')
        PARRY  = 'PARRY', _('PARRY')
        POLEARM = 'POLEARM', _('POLEARM')
        SLING = 'SLING', _('SLING')
        THROWING = 'THROWING', _('THROWING')
        TWOHANDED = 'TWO-HANDED', _('TWO-HANDED')
    name = models.CharField(max_length= 50, verbose_name="Name")
    weapon_group = models.CharField(max_length=14, choices=WeaponGroup.choices, default=WeaponGroup.BASIC, verbose_name="Weapon Group")
    price = models.IntegerField(default=0, verbose_name="Price")
    encumbrance = models.IntegerField(default=1, verbose_name="Encumbrance")
    availability = models.CharField(max_length=6, choices=Availability.choices, default=Availability.COMMON, verbose_name="Availability")
    damage = models.IntegerField(default=0, verbose_name="Damage")
    qualities_and_flaws = models.CharField(max_length= 250, default="-", verbose_name="Qualities & Flaws")
    reference = models.ForeignKey(Reference, default=None, blank=True, null=True, on_delete=models.SET(None))

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        data['reach_range'] = self.reach_range
        return data

    @property
    def reach_range(self):
        raise NotImplementedError("reach_range not implemented in Weapon class")

class MeleeWeapons(Weapon):
    class Reach(models.TextChoices):
        AVERAGE = 'AVERAGE', _('Average')
        LONG = 'LONG', _('Long')
        MASSIVE = 'MASSIVE', _('Massive')
        MEDIUM = 'MEDIUM', _('Medium')
        PERSONAL = 'PERSONAL', _('Personal')
        VARIES = 'VARIES', _('Varies')
        VERY_LONG = 'VERY_LONG', _('Very_Long')
        VERY_SHORT = 'VERY_SHORT', _('Very Short')
    reach = models.CharField(max_length=14, choices=Reach.choices, default=Reach.VERY_SHORT, verbose_name="Reach")

    @property
    def reach_range(self):
        return self.reach

    def get_absolute_url(self):
        return reverse("MeleWeaponListView")


class RangedWeapon(Weapon):
    range = models.IntegerField(default=0, verbose_name="Range")

    @property
    def reach_range(self):
        return self.range

    def get_absolute_url(self):
        return reverse("RangedWeaponListView")

class Spells(models.Model):
    class SpellList(models.TextChoices):
        PETTY_SPELLS            = 'PETTY_SPELLS',               _('Petty Spells')
        ARCANE_SPELLS           = 'ARCANE_SPELLS',              _('Arcane Spells')
        THE_LORE_OF_BEASTS      = 'THE_LORE_OF_BEASTS',         _('The Lore of Beasts')
        THE_LORE_OF_DEATH       = 'THE_LORE_OF_DEATH',          _('The Lore of Death')
        THE_LORE_OF_FIRE        = 'THE_LORE_OF_FIRE',           _('The Lore of Fire')
        THE_LORE_OF_HEAVENS     = 'THE_LORE_OF_HEAVENS',        _('The Lore of Heavens')
        THE_LORE_OF_METAL       = 'THE_LORE_OF_METAL',          _('The Lore of Metal')
        THE_LORE_OF_LIFE        = 'THE_LORE_OF_LIFE',           _('The Lore of Life')
        THE_LORE_OF_LIGHT       = 'THE_LORE_OF_LIGHT',          _('The Lore of Light')
        THE_LORE_OF_SHADOWS     = 'THE_LORE_OF_SHADOWS',        _('The Lore of Shadows')
        THE_LORE_OF_HEDGECRAFT  = 'THE_LORE_OF_HEDGECRAFT',     _('The Lore of Hedgecraft')
        THE_LORE_OF_WITCHCRAFT  = 'THE_LORE_OF_WITCHCRAFT',     _('The Lore of Witchcraft')
        THE_LORE_OF_DAEMONOLOGY = 'THE_LORE_OF_DAEMONOLOGY',    _('The Lore of Daemonology')
        THE_LORE_OF_NECROMANCY  = 'THE_LORE_OF_NECROMANCY',     _('Lore of Necromancy')
        THE_LORE_OF_NURGLE      = 'THE_LORE_OF_NURGLE',         _('The Lore of Nurgle')
        THE_LORE_OF_SLAANESH    = 'THE_LORE_OF_SLAANESH',       _('The Lore of Slaanesh')
        THE_LORE_OF_TZEENTCH    = 'THE_LORE_OF_TZEENTCH',       _('The Lore of Tzeentch')
    name = models.CharField(max_length= 50, verbose_name="Name")
    spellLists = models.CharField(max_length=23, choices=SpellList.choices, default=SpellList.PETTY_SPELLS, verbose_name="Spell List")
    cn = models.IntegerField(default=0, verbose_name="cn")
    range = models.CharField(max_length= 50, verbose_name="Range")
    target  = models.CharField(max_length= 50, verbose_name="Target")
    duration  = models.CharField(max_length= 50, verbose_name="Duration")
    effect = models.TextField(verbose_name="Effect", default="")

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

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
    movement_movement = models.IntegerField(default="0", verbose_name="movement_movement")
    movement_walk = models.IntegerField(default="0", verbose_name="movement_walk")
    movement_run = models.IntegerField(default="0", verbose_name="movement_run")
    ambitions_shortterm = models.TextField(verbose_name="Shortterm", default="")
    ambitions_longterm = models.TextField(verbose_name="Longterm", default="")
    armour = models.ManyToManyField(Armour, verbose_name="Armour")
    weapon = models.ManyToManyField(Weapon, verbose_name="Weapon")
    spells = models.ManyToManyField(Spells, verbose_name="Spells")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Character2Trappingl(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    trapping = models.ForeignKey(Trapping, on_delete=models.CASCADE)
    enc = models.IntegerField(default="0", verbose_name="enc")
    is_basic_skill = models.BooleanField(default=False)
    is_species_skill = models.BooleanField(default=False)
    is_career_skill = models.BooleanField(default=False)

    class Meta:
        unique_together = ('characters', 'trapping',)

class Character2Skill(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    skills = models.ForeignKey(Skils, on_delete=models.CASCADE)
    adv = models.IntegerField(default="0", verbose_name="adv")
    is_basic_skill = models.BooleanField(default=False)
    is_species_skill = models.BooleanField(default=False)
    is_career_skill = models.BooleanField(default=False)

    class Meta:
        unique_together = ('characters', 'skills',)

class Character2Talent(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    taken = models.IntegerField(default="0", verbose_name="Taken")
    is_basic_skill = models.BooleanField(default=False)
    is_species_skill = models.BooleanField(default=False)
    is_career_skill = models.BooleanField(default=False)
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

class ClassTrappings(models.Model):
    ch_class = models.ForeignKey(Class, verbose_name="Class", default="1", on_delete=models.CASCADE)
    trapping = models.ForeignKey(Trapping, verbose_name="Trapping", default="1", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('ch_class', 'trapping',)

    def __str__(self):
        return u"{0} - {1}".format(self.ch_class.name, self.trapping.name)

    def __unicode__(self):
        return u"{0} - {1}".format(self.ch_class.name, self.trapping.name)

class ImprovementXPCosts(models.Model):
    advances_interval_start = models.IntegerField(default="0", verbose_name="Advances Interval Start")
    advances_interval_end = models.IntegerField(default="0", verbose_name="Advances Interval End")
    characteristics_xp_cost = models.IntegerField(default="0", verbose_name="Characteristics xp cost")
    skills_xp_cost = models.IntegerField(default="0", verbose_name="Skills Xp Cost")

    def __str__(self):
        return u"{0} -> {1}; {2}; {3}".format(self.advances_interval_start, self.advances_interval_end, self.characteristics_xp_cost, self.skills_xp_cost)

    def __unicode__(self):
        return u"{0} -> {1}; {2}; {3}".format(self.advances_interval_start, self.advances_interval_end, self.characteristics_xp_cost, self.skills_xp_cost)

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data