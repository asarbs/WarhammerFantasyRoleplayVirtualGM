from django import template
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

@register.simple_tag
def loggedUser(user):
    if user.is_anonymous:
        return ""
    return "Logged in as: " + str(user)
