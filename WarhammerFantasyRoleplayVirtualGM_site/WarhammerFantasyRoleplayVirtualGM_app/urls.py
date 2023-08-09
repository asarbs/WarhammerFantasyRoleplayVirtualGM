from django.urls import path

from . import views

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
    path("ajax_save_character_species", views.ajax_save_character_species, name="ajax_save_character_species"),
    path('ajax_randomSpecies', views.ajax_randomSpecies, name="ajax_randomSpecies"),
    path('ajax_randomClass', views.ajax_randomClass, name="ajax_randomClass"),
]