from django.forms import Form
from django.forms import CharField
from django.forms import ModelForm
from django.forms import PasswordInput
from django.contrib.auth.models import User
from django.forms.utils import ErrorList

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
        fields = ['name', 'party_name', 'ambitions_shortterm', 'ambitions_longterm']
