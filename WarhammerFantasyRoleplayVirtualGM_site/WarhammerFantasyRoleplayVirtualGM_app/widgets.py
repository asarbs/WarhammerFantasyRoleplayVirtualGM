from collections.abc import Sequence
from typing import Any
from django.forms import CharField
from django.forms.widgets import Widget

import math



class PriceCharFiled(CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def prepare_value(self, wealth):
        GC = math.floor(wealth / 240)
        GC_left = wealth % 240
        SC = math.floor(GC_left / 12)
        SC_left = GC_left % 12
        BC = SC_left
        return "{} GC {}/{}".format(GC, SC, BC)