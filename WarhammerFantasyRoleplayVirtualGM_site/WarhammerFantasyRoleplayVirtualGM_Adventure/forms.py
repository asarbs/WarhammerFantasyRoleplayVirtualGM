from django.forms import ModelForm
from django.contrib.admin import site as admin_site
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper

import logging
logger = logging.getLogger(__name__)

from . import models

class AdventureForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AdventureForm, self).__init__(*args, **kwargs)
        self.fields['npcs'].widget = (
            RelatedFieldWidgetWrapper(self.fields['npcs'].widget, self.instance._meta.get_field('npcs').remote_field, admin_site)
            
        )
    
    class Meta:
        model = models.Adventure
        fields = ['name', 'campaign', 'npcs']