from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.forms import Form
from django.forms import CharField
from django.forms import PasswordInput
from django.views.generic.edit import UpdateView
from django.db.models import Q

import random

from django.urls import reverse


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
    basic_skills = Skils.objects.filter(basic_skills_criterion1 & basic_skills_criterion2).order_by("name").order_by('name').values()
    player = Player.objects.get(user=request.user)
    character = Character(player=player, career_path_id='1', ch_class_id='1', eyes_id='1', hair_id='1', species_id='1')
    character.save()

    for skill in basic_skills:
        c2s = Character2Skill(characters_id=character.id, skills_id = skill['id'])
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

        logger.info("{} {}".format(character_id, species_id))

        character = Character.objects.get(id = character_id)
        character.species = Species.objects.get(id = species_id)
        character.save()

        return JsonResponse({'status': 'ok', 'species_id': species_id})
    logger.error("ajax_save_character_species is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)

def ajax_randomSpecies(request):
    if request.method == 'POST':
        character_id = request.POST['characer_id']
        species_list = Species.objects.all()
        r = random.randrange(1, 100)
        species = None
        for s in species_list:

            if r >= s.random_interal_start and r <= s.random_interal_end:
                species = s
                break

        logger.info("ajax_randomSpecies: r={}, character_id={}, species.id={}".format(r, character_id, species.id))
        character = Character.objects.get(id = character_id)
        character.species = species
        character.save()

        return JsonResponse({'status': 'ok', 'species_id': species.id})
    logger.error("ajax_save_character_species is GET")
    return JsonResponse({'status': 'Invalid request'}, status=400)


def detailsCampaign(request, CampaignId):
    c = Campaign.objects.get(id=CampaignId)
    dic ={'camaing': c}
    return render(request, 'detailsCampaign.html', dic)

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