from django.db import models

# Create your models here.
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign
from WarhammerFantasyRoleplayVirtualGM_NPC.models import NPC


class Adventure(models.Model):
    name = models.CharField(max_length= 250)
    campaign = models.ForeignKey(Campaign, verbose_name="Campaign", blank=False, on_delete=models.PROTECT)
    npcs = models.ManyToManyField(NPC, verbose_name="NPCs", blank=True)

    def __str__(self):
        return u"{0}".format(self.name)

    def __unicode__(self):
        return u"{0}".format(self.name)