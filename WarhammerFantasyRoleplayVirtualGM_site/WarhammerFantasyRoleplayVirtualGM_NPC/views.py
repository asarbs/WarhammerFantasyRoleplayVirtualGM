from django.shortcuts import render

from .models import *

import logging
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    data = {}
    data["npc"] = [] 
    for n in NPC.objects.all():
        one_npc_data = {}
        one_npc_data["npc"] = n
        one_npc_data["npc2skill"] = []
        one_npc_data["npc2talent"] = []
        one_npc_data["npc2trapping"] = []
        for s in n.skills.all():
            _NPC2Skill = NPC2Skill.objects.get(npc=n, skill=s)
            one_npc_data["npc2skill"].append(_NPC2Skill)
        for t in n.talents.all():
            _NPC2Talent = NPC2Talent.objects.get(npc=n, talent=t)
            one_npc_data["npc2talent"].append(_NPC2Talent)
        for t in n.trappings.all():
            _NPC2Trapping = NPC2Trapping.objects.get(npc=n, trapping=t)
            one_npc_data["npc2trapping"].append(_NPC2Trapping)

        data["npc"].append(one_npc_data)
    logger.info(data)
    return render(request, 'npc.html', data)