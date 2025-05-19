from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView



from WarhammerFantasyRoleplayVirtualGM_Adventure.models import *
from WarhammerFantasyRoleplayVirtualGM_NPC.models import *
from WarhammerFantasyRoleplayVirtualGM_app.models import Note
from WarhammerFantasyRoleplayVirtualGM_app.models import Condition

import logging
logger = logging.getLogger(__name__)


from . import forms
from . import models

# Create your views here.
@login_required
def adventureDetails(request, adventure_id):
    adventure = Adventure.objects.get(id=adventure_id)
    data = {"adventure":adventure, "npc":[], "conditions":[], "npc_lib":[]}
    
    conditions = Condition.objects.all()
    
    for adv2npc in Adventure2NPC.objects.filter(adventure=adventure):
        one_npc_data = {}
        logger.info(f"{adv2npc.id}: {adv2npc}")
        one_npc_data["adv2npc"] = adv2npc
        one_npc_data["npc"] = adv2npc.npc
        one_npc_data["current_wounds"] = adv2npc.current_wounds
        one_npc_data["npc2skill"] = []
        one_npc_data["npc2talent"] = []
        one_npc_data["npc2trapping"] = []
        one_npc_data["npc2creatureTraits"] = []
        one_npc_data["npc2spells"] = []
        one_npc_data["npc2condition"] = []
        
        for s in adv2npc.npc.skills.all():
            _NPC2Skill = NPC2Skill.objects.get(npc=adv2npc.npc, skill=s)
            one_npc_data["npc2skill"].append(_NPC2Skill)
        for t in adv2npc.npc.talents.all():
            _NPC2Talent = NPC2Talent.objects.get(npc=adv2npc.npc, talent=t)
            one_npc_data["npc2talent"].append(_NPC2Talent)
        for t in adv2npc.npc.trappings.all():
            _NPC2Trapping = NPC2Trapping.objects.get(npc=adv2npc.npc, trapping=t)
            one_npc_data["npc2trapping"].append(_NPC2Trapping)
        for ct in adv2npc.npc.creatureTraits.all():
            _NPC2CreatureTraits = NPC2CreatureTraits.objects.get(npc=adv2npc.npc, creatureTraits=ct)
            one_npc_data["npc2creatureTraits"].append(_NPC2CreatureTraits)
        for s in adv2npc.npc.spells.all():
            _NPC2Spells = NPC2Spells.objects.get(npc=adv2npc.npc, spell=s)
            one_npc_data["npc2spells"].append(_NPC2Spells)
        for con in conditions:
            if con in adv2npc.condition.all():
                one_npc_data["npc2condition"].append({"condition":con, "has":True})
            else:
                one_npc_data["npc2condition"].append({"condition":con, "has": False})

        data["npc"].append(one_npc_data)


    for npc in NPC.objects.all():
       data['npc_lib'].append({"id": npc.id, "name": npc.name})

    return render(request, 'adventure.html', data)

@login_required
def createNewAdventure(request, campaign_id):
    adventure = Adventure.objects.create(name = "Name", campaign_id = campaign_id)
    adventure.save()
    return redirect(reverse('AdventureEdit', args=(adventure.id,)))
    
    
@login_required
def addNpscToAdventure(request, adventure_id):
    if request.method == 'POST':
        npc_id = request.POST.get('new_npc')
        adventure = get_object_or_404(Adventure, id=adventure_id)
        npc = get_object_or_404(NPC, id=npc_id)

        # Sprawdź, czy taki rekord już istnieje
        existing = Adventure2NPC.objects.filter(adventure=adventure, npc=npc).first()
        if not existing:
            # Utwórz powiązanie przez model pośredni
            Adventure2NPC.objects.create(adventure=adventure, npc=npc)

        return redirect(adventure.get_absolute_url())

    return redirect('main')  # lub inna strona, jeśli użytkownik wejdzie przez GET

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

@login_required
def ajax_saveConditionState(request):
    adventure_id = request.POST['adventure_id']
    condition_id = request.POST['condition_id']
    npc_id = request.POST['npc_id']
    adv2npc_id = request.POST['adv2npc_id']
    checked = request.POST['checked']
    logger.info(f"request.POST={request.POST}")
    
    adv2npc = Adventure2NPC.objects.get(id=adv2npc_id)
    condition = Condition.objects.get(id=condition_id)

    if checked:
        adv2npc.condition.add(condition)
    else:
        adv2npc.condition.remove(condition) 

    ret = {'status': 'ok'}
    logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_saveCurrentWounds(request):
    adv2npc_id = request.POST['adv2npc_id']
    current_wounds = request.POST['current_wounds']
    logger.info(f"request.POST={request.POST}")
    
    adv2npc = Adventure2NPC.objects.get(id=adv2npc_id)
    adv2npc.current_wounds = current_wounds
    adv2npc.save()

    ret = {'status': 'ok'}
    logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_getConditionsDetails(request):
    conditions = Condition.objects.all()
    ret = {'status': 'ok', "conditions":[]}
    for con in conditions:
        ret['conditions'].append({"id":con.id, "name":con.name, "description":con.description})

    return JsonResponse(ret)