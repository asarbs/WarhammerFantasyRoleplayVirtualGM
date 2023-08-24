import django
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.forms import Form
from django.forms import CharField
from django.forms import PasswordInput
from django.views.generic.edit import UpdateView
from django.db.models import Q

import random
import math
import json

from django.urls import reverse

from dal import autocomplete

import logging
logger = logging.getLogger(__name__)


from WarhammerFantasyRoleplayVirtualGM_app.forms import UserForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import RemindPasswordForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import CreateCampaignForm
from WarhammerFantasyRoleplayVirtualGM_app.models import Player
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign2Player
from WarhammerFantasyRoleplayVirtualGM_app.models import Skils
from WarhammerFantasyRoleplayVirtualGM_app.models import Character
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Skill
from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import ExampleName
from WarhammerFantasyRoleplayVirtualGM_app.models import Career
from WarhammerFantasyRoleplayVirtualGM_app.models import RandomAttributesTable
from WarhammerFantasyRoleplayVirtualGM_app.models import Eyes
from WarhammerFantasyRoleplayVirtualGM_app.models import Hair
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import Trapping
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import CareersAdvanceScheme

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


def addCharacter(request):
    basic_skills_criterion1 = Q(id__gte = 1)
    basic_skills_criterion2 = Q(id__lte = 26)
    basic_skills = Skils.objects.filter(basic_skills_criterion1 & basic_skills_criterion2).order_by("name").values()
    player = Player.objects.get(user=request.user)
    character = Character(player=player)
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
        character_id = request.POST['characer_id']
        species_id = request.POST['species_id']
        species = Species.objects.get(id=species_id)
        eyes_rand = random.randrange(1, 10) + random.randrange(1, 10)
        hair_rand = random.randrange(1, 10) + random.randrange(1, 10)

        q_species = Q(species=species)

        character = Character.objects.get(id = character_id)
        character.species = Species.objects.get(id = species_id)
        character.eyes = Eyes.objects.get(q_species & Q(random_table_start__lte = eyes_rand) & Q(random_table_end__gte = eyes_rand))
        character.hair = Hair.objects.get(q_species & Q(random_table_start__lte = hair_rand) & Q(random_table_end__gte = hair_rand))
        character.age = get_age(species.name)
        character.height = get_height(species.name)
        character.save()

        species_skills = {}

        Character2Skill.objects.filter(characters=character, type=Character2Skill.SkillType.NORMAL_SKILL).delete()
        basic_skills = Character2Skill.objects.filter(characters=character)
        for ss in basic_skills.all():
            species_skills[ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'type': 'basic_skill'}

        created = -1
        for ss in species.skills.all():
            species_skills[ss.id] = {'id': ss.id, 'name': ss.name, 'characteristics': ss.characteristics, 'description': ss.description, 'adv': 0, 'type': 'species_skill'}
            try:
                ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0, type=Character2Skill.SkillType.NORMAL_SKILL)
                ch2Skill.save()
            except django.db.utils.IntegrityError as e:
                logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

        Character2Talent.objects.filter(characters=character).delete()
        species_tallents = get_species_tallens(species)
        for st in species_tallents:
            ch2t, created = Character2Talent.objects.get_or_create(characters=character, talent_id=st['id'], taken=0)
            ch2t.save()

        return JsonResponse({'status': 'ok', 'species_id': species_id, 'eyes': character.eyes.id, 'hair': character.hair.id, 'age': character.age, 'height': character.height, 'species_skills': species_skills, 'species_tallents':species_tallents})
    logger.error("ajax_save_character_species is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_randomSpecies(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        character = Character.objects.get(id = character_id)
        species_list = Species.objects.all()
        r = random.randrange(1, 100)
        eyes_rand = random.randrange(1, 10) + random.randrange(1, 10)
        hair_rand = random.randrange(1, 10) + random.randrange(1, 10)
        species = None
        for s in species_list:
            if r >= s.random_interal_start and r <= s.random_interal_end:
                species = s
                break

        names = ExampleName.objects.filter(species = species)
        name = names[random.randrange(0, len(names))]

        q_species = Q(species=species)

        character.name = name.name
        character.species = species
        character.eyes = Eyes.objects.get(q_species & Q(random_table_start__lte = eyes_rand) & Q(random_table_end__gte = eyes_rand))
        character.hair = Hair.objects.get(q_species & Q(random_table_start__lte = hair_rand) & Q(random_table_end__gte = hair_rand))
        character.age = get_age(species.name)
        character.height = get_height(species.name)
        character.save()

        species_skills = {}
        Character2Skill.objects.filter(characters=character, is_basic_skill=False, is_species_skill=True, is_carrer_skill=True).delete()
        basic_skills = Character2Skill.objects.filter(characters=character)
        for ss in basic_skills.all():
            species_skills[ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'is_basic_skill':ss.is_basic_skill , 'is_species_skill': ss.is_species_skill, 'is_carrer_skill': ss.is_carrer_skill}
        created = -1

        for ss in species.skills.all():
            try:
                ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0)
                ch2Skill.is_species_skill = True
                ch2Skill.save()
                species_skills[ss.id] = {'id': ch2Skill.skills.id, 'name': ch2Skill.skills.name, 'characteristics': ch2Skill.skills.characteristics, 'description': ch2Skill.skills.description, 'adv': ch2Skill.adv , 'is_basic_skill':ch2Skill.is_basic_skill , 'is_species_skill': ch2Skill.is_species_skill, 'is_carrer_skill': ch2Skill.is_carrer_skill}
            except django.db.utils.IntegrityError as e:
                logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

        species_tallents = get_species_tallens(species)
        Character2Talent.objects.filter(characters=character).delete()
        for st in species_tallents:
            ch2t, created = Character2Talent.objects.get_or_create(characters=character, talent_id=st['id'], taken=0)
            ch2t.save()

        res = {'status': 'ok',
               'species_id': species.id,
               'name': name.name,
               'eyes': character.eyes.id,
               'hair': character.hair.id,
               'age': character.age,
               'height': character.height,
               'species_skills': species_skills,
               'species_tallents':species_tallents
               }

        return JsonResponse(res)
    logger.error("ajax_randomSpecies is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

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

            for ss in CareersAdvanceScheme.objects.get(career=career).advances_level_1.skills:
                try:
                    ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0)
                    ch2Skill.is_carrer_skill = True
                    ch2Skill.save()
                except django.db.utils.IntegrityError as e:
                    logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

            skills = {}
            for ss in Character2Skill.objects.get(character=character):
                skills[ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'is_basic_skill':ss.is_basic_skill , 'is_species_skill': ss.is_species_skill, 'is_carrer_skill': ss.is_carrer_skill}


            return JsonResponse({'status': 'ok',
                                 'career_name': career.name,
                                 'ch_class_name': character.ch_class.name,
                                 'skills': skills
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
    if request.method == 'POST':
        rat = RandomAttributesTable.objects.all()
        ret = {'attributesTable':{}, 'eyesTable': {}, 'hairTable': {}}
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

        # logger.debug(ret)
        return JsonResponse(ret)
    logger.error("ajax_randomClass is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_saveAttributes(request):
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
        print(request.POST)
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
        character = Character.objects.get(id = character_id)
        if character is not None:
            hair, created = Hair.objects.get_or_create(name=request.POST['hair'])
            if created:
                character.hair    = hair
                character.save()
                ret = {'status': 'ok'  }
                logger.debug(ret)
                return JsonResponse(ret)
            else :
                logger.error("ajax_saveHair: hair:{}; character_id:{}".format(request.POST['hair'],character_id ))
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
            eye_color, created = Eyes.objects.get_or_create(name=request.POST['eyes'])
            if created:
                character.eyes    = eye_color
                character.save()
                ret = {'status': 'ok'  }
                logger.debug(ret)
                return JsonResponse(ret)
            else :
                logger.error("ajax_saveEyes: eyesColor:{}; character_id:{}".format(request.POST['eyes'],character_id ))
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

def detailsCampaign(request, CampaignId):
    c = Campaign.objects.get(id=CampaignId)
    dic ={'camaing': c}
    return render(request, 'detailsCampaign.html', dic)


def showCareersAdvanceSchemes(request, casId):
        cas = CareersAdvanceScheme.objects.get(id=casId)
        return render(request, 'showCareersAdvanceSchemes.html', {'cas':cas} )

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
