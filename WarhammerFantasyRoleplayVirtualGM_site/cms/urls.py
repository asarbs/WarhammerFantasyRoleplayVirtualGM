from django.urls import path
from django.urls import include
from django.urls import re_path as url
from rest_framework import routers


from dal import autocomplete

from . import views

router = routers.DefaultRouter()
router.register(r'api_news', views.NewsViewSet)


urlpatterns = [
    path("newsList/<int:page>", views.index, name="newsList"),
    path("newsDetail/<int:pk>", views.newsDetail, name="newsDetail"),
    path('', include(router.urls))

]