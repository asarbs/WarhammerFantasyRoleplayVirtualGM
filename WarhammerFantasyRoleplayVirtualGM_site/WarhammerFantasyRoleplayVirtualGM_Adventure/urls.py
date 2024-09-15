from django.urls import path
from django.urls import re_path as url

from dal import autocomplete

from . import views

urlpatterns = [
    path("Details/<int:adventure_id>", views.adventureDetails, name="AdventureDetails"),
    path("Create/<int:campaign_id>", views.createNewAdventure, name="AdventureCreate"),
    path("Edit/<int:pk>", views.AdventureEditView.as_view(), name="AdventureEdit"),
    path('ajax_saveAdventureNotes', views.ajax_saveAdventureNotes, name="ajax_saveAdventureNotes"),
    path('ajax_saveConditionState', views.ajax_saveConditionState, name="ajax_saveConditionState"),
    path('ajax_saveCurrentWounds', views.ajax_saveCurrentWounds, name="ajax_saveCurrentWounds"),
    path('ajax_getConditionsDetails', views.ajax_getConditionsDetails, name="ajax_getConditionsDetails"),
]