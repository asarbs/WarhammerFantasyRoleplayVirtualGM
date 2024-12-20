"""WarhammerFantasyRoleplayVirtualGM_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from ajax_select import urls as ajax_select_urls

from django.contrib.auth import views as auth_views
from cms import views as MainView
from WarhammerFantasyRoleplayVirtualGM_app.views import *
from WarhammerFantasyRoleplayVirtualGM_NPC.views import *

admin.autodiscover()

urlpatterns = [
    path('', MainView.index),
    path('wfrpg_gm/', include("WarhammerFantasyRoleplayVirtualGM_app.urls")),
    path('wfrpg_npc/', include("WarhammerFantasyRoleplayVirtualGM_NPC.urls")),
    path('Adventure/', include("WarhammerFantasyRoleplayVirtualGM_Adventure.urls")),
    path('Map/', include("WarhammerFantasyRoleplayVirtualGM_map.urls")),
    path('cms/', include("cms.urls")),
    path('chat', include("WarhammerFantasyRoleplayVirtualGM_chat.urls")),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/login/'), name='logout'),
    path('admin/', admin.site.urls),
    path('tiny_mce/', include('tinymce.urls')),
    path('skills-autocomplete/', AutocompleteSkills.as_view(), name='skills-autocomplete'),
    path('talent-autocomplete/', AutocompleteTalent.as_view(), name='talent-autocomplete'),
    path('trappings-autocomplete/', AutocompleteTrappings.as_view(), name='trappings-autocomplete'),
    path('player-autocomplete/', AutocompletePlayer.as_view(), name='player-autocomplete'),
    path('ajax_select/', include(ajax_select_urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]
