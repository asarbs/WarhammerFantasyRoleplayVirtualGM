import django
from django.forms.models import BaseModelForm
from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator
from django.db.models import Q
from django.forms import CharField
from django.forms import Form
from django.forms import PasswordInput
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from pprint import pformat

import random
import math
import json

from django.urls import reverse

from dal import autocomplete

import logging
logger = logging.getLogger(__name__)


from WarhammerFantasyRoleplayVirtualGM_app.forms import CreateCampaignForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import MeleWeaponForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import RangedWeaponForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import RemindPasswordForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import SpellsForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import UserForm
from WarhammerFantasyRoleplayVirtualGM_app.models import *
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign2Player
from WarhammerFantasyRoleplayVirtualGM_app.models import Career
from WarhammerFantasyRoleplayVirtualGM_app.models import CareersAdvanceScheme
from WarhammerFantasyRoleplayVirtualGM_app.models import Character
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Skill
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import ClassTrappings
from WarhammerFantasyRoleplayVirtualGM_app.models import ExampleName
from WarhammerFantasyRoleplayVirtualGM_app.models import Eyes
from WarhammerFantasyRoleplayVirtualGM_app.models import Hair
from WarhammerFantasyRoleplayVirtualGM_app.models import Player
from WarhammerFantasyRoleplayVirtualGM_app.models import RandomAttributesTable
from WarhammerFantasyRoleplayVirtualGM_app.models import Skils
from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import Trapping
from WarhammerFantasyRoleplayVirtualGM_app.tables import MeleeWeaponsTable
from WarhammerFantasyRoleplayVirtualGM_app.tables import RangedWeaponsTable
from WarhammerFantasyRoleplayVirtualGM_app.tables import SpellsTable

from WarhammerFantasyRoleplayVirtualGM_app.character_creations_helpers import *


# Create your views here.
from django.http import HttpResponse


def index(request):
    data = {}
    return render(request, 'main/main.html', data)

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

def addCharacter(request, CampaignId):
    basic_skills_criterion1 = Q(id__gte = 1)
    basic_skills_criterion2 = Q(id__lte = 26)
    basic_skills = Skils.objects.filter(basic_skills_criterion1 & basic_skills_criterion2).order_by("name").values()
    player = Player.objects.get(user=request.user)
    character = Character(player=player, campaign_id = CampaignId)
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


    context = {
        'characker_id': character.id,
        'basic_skills': basic_skills,
        'species': species
        }
    return render(request, 'addCharacter.html',context)

def ajax_save_character_species(request):
    if request.method == 'POST':
        species_id = request.POST['species_id']
        species = Species.objects.get(id=species_id)
        return set_character_species(species=species, character_id=request.POST['characer_id'])
    logger.error("ajax_save_character_species is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_randomSpecies(request):
    if request.method == 'POST':
        species_list = Species.objects.all()
        r = random.randrange(1, 100)
        species = None
        for s in species_list:
            if r >= s.random_interal_start and r <= s.random_interal_end:
                species = s
                break
        return set_character_species(species=species, character_id=request.POST['characer_id'])

    logger.error("ajax_randomSpecies is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_addTalentToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['characer_id']
    talent_id = request.POST['new_talent_id']
    try:
        char2tal, created = Character2Talent.objects.get_or_create(characters_id=character_id, talent_id=talent_id, taken=1)
        char2tal.save();
    except django.db.utils.IntegrityError as e:
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character_id, char2tal.talent.name, created))
    return JsonResponse({'status': 'ok'})

def ajax_replaceTalentToCharacter(request):
    if not request.method == 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    character_id = request.POST['characer_id']
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
        logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))
    talents = get_character_talents(Character.objects.get(id = character_id))
    return JsonResponse({'status': 'ok', 'talents': talents})

def ajax_randomClass(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
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
            character.save()

            Character2Skill.objects.filter(characters=character, is_career_skill = True).delete()
            ad = CareersAdvanceScheme.objects.get(career=career).advances_level_1
            for ss in ad.skills.all():
                try:
                    ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0)
                    ch2Skill.is_career_skill = True
                    ch2Skill.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

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



            Character2Trappingl.objects.filter(characters=character, is_career_skill = True).delete()
            for classTraping in ClassTrappings.objects.filter(ch_class=career.ch_class).all():
                try:
                    ch2STrappingl, created = Character2Trappingl.objects.get_or_create(characters=character, trapping=classTraping.trapping, enc=classTraping.trapping.encumbrance)
                    logger.debug("ClassTrappings.trapping.id={} name={};".format(classTraping.trapping.id, classTraping.trapping.name))
                    ch2STrappingl.is_career_skill = True
                    ch2STrappingl.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} Trappings:{} created:{}".format(character.id, classTraping.trapping.name, created))

            for trapping in ad.trappings.all():
                try:
                    ch2STrappingl, created = Character2Trappingl.objects.get_or_create(characters=character, trapping=trapping, enc=trapping.encumbrance)
                    ch2STrappingl.is_career_skill = True
                    ch2STrappingl.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} Trappings:{} created:{}".format(character.id, trapping.name, created))

            trappings = {}
            for ch2STrappingl in Character2Trappingl.objects.filter(characters=character).all():
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

def ajax_saveName(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        character = Character.objects.get(id = character_id)

        if character is not None:
            character.name = request.POST['name']
            logger.debug("character name: {}".format(character.name))
            character.save()
            return JsonResponse({'status': 'ok', 'name': character.name})
        else:
            logger.error("ajax_saveName character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_randomClass is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

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

def ajax_randomAttributes(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
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

def ajax_saveAttribute(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
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

def ajax_saveFate_and_fortune(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
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

def ajax_saveAge(request):
    if request.method == 'POST':
        logger.debug(request.POST)
        character_id = request.POST['characer_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            character.age    = int(request.POST['age'])
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveAge not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveAge is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_saveHeight(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            character.height    = int(request.POST['height'])
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveHeight not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveHeight is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_saveHair(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        hair = request.POST['hair']
        character = Character.objects.get(id = character_id)
        if character is not None:
            hair = Hair.objects.get(id=hair)
            character.hair    = hair
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveHair not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveHair is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_saveEyes(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        character = Character.objects.get(id = character_id)
        if character is not None:
            eye_color = Eyes.objects.get(name=request.POST['eyes'])
            character.eyes = eye_color
            character.save()
            ret = {'status': 'ok'  }
            logger.debug(ret)
            return JsonResponse(ret)
        else:
            logger.error("ajax_saveEyes not found: character_id={}".format(character_id))
            return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.error("ajax_saveEyes is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_saveSkillAdv(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        logger.info(request.POST)
        # logger.info("character_id={}; skill_id={}; points={}; old_skill_adv={}".format(character_id, request.POST['skill_id'], request.POST['points'], request.POST['old_skill_adv']))
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

def ajax_getCareersAdvanceScheme(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)
    logger.debug(request.POST)

    cas = CareersAdvanceScheme.objects.get(career__id = request.POST['career_id'])
    ret = {'status': 'ok', 'careersAdvanceScheme': cas.serialize() }
    return JsonResponse(ret)

def ajax_addArmourToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['characer_id']
    character = Character.objects.get(id = character_id)
    character.armour.add(Armour.objects.get(id=request.POST['armour_id']))
    character.save()
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

def ajax_addWeaponToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['characer_id']
    character = Character.objects.get(id = character_id)
    character.weapon.add(Weapon.objects.get(id=request.POST['weapon_id']))
    character.save()
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

def ajax_addSpellsToCharacter(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['characer_id']
    character = Character.objects.get(id = character_id)
    character.spells.add(Spells.objects.get(id=request.POST['spell_id']))
    character.save()
    ret = {'status': 'ok'  }
    return JsonResponse(ret)

def ajax_saveSkillsXPSpend(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['characer_id']
    character = Character.objects.get(id = character_id)

    c2s = Character2Skill.objects.get(characters = character, skills__id = request.POST['skill_id'])
    c2s.adv = request.POST['newVal']
    c2s.save()

    character.experience_current = request.POST['experience_current']
    character.experience_spent = request.POST['experience_spent']
    character.save()

    ret = {'status': 'ok'  }
    return JsonResponse(ret)

def ajax_saveTalentXPSpend(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'Invalid request'}, status=400)

    logger.debug(request.POST)

    character_id = request.POST['characer_id']
    character = Character.objects.get(id = character_id)

    c2t = Character2Talent.objects.get(characters = character, skills__id = request.POST['tallent_id'])
    c2t.adv = request.POST['newVal']
    c2t.save()

    character.experience_current = request.POST['experience_current']
    character.experience_spent = request.POST['experience_spent']
    character.save()

    ret = {'status': 'ok'  }
    return JsonResponse(ret)

def detailsCampaign(request, CampaignId):
    c = Campaign.objects.get(id=CampaignId)
    players = []
    for c2p in Campaign2Player.objects.filter(campaign=c):
        players.append(c2p.player)
    characters = Character.objects.filter(campaign=c, player__in=players)
    dic ={'camaing': c, "players":players, "characters": characters}
    logging.debug(dic)
    return render(request, 'detailsCampaign.html', dic)

def showCareersAdvanceSchemes(request, casId):
        cas = CareersAdvanceScheme.objects.get(id=casId)
        return render(request, 'showCareersAdvanceSchemes.html', {'cas':cas} )

def listCareersAdvanceSchemes(request):
    cas = CareersAdvanceScheme.objects.all()
    return render(request, 'listCareersAdvanceSchemes.html', {'cas':cas} )

class ChangePasswordForm(Form):
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

def addUserConfirm(request):
    return render(request, "confirm.html", {})

class UpdatePlayer(UpdateView):
    model = Player

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

class MeleWeaponListView(SingleTableView):
    model = MeleeWeapons
    table_class = MeleeWeaponsTable
    template_name = 'MeleWeaponList.html'
    paginator_class = LazyPaginator

class MeleWeaponFormView(CreateView):
    template_name = "create_mele_weapon.html"
    form_class = MeleWeaponForm

class MeleWeaponEditView(UpdateView):
    template_name = "update_mele_weapon.html"
    form_class = MeleWeaponForm
    model = MeleeWeapons

class RangedWeaponListView(SingleTableView):
    model = RangedWeapon
    table_class = RangedWeaponsTable
    template_name = 'RangedWeaponList.html'
    paginator_class = LazyPaginator

class RangedWeaponFormView(CreateView):
    template_name = "create_ranged_weapon.html"
    form_class = RangedWeaponForm

class RangedWeaponEditView(UpdateView):
    template_name = "update_ranged_weapon.html"
    form_class = RangedWeaponForm
    model = RangedWeapon

class SpellListView(SingleTableView):
    model = Spells
    table_class = SpellsTable
    template_name = 'Spellsist.html'
    paginator_class = LazyPaginator

class SpellsCreateFormView(CreateView):
    template_name = "create_spells.html"
    form_class = SpellsForm

class SpellsEditView(UpdateView):
    template_name = "update_spells.html"
    form_class = SpellsForm
    model = Spells
