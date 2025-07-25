import math

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from WarhammerFantasyRoleplayVirtualGM_app.validators import validator_sex

def format_currency(p: int):
    GC = math.floor(p / 240)
    GC_left = p % 240
    SC = math.floor(GC_left / 12)
    SC_left = GC_left % 12
    BC = SC_left
    return f"{GC}GC {SC}/{BC}"

# Create your models here.

class Availability(models.TextChoices):
    COMMON = "Common", _('Common')
    SCARCE = "Scarce", _('Scarce')
    RARE = "Rare", _('Rare')
    EXOTIC = "Exotic", _('Exotic')


class RefBook(models.Model):
    name = models.CharField(max_length= 250)

    class Meta:
        ordering = ['name']

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

class Ambitions(models.Model):
    description = models.TextField(verbose_name="Description", default="")
    achieved = models.BooleanField(verbose_name="Status", default=False)

    def __str__(self):
        return u"{0}".format(self.description)

    def __unicode__(self):
        return u"{0}".format(self.description)

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

class Note(models.Model):
    datetime_create = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Create Time")
    datetime_update = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name="Update Time")
    note_text = models.TextField(verbose_name="Note Text", default="", blank=False, null=False)
    author = models.ForeignKey(User, verbose_name='User', blank=True, null=True, on_delete=models.CASCADE)
    class Meta:
        ordering = ['-datetime_update']

    def __str__(self):
        return u"{0}".format(self.datetime_create)

    def __unicode__(self):
        return u"{0}".format(self.datetime_create)

    @property
    def timestamp(self):
        return self.datetime_create.strftime('%Y%m%d%H%M%S')

    @property
    def formated_datatime(self):
        return self.datetime_create.strftime('%Y-%m-%d %H:%M')

    @property
    def user_name(self):
        if self.author == None:
            return "--"
        return u"{0} \"{1}\" {2}".format(self.author.first_name, self.author.username, self.author.last_name)

    def to_dict(self):
        return {"id": self.id, "datetime_create": self.formated_datatime , "timestamp": self.timestamp, "note_text":self.note_text, "author":self.user_name}

class Campaign(models.Model):
    name = models.CharField(max_length= 250)
    party_name = models.CharField(max_length= 250, default="")
    ambitions_shortterm = models.ManyToManyField(Ambitions, verbose_name="Shortterm Ambitions", related_name="campaign_ambitions_shortterm")
    ambitions_longterm = models.ManyToManyField(Ambitions, verbose_name="Longterm Ambitions", related_name="campaign_ambitions_longterm")
    notes =  models.ManyToManyField(Note, verbose_name="Notes", blank=True)

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

    def serialize(self):
        return {"name": self.name,
                "characteristics": self.characteristics,
                "description": self.description,
                "ref": str(self.ref),
                }

class Talent(models.Model):
    name = models.CharField(max_length= 50)
    max =  models.CharField(max_length= 50, default="")
    tests = models.CharField(max_length= 50, default="", blank=True, null=True)
    description = models.TextField(verbose_name="Description", default="")
    ref = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)
    talent_parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    @property
    def my_talent_id(self):
        return self.id

    def to_dict(self):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

    def get_absolute_url(self):
        return reverse("TalentsListView")

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
            "tests": self.tests,
            "ref": str(self.ref),
        }

class Trapping(models.Model):
    name = models.CharField(max_length= 50, unique=True)
    description = models.TextField(verbose_name="Description", default="")
    encumbrance = models.IntegerField(default=1, verbose_name="Encumbrance")
    price = models.IntegerField(default=0, verbose_name="Price")
    availability = models.CharField(max_length=6, choices=Availability.choices, default=Availability.COMMON, verbose_name="Availability")
    to_view = models.BooleanField(default=True, verbose_name="To View")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("TrappingsListView")

    def serialize(self):
        return {
            "name": self.name,
            "description": self.description,
        }

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

    class Meta:
        ordering = ['name']

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

    def to_dict(self):
        data = {"id":self.id, "name":self.name, "carrer":{}}
        for c in Career.objects.filter(ch_class=self):
            data['carrer'][c.id] = c.to_dict()
        return data

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
    random_table_wood_ogre_start = models.IntegerField(default="0", verbose_name="random_table_wood_ogre_start")
    random_table_wood_ogre_end = models.IntegerField(default="0", verbose_name="random_table_wood_ogre_end")


    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self):
        data = {"id": self.id, "name":self.name, "careersAdvanceScheme":{} }
        for cas in CareersAdvanceScheme.objects.filter(career=self):
            data['careersAdvanceScheme'][cas.id] = cas.serialize()
        return data

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
                'tier': self.status.tier if self.status is not None else "-",
                'level': self.status.level if self.status is not None else "-",
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

    def to_dict(self):
        return {'id':self.id, 'name':self.name}

class Eyes(models.Model):
    name = models.CharField(max_length= 50)
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    random_table_start = models.IntegerField(default="0", verbose_name="random_table_human_start")
    random_table_end = models.IntegerField(default="0", verbose_name="random_table_human_end")

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self):
        return {'id':self.id, 'name':self.name}

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

    def to_dict(self, is_in_inventory=False):
        opts = self._meta
        data = {}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        loc = []
        for l in self.locations.all():
            loc.append(l)
        data['locations'] = self.armour_locations
        data['is_in_inventory'] = is_in_inventory
        return data

    @property
    def armour_locations(self):
        loc = []
        for l in self.locations.all():
            loc.append(str(l))
        out = ", ".join(loc)
        return out


    @property
    def price_formated(self):
        return format_currency(self.price)

class WeaponQualities(models.Model):
    class WeaponQualitiesTypes(models.TextChoices):
        QUALITIES = 'Qualities', _('QUALITIES')
        FLAWS = 'Flaws', _('FLAWS')
    name = models.CharField(max_length= 50, verbose_name="Name")
    type = models.CharField(max_length=14, choices=WeaponQualitiesTypes.choices, default=WeaponQualitiesTypes.QUALITIES, verbose_name="Type")
    description = models.TextField(verbose_name="Description", default="")
    ref = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

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
    qualities_and_flaws = models.CharField(max_length= 250, default="-", blank=True, verbose_name="Notes")
    qualities = models.ManyToManyField(WeaponQualities, verbose_name="Qualities & Flaws", blank=True,)
    reference = models.ForeignKey(Reference, default=None, blank=True, null=True, on_delete=models.SET(None))

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self, is_in_inventory=False):
        opts = self._meta
        data = {'is_in_inventory': is_in_inventory}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        data['reach_range'] = self.reach_range
        data["qualities"] = []
        for q in self.qualities.all():
            data["qualities"].append({"id":q.id, "name": q.name, "description": q.description, "ref": str(q.ref)})
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
        SHORT = 'SHORT', _('Short')
        VARIES = 'VARIES', _('Varies')
        VERY_LONG = 'VERY_LONG', _('Very Long')
        VERY_SHORT = 'VERY_SHORT', _('Very Short')
    reach = models.CharField(max_length=14, choices=Reach.choices, default=Reach.VERY_SHORT, verbose_name="Reach")

    @property
    def reach_range(self):
        return self.reach

    def get_absolute_url(self):
        return reverse("MeleWeaponListView")

    def to_dict(self, is_in_inventory=False, quantity=0):
        data = super().to_dict(is_in_inventory)
        data['is_range'] = False
        data['quantity'] = "N/A"
        return data

class RangedWeapon(Weapon):
    range = models.IntegerField(default=0, verbose_name="Range")

    @property
    def reach_range(self):
        return self.range

    def get_absolute_url(self):
        return reverse("RangedWeaponListView")

    def to_dict(self, is_in_inventory=False, quantity=0):
        data = super().to_dict(is_in_inventory)
        data['is_range'] = True
        data['quantity'] = quantity
        return data

class Spells(models.Model):
    class SpellList(models.TextChoices):
        PETTY_SPELLS            = 'PETTY_SPELLS'               ,_('Petty Spells')
        ARCANE_SPELLS           = 'ARCANE_SPELLS'              ,_('Arcane Spells')
        THE_LORE_OF_BEASTS      = 'THE_LORE_OF_BEASTS'         ,_('The Lore of Beasts')
        THE_LORE_OF_DEATH       = 'THE_LORE_OF_DEATH'          ,_('The Lore of Death')
        THE_LORE_OF_FIRE        = 'THE_LORE_OF_FIRE'           ,_('The Lore of Fire')
        THE_LORE_OF_HEAVENS     = 'THE_LORE_OF_HEAVENS'        ,_('The Lore of Heavens')
        THE_LORE_OF_METAL       = 'THE_LORE_OF_METAL'          ,_('The Lore of Metal')
        THE_LORE_OF_LIFE        = 'THE_LORE_OF_LIFE'           ,_('The Lore of Life')
        THE_LORE_OF_LIGHT       = 'THE_LORE_OF_LIGHT'          ,_('The Lore of Light')
        THE_LORE_OF_SHADOWS     = 'THE_LORE_OF_SHADOWS'        ,_('The Lore of Shadows')
        THE_LORE_OF_HEDGECRAFT  = 'THE_LORE_OF_HEDGECRAFT'     ,_('The Lore of Hedgecraft')
        THE_LORE_OF_WITCHCRAFT  = 'THE_LORE_OF_WITCHCRAFT'     ,_('The Lore of Witchcraft')
        THE_LORE_OF_DAEMONOLOGY = 'THE_LORE_OF_DAEMONOLOGY'    ,_('The Lore of Daemonology')
        THE_LORE_OF_NECROMANCY  = 'THE_LORE_OF_NECROMANCY'     ,_('Lore of Necromancy')
        THE_LORE_OF_NURGLE      = 'THE_LORE_OF_NURGLE'         ,_('The Lore of Nurgle')
        THE_LORE_OF_SLAANESH    = 'THE_LORE_OF_SLAANESH'       ,_('The Lore of Slaanesh')
        THE_LORE_OF_TZEENTCH    = 'THE_LORE_OF_TZEENTCH'       ,_('The Lore of Tzeentch')
        BLESSINGS               = 'BLESSINGS'                  ,_('Blessings')
        MIRACLES_OF_MANANN      = 'MIRACLES_OF_MANANN'         ,_('Miracles of Manann')
        MIRACLES_OF_MORR        = 'MIRACLES_OF_MORR'           ,_('Miracles of Morr')
        MIRACLES_OF_MYRMIDIA    = 'MIRACLES_OF_MYRMIDIA'       ,_('Miracles of Myrmidia')
        MIRACLES_OF_RANALD      = 'MIRACLES_OF_RANALD'         ,_('Miracles of Ranald')
        MIRACLES_OF_RHYA        = 'MIRACLES_OF_RHYA'           ,_('Miracles of Rhya')
        MIRACLES_OF_SHALLYA     = 'MIRACLES_OF_SHALLYA'        ,_('Miracles of Shallya')
        MIRACLES_OF_SIGMAR      = 'MIRACLES_OF_SIGMAR'         ,_('Miracles of Sigmar')
        MIRACLES_OF_TAAL        = 'MIRACLES_OF_TAAL'           ,_('Miracles of Taal')
        MIRACLES_OF_ULRIC       = 'MIRACLES_OF_ULRIC'          ,_('Miracles of Ulric')
        MIRACLES_OF_VERENA      = 'MIRACLES_OF_VERENA'         ,_('Miracles of Verena')
        MIRACLES_OF_BYLORAK     = 'MIRACLES_OF_BYLORAK'        ,_('Miracles of Bylorak')

    name = models.CharField(max_length= 50, verbose_name="Name")
    spellLists = models.CharField(max_length=23, choices=SpellList.choices, default=SpellList.PETTY_SPELLS, verbose_name="Spell List")
    cn = models.IntegerField(default=0, verbose_name="cn")
    range = models.CharField(max_length= 50, verbose_name="Range")
    target  = models.CharField(max_length= 50, verbose_name="Target")
    duration  = models.CharField(max_length= 50, verbose_name="Duration")
    effect = models.TextField(verbose_name="Effect", default="")

    class Meta:
        ordering = ['spellLists', 'name']

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def to_dict(self, is_in_inventory=False):
        opts = self._meta
        data = {'is_in_inventory': is_in_inventory}
        for f in opts.concrete_fields:
            data[f.name] = f.value_from_object(self)
        return data

    def get_absolute_url(self):
        return reverse("SpellListView")

    def serialize(self):
        return {
            "name": self.name,
            "spellLists": self.spellLists,
            "cn": self.cn,
            "range": self.range,
            "target": self.target,
            "duration": self.duration,
            "effect": self.effect
        }

class Character(models.Model):
    player = models.ForeignKey(Player, verbose_name="Player", on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, verbose_name="Campaign", on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length= 50, verbose_name="Character name")
    species = models.ForeignKey(Species, verbose_name="Species", on_delete=models.CASCADE, null=True)
    ch_class = models.ForeignKey(Class, verbose_name="Class", on_delete=models.CASCADE, null=True)
    career = models.ForeignKey(Career, verbose_name="Career", on_delete=models.CASCADE, null=True)
    career_level = models.IntegerField(default="1", verbose_name="Career  Level")
    career_path = models.ManyToManyField(CareerPath, verbose_name="CareerPath", through="Character2CareerPath")
    status = models.ForeignKey(Status, verbose_name="Status", on_delete=models.CASCADE, null=True)
    age = models.IntegerField(default="1", verbose_name="Age")
    height = models.IntegerField(default="1", verbose_name="Height")
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
    current_wounds = models.IntegerField(default="0", verbose_name="Current Wounds")
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
    ambitions_shortterm = models.ManyToManyField(Ambitions, verbose_name="Shortterm Ambitions", related_name="character_ambitions_shortterm")
    ambitions_longterm = models.ManyToManyField(Ambitions, verbose_name="Longterm Ambitions", related_name="character_ambitions_longterm")
    armour = models.ManyToManyField(Armour, verbose_name="Armour")
    weapons_with_quantity = models.ManyToManyField(Weapon, through="Character2Weapon", related_name="characters_with_quantity", verbose_name="Weapons (with quantity)")
    spells = models.ManyToManyField(Spells, verbose_name="Spells", blank=True)
    wealth = models.IntegerField(default=0, verbose_name="Wealth")
    notes =  models.ManyToManyField(Note, verbose_name="Notes", blank=True)
    hash_id = models.CharField(max_length=29, verbose_name="Hash ID", default="")
    deleted = models.BooleanField(default=False, verbose_name="Is delated")
    psychology = models.TextField(verbose_name="Psychology", default="", blank=False, null=False)
    coruption_and_mutation = models.TextField(verbose_name="Coruption & Mutation", default="", blank=False, null=False)


    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

class Character2Weapon(models.Model):
    character = models.ForeignKey('Character', on_delete=models.CASCADE)
    weapon = models.ForeignKey('Weapon', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.character.name} - {self.weapon.name} x{self.quantity}"

class Character2CareerPath(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    career_path = models.ForeignKey(CareerPath, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return u"{0} -> {1}".format(self.character, self.career_path)

    def __unicode__(self):
        return u"{0} -> {1}".format(self.character, self.career_path)

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


class CharacterChangeLog(models.Model):
    datetime_create = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="Create Time")
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, verbose_name='Character', on_delete=models.CASCADE)
    log = models.TextField(verbose_name="Log", default="", blank=False, null=False)

    def __str__(self):
        return u"{0} -> {1}; {2}; {3}".format(self.datetime_create, self.user, self.character, self.log)

    def __unicode__(self):
        return u"{0} -> {1}; {2}; {3}".format(self.datetime_create, self.user, self.character, self.log)

    @property
    def formated_datatime(self):
        return self.datetime_create.strftime('%Y-%m-%d %H:%M')

    @property
    def timestamp(self):
        return self.datetime_create.strftime('%Y%m%d%H%M%S')

    @property
    def user_name(self):
        return u"{0} \"{1}\" {2}".format(self.user.first_name, self.user.username, self.user.last_name)

    def to_dict(self):
        return {"id": self.id, "datetime_create": self.formated_datatime, 'timestamp':self.timestamp , "user": self.user_name, "log":self.log}

def createCharacterLog(u:User, c:Character, l:str):
    ccl =CharacterChangeLog.objects.create(user=u, character=c,log=l)
    ccl.save()

class Containers(models.Model):
    name = models.CharField(max_length= 50)
    encumbrance = models.IntegerField(default=0, verbose_name="Encumbrance")
    carries = models.IntegerField(default=0, verbose_name="Carries")
    price = models.IntegerField(default=0, verbose_name="Price")
    availability = models.CharField(max_length=6, choices=Availability.choices, default=Availability.COMMON, verbose_name="Availability")
    trapping = models.ForeignKey(Trapping, on_delete=models.CASCADE)


    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)

    def get_absolute_url(self):
        return reverse("ContainersListView")

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'carries': self.carries, 'encumbrance': self.encumbrance}

class Character2Container(models.Model):
    character = models.ForeignKey(Character, verbose_name='Character', on_delete=models.CASCADE)
    container = models.ForeignKey(Containers, verbose_name='Container', on_delete=models.CASCADE)

    def __str__(self):
        return f"[{self.id}]{self.character} -> {self.container}"

    def __unicode__(self):
        return f"[{self.id}]{self.character} -> {self.container}"

    def to_dict(self):
        return {'Character2Container_id': self.id, 'container': self.container.to_dict()}

class Character2Trapping(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    trapping = models.ForeignKey(Trapping, on_delete=models.CASCADE)
    container = models.ForeignKey(Character2Container, null=True, blank=True,  on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, verbose_name="Quantity")


    class Meta:
        unique_together = ('characters', 'trapping',)

    def __str__(self):
        return f"{self.id}; {self.characters} -> {self.trapping}; {self.container}"

    def __unicode__(self):
        return f"{self.id}; {self.characters} -> {self.trapping}; {self.container}"

class Condition(models.Model):
    name = models.CharField(max_length= 50)
    description = models.TextField(verbose_name="Description", default="")

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}"

class Condition2Character(models.Model):
    characters = models.ForeignKey(Character, on_delete=models.CASCADE)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    occurrence = models.IntegerField(default=0, verbose_name="Occurrence")

    def __str__(self):
        return f"{self.characters.name} -> {self.condition.name}"

    def __unicode__(self):
        return f"{self.characters.name} -> {self.condition.name}"

    def to_dict(self):
        return {'Condition2Character_id': self.id, 'condition': self.condition.id, 'occurrence': self.occurrence}