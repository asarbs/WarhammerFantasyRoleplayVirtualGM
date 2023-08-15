import random

import logging
logger = logging.getLogger(__name__)


def random_d10(amo:int) :
    return sum( random.randrange(1, 10) for x in range(amo))

def get_age(species: str):
    logger.debug("species:{}".format(species))
    if species == "Human":
        return 15 + random_d10(1)
    elif species == "Dwarf":
        return 15 + random_d10(10)
    elif species == "Halfling":
        return 15 + random_d10(5)
    elif species in ("High Elf", "Wood Elf"):
        return 30 + random_d10(10)
    return -1

def get_height(species: str):
    logger.debug("species:{}".format(species))
    if species == "Human":
        return 145 + random_d10(2)
    elif species == "Dwarf":
        return 130 + random_d10(1)
    elif species == "Halfling":
        return 15 + random_d10(1)
    elif species in ("High Elf", "Wood Elf"):
        return 94 + random_d10(1)
    return -1