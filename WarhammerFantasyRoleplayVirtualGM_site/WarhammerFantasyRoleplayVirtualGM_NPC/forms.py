from django.forms import ModelForm
from django.contrib.admin import site as admin_site
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

import logging
logger = logging.getLogger(__name__)

from . import models

class NPCForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(NPCForm, self).__init__(*args, **kwargs)
        self.fields['creatureTraits'].widget =  (RelatedFieldWidgetWrapper(self.fields['creatureTraits'].widget, self.instance._meta.get_field('creatureTraits').remote_field,  admin_site))
        self.fields['skills'].widget =          (RelatedFieldWidgetWrapper(self.fields['skills'].widget,         self.instance._meta.get_field('skills').remote_field,          admin_site))
        self.fields['talents'].widget =         (RelatedFieldWidgetWrapper(self.fields['talents'].widget,        self.instance._meta.get_field('talents').remote_field,         admin_site))
        self.fields['trappings'].widget =       (RelatedFieldWidgetWrapper(self.fields['trappings'].widget,      self.instance._meta.get_field('trappings').remote_field,       admin_site))

    class Meta:
        model = models.NPC
        fields = [
            "name",
            "species",
            "portrait",
            "characteristics_m",
            "characteristics_ws",
            "characteristics_bs",
            "characteristics_s",
            "characteristics_t",
            "characteristics_i",
            "characteristics_ag",
            "characteristics_dex",
            "characteristics_int",
            "characteristics_wp",
            "characteristics_fel",
            "characteristics_w",
            "skills",
            "talents",
            "weapons",
            "trappings",
            "creatureTraits"]