from django.urls import path
from django.urls import re_path as url

from dal import autocomplete

from . import views

urlpatterns = [
    path("Details/<int:adventure_id>", views.adventureDetails, name="Details"),
]