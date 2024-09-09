from django.db import models
from django.urls import reverse

# Create your models here.
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign
from WarhammerFantasyRoleplayVirtualGM_app.models import Note
from WarhammerFantasyRoleplayVirtualGM_app.models import Condition
from WarhammerFantasyRoleplayVirtualGM_NPC.models import NPC



class Adventure(models.Model):
    name = models.CharField(max_length= 250)
    campaign = models.ForeignKey(Campaign, verbose_name="Campaign", blank=False, on_delete=models.PROTECT)
    # npcs = models.ManyToManyField(NPC, verbose_name="NPCs", blank=True, related_name="old_npc")
    npcs2 = models.ManyToManyField(NPC, through="Adventure2NPC", verbose_name="NPC2s", blank=True, related_name="new_npc")
    notes =  models.ManyToManyField(Note, verbose_name="Notes", blank=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)
    
    def get_absolute_url(self):
        return reverse("AdventureDetails", args=(self.id,) )
    
class Adventure2NPC(models.Model):
    npc = models.ForeignKey(NPC, on_delete=models.CASCADE)
    adventure = models.ForeignKey(Adventure, on_delete=models.CASCADE)
    name = models.CharField(max_length= 250, default="", blank=True)
    condition = models.ManyToManyField(Condition, null=True, blank=True)
    current_wounds = models.IntegerField(default="0", verbose_name="Current Wounds")
    
    def save(self, *args, **kwargs):
        if self.current_wounds == 0:
            self.current_wounds = self.npc.characteristics_w
        super(Adventure2NPC, self).save(*args, **kwargs)
    
    def __str__(self):
        return u"{0} -> {1}".format(self.npc, self.adventure)

    def __unicode__(self):
        return u"{0} -> {1}".format(self.npc, self.adventure)
