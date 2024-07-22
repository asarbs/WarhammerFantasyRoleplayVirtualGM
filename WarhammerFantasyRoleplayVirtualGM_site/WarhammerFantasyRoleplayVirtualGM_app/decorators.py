from django.http import HttpResponse
from django.shortcuts import redirect


from WarhammerFantasyRoleplayVirtualGM_app.models import *

import logging
logger = logging.getLogger(__name__)

ACCESS_DENIED = "Access denied"

def can_view_character(func):
    def wrapper(request, *args, **kwargs):
        logger.debug(request.GET)
        if (request.user.is_anonymous) :
            return redirect("login")
        groups_names = [group.name for group in request.user.groups.all() ]
        character = Character.objects.get(pk=kwargs['pk'])
        players_in_campain = Campaign2Player.objects.filter(campaign=character.campaign)
        user_in_campain = [c2p.player.user for c2p in players_in_campain]
        if "Admin" in groups_names:
            logger.debug("admin")
            return func(request, *args, **kwargs)
        elif request.user == character.player.user:
            logger.debug("player_characeter")
            return func(request, *args, **kwargs)
        if request.user in user_in_campain:
            logger.debug("user_in_campain")
            return func(request, *args, **kwargs)
        else:
            HttpResponse(ACCESS_DENIED)
    return wrapper