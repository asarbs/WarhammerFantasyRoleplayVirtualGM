from collections.abc import Sequence
from typing import Any
from django.forms import CharField
from django.forms.widgets import Widget

import math

from WarhammerFantasyRoleplayVirtualGM_app.character_creations_helpers import format_currency
from WarhammerFantasyRoleplayVirtualGM_app.character_creations_helpers import calc_price_to_brass



class PriceCharFiled(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def prepare_value(self, wealth):
        if wealth is None:
            return "{} GC{}/{}".format(0, 0, 0)
        if isinstance(wealth, str):
            return calc_price_to_brass(wealth)
        elif isinstance(wealth, int):
            return format_currency(wealth)
        raise ValueError("wealth: \"{}\" is type {} expected int or str".format(wealth, type(wealth)))