import random

from WarhammerFantasyRoleplayVirtualGM_app.models import Species
from WarhammerFantasyRoleplayVirtualGM_app.models import Talent
from WarhammerFantasyRoleplayVirtualGM_app.models import RandomTalentsTable

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
