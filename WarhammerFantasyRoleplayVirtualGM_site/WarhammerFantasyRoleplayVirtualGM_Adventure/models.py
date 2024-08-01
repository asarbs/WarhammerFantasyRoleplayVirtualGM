from django.db import models

# Create your models here.
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign
from WarhammerFantasyRoleplayVirtualGM_app.models import Note
from WarhammerFantasyRoleplayVirtualGM_NPC.models import NPC


class Adventure(models.Model):
    name = models.CharField(max_length= 250)
    campaign = models.ForeignKey(Campaign, verbose_name="Campaign", blank=False, on_delete=models.PROTECT)
    npcs = models.ManyToManyField(NPC, verbose_name="NPCs", blank=True)
    notes =  models.ManyToManyField(Note, verbose_name="Notes", blank=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)