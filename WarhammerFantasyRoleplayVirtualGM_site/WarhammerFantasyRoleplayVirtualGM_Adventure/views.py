from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required


from WarhammerFantasyRoleplayVirtualGM_Adventure.models import Adventure
from WarhammerFantasyRoleplayVirtualGM_NPC.models import *
from WarhammerFantasyRoleplayVirtualGM_app.models import Note

import logging
logger = logging.getLogger(__name__)


from . import forms
from . import models

# Create your views here.
@login_required
def adventureDetails(request, adventure_id):
    adventure = Adventure.objects.get(id=adventure_id)
    data = {"adventure":adventure, "npc":[]}
    for n in adventure.npcs.all():
        one_npc_data = {}
        one_npc_data["npc"] = n
        one_npc_data["npc2skill"] = []
        one_npc_data["npc2talent"] = []
        one_npc_data["npc2trapping"] = []
        one_npc_data["npc2creatureTraits"] = []
        one_npc_data["npc2spells"] = []
        for s in n.skills.all():
            _NPC2Skill = NPC2Skill.objects.get(npc=n, skill=s)
            one_npc_data["npc2skill"].append(_NPC2Skill)
        for t in n.talents.all():
            _NPC2Talent = NPC2Talent.objects.get(npc=n, talent=t)
            one_npc_data["npc2talent"].append(_NPC2Talent)
        for t in n.trappings.all():
            _NPC2Trapping = NPC2Trapping.objects.get(npc=n, trapping=t)
            one_npc_data["npc2trapping"].append(_NPC2Trapping)
        for ct in n.creatureTraits.all():
            _NPC2CreatureTraits = NPC2CreatureTraits.objects.get(npc=n, creatureTraits=ct)
            one_npc_data["npc2creatureTraits"].append(_NPC2CreatureTraits)
        for s in n.spells.all():
            _NPC2Spells = NPC2Spells.objects.get(npc=n, spell=s)
            one_npc_data["npc2spells"].append(_NPC2Spells)

        data["npc"].append(one_npc_data)

    return render(request, 'adventure.html', data)

@login_required
def createNewAdventure(request, campaign_id):
    adventure = Adventure.objects.create(name = "Name", campaign_id = campaign_id)
    adventure.save()
    return redirect(reverse('AdventureEdit', args=(adventure.id,)))
    

class AdventureEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_Adventure.html"
    form_class =  forms.AdventureForm
    model = models.Adventure
    
@login_required
def ajax_saveAdventureNotes(request):
    adventure_id = request.POST['adventure_id']
    adventure = Adventure.objects.get(id=adventure_id)
    
    note = Note.objects.create(note_text=request.POST['note_text'], author=request.user)
    note.save()
    
    adventure.notes.add(note)
    adventure.save()
    
    ret = {'status': 'ok', 'id': note.id, 'datetime_create': note.formated_datatime, 'timestamp': note.timestamp, 'author': str(note.author)}
    logger.debug(ret)
    return JsonResponse(ret)