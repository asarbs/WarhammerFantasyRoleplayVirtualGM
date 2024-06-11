from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from WarhammerFantasyRoleplayVirtualGM_app.models import RefBook
import logging
logger = logging.getLogger(__name__)


def __getNPCs(ref_book_id):
    if ref_book_id == "None":
        return NPC.objects.all()
    else:
        references = Reference.objects.filter(refBook_id = ref_book_id)
        npc = NPC.objects.filter(ref__id__in=references.all())
        return npc

# Create your views here.
@login_required
def index(request):
    npcs_objects = __getNPCs(ref_book_id=request.POST['ref_book_id']) if request.method == "POST" else  NPC.objects.all()
    
    data = {}
    data["npc"] = [] 
    for n in npcs_objects:
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
    
    data["refBook"] = RefBook.objects.all()
        
    return render(request, 'npc.html', data)

class NPCCreateView(LoginRequiredMixin, CreateView):
    template_name = "NPCCreateView.html"
    form_class = NPCForm
    model = NPC

class NPCUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "NPCUpdateView.html"
    form_class = NPCForm
    model = NPC

@login_required
def ajax_npc_get_skill_description(request):
    skill_id = request.POST['skill_id']
    skill = Skils.objects.get(id=skill_id)
    ret = {'status': 'ok', "skill": skill.serialize()}
    return JsonResponse(ret)

@login_required
def ajax_npc_get_talent_description(request):
    talent_id = request.POST['talent_id']
    talent = Talent.objects.get(id=talent_id)
    ret = {'status': 'ok', "talent":talent.serialize()}
    return JsonResponse(ret)

@login_required
def ajax_npc_get_trapping_description(request):
    trapping_id = request.POST['trapping_id']
    trapping = Trapping.objects.get(id=trapping_id)
    ret = {'status': 'ok', "trapping":trapping.serialize()}
    return JsonResponse(ret)

@login_required
def ajax_npc_get_creatureTraits_description(request):
    trait_id = request.POST['creatureTraits_id']
    trait = CreatureTraits.objects.get(id=trait_id)

    ret = {'status': 'ok', "trait":trait.serialize()}
    return JsonResponse(ret)

@login_required
def ajax_npc_get_spell_description(request):
    spell_id = request.POST['spell_id']
    spell = Spells.objects.get(id=spell_id)

    ret = {'status': 'ok', "spell":spell.serialize()}
    return JsonResponse(ret)