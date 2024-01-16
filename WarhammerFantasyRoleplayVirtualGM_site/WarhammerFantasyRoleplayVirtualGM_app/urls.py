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
    path('addCharacter/<int:CampaignId>', views.addCharacter, name="addCharacter"),
    path('showCareersAdvanceSchemes/<int:casId>', views.showCareersAdvanceSchemes, name="showCareersAdvanceSchemes"),
    path('listCareersAdvanceSchemes', views.listCareersAdvanceSchemes, name="listCareersAdvanceSchemes"),
    path('MeleWeaponListView', views.MeleWeaponListView.as_view(), name="MeleWeaponListView"),
    path('CreateMeleWeapon', views.MeleWeaponFormView.as_view(), name="CreateMeleWeapon"),
    path('EditMeleWeapon/<int:pk>', views.MeleWeaponEditView.as_view(), name="EditMeleWeapon"),
    path('RangedWeaponListView', views.RangedWeaponListView.as_view(), name="RangedWeaponListView"),
    path('CreateRangedWeapon', views.RangedWeaponFormView.as_view(), name="CreateRangedWeapon"),
    path('EditRangedWeapon/<int:pk>', views.RangedWeaponEditView.as_view(), name="EditRangedWeapon"),
    path('SpellListView', views.SpellListView.as_view(), name="SpellListView"),
    path('SpellsCreateFormView', views.SpellsCreateFormView.as_view(), name="SpellsCreateFormView"),
    path('SpellsEditView/<int:pk>', views.SpellsEditView.as_view(), name="SpellsEditView"),
    path('SkillsListView', views.SkillsListView.as_view(), name="SkillsListView"),
    path('SkillsCreateFormView', views.SkillsCreateFormView.as_view(), name="SkillsCreateFormView"),
    path('SkillsEditView/<int:pk>', views.SkillsEditView.as_view(), name="SkillsEditView"),


    path('TrappingsListView', views.TrappingsListView.as_view(), name="TrappingsListView"),
    path('TrappingssCreateFormView', views.TrappingssCreateFormView.as_view(), name="TrappingssCreateFormView"),
    path('TrappingssEditView/<int:pk>', views.TrappingssEditView.as_view(), name="TrappingssEditView"),

    path('TalentsListView', views.TalentsListView.as_view(), name="TalentsListView"),
    path('TalentsCreateFormView', views.TalentsCreateFormView.as_view(), name="TalentsCreateFormView"),
    path('TalentsEditView/<int:pk>', views.TalentsEditView.as_view(), name="TalentsEditView"),

    path('ContainersListView',          views.ContainersListView.as_view(),       name="ContainersListView"),
    path('ContainersCreateFormView',    views.ContainersCreateFormView.as_view(), name="ContainersCreateFormView"),
    path('ContainersEditView/<int:pk>', views.ContainersEditView.as_view(),       name="ContainersEditView"),


    path("ajax_save_character_species", views.ajax_save_character_species, name="ajax_save_character_species"),
    path("ajax_saveSpecies", views.ajax_saveSpecies, name="ajax_saveSpecies"),
    path("ajax_saveClass", views.ajax_saveClass, name="ajax_saveClass"),
    path("ajax_saveCareer", views.ajax_saveCareer, name="ajax_saveCareer"),
    path("ajax_saveCareer_level", views.ajax_saveCareer_level, name="ajax_saveCareer_level"),
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
    path('ajax_saveFate', views.ajax_saveFate, name="ajax_saveFate"),
    path('ajax_saveFortune', views.ajax_saveFortune, name="ajax_saveFortune"),
    path('ajax_saveSkillAdv', views.ajax_saveSkillAdv, name="ajax_saveSkillAdv"),
    path('ajax_replaceTalentToCharacter', views.ajax_replaceTalentToCharacter, name="ajax_replaceTalentToCharacter"),
    path('ajax_saveTalentToCharacter', views.ajax_saveTalentToCharacter, name="ajax_replaceTalentToCharacter"),
    path('ajax_addArmourToCharacter', views.ajax_addArmourToCharacter, name="ajax_addArmourToCharacter"),
    path('ajax_addWeaponToCharacter', views.ajax_addWeaponToCharacter, name="ajax_addWeaponToCharacter"),
    path('ajax_addSpellsToCharacter', views.ajax_addSpellsToCharacter, name="ajax_addSpellsToCharacter"),
    path('ajax_getCareersAdvanceScheme', views.ajax_getCareersAdvanceScheme, name="ajax_getCareersAdvanceScheme"),
    path('ajax_saveSkillsXPSpend', views.ajax_saveSkillsXPSpend, name="ajax_saveSkillsXPSpend"),
    path('ajax_saveTalentXPSpend', views.ajax_saveTalentXPSpend, name="ajax_saveTalentXPSpend"),
    path('ajax_saveFreeHandSkillAdv', views.ajax_saveFreeHandSkillAdv, name="ajax_saveFreeHandSkillAdv"),
    path('ajax_saveFreeHandCharacteristicAdv', views.ajax_saveFreeHandCharacteristicAdv, name="ajax_saveFreeHandCharacteristicAdv"),
    path('ajax_saveFreeHandCharacteristicInit', views.ajax_saveFreeHandCharacteristicInit, name="ajax_saveFreeHandCharacteristicInit"),
    path('ajax_saveAmbitions', views.ajax_saveAmbitions, name="ajax_saveAmbitions"),
    path('ajax_saveCurrentEp', views.ajax_saveCurrentEp, name="ajax_saveCurrentEp"),
    path('ajax_savePlayerNote', views.ajax_savePlayerNote, name="ajax_savePlayerNote"),
    path('ajax_saveMotivation', views.ajax_saveMotivation, name="ajax_saveMotivation"),
    path('ajax_saveResolve', views.ajax_saveResolve, name="ajax_saveResolve"),
    path('ajax_saveResilience', views.ajax_saveResilience, name="ajax_saveResilience"),
    path('ajax_saveTrappingToCharacter', views.ajax_saveTrappingToCharacter, name="ajax_saveTrappingToCharacter"),
    path("ajax_saveWealth", views.ajax_saveWealth, name="ajax_saveWealth"),
    path("ajax_fullSkillList", views.ajax_fullSkillList, name="ajax_fullSkillList"),
    path("ajax_saveSkill2Character", views.ajax_saveSkill2Character, name="ajax_saveSkill2Character"),
    path("ajax_saveExperience_current", views.ajax_saveExperience_current, name="ajax_saveExperience_current"),
    path("ajax_saveExperience_spent", views.ajax_saveExperience_spent, name="ajax_saveExperience_spent"),
    path("ajax_getSpeciesList", views.ajax_getSpeciesList, name="ajax_getSpeciesList"),
    path("ajax_getClassList", views.ajax_getClassList, name="ajax_getClassList"),
    path("ajax_getHairList", views.ajax_getHairList, name="ajax_getHairList"),
    path("ajax_getEyesList", views.ajax_getEyesList, name="ajax_getEyesList"),
    path("ajax_removeAmbitions", views.ajax_removeAmbitions, name="ajax_removeAmbitions"),
    path("ajax_removeWeapon", views.ajax_removeWeapon, name="ajax_removeWeapon"),
    path("ajax_removeArmour", views.ajax_removeArmour, name="ajax_removeArmour"),
    path("ajax_removeTrappings", views.ajax_removeTrappings, name="ajax_removeTrappings"),
    path("ajax_removeSpells", views.ajax_removeSpells, name="ajax_removeSpells"),

    path("ajax_saveTraping2Container", views.ajax_saveTraping2Container, name="ajax_saveTraping2Container"),
    path('ajax_saveCampaignAmbitions', views.ajax_saveCampaignAmbitions, name="ajax_saveCampaignAmbitions"),
    path('ajax_saveCampaignNotes', views.ajax_saveCampaignNotes, name="ajax_saveCampaignNotes"),

    path("viewCharacter/<int:pk>", views.viewCharacter, name="viewCharacter"),
    path("ajax_view_getCharacterData", views.ajax_view_getCharacterData, name="ajax_view_getCharacterData"),
    path("AddPlayer2Campaign", views.addPlayer2Campaign, name="AddPlayer2Campaign")
]