import django
from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.forms import CharField
from django.forms import Form
from django.forms import PasswordInput
from django.forms.models import BaseModelForm
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.urls import reverse


from pprint import pformat

import random
import math
import json

from django.urls import reverse

from dal import autocomplete

import logging
logger = logging.getLogger(__name__)


from WarhammerFantasyRoleplayVirtualGM_app.forms import *
from WarhammerFantasyRoleplayVirtualGM_app.models import *
from WarhammerFantasyRoleplayVirtualGM_app.models import createCharacterLog as ccl
from WarhammerFantasyRoleplayVirtualGM_app.tables import *

from WarhammerFantasyRoleplayVirtualGM_app.character_creations_helpers import *


# Create your views here.
from django.http import HttpResponse


def index(request):
    data = {}
    return render(request, 'main/main.html', data)

@login_required
def createCampaign(request):
    if request.method == 'POST':
        campaign_form = CreateCampaignForm(request.POST, prefix='user')
        if campaign_form.is_valid():
            campaign = campaign_form.save()
            player = Player.objects.get(user=request.user)
            c2p = Campaign2Player(player=player, campaign=campaign)
            c2p.save()
            return HttpResponseRedirect("/wfrpg_gm/")
    else:
        campaign_form = CreateCampaignForm(prefix='user')
    return render(request, 'addCampaign.html', dict(form=campaign_form))

@login_required
def addCharacter(request, CampaignId):
    basic_skills_criterion1 = Q(id__gte = 1)
    basic_skills_criterion2 = Q(id__lte = 26)
    basic_skills = Skils.objects.filter(basic_skills_criterion1 & basic_skills_criterion2).order_by("name").values()
    player = Player.objects.get(user=request.user)
    character = Character(player=player,
                          campaign_id = CampaignId,
                          name="Example Name",
                          species_id = 2,
                          ch_class_id=8,
                          career_id=58,
                          career_path_id=487,
                          hair_id = 9,
                          eyes_id = 10,
                          )
    character.save()

    for skill in basic_skills:
        c2s = Character2Skill(characters_id=character.id, skills_id = skill['id'], is_basic_skill=True)
        c2s.save()

    skills_values = Character2Skill.objects.filter(characters_id=character.id)
    for skill in basic_skills:
        for skill_val in skills_values:
            if skill['id'] == skill_val.skills_id:
                skill['adv'] = skill_val.adv
    species = Species.objects.all()

    return redirect(reverse('viewCharacter', args=(character.id,)))
    # context = {
    #     'characker_id': character.id,
    #     'basic_skills': basic_skills,
    #     'species': species
    #     }
    # return render(request, 'addCharacter.html',context)

@login_required
def ajax_save_character_species(request):
    if request.method == 'POST':
        species_id = request.POST['species_id']
        species = Species.objects.get(id=species_id)
        return set_character_species(species=species, character_id=request.POST['character_id'])
    logger.error("ajax_save_character_species is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveSpecies(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character = Character.objects.get(id= request.POST['character_id'])
    species = Species.objects.get(id=request.POST['species_id'])
    character.species = species
    rat = RandomAttributesTable.objects.get(species=species)
    character.movement_movement = rat.movement
    character.movement_walk     = 2 * rat.movement
    character.movement_run      = 4 * rat.movement
    character.save()
    ccl(request.user, character, "set species  to {}; movement={}; walk={}; run{}".format(character.species, character.movement_movement, character.movement_walk, character.movement_run))
    res = {'status': 'ok',
           "species_id": character.species.id,
           'movement_movement': character.movement_movement,
           'movement_walk': character.movement_walk,
           'movement_run': character.movement_run,
           }
    return JsonResponse(res)

def ajax_saveClass(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character = Character.objects.get(id= request.POST['character_id'])
    character.ch_class = Class.objects.get(id=request.POST['class_id'])
    character.save()
    ccl(request.user, character, "set class  to {}".format(character.ch_class))
    return JsonResponse({'status': 'ok', 'class_id':character.ch_class.id})

def ajax_saveCareer(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)


    logger.debug(request.POST)
    character = Character.objects.get(id= request.POST['character_id'])
    character.career = Career.objects.get(id=request.POST['career_id'])
    character.save()
    ccl(request.user, character, "set career  to {}".format(character.career))
    return JsonResponse({'status': 'ok', 'career_id':character.career.id})


def ajax_saveCareer_level(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character = Character.objects.get(id= request.POST['character_id'])
    character.career_level = id=request.POST['career_level']
    character.save()
    ccl(request.user, character, "set career level to {}".format(character.career_level))
    return JsonResponse({'status': 'ok', 'career_level':character.career_level})

@login_required
def ajax_randomSpecies(request):
    if request.method == 'POST':
        species_list = Species.objects.all()
        r = random.randrange(1, 100)
        species = None
        for s in species_list:
            if r >= s.random_interal_start and r <= s.random_interal_end:
                species = s
                break
        return set_character_species(species=species, character_id=request.POST['character_id'])

    logger.error("ajax_randomSpecies is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_addTalentToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['character_id']
    talent_id = request.POST['new_talent_id']
    try:
        char2tal, created = Character2Talent.objects.get_or_create(characters_id=character_id, talent_id=talent_id, taken=1)
        char2tal.save();
    except django.db.utils.IntegrityError as e:
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character_id, char2tal.talent.name, created))
    return JsonResponse({'status': 'ok'})

@login_required
def ajax_replaceTalentToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['character_id']
    new_talent_id = request.POST['new_talent_id']
    old_talent_id = request.POST['old_talent_id']
    logger.debug("character_id={}; new_talent_id={}; old_talent_id={}".format(character_id, new_talent_id, old_talent_id))
    try:
        Character2Talent.objects.get(characters_id=character_id, talent_id=old_talent_id).delete()
    except Character2Talent.DoesNotExist as e:
        logger.debug("{}: old_talent_id={};".format(e, old_talent_id))
    try:
        char2tal, created = Character2Talent.objects.get_or_create(characters_id=character_id, talent_id=new_talent_id, taken=1)
        char2tal.save();
    except django.db.utils.IntegrityError as e:
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character_id, char2tal.taken.name, created))
    talents = get_character_talents(Character.objects.get(id = character_id))
    return JsonResponse({'status': 'ok', 'talents': talents})

@login_required
def ajax_saveTalentToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['character_id']
    talent_id = request.POST['talent_id']
    talent_taken = request.POST['talent_taken']
    try:
        character = Character.objects.get(id=character_id)
        char2tal, created = Character2Talent.objects.get_or_create(characters=character, talent_id=talent_id, taken=talent_taken)
        ccl(request.user, character, "add talen \"{}\".".format(char2tal.talent.name))
        char2tal.save()
    except django.db.utils.IntegrityError as e:
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character_id, char2tal.taken.name, created))
    return JsonResponse({'status': 'ok'})

@login_required
def ajax_saveTrappingToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['character_id']
    trapping_id = request.POST['trapping_id']
    try:
        character = Character.objects.get(id=character_id)
        char2tal, created = Character2Trapping.objects.get_or_create(characters=character, trapping_id=trapping_id)
        ccl(request.user, character, "add Traping \"{}\".".format(char2tal.trapping.name))
        char2tal.save()

        containers = Containers.objects.filter(trapping_id=trapping_id)
        if containers.exists():
            for c in containers:
                logger.debug(f"container: {c.name}")
                char2Cont, created = Character2Container.objects.get_or_create(character = character, container = c)
                ccl(request.user, character, "add Containers \"{}\".".format(char2Cont.container.name))
                char2Cont.save()


    except django.db.utils.IntegrityError as e:
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character_id, char2tal.trapping.name, created))
    return JsonResponse({'status': 'ok'})

@login_required
def ajax_randomClass(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)

        r = random.randrange(1, 100)
        career = None
        conditions = {
            1: [Q(random_table_high_elf_start__lte = r) , Q(random_table_high_elf_end__gte = r)],
            2: [Q(random_table_human_start__lte = r), Q(random_table_human_end__gte = r)],
            3: [Q(random_table_halfling_start__lte = r), Q(random_table_halfling_end__gte = r) ],
            4: [Q(random_table_dwarf_start__lte = r), Q(random_table_dwarf_end__gte = r) ],
            5: [Q(random_table_wood_elf_start__lte = r), Q(random_table_wood_elf_end__gte = r) ],
        }
        if character.species.id >=1 and character.species.id <= 5:
            career_criterion1 = conditions[character.species.id][0]
            career_criterion2 = conditions[character.species.id][1]
            queryset = Career.objects.filter(career_criterion1 & career_criterion2)
            career = queryset.first()
        else:
            logger.error("ajax_randomClass incorect species.id={}".format(character.species.id))

        if career is not None:
            character.career = career
            character.ch_class = career.ch_class


            Character2Skill.objects.filter(characters=character, is_career_skill = True).delete()
            ad = CareersAdvanceScheme.objects.get(career=career).advances_level_1
            for ss in ad.skills.all():
                try:
                    ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0)
                    ch2Skill.is_career_skill = True
                    ch2Skill.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

            character.career_path = ad
            character.status = ad.status
            character.save()
            skills = {}
            for ss in Character2Skill.objects.filter(characters=character).all():
                logger.debug("ss.name:{}; is_basic_skill:{}; is_species_skill:{}; is_career_skill:{}".format(ss.skills.name, ss.is_basic_skill , ss.is_species_skill, ss.is_career_skill))
                skills[ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'is_basic_skill':ss.is_basic_skill , 'is_species_skill': ss.is_species_skill, 'is_career_skill': ss.is_career_skill}

            Character2Talent.objects.filter(characters=character, is_career_skill = True).delete()
            for talent in ad.talents.all():
                try:
                    c2talent, created = Character2Talent.objects.get_or_create(characters=character, talent=talent, taken=1)
                    c2talent.is_career_skill = True
                    c2talent.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} talent:{} created:{}".format(character.id, talent.name, created))



            Character2Trapping.objects.filter(characters=character, is_career_skill = True).delete()
            for classTraping in ClassTrappings.objects.filter(ch_class=career.ch_class).all():
                try:
                    ch2STrappingl, created = Character2Trapping.objects.get_or_create(characters=character, trapping=classTraping.trapping, enc=classTraping.trapping.encumbrance)
                    logger.debug("ClassTrappings.trapping.id={} name={};".format(classTraping.trapping.id, classTraping.trapping.name))
                    ch2STrappingl.is_career_skill = True
                    ch2STrappingl.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} Trappings:{} created:{}".format(character.id, classTraping.trapping.name, created))

            for trapping in ad.trappings.all():
                try:
                    ch2STrappingl, created = Character2Trapping.objects.get_or_create(characters=character, trapping=trapping, enc=trapping.encumbrance)
                    ch2STrappingl.is_career_skill = True
                    ch2STrappingl.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} Trappings:{} created:{}".format(character.id, trapping.name, created))

            trappings = {}
            for ch2STrappingl in Character2Trapping.objects.filter(characters=character).all():
                logger.debug("'id': {}, 'name': {}, 'description': {}, 'enc': {}".format(ch2STrappingl.id, ch2STrappingl.trapping.name, ch2STrappingl.trapping.description, ch2STrappingl.enc))
                trappings[ch2STrappingl.id] = {
                    'id': ch2STrappingl.id,
                    'name': ch2STrappingl.trapping.name,
                    'description': ch2STrappingl.trapping.description,
                    'enc': ch2STrappingl.enc
                }

            return JsonResponse({'status': 'ok',
                                 'career_id': career.id,
                                 'career_name': career.name,
                                 'ch_class_name': character.ch_class.name,
                                 'skills': skills,
                                 'career_path': ad.name,
                                 'status': str(ad.status),
                                 'career_level' : 1,
                                 'trappings': trappings
                                 })
        else:
            logger.error("ajax_randomClass career not found: career={}".format(career))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_randomClass is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveName(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)

        if character is not None:
            character.name = request.POST['name']
            logger.debug("character name: {}".format(character.name))
            character.save()
            ccl(request.user, character, "change character name to {} ".format(character.name))
            return JsonResponse({'status': 'ok', 'name': character.name})
        else:
            logger.error("ajax_saveName character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_randomClass is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_getRandomAttributesTable(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    rat = RandomAttributesTable.objects.all()
    ret = {'attributesTable':{}, 'eyesTable': {}, 'hairTable': {}, 'armour': [], 'weapon':[], "spells":[], "careersAdvanceScheme":{}, "improvementXPCosts": []}
    for r in rat:
        ret['attributesTable'][r.species.id] = {
            "characteristics_ws_initial" : r.weapon_skill,
            "characteristics_bs_initial" : r.ballistic_skill,
            "characteristics_s_initial" : r.strength,
            "characteristics_t_initial" : r.toughness,
            "characteristics_i_initial" : r.initiative,
            "characteristics_ag_initial" : r.agility,
            "characteristics_dex_initial" : r.dexterity,
            "characteristics_int_initial" : r.intelligence,
            "characteristics_wp_initial" : r.willpower,
            "characteristics_fel_initial" : r.fellowship,
        }
    for r in Eyes.objects.all():
        if r.species.id not in ret['eyesTable']:
            ret['eyesTable'][r.species.id] = []
        ret['eyesTable'][r.species.id].append({'val': r.id, 'name': r.name})
    for r in Hair.objects.all():
        if r.species.id not in ret['hairTable']:
            ret['hairTable'][r.species.id] = []
        ret['hairTable'][r.species.id].append({'val': r.id, 'name': r.name})
    for r in Armour.objects.all():
        ret['armour'].append(r.to_dict())
    for mw in MeleeWeapons.objects.all():
        ret['weapon'].append(mw.to_dict())
    for rm in RangedWeapon.objects.all():
        ret['weapon'].append(rm.to_dict())
    for s in Spells.objects.all():
        ret['spells'].append(s.to_dict())
    for impv in ImprovementXPCosts.objects.all():
        ret['improvementXPCosts'].append(impv.to_dict())
    # logger.debug(pformat(ret))
    return JsonResponse(ret)

@login_required
def ajax_randomAttributes(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        logger.info("ajax_saveAttributes: character={}; species={}".format(character, character.species))
        rat = RandomAttributesTable.objects.get(species=character.species)
        if character is not None:
            character.characteristics_ws_initial = rat.weapon_skill + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_bs_initial = rat.ballistic_skill + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_s_initial = rat.strength + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_t_initial = rat.toughness + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_i_initial = rat.initiative + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_ag_initial = rat.agility + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_dex_initial = rat.dexterity + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_int_initial = rat.intelligence + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_wp_initial = rat.willpower + random.randrange(1, 10) + random.randrange(1, 10)
            character.characteristics_fel_initial = rat.fellowship + random.randrange(1, 10) + random.randrange(1, 10)
            character.fate_fate = rat.fate
            character.fate_fortune = rat.fate
            character.resilience_resilience = rat.resilience
            character.resilience_resolve = rat.resilience
            character.movement_movement = rat.movement
            character.movement_walk = 2 * rat.movement
            character.movement_run = 4 * rat.movement
            SB = math.floor(character.characteristics_s_initial / 10.0)
            TB = math.floor(character.characteristics_t_initial / 10.0)
            WPB = math.floor(character.characteristics_wp_initial / 10.0)
            character.wounds = SB + (2 * TB) + WPB
            character.save()
            ret = {'status': 'ok',
                   'extra_points': rat.extra_points,
                   'characteristics_ws_initial': character.characteristics_ws_initial,
                   'characteristics_bs_initial': character.characteristics_bs_initial,
                   'characteristics_s_initial': character.characteristics_s_initial,
                   'characteristics_t_initial': character.characteristics_t_initial,
                   'characteristics_i_initial': character.characteristics_i_initial,
                   'characteristics_ag_initial': character.characteristics_ag_initial,
                   'characteristics_dex_initial': character.characteristics_dex_initial,
                   'characteristics_int_initial': character.characteristics_int_initial,
                   'characteristics_wp_initial': character.characteristics_wp_initial,
                   'characteristics_fel_initial': character.characteristics_fel_initial,
                   'fate_fate': character.fate_fate,
                   'fate_fortune': character.fate_fortune,
                   'resilience_resilience': character.resilience_resilience,
                   'resilience_resolve': character.resilience_resilience,
                   'movement_movement': character.movement_movement,
                   'wounds': character.wounds
            }
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveAttributes not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_randomClass is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveAttribute(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        logger.debug(request.POST)
        if 'newVal[experience_current]' not in request.POST or 'newVal[experience_spent]' not in request.POST:
            raise ValueError("Missing experience_current or experience_spent")
        if character is not None:
            character.characteristics_ws_initial    = int(request.POST['newVal[characteristics_ws_initial]'])
            character.characteristics_bs_initial    = int(request.POST['newVal[characteristics_bs_initial]'])
            character.characteristics_s_initial     = int(request.POST['newVal[characteristics_s_initial]'])
            character.characteristics_t_initial     = int(request.POST['newVal[characteristics_t_initial]'])
            character.characteristics_i_initial     = int(request.POST['newVal[characteristics_i_initial]'])
            character.characteristics_ag_initial    = int(request.POST['newVal[characteristics_ag_initial]'])
            character.characteristics_dex_initial   = int(request.POST['newVal[characteristics_dex_initial]'])
            character.characteristics_int_initial   = int(request.POST['newVal[characteristics_int_initial]'])
            character.characteristics_wp_initial    = int(request.POST['newVal[characteristics_wp_initial]'])
            character.characteristics_fel_initial   = int(request.POST['newVal[characteristics_fel_initial]'])
            character.characteristics_ws_advances   = int(request.POST['newVal[characteristics_ws_advances]'])
            character.characteristics_bs_advances   = int(request.POST['newVal[characteristics_bs_advances]'])
            character.characteristics_s_advances    = int(request.POST['newVal[characteristics_s_advances]'])
            character.characteristics_t_advances    = int(request.POST['newVal[characteristics_t_advances]'])
            character.characteristics_i_advances    = int(request.POST['newVal[characteristics_i_advances]'])
            character.characteristics_ag_advances   = int(request.POST['newVal[characteristics_ag_advances]'])
            character.characteristics_dex_advances  = int(request.POST['newVal[characteristics_dex_advances]'])
            character.characteristics_int_advances  = int(request.POST['newVal[characteristics_int_advances]'])
            character.characteristics_wp_advances   = int(request.POST['newVal[characteristics_wp_advances]'])
            character.characteristics_fel_advances  = int(request.POST['newVal[characteristics_fel_advances]'])
            character.experience_current            = int(request.POST['newVal[experience_current]'])
            character.experience_spent              = int(request.POST['newVal[experience_spent]'])

            SB = math.floor(int(character.characteristics_s_initial) / 10.0)
            TB = math.floor(int(character.characteristics_t_initial) / 10.0)
            WPB = math.floor(int(character.characteristics_wp_initial) / 10.0)
            character.wounds = SB + (2 * TB) + WPB
            character.save()
            ret = {'status': 'ok',
                   'characteristics_ws_initial':    int(character.characteristics_ws_initial),
                   'characteristics_bs_initial':    int(character.characteristics_bs_initial),
                   'characteristics_s_initial':     int(character.characteristics_s_initial),
                   'characteristics_t_initial':     int(character.characteristics_t_initial),
                   'characteristics_i_initial':     int(character.characteristics_i_initial),
                   'characteristics_ag_initial':    int(character.characteristics_ag_initial),
                   'characteristics_dex_initial':   int(character.characteristics_dex_initial),
                   'characteristics_int_initial':   int(character.characteristics_int_initial),
                   'characteristics_wp_initial':    int(character.characteristics_wp_initial),
                   'characteristics_fel_initial':   int(character.characteristics_fel_initial),
                   'characteristics_ws_advances':   int(character.characteristics_ws_advances),
                   'characteristics_bs_advances':   int(character.characteristics_bs_advances),
                   'characteristics_s_advances':    int(character.characteristics_s_advances),
                   'characteristics_t_advances':    int(character.characteristics_t_advances),
                   'characteristics_i_advances':    int(character.characteristics_i_advances),
                   'characteristics_ag_advances':   int(character.characteristics_ag_advances),
                   'characteristics_dex_advances':  int(character.characteristics_dex_advances),
                   'characteristics_int_advances':  int(character.characteristics_int_advances),
                   'characteristics_wp_advances':   int(character.characteristics_wp_advances),
                   'characteristics_fel_advances':  int(character.characteristics_fel_advances),
                   'fate_fate':                     int(character.fate_fate),
                   'fate_fortune':                  int(character.fate_fortune),
                   'resilience_resilience':         int(character.resilience_resilience),
                   'resilience_resolve':            int(character.resilience_resilience),
                   'movement_movement':             int(character.movement_movement),
                   'wounds':                        int(character.wounds)
            }
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveAttribute not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveAttribute is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveFate_and_fortune(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        print(request.POST)
        if character is not None:
            character.fate_fate    = int(request.POST['newVal[fate_fate]'])
            character.fate_fortune    = int(request.POST['newVal[fate_fortune]'])
            character.save()
            ret = {'status': 'ok',
                   'fate_fate':    int(character.fate_fate),
                   'fate_fortune':     int(character.fate_fortune),
            }
            logger.debug(ret)
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveFate_and_fortune not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveFate_and_fortune is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveFate(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            character.fate_fate    = int(request.POST['fate_fate'])
            character.save()
            ret = {'status': 'ok',
                   'fate_fate':    int(character.fate_fate),
            }
            logger.debug(ret)
            ccl(request.user, character, "change character fate to  {} ".format(character.fate_fate))
            return JsonResponse(ret)
        else:
            logger.error("ajax_save_fate not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_save_fate is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveFortune(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        print(request.POST)
        if character is not None:
            character.fate_fortune    = int(request.POST['fate_fortune'])
            character.save()
            ret = {'status': 'ok',
                   'fate_fortune':     int(character.fate_fortune),
            }
            logger.debug(ret)
            ccl(request.user, character, "change character fortune to  {} ".format(character.fate_fortune))
            return JsonResponse(ret)
        else:
            logger.error("ajax_save_fortune not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_save_fortune is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveAge(request):
    if request.method == 'POST':
        logger.debug(request.POST)
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            character.age    = int(request.POST['age'])
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            ccl(request.user, character, "set character age to {}".format(character.age))
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveAge not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveAge is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveHeight(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            character.height    = int(request.POST['height'])
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            ccl(request.user, character, "set character high to {}".format(character.height))
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveHeight not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveHeight is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveHair(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        hair = request.POST['hair']
        character = Character.objects.get(id = character_id)
        if character is not None:
            hair = Hair.objects.get(id=hair)
            character.hair    = hair
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            ccl(request.user, character, "set character hair to {}".format(character.hair))
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveHair not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveHair is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveEyes(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            eye_color = Eyes.objects.get(id=request.POST['eyes'])
            character.eyes = eye_color
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            ccl(request.user, character, "set character eyes to {}".format(character.eyes))
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveEyes not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveEyes is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveSkillAdv(request):
    if request.method == 'POST':
        character_id = request.POST['character_id']
        logger.info(request.POST)
        logger.info("character_id={}; skill_id={}; points={}; old_skill_adv={}".format(character_id, request.POST['skill_id'], request.POST['points'], request.POST['old_skill_adv']))
        if request.POST['skill_id'] == 0:
            ch2skill = Character2Skill.objects.get(characters_id=character_id, skills_id=request.POST['skill_id'])
            if ch2skill is not None:
                ch2skill.adv =request.POST['points']

                ch2skill.save()
            else:
                logger.error("ajax_saveSkillAdv not found: character_id={}".format(character_id))
                return JsonResponse({'status': 'Invalid request'}, status=400)

        old_skill_adv = request.POST.get('old_skill_adv', None)
        if old_skill_adv is not None:
            ch2skill = Character2Skill.objects.get(characters_id=character_id, skills_id=request.POST['old_skill_adv'])
            if ch2skill is not None:
                ch2skill.adv = 0
                ch2skill.save()
            else:
                logger.error("ajax_saveSkillAdv not found: character_id={}".format(character_id))
                return JsonResponse({'status': 'Invalid request'}, status=400)

        ret = {'status': 'ok'  }
        return JsonResponse(ret)
    logger.error("ajax_saveSkillAdv is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

@login_required
def ajax_saveFreeHandSkillAdv(request):
    if not request.method == 'POST':
        logger.error("ajax_saveFreeHandSkillAdv is {}".format(request.method))
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)
    ch2skill = Character2Skill.objects.get(characters_id=request.POST['character_id'], skills_id=request.POST['skill_id'])
    ch2skill.adv = request.POST['skill_adv_val']
    ch2skill.save()
    ccl(request.user, ch2skill.characters, "Update \"{}\" to {}.".format(ch2skill.skills, ch2skill.adv))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveFreeHandCharacteristicAdv(request):
    if not request.method == 'POST':
        logger.error("ajax_saveFreeHandSkillAdv is {}".format(request.method))
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)
    ch = Character.objects.get(id=request.POST['character_id'])

    ch.characteristics_ws_advances  = request.POST['characteristics_ws_advances']
    ch.characteristics_bs_advances  = request.POST['characteristics_bs_advances']
    ch.characteristics_s_advances   = request.POST['characteristics_s_advances']
    ch.characteristics_t_advances   = request.POST['characteristics_t_advances']
    ch.characteristics_i_advances   = request.POST['characteristics_i_advances']
    ch.characteristics_ag_advances  = request.POST['characteristics_ag_advances']
    ch.characteristics_dex_advances = request.POST['characteristics_dex_advances']
    ch.characteristics_int_advances = request.POST['characteristics_int_advances']
    ch.characteristics_wp_advances  = request.POST['characteristics_wp_advances']
    ch.characteristics_fel_advances = request.POST['characteristics_fel_advances']

    ch.save()

    ccl(request.user, ch, "set characteristics: ws_advances  = {}; bs_advances  = {}; s_advances   = {}; t_advances   = {}; i_advances   = {}; ag_advances  = {}; dex_advances = {}; int_advances = {}; wp_advances  = {}; fel_advances = {};".format(request.POST['characteristics_ws_advances'], request.POST['characteristics_bs_advances'], request.POST['characteristics_s_advances'], request.POST['characteristics_t_advances'], request.POST['characteristics_i_advances'], request.POST['characteristics_ag_advances'], request.POST['characteristics_dex_advances'], request.POST['characteristics_int_advances'], request.POST['characteristics_wp_advances'], request.POST['characteristics_fel_advances']))

    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveFreeHandCharacteristicInit(request):
    if not request.method == 'POST':
        logger.error("ajax_saveFreeHandCharacteristicInit is {}".format(request.method))
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)
    ch = Character.objects.get(id=request.POST['character_id'])

    ch.characteristics_ws_initial  = request.POST['characteristics_ws_initial']
    ch.characteristics_bs_initial  = request.POST['characteristics_bs_initial']
    ch.characteristics_s_initial   = request.POST['characteristics_s_initial']
    ch.characteristics_t_initial   = request.POST['characteristics_t_initial']
    ch.characteristics_i_initial   = request.POST['characteristics_i_initial']
    ch.characteristics_ag_initial  = request.POST['characteristics_ag_initial']
    ch.characteristics_dex_initial = request.POST['characteristics_dex_initial']
    ch.characteristics_int_initial = request.POST['characteristics_int_initial']
    ch.characteristics_wp_initial  = request.POST['characteristics_wp_initial']
    ch.characteristics_fel_initial = request.POST['characteristics_fel_initial']
    ch.save()
    ccl(request.user, ch, "set characteristics: ws_initial  = {}; bs_initial  = {}; s_initial   = {}; t_initial   = {}; i_initial   = {}; ag_initial  = {}; dex_initial = {}; int_initial = {}; wp_initial  = {}; fel_initial = {};".format(request.POST['characteristics_ws_initial'], request.POST['characteristics_bs_initial'], request.POST['characteristics_s_initial'], request.POST['characteristics_t_initial'], request.POST['characteristics_i_initial'], request.POST['characteristics_ag_initial'], request.POST['characteristics_dex_initial'], request.POST['characteristics_int_initial'], request.POST['characteristics_wp_initial'], request.POST['characteristics_fel_initial']))



    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_getCareersAdvanceScheme(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)

    cas = CareersAdvanceScheme.objects.get(career__id = request.POST['career_id'])
    ret = {'status': 'ok', 'careersAdvanceScheme': cas.serialize() }
    return JsonResponse(ret)

@login_required
def ajax_addArmourToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)
    armour = Armour.objects.get(id=request.POST['armour_id'])
    character.armour.add(armour)
    character.save()
    ccl(request.user, character, "add armour \"{}\".".format(armour))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_addWeaponToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    weapon = Weapon.objects.get(id=request.POST['weapon_id'])
    character = Character.objects.get(id = character_id)
    character.weapon.add(weapon)
    character.save()
    ccl(request.user, character, "add weapon \"{}\".".format(weapon))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_addSpellsToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)
    spell = Spells.objects.get(id=request.POST['spell_id'])
    character.spells.add(spell)
    character.save()
    ccl(request.user, character, "add spell \"{}\".".format(spell))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveSkillsXPSpend(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    c2s = Character2Skill.objects.get(characters = character, skills__id = request.POST['skill_id'])
    c2s.adv = request.POST['newVal']
    c2s.save()

    character.experience_current = request.POST['experience_current']
    character.experience_spent = request.POST['experience_spent']
    character.save()

    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveTalentXPSpend(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    c2t = Character2Talent.objects.get(characters = character, skills__id = request.POST['tallent_id'])
    c2t.adv = request.POST['newVal']
    c2t.save()

    character.experience_current = request.POST['experience_current']
    character.experience_spent = request.POST['experience_spent']
    character.save()

    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveAmbitions(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug("ambitions_id={}; description={}; achieved={}; character_id={}; is_shortterm={}".format(request.POST['ambitions_id'], request.POST['description'], request.POST['achieved'], request.POST['character_id'], request.POST['is_shortterm']))

    ami, created  = (Ambitions.objects.create(description=request.POST['description']), True) if int(request.POST['ambitions_id']) == 0 else (Ambitions.objects.get(id=request.POST['ambitions_id']), False)
    ami.achieved = True if request.POST['achieved'] == 'true' else False
    ami.save()

    logger.debug("created={}".format(created))

    if created:
        character = Character.objects.get(id=request.POST['character_id'])
        if request.POST['is_shortterm'] == "true":
            character.ambitions_shortterm.add(ami)
        else:
            character.ambitions_longterm.add(ami)
        character.save()


    ccl(request.user, character, "add ambition \"{}\"; achieved={}".format(request.POST['description'], ami.achieved) )
    ret = {'status': 'ok' , 'id':ami.id}
    logger.debug(ret)
    return JsonResponse(ret)


@login_required
def ajax_saveCurrentEp(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)

    ch, created = Character.objects.get_or_create(id=request.POST['character_id'])
    ch.experience_current = request.POST['experience_current']

    ccl(request.user, ch, "change character experience current to  {} ".format(character.experience_current))
    ch.save()

    ret = {'status': 'ok'}
    return JsonResponse(ret)

@login_required
def detailsCampaign(request, CampaignId):
    c = Campaign.objects.get(id=CampaignId)
    players = []
    createNewCharacter = False
    logged_player = Player.objects.get(user=request.user)
    for c2p in Campaign2Player.objects.filter(campaign=c):
        players.append(c2p.player)
    characters = Character.objects.filter(campaign=c, player__in=players)
    for character in characters:
        if logged_player == character.player:
            createNewCharacter = True
    campaign_2_player_form = Campaign2PlayerForm()
    dic ={'camaing': c, "players":players, "characters": characters, "createNewCharacter": createNewCharacter, "campaign_2_player_form":campaign_2_player_form}
    logging.debug(dic)
    return render(request, 'detailsCampaign.html', dic)


@login_required
def showCareersAdvanceSchemes(request, casId):
        cas = CareersAdvanceScheme.objects.get(id=casId)
        return render(request, 'showCareersAdvanceSchemes.html', {'cas':cas} )

@login_required
def listCareersAdvanceSchemes(request):
    cas = CareersAdvanceScheme.objects.all()
    return render(request, 'listCareersAdvanceSchemes.html', {'cas':cas} )

class ChangePasswordForm(LoginRequiredMixin, Form):
    new_password = CharField(widget=PasswordInput(), label="New Password")
    new_password_confirm = CharField(widget=PasswordInput(), label="Confirm")

    def __init__(self, user, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        if not self.cleaned_data.get('new_password') == self.cleaned_data.get('new_password_confirm'):
            self.add_error('new_password_confirm', "Passwords do not match")

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data["new_password"])
        if commit:
            self.user.save()
        return self.user

@login_required
def changePassword(request):
    if request.method == 'POST':
        changePasswordForm = ChangePasswordForm(data=request.POST, user=request.user)
        if changePasswordForm.is_valid():
            changePasswordForm.save()
            return HttpResponseRedirect("/logout/")
    else:
        changePasswordForm = ChangePasswordForm(user=request.user)
    return render(request, "changePassword.html", dict(form=changePasswordForm))

def addUser(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        if uf.is_valid():
            user = uf.save()
            pf = Player(user=user)
            pf.save()
            return HttpResponseRedirect(reverse("addUserConfirm"))
    else:
        uf = UserForm(prefix='user')
    return render(request, 'addUser.html', dict(form=uf))

@login_required
def addUserConfirm(request):
    return render(request, "confirm.html", {})

class UpdatePlayer(LoginRequiredMixin, UpdateView):
    model = Player

@login_required
def RemindPassword(request):
    if request.method == 'POST':
        remindPasswordForm = RemindPasswordForm(request.POST)
        if remindPasswordForm.is_valid():
            username_mail = request.POST['username_mail']
            user = User.objects.filter(Q(username=username_mail) | Q(email=username_mail))
            if user:
                for p in user:
                    password = random_password()
                    email_text = """Hi,

New password for {0} "{1}" {2} is {3}

Tournament Calculator admin (Bartosz Skorupa)
                                 """.format(p.first_name, p.username, p.last_name, password)
                    email = EmailMessage('Tournament Calculator New password', email_text, to=[p.email],
                                         from_email="turniej@infinity.wroclaw.pl",
                                         reply_to=["bartosz@skorupa.net"])
                    email.send()
                    p.set_password(password)
                    p.save()
                return HttpResponseRedirect(reverse("RemindPassword"))
            else:
                remindPasswordForm.add_error('username_mail', u'User not found')
    else:
        remindPasswordForm = RemindPasswordForm()
    return render(request, 'RemindPassword.html', dict(form=remindPasswordForm))

class AutocompleteSkills(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Skils.objects.none()

        qs = Skils.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q).order_by('name')

        return qs

class AutocompleteTalent(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Talent.objects.none()

        qs = Talent.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q).order_by('name')

        return qs

class AutocompleteTrappings(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Trapping.objects.none()

        qs = Trapping.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q).order_by('name')

        return qs

class AutocompletePlayer(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Trapping.objects.none()

        qs = User.objects.all()

        if self.q:
            qs = qs.filter(Q(username__startswith=self.q) | Q(first_name__startswith=self.q) | Q(last_name__startswith=self.q)).order_by('last_name')

        players = Player.objects.filter(user__in=qs)
        return players

class MeleWeaponListView(LoginRequiredMixin, SingleTableView):
    model = MeleeWeapons
    table_class = MeleeWeaponsTable
    template_name = 'MeleWeaponList.html'
    paginator_class = LazyPaginator

class MeleWeaponFormView(LoginRequiredMixin, CreateView):
    template_name = "create_mele_weapon.html"
    form_class = MeleWeaponForm

class MeleWeaponEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_mele_weapon.html"
    form_class = MeleWeaponForm
    model = MeleeWeapons

class RangedWeaponListView(LoginRequiredMixin, SingleTableView):
    model = RangedWeapon
    table_class = RangedWeaponsTable
    template_name = 'RangedWeaponList.html'
    paginator_class = LazyPaginator

class RangedWeaponFormView(LoginRequiredMixin, CreateView):
    template_name = "create_ranged_weapon.html"
    form_class = RangedWeaponForm

class RangedWeaponEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_ranged_weapon.html"
    form_class = RangedWeaponForm
    model = RangedWeapon

class SpellListView(LoginRequiredMixin, SingleTableView):
    model = Spells
    table_class = SpellsTable
    template_name = 'Spellsist.html'
    paginator_class = LazyPaginator

class SpellsCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "create_spells.html"
    form_class = SpellsForm

class SpellsEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_spells.html"
    form_class = SpellsForm
    model = Spells

class SkillsListView(LoginRequiredMixin, SingleTableView):
    model = Skils
    table_class = SkillsTable
    template_name = 'list_Skills.html'
    paginator_class = LazyPaginator

class SkillsCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "create_Skills.html"
    form_class = SkillsForm

class SkillsEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_Skills.html"
    form_class = SkillsForm
    model = Skils

class TrappingsListView(LoginRequiredMixin, SingleTableView):
    model = Trapping
    table_class = TrappingTable
    template_name = 'list_Trapping.html'
    paginator_class = LazyPaginator

class TrappingssCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "create_Trapping.html"
    form_class = TrappingForm

class TrappingssEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_Trapping.html"
    form_class = TrappingForm
    model = Trapping

class TalentsListView(SingleTableView):
    model = Talent
    table_class = TalentTable
    template_name = 'list_Talent.html'
    paginator_class = LazyPaginator

class TalentsCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "create_Talent.html"
    form_class = TalentForm

class TalentsEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_Talent.html"
    form_class = TalentForm
    model = Talent

class ContainersListView(SingleTableView):
    model = Containers
    table_class = ContainerTable
    template_name = 'list_Container.html'
    paginator_class = LazyPaginator

class ContainersCreateFormView(LoginRequiredMixin, CreateView):
    template_name = "create_Container.html"
    form_class = ContainersForm

class ContainersEditView(LoginRequiredMixin, UpdateView):
    template_name = "update_Container.html"
    form_class = ContainersForm
    model = Containers

@login_required
def viewCharacter(request, pk):
    character=Character.objects.get(pk=pk)
    return render(request, 'viewCharacter.html', dict(character=character))

@login_required
def ajax_view_getCharacterData(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    ret = {'status': 'ok',
           'skills': {},
           'trappings': {},
           'containers': [],
           'armour':[],
           'spells':[],
           "weapon":[],
           "notes":[],
           'party': {
                'name': "",
                'members': [],
                'ambitions' : {
                    'short_term':[],
                    'long_term': []
                }
            },
            'talents_all': [],
            'careers_advance_scheme': {},
            'characterChangeLog': [],
            'condition': [],
        }

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)
    ret['character'] = {
            "id"                           : character.id,
            "name"                         : character.name,
            "species"                      : character.species.id,
            "ch_class"                     : character.ch_class.id,
            "career"                       : character.career.id,
            "career_level"                 : int(character.career_level),
            "age"                          : character.age,
            "height"                       : character.height,
            "career_path"                  : character.career_path.id,
            "status"                       : str(character.status),
            "hair"                         : character.hair.id,
            "eyes"                         : character.eyes.id,
            "characteristics_ws_initial"   : character.characteristics_ws_initial,
            "characteristics_bs_initial"   : character.characteristics_bs_initial,
            "characteristics_s_initial"    : character.characteristics_s_initial,
            "characteristics_t_initial"    : character.characteristics_t_initial,
            "characteristics_i_initial"    : character.characteristics_i_initial,
            "characteristics_ag_initial"   : character.characteristics_ag_initial,
            "characteristics_dex_initial"  : character.characteristics_dex_initial,
            "characteristics_int_initial"  : character.characteristics_int_initial,
            "characteristics_wp_initial"   : character.characteristics_wp_initial,
            "characteristics_fel_initial"  : character.characteristics_fel_initial,
            "characteristics_ws_advances"  : character.characteristics_ws_advances,
            "characteristics_bs_advances"  : character.characteristics_bs_advances,
            "characteristics_s_advances"   : character.characteristics_s_advances,
            "characteristics_t_advances"   : character.characteristics_t_advances,
            "characteristics_i_advances"   : character.characteristics_i_advances,
            "characteristics_ag_advances"  : character.characteristics_ag_advances,
            "characteristics_dex_advances" : character.characteristics_dex_advances,
            "characteristics_int_advances" : character.characteristics_int_advances,
            "characteristics_wp_advances"  : character.characteristics_wp_advances,
            "characteristics_fel_advances" : character.characteristics_fel_advances,
            "wounds"                       : character.wounds,
            "fate_fate"                    : character.fate_fate,
            "fate_fortune"                 : character.fate_fortune,
            "resilience_resilience"        : character.resilience_resilience,
            "resilience_resolve"           : character.resilience_resolve,
            "resilience_motivation"        : character.resilience_motivation,
            "experience_current"           : character.experience_current,
            "experience_spent"             : character.experience_spent,
            "movement_movement"            : character.movement_movement,
            "movement_walk"                : character.movement_walk,
            "movement_run"                 : character.movement_run,
            "wealth"                       : character.wealth
        }

    cas = CareersAdvanceScheme.objects.get(career = character.career)
    ret['careers_advance_scheme'] = cas.serialize()
    ret['character']["ambitions_shortterm"] = []
    for ambitions_shortterm in character.ambitions_shortterm.all():
        ret['character']["ambitions_shortterm"].append(ambitions_shortterm.to_dict())

    ret['character']["ambitions_longterm"] = []
    for ambitions_longterm in character.ambitions_longterm.all():
        ret['character']["ambitions_longterm"].append(ambitions_longterm.to_dict())

    for ss in Character2Skill.objects.filter(characters=character).all():
        # logger.debug("ss.name:{}; is_basic_skill:{}; is_species_skill:{}; is_career_skill:{}".format(ss.skills.name, ss.is_basic_skill , ss.is_species_skill, ss.is_career_skill))
        ret['skills'][ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'is_basic_skill':ss.is_basic_skill , 'is_species_skill': ss.is_species_skill, 'is_career_skill': ss.is_career_skill}

    ch2STrappingQuerySet = Character2Trapping.objects.filter(characters=character)
    ch2STrapping = list(ch2STrappingQuerySet.values_list("trapping", flat=-True))

    for trapping in Trapping.objects.all():
        # logger.debug("'id': {}, 'name': {}, 'description': {}, 'enc': {}".format(trapping.id, trapping.name, trapping.description, trapping.encumbrance))
        ret['trappings'][trapping.id] = {
            'id': trapping.id,
            'name': trapping.name,
            'description': trapping.description,
            'enc': trapping.encumbrance,
            'is_in_inventory': True if trapping.id in ch2STrapping else False,
            'container_id': get_cotainer_id(trapping, ch2STrappingQuerySet) if trapping.id in ch2STrapping else -1
        }

    for r in Armour.objects.all():
        is_in_inventory = character.armour.filter(id=r.id).exists()
        ret['armour'].append(r.to_dict(is_in_inventory))

    for hw in MeleeWeapons.objects.all():
        is_in_inventory = character.weapon.filter(id=hw.id).exists()
        ret['weapon'].append(hw.to_dict(is_in_inventory))

    for rw in RangedWeapon.objects.all():
        is_in_inventory = character.weapon.filter(id=rw.id).exists()
        ret['weapon'].append(rw.to_dict(is_in_inventory))

    for s in Spells.objects.all():
        is_in_inventory = character.spells.filter(id=s.id).exists()
        ret['spells'].append(s.to_dict(is_in_inventory))

    ret['talents'] = get_character_talents(character)

    for n in character.notes.order_by('datetime_create'):
        ret['notes'].append(n.to_dict())

    for l in CharacterChangeLog.objects.filter(character=character).order_by("id")[0:50]:
        ret['characterChangeLog'].append(l.to_dict())

    ret['party']['name'] = character.campaign.party_name
    for a in character.campaign.ambitions_shortterm.all():
        ret['party']['ambitions']['short_term'].append(a.to_dict())
    for a in character.campaign.ambitions_longterm.all():
        ret['party']['ambitions']['long_term'].append(a.to_dict())

    campaign2Player = Campaign2Player.objects.filter(campaign=character.campaign)
    for c2p in campaign2Player:
        ret['party']['members'].append(str(c2p.player))

    for cc in Character2Container.objects.filter(character=character):
        ret['containers'].append(cc.to_dict())

    for con in Condition2Character.objects.filter(characters=character):
        ret['condition'].append(con.to_dict())

    return JsonResponse(ret)

@login_required
def addPlayer2Campaign(request):
    c2p, created = Campaign2Player.objects.get_or_create(campaign_id = request.POST['campaign_id'], player_id=request.POST['campaign_2_player_lookup_channel'])
    c2p.save()

    logger.debug(str(request.POST))
    logger.debug(c2p)
    return redirect(reverse('detailsCampaign', args=(request.POST['campaign_id'],)))

@login_required
def ajax_savePlayerNote(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    note = Note.objects.create(note_text=request.POST['note_text'])
    note.author = request.user
    note.save()

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)
    character.notes.add(note)
    character.save()

    ret = {'status': 'ok', 'id': note.id, 'datetime_create': note.formated_datatime, 'timestamp': note.timestamp, 'author':note.user_name}

    return JsonResponse(ret)

@login_required
def ajax_saveCampaignAmbitions(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug("ambitions_id={}; description={}; achieved={}; camaing_id={}; is_shortterm={}".format(request.POST['ambitions_id'], request.POST['description'], request.POST['achieved'], request.POST['camaing_id'], request.POST['is_shortterm']))

    ami, created  = (Ambitions.objects.create(description=request.POST['description']), True) if int(request.POST['ambitions_id']) == 0 else (Ambitions.objects.get(id=request.POST['ambitions_id']), False)
    achieved_was = ami.achieved
    ami.achieved = True if request.POST['achieved'] == 'true' else False
    ami.save()

    logger.debug("achieved_was={} and ami.achieved={}".format(achieved_was, ami.achieved))
    if achieved_was == False and ami.achieved == True:
        for c in Character.objects.filter(campaign__id = request.POST['camaing_id']):
            logger.debug("{}".format(str(c)))
            if request.POST['is_shortterm'] == "true":
                logger.debug("{} get 50 xp".format(str(c)))
                c.experience_current += 50
            else:
                logger.debug("{} get 500 xp".format(str(c)))
                c.experience_current += 500
            c.save()


    ret = {'status': 'ok' , 'id':ami.id, 'description':ami.description}
    logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_saveCampaignNotes(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug("camaing_id={}; note={};".format(request.POST['camaing_id'], request.POST['note_text']))

    note = Note.objects.create(note_text=request.POST['note_text'])
    note.save()

    campaign = Campaign.objects.get(id=request.POST['camaing_id'])
    campaign.notes.add(note)
    campaign.save()

    ret = {'status': 'ok', 'id': note.id, 'datetime_create': note.formated_datatime, 'timestamp': note.timestamp}
    logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_saveMotivation(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.resilience_motivation = request.POST['resilience_motivation']
    character.save()
    ccl(request.user, character, "change character motivation to  {} ".format(character.resilience_motivation))
    ret = {'status': 'ok'}
    return JsonResponse(ret)

@login_required
def ajax_saveResolve(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.resilience_resolve = request.POST['resilience_resolve']
    character.save()
    ccl(request.user, character, "change character resolve to  {} ".format(character.resilience_resolve))
    ret = {'status': 'ok'}
    return JsonResponse(ret)

@login_required
def ajax_saveResilience(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.resilience_resilience = request.POST['resilience_resilience']

    ccl(request.user, character, "change character resilience to  {} ".format(character.resilience_resilience))
    character.save()
    ret = {'status': 'ok'}
    return JsonResponse(ret)

@login_required
def ajax_saveWealth(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.wealth = calc_price_to_brass(request.POST['wealth'])
    character.save()
    ret = {'status': 'ok', 'wealth': character.wealth}
    logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_fullSkillList(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    skills = []
    for s in Skils.objects.all().order_by('name'):
        skills.append({"id": s.id, "name":s.name})

    ret = {'status': 'ok', 'skills': skills}
    # logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_saveSkill2Character(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)
    character = Character.objects.get(id=request.POST['character_id'])
    c2s, crated = Character2Skill.objects.get_or_create(characters_id = request.POST['character_id'], skills_id = request.POST['skill_id'])

    skill = {'id': c2s.skills.id, 'name': c2s.skills.name, 'characteristics': c2s.skills.characteristics, 'description': c2s.skills.description, 'adv':c2s.adv, 'is_basic_skill':c2s.is_basic_skill , 'is_species_skill': c2s.is_species_skill, 'is_career_skill': c2s.is_career_skill}
    ccl(request.user, character, "add skil to character {} with adv = {}".format(c2s.skills.name, c2s.adv))
    ret = {'status': 'ok', 'skill': skill, 'crated':crated}
    # logger.debug(ret)
    return JsonResponse(ret)

@login_required
def ajax_saveExperience_current(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.experience_current = request.POST['experience_current']
    character.save()
    ccl(request.user, character, "change character current experience to  {} ".format(character.experience_current))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_saveExperience_spent(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['character_id']
    character = Character.objects.get(id = character_id)

    character.experience_spent = request.POST['experience_spent']
    character.save()
    ccl(request.user, character, "change character spend experience to  {} ".format(character.experience_spent))
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

@login_required
def ajax_getSpeciesList(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    speciesList = []
    for species in Species.objects.all().order_by("name"):
        speciesList.append({'id':species.id, "name": species.name})

    ret = {'status': 'ok', "species":speciesList}
    return JsonResponse(ret)

@login_required
def ajax_getClassList(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    cList = {}
    for c in Class.objects.all().order_by("name"):
        cList[c.id] = c.to_dict()

    ret = {'status': 'ok', "character_class":cList}
    return JsonResponse(ret)

@login_required
def ajax_getHairList(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])

    hairsList = {}
    for c in Hair.objects.filter(species=c.species).order_by("name"):
        hairsList[c.id] = c.to_dict()

    ret = {'status': 'ok', "hair":hairsList}
    return JsonResponse(ret)

@login_required
def ajax_getEyesList(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])

    eyesList = {}
    for c in Eyes.objects.filter(species=c.species).order_by("name"):
        eyesList[c.id] = c.to_dict()

    ret = {'status': 'ok', "eyes":eyesList}
    return JsonResponse(ret)

@login_required
def ajax_removeAmbitions(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    res = Ambitions.objects.get(id=request.POST['ambition_id']).delete()
    logger.debug("remove ambition id:{}; res={}".format(request.POST['ambition_id'], res))
    ccl(request.user, c, "remove ambitions {}".format(res))
    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_removeWeapon(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])
    weapon = Weapon.objects.get(id = request.POST['weapon_id'])
    c.weapon.remove(weapon)
    ccl(request.user, c, "remove weapon {}".format(weapon))
    logger.debug("remove weapon {} from {}".format(weapon, c))

    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_removeArmour(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])
    armour = Armour.objects.get(id = request.POST['armour_id']);
    c.armour.remove(armour)
    ccl(request.user, c, "remove armour \"{}\".".format(armour))
    logger.debug("remove armour {} from {}".format(armour, c))

    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_removeTrappings(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    ch2t =Character2Trapping.objects.get(characters_id= request.POST['character_id'], trapping_id=request.POST['trapping_id'])
    ccl(request.user, ch2t.characters, "remove Trapping \"{}\".".format(ch2t.trapping))

    ch2t.delete()
    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_removeSpells(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])
    spells = Spells.objects.get(id = request.POST['spells_id']);
    c.spells.remove(spells)
    ccl(request.user, c, "remove spell \"{}\".".format(spells))
    logger.debug("remove spells {} from {}".format(spells, c))

    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_saveTraping2Container(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character2Trapping,created = Character2Trapping.objects.get_or_create(characters_id = request.POST['character_id'], trapping_id = request.POST['trapping_id'])

    logger.debug(f"{request.POST['character2container_id']}, {created}, {character2Trapping}")

    if int(request.POST['character2container_id']) is not -1:
        character2Container = Character2Container.objects.get(id=request.POST['character2container_id'])
        character2Trapping.container = character2Container
    else:
        character2Trapping.container = None
    character2Trapping.save()

    logger.debug(f"created={created}; character_id: {request.POST['character_id']}; trapping_id: {request.POST['trapping_id']}; character2container_id: {request.POST['character2container_id']}")

    ret = {'status': 'ok', }
    return JsonResponse(ret)

@login_required
def ajax_get_fullConditionsList(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    ret = {'status': 'ok', 'conditions':[]}

    for c in Condition.objects.all():
        ret['conditions'].append({'id':c.id, 'name': c.name, 'description': c.description})

    return JsonResponse(ret)

@login_required
def ajax_updateConditionOccurrence(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    c = Character.objects.get(id = request.POST['character_id'])
    con = Condition.objects.get(id = request.POST['condition_id'])

    c2c, created = Condition2Character.objects.get_or_create(characters=c, condition=con)
    c2c.occurrence = request.POST['cccurrence']
    c2c.save()

    ccl(request.user, c, f"update condition {con} to {c2c.occurrence}")
    ret = {'status': 'ok'}
    return JsonResponse(ret)