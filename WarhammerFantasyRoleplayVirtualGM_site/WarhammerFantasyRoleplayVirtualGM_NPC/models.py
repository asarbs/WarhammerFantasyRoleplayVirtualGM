from django.db import models

from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import Skils
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import Weapon
from WarhammerFantasyRoleplayVirtualGM_app.models import Trapping


# Create your models here.


class NPC(models.Model):
    name = models.CharField(max_length= 50, verbose_name="Name")
    species = models.ForeignKey(Species, verbose_name="Species", related_name="npc_species", on_delete=models.CASCADE, null=True)
    portrait = models.ImageField(upload_to='static/page_images/', null=True, default="static/page_images/default.png")
    characteristics_ws = models.IntegerField(default="0", verbose_name="ws")
    characteristics_bs = models.IntegerField(default="0", verbose_name="bs")
    characteristics_s = models.IntegerField(default="0", verbose_name="s")
    characteristics_t = models.IntegerField(default="0", verbose_name="t")
    characteristics_i = models.IntegerField(default="0", verbose_name="i")
    characteristics_ag = models.IntegerField(default="0", verbose_name="ag")
    characteristics_dex = models.IntegerField(default="0", verbose_name="dex")
    characteristics_int = models.IntegerField(default="0", verbose_name="int")
    characteristics_wp = models.IntegerField(default="0", verbose_name="wp")
    characteristics_fel = models.IntegerField(default="0", verbose_name="fel")
    skills = models.ManyToManyField(Skils, through="NPC2Skill", blank=True)
    talents = models.ManyToManyField(Talent, through="NPC2Talent", blank=True)
    weapons = models.ManyToManyField(Weapon, verbose_name="Weapon", blank=True)
    trappings = models.ManyToManyField(Trapping, through="NPC2Trapping", blank=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
class NPC2Skill(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skils, on_delete=models.CASCADE)
    value = models.IntegerField(default="0", verbose_name="Value")

    def __str__(self):
        return f"Skill: {self.npc} -> {self.skill} [{self.value}]"

    def __unicode__(self):
        return f"Skill: {self.npc} -> {self.skill} [{self.value}]"

class NPC2Talent(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    talent = models.ForeignKey(Talent, on_delete=models.CASCADE)
    value = models.IntegerField(default="0", verbose_name="Value")
    def __str__(self):
        return f"Tallent: {self.npc} -> {self.talent} [{self.value}]"

    def __unicode__(self):
        return f"Tallent: {self.npc} -> {self.talent} [{self.value}]"

class NPC2Trapping(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    trapping = models.ForeignKey(Trapping, on_delete=models.CASCADE)
    amount = models.IntegerField(default="0", verbose_name="Amount")

    def __str__(self):
        return f"Trapping: {self.npc} -> {self.trapping} [{self.amount}]"

    def __unicode__(self):
        return f"Trapping: {self.npc} -> {self.trapping} [{self.amount}]"