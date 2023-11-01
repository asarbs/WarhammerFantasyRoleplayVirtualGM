import random
import math

import django
from django.http import JsonResponse
from django.db.models import Q

from WarhammerFantasyRoleplayVirtualGM_app.models import Character
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Skill
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import ExampleName
from WarhammerFantasyRoleplayVirtualGM_app.models import Eyes
from WarhammerFantasyRoleplayVirtualGM_app.models import Hair
from WarhammerFantasyRoleplayVirtualGM_app.models import RandomTalentsTable
from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent

import logging
logger = logging.getLogger(__name__)


def random_d10(amo:int) :
    return sum( random.randrange(1, 10) for x in range(amo))

def get_age(species: str):
    if species == "Human  (Reiklander)":
        return 15 + random_d10(1)
    elif species == "Dwarf":
        return 15 + random_d10(10)
    elif species == "Halfling":
        return 15 + random_d10(5)
    elif species in ("High Elf", "Wood Elf"):
        return 30 + random_d10(10)
    return -1

def get_height(species: str):
    if species == "Human  (Reiklander)":
        return 145 + random_d10(2)
    elif species == "Dwarf":
        return 130 + random_d10(1)
    elif species == "Halfling":
        return 15 + random_d10(1)
    elif species in ("High Elf", "Wood Elf"):
        return 94 + random_d10(1)
    return -1

def get_species_tallens(speceies: Species):
    species_talents = list(speceies.talents.all())
    talens = list(RandomTalentsTable.objects.all())
    if speceies.id == 2:
        rs = random.sample(talens, 3)
        species_talents = species_talents + rs
    elif speceies.id == 3:
        rs = random.sample(talens, 2)
        species_talents = species_talents + rs
    species_talents_list = []

    for st in species_talents:
        dic_talent = {
            'id': st.my_talent_id,
            'name': st.name,
            'max':  st.max,
            'tests': st.tests,
            'description': st.description,
            'ref': str(st.ref)
        }
        species_talents_list.append(dic_talent)
    return species_talents_list

def get_character_talents(character: Character):
    character_talents = {}
    for st in Character2Talent.objects.filter(characters=character):
        character_talents[st.talent.my_talent_id] = st.taken

    talents_list = []
    for t in Talent.objects.all():
        dic_talent = {
            'id': t.my_talent_id,
            'name': t.name,
            'max':  t.max,
            'tests': t.tests,
            'description': t.description,
            'taken': (character_talents[t.my_talent_id] if t.my_talent_id in character_talents else 0),
            'ref': str(st.talent.ref)
        }
        talents_list.append(dic_talent)
    return talents_list

def set_character_species(species: Species, character_id: int):
        character = Character.objects.get(id = character_id)
        eyes_rand = random.randrange(1, 10) + random.randrange(1, 10)
        hair_rand = random.randrange(1, 10) + random.randrange(1, 10)

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
        Character2Skill.objects.filter(characters=character, is_basic_skill=False, is_species_skill=True, is_career_skill=True).delete()
        basic_skills = Character2Skill.objects.filter(characters=character)
        for ss in basic_skills.all():
            species_skills[ss.skills.id]= {'id': ss.skills.id, 'name': ss.skills.name, 'characteristics': ss.skills.characteristics, 'description': ss.skills.description, 'adv':ss.adv, 'is_basic_skill':ss.is_basic_skill , 'is_species_skill': ss.is_species_skill, 'is_career_skill': ss.is_career_skill}
        created = -1

        for ss in species.skills.all():
            try:
                ch2Skill, created = Character2Skill.objects.get_or_create(characters=character, skills=ss, adv=0)
                ch2Skill.is_species_skill = True
                ch2Skill.save()
                species_skills[ss.id] = {'id': ch2Skill.skills.id, 'name': ch2Skill.skills.name, 'characteristics': ch2Skill.skills.characteristics, 'description': ch2Skill.skills.description, 'adv': ch2Skill.adv , 'is_basic_skill':ch2Skill.is_basic_skill , 'is_species_skill': ch2Skill.is_species_skill, 'is_career_skill': ch2Skill.is_career_skill}
            except django.db.utils.IntegrityError as e:
                logger.debug("UNIQUE constraint failed: characters:{} skill:{} created:{}".format(character.id, ss.name, created))

        species_tallents = get_species_tallens(species)

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

def format_currency(p: int):
    GC = math.floor(p / 240)
    GC_left = p % 240
    SC = math.floor(GC_left / 12)
    SC_left = GC_left % 12
    BC = SC_left

    out = ""
    if GC > 0:
        out += "{}GC ".format(GC)
    if SC > 0:
        out += "{}/".format(SC)
    if GC == 0 and SC > 0 and BC == 0:
        out += "0"
    if BC > 0:
        out += "{} ".format(BC)

    logger.debug("{} -> {}".format(p, out))
    return out

def calc_price_to_brass(price_str):
    price_str = price_str.replace(' ', '')
    if 'GC' not in price_str:
        price_str = "0GC" + price_str
    if "/" not in price_str:
        price_str = price_str + "0/0"
    split = [p.strip() for p in price_str.split("GC")]
    split = [p.split("/") for p in split]
    split = sum(split, [])
    split = [ int(p) for p in split]
    return split[0] * 240 + split[1] * 12 + split[2]

