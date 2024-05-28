from django.db import models

from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import Skils
from WarhammerFantasyRoleplayVirtualGM_app.models import Spells
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import Weapon
from WarhammerFantasyRoleplayVirtualGM_app.models import Trapping
from WarhammerFantasyRoleplayVirtualGM_app.models import Reference


# Create your models here.

class CreatureTraits(models.Model):
    name = models.CharField(max_length= 50, unique=True)
    description = models.TextField(verbose_name="Description", default="")
    ref = models.ForeignKey(Reference, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"

    def __unicode__(self):
        return f"{self.name}"
    
    def serialize(self):
        data = {
            "name": self.name,
            "description": self.description,
            "ref": str(self.ref),
        }
        return data

class NPC(models.Model):
    name = models.CharField(max_length=150, verbose_name="Name")
    species = models.ForeignKey(Species, verbose_name="Species", related_name="npc_species", on_delete=models.CASCADE, null=True, blank=True)
    portrait = models.ImageField(upload_to='npc', null=True, default="static/page_images/default.png")
    characteristics_m = models.IntegerField(default="0", verbose_name="Move")
    characteristics_ws = models.IntegerField(default="0", verbose_name="Weapon Skill")
    characteristics_bs = models.IntegerField(default="0", verbose_name="Ballistic Skill")
    characteristics_s = models.IntegerField(default="0", verbose_name="Strength")
    characteristics_t = models.IntegerField(default="0", verbose_name="Toughness")
    characteristics_i = models.IntegerField(default="0", verbose_name="Initiative")
    characteristics_ag = models.IntegerField(default="0", verbose_name="Agility")
    characteristics_dex = models.IntegerField(default="0", verbose_name="Dexterity")
    characteristics_int = models.IntegerField(default="0", verbose_name="Intelligence")
    characteristics_wp = models.IntegerField(default="0", verbose_name="Willpower")
    characteristics_fel = models.IntegerField(default="0", verbose_name="Fellowship")
    characteristics_w = models.IntegerField(default="0", verbose_name="Wounds")
    skills = models.ManyToManyField(Skils, through="NPC2Skill", blank=True)
    talents = models.ManyToManyField(Talent, through="NPC2Talent", blank=True)
    weapons = models.ManyToManyField(Weapon, verbose_name="Weapon", blank=True)
    trappings = models.ManyToManyField(Trapping, through="NPC2Trapping", blank=True)
    creatureTraits = models.ManyToManyField(CreatureTraits, through="NPC2CreatureTraits", blank=True)
    spells = models.ManyToManyField(Spells, through="NPC2Spells", blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class NPC2Skill(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skils, on_delete=models.CASCADE)
    value = models.CharField(max_length=150, verbose_name="Value", blank=True, null=True)

    class Meta:
        ordering = ['skill']

    def __str__(self):
        return f"Skill: {self.npc} -> {self.skill} [{self.value}]"

    def __unicode__(self):
        return f"Skill: {self.npc} -> {self.skill} [{self.value}]"

class NPC2Talent(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    value = models.CharField(max_length=150, verbose_name="Value", blank=True, null=True)

    class Meta:
        ordering = ['talent']

    def __str__(self):
        return f"Tallent: {self.npc} -> {self.talent} [{self.value}]"

    def __unicode__(self):
        return f"Tallent: {self.npc} -> {self.talent} [{self.value}]"

class NPC2Trapping(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    trapping = models.ForeignKey(Trapping, on_delete=models.CASCADE)
    amount  = models.CharField(max_length=150, verbose_name="Amount", blank=True, null=True)

    class Meta:
        ordering = ['trapping']

    def __str__(self):
        return f"Trapping: {self.npc} -> {self.trapping} [{self.amount}]"

    def __unicode__(self):
        return f"Trapping: {self.npc} -> {self.trapping} [{self.amount}]"
    
class NPC2CreatureTraits(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    creatureTraits = models.ForeignKey(CreatureTraits, on_delete=models.CASCADE)
    amount = models.CharField(max_length=150, verbose_name="Value", blank=True, null=True)

    class Meta:
        ordering = ['creatureTraits']

    def __str__(self):
        return f"Trapping: {self.npc} -> {self.creatureTraits} [{self.amount}]"

    def __unicode__(self):
        return f"Trapping: {self.npc} -> {self.creatureTraits} [{self.amount}]"
    
class NPC2Spells(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    spell = models.ForeignKey(Spells, on_delete=models.CASCADE)
    amount = models.CharField(max_length=150, verbose_name="Value", blank=True, null=True)

    class Meta:
        ordering = ['spell']

    def __str__(self):
        return f"Trapping: {self.npc} -> {self.spell} [{self.amount}]"

    def __unicode__(self):
        return f"Trapping: {self.npc} -> {self.spell} [{self.amount}]"