from ajax_select import register, LookupChannel
from ajax_select.fields import AutoCompleteSelectField
from django.contrib.admin import site as admin_site
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.contrib.auth.models import User
from django.core import validators
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.forms import BaseInlineFormSet
from django.forms import CharField
from django.forms import Form
from django.forms import HiddenInput
from django.forms import inlineformset_factory
from django.forms import ModelForm
from django.forms import PasswordInput
from django.forms.utils import ErrorList



from dal import autocomplete

import logging
logger = logging.getLogger(__name__)

from . import models

class UserForm(ModelForm):
    password = CharField(widget=PasswordInput())
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        exclude = ('user_permissions', 'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined', 'groups')

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class RemindPasswordForm(Form):
    username_mail = CharField(label="User Name / E-mail")

class CreateCampaignForm(ModelForm):
    class Meta:
        model = models.Campaign
        fields = ['name', 'party_name']

class SpeciesForm(ModelForm):
    class Meta:
        model = models.Species
        fields = ('__all__')
        widgets = {
            'skills': autocomplete.ModelSelect2Multiple(url='skills-autocomplete'),
            'talents': autocomplete.ModelSelect2Multiple(url='talent-autocomplete')
        }

class CareerPathForm(ModelForm):
    class Meta:
        model = models.CareerPath
        fields = ('__all__')
        widgets = {
            'skills': autocomplete.ModelSelect2Multiple(url='skills-autocomplete'),
            'talents': autocomplete.ModelSelect2Multiple(url='talent-autocomplete'),
            'trappings': autocomplete.ModelSelect2Multiple(url='trappings-autocomplete')
        }

class ClassTrappingsForm(ModelForm):
    class Meta:
        model = models.ClassTrappings
        fields = ('__all__')
        widgets = {
            'trapping': autocomplete.ModelSelect2(url='trappings-autocomplete')
        }


@register('campaign_2_player_lookup_channel')
class Campaign2PlayerFormLookupChannel(LookupChannel):
    def get_query(self, q, request):
        qs = User.objects.all()
        if q:
            qs = qs.filter(Q(username__startswith=q) | Q(first_name__startswith=q) | Q(last_name__startswith=q)).order_by('last_name')
        players = models.Player.objects.filter(user__in=qs)
        return players

    def format_item_display(self, item):
        return "<span class='campaign_2_player'>{}</span>".format(str(item))


class Campaign2PlayerForm(ModelForm):
    class Meta:
        model = models.Campaign2Player
        fields = ()
    campaign_2_player_lookup_channel = AutoCompleteSelectField('campaign_2_player_lookup_channel', label="Add Player to Campain")


def validator_price(price):
    if price.endswith("GC"):
        return
    elif price.endswith("/-"):
        return
    elif  price.endswith("d"):
        return
    elif price.isdigit():
        return
    else:
        raise ValidationError("Price should ends with GC, /-, d");

class MeleWeaponForm(ModelForm):
    price = CharField(validators=[validator_price], help_text="Price should ends with GC, /-, d")

    def __init__(self, *args, **kwargs):
        super(MeleWeaponForm, self).__init__(*args, **kwargs)
        self.fields['reference'].widget = (
            RelatedFieldWidgetWrapper(self.fields['reference'].widget, self.instance._meta.get_field('reference').remote_field, admin_site)
        )


    class Meta:
        model = models.MeleeWeapons
        fields = ["name", "weapon_group", "price", "encumbrance", "availability", "damage", "qualities_and_flaws", "reach", "reference"]

    def calc_price_to_brass(self):
        logger.debug("price:{}".format(self.data['price']))
        price = self.data['price']
        if price.endswith("GC"):
            price_int = int(price[0:-2])
            self.data['price'] = price_int * 240
            return True
        elif price.endswith("/-"):
            price_int = int(price[0:-2])
            self.data['price'] = price_int * 12
            return True
        elif  price.endswith("d"):
            price_int = int(price[0:-1])
            self.data['price'] = price_int
            return True
        logger.error("price: {} [type:{}] is invalid for conversion".format(price, type(price)))
        return False

    def is_valid(self) -> bool:
        self.data._mutable = True
        price_calc = self.calc_price_to_brass()
        self.data._mutable = False
        valid = super(MeleWeaponForm,self).is_valid()
        logger.debug("price:{};valid={}; price_calc={}".format(self.data['price'], valid, price_calc))
        return valid

    def save(self, commit=True):
        mwf = super(MeleWeaponForm, self).save(commit=False)
        mwf.save()
        return mwf

class RangedWeaponForm(ModelForm):
    price = CharField(validators=[validator_price], help_text="Price should ends with GC, /-, d")

    def __init__(self, *args, **kwargs):
        super(RangedWeaponForm, self).__init__(*args, **kwargs)
        self.fields['reference'].widget = (
            RelatedFieldWidgetWrapper(self.fields['reference'].widget, self.instance._meta.get_field('reference').remote_field, admin_site)
        )

    class Meta:
        model = models.RangedWeapon
        fields = ["name", "weapon_group", "price", "encumbrance", "availability", "damage", "qualities_and_flaws", "range", "reference"]

    def calc_price_to_brass(self):
        logger.debug("price:{}".format(self.data['price']))
        price = self.data['price']
        if price.endswith("GC"):
            price_int = int(price[0:-2])
            self.data['price'] = price_int * 240
            return True
        elif price.endswith("/-"):
            price_int = int(price[0:-2])
            self.data['price'] = price_int * 12
            return True
        elif  price.endswith("d"):
            price_int = int(price[0:-1])
            self.data['price'] = price_int
            return True
        logger.error("price: {} [type:{}] is invalid for conversion".format(price, type(price)))
        return False

    def is_valid(self) -> bool:
        self.data._mutable = True
        price_calc = self.calc_price_to_brass()
        self.data._mutable = False
        valid = super(RangedWeaponForm,self).is_valid()
        logger.debug("price:{};valid={}; price_calc={}".format(self.data['price'], valid, price_calc))
        return valid

    def save(self, commit=True):
        mwf = super(RangedWeaponForm, self).save(commit=False)
        mwf.save()
        return mwf

class SpellsForm(ModelForm):
    class Meta:
        model = models.Spells
        fields = ['spellLists', 'name',  'cn', 'range', 'target', 'duration', 'effect']

class TrappingForm(ModelForm):
    class Meta:
        model = models.Trapping
        fields = ['name',  'description', 'encumbrance']

class TalentForm(ModelForm):
    class Meta:
        model = models.Talent
        fields = ['name',  'description', "max", 'ref']

    def __init__(self, *args, **kwargs):
        super(TalentForm, self).__init__(*args, **kwargs)
        self.fields['ref'].widget = (
            RelatedFieldWidgetWrapper(self.fields['ref'].widget, self.instance._meta.get_field('ref').remote_field, admin_site)
        )