from django.urls import path
from django.urls import re_path as url

from dal import autocomplete

from . import views
from .models import Eyes, Hair

urlpatterns = [
    path("", views.index, name="index"),
    path("addUser", views.addUser, name="addUser"),
    path('changePassword', views.changePassword, name="changePassword"),
    path('addUserConfirm/', views.addUserConfirm, name="addUserConfirm"),
    path('editPlayer/(?P<pk>\d+)/',  views.UpdatePlayer.as_view(success_url="/"), name='updatePlayer'),
    path('remindPassword', views.RemindPassword, name="remindPassword"),
    path("createCampaign", views.createCampaign, name="createCampaign"),
    path("detailsCampaign/<int:CampaignId>", views.detailsCampaign, name="detailsCampaign"),
    path('addCharacter', views.addCharacter, name="addCharacter"),
    path('showCareersAdvanceSchemes/<int:casId>', views.showCareersAdvanceSchemes, name="showCareersAdvanceSchemes"),
    path('listCareersAdvanceSchemes', views.listCareersAdvanceSchemes, name="listCareersAdvanceSchemes"),
    path('MeleWeaponListView', views.MeleWeaponListView.as_view(), name="MeleWeaponListView"),
    path('CreateMeleWeapon', views.MeleWeaponFormView.as_view(), name="CreateMeleWeapon"),
    path('EditMeleWeapon/<int:pk>', views.MeleWeaponEditView.as_view(), name="EditMeleWeapon"),

    path("ajax_save_character_species", views.ajax_save_character_species, name="ajax_save_character_species"),
    path('ajax_randomSpecies', views.ajax_randomSpecies, name="ajax_randomSpecies"),
    path('ajax_randomClass', views.ajax_randomClass, name="ajax_randomClass"),
    path('ajax_saveName', views.ajax_saveName, name="ajax_saveName"),
    path('ajax_randomAttributes', views.ajax_randomAttributes, name="ajax_randomAttributes"),
    path('ajax_saveAttribute', views.ajax_saveAttribute, name="ajax_saveAttributea"),
    path('ajax_getRandomAttributesTable', views.ajax_getRandomAttributesTable, name="ajax_getRandomAttributesTable"),
    path('ajax_saveFate_and_fortune', views.ajax_saveFate_and_fortune, name="ajax_saveFate_and_fortune"),
    path('ajax_saveAge', views.ajax_saveAge, name="ajax_saveAge"),
    path('ajax_saveHeight', views.ajax_saveHeight, name="ajax_saveHeight"),
    path('ajax_saveHair', views.ajax_saveHair, name="ajax_saveHair"),
    path('ajax_saveEyes', views.ajax_saveEyes, name="ajax_saveEyes"),
    path('ajax_saveSkillAdv', views.ajax_saveSkillAdv, name="ajax_saveEyes"),
    path('ajax_replaceTalentToCharacter', views.ajax_replaceTalentToCharacter, name="ajax_replaceTalentToCharacter"),
    path('ajax_addArmourToCharacter', views.ajax_addArmourToCharacter, name="ajax_addArmourToCharacter"),
    path('ajax_addWeaponToCharacter', views.ajax_addWeaponToCharacter, name="ajax_addWeaponToCharacter"),
    path('ajax_addSpellsToCharacter', views.ajax_addSpellsToCharacter, name="ajax_addSpellsToCharacter"),
    path('ajax_getCareersAdvanceScheme', views.ajax_getCareersAdvanceScheme, name="ajax_getCareersAdvanceScheme"),
    path('ajax_saveSkillsXPSpend', views.ajax_saveSkillsXPSpend, name="ajax_saveSkillsXPSpend"),
    path('ajax_saveTalentXPSpend', views.ajax_saveTalentXPSpend, name="ajax_saveTalentXPSpend"),
]