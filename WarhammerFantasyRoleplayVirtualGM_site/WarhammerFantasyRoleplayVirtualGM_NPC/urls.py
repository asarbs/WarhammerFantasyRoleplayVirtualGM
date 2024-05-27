from django.urls import path
from django.urls import re_path as url

from dal import autocomplete

from . import views

urlpatterns = [
    path("NPC_MainView", views.index, name="NPC_MainView"),
    
    path("ajax_npc_get_skill_description", views.ajax_npc_get_skill_description, name="ajax_npc_get_skill_description"),
    path("ajax_npc_get_talent_description", views.ajax_npc_get_talent_description, name="ajax_npc_get_talent_description"),
    path("ajax_npc_get_trapping_description", views.ajax_npc_get_trapping_description, name="ajax_npc_get_trapping_description"),
    path("ajax_npc_get_creatureTraits_description", views.ajax_npc_get_creatureTraits_description, name="ajax_npc_get_creatureTraits_description"),
]