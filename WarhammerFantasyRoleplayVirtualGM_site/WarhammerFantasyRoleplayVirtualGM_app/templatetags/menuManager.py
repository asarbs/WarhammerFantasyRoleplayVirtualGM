from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django import template
from django.utils.safestring import mark_safe

from WarhammerFantasyRoleplayVirtualGM_app.models import Player
from WarhammerFantasyRoleplayVirtualGM_app.models import Campaign2Player
from WarhammerFantasyRoleplayVirtualGM_app.models import CareersAdvanceScheme

class MenuElement(object):
    def __init__(self, name, url="", visible=True):
        self.name = name
        self.url = url if url else self.name
        self.visible = visible
        self.children = []

    def hasChildren(self):
        return len(self.children) > 0

    def getChildren(self):
        return self.children

    def addChildraen(self, children):
        if not children.visible:
            return
        self.children.append(children)

    def __str__(self):
        return u"{} {} {} {}".format(self.name, self.url, self.visible, self.children)

    def __unicode__(self):
        return u"{} {} {} {}".format(self.name, self.url, self.visible, self.children)

    def getLinkTag(self):
        return '<a href="{}">{}</a>'.format(self.url, self.name)

class MenuHeader(MenuElement):
    def __init__(self, name, visible=True):
        MenuElement.__init__(self, name , "", visible)

    def getLinkTag(self):
        return '<a>{}</a>'.format(self.url)

class AuthenticationStateMenuElement(MenuElement):
    def __init__(self, request, visible=None):
        MenuElement.__init__(self, request, request, visible)
        if request.user.is_authenticated:
            self.name = "Logout"
            self.url = "/logout/"
        else:
            self.name = "Login"
            self.url = "/login"
        if visible is not None:
            self.visible = visible
        else:
            self.visible = True

    def __str__(self):
        return u"{} {} {} {}".format(self.name, self.url, self.visible, self.children)

    def __unicode__(self):
        return u"{} {} {} {}".format(self.name, self.url, self.visible, self.children)


class LogedInMenuElement(MenuElement):
    def __init__(self, request, name, url="", visible=False):
        MenuElement.__init__(self, name, url, visible)
        if request.user.is_authenticated():
            self.visible = True


class NotLogedInMenuElement(MenuElement):
    def __init__(self, request, name, url="", visible=False):
        MenuElement.__init__(self, name, url, visible)
        if not request.user.is_authenticated():
            self.visible = True


class RegisterMenuElement(MenuElement):
    def __init__(self, request, visible=None):
        MenuElement.__init__(self, request, request, visible)
        self.name = "Register"
        self.url = "/wfrpg_gm/addUser"
        self.visible = False
        if not request.user.is_authenticated:
            self.visible = True


class MenuElementWithPrivileges(MenuElement):
    def __init__(self, name, url, request, groups=[]):
        MenuElement.__init__(self, name, url, request.user.is_authenticated())
        if len(groups) > 0:
            for group in groups:
                self.visible = self.visible and request.user.groups.filter(name=group).exists()


class MenuManager(object):
    def __init__(self, request):
        self.request = request
        module = self.request.get_full_path().split("/")[1]
        self.l = [
            MenuElement("Main", "/"),
            MenuElement("Create Campaign",  reverse("createCampaign")),
        ]

        if not request.user.is_anonymous:
            logger_player = Player.objects.get(user=request.user)
            if logger_player:
                player_campaign = Campaign2Player.objects.filter(player=logger_player)
                if player_campaign:
                    for campaign in player_campaign:
                        self.l[1].addChildraen(MenuElement(campaign.campaign.name, reverse("detailsCampaign", args=(campaign.campaign.id,) )))

        self.l.append(MenuHeader("Careers Advance Schemes"))
        if not request.user.is_anonymous:
            cas = CareersAdvanceScheme.objects.all().order_by("career__name")
            for c in cas:
                self.l[2].addChildraen(MenuElement(c.career.name, reverse("showCareersAdvanceSchemes", args=(c.id,) )))



        # self.l.append( MenuElement("League", "/tc_league/leagueList") )
        # if module == "tc_league":
        #     self.l[-1].addChildraen(MenuElementWithPrivileges("Add a League", "/tc_league/addLeague", self.request,  ["Owners"]) )


        # if module == "tc2":
        #     self.l[-1].addChildraen(MenuElementWithPrivileges("Add a tournament", reverse("tc2_addNewTournament"), self.request, ["Owners"]) )
        #     self.l[-1].addChildraen(
        #         MenuElementWithPrivileges("Additional points category list", reverse("tc2_AdditionalPointsCategoryList"), self.request,
        #                                   ["Owners"]))

        # self.l.append(MenuElement("FAQ", "/news/1/"))
        self.l.append(RegisterMenuElement(self.request) )
        self.l.append(AuthenticationStateMenuElement(self.request))
        #self.l.append(NotLogedInMenuElement(request= self.request, name="Remind Password", url=reverse("RemindPassword")))
        # self.l.append(LogedInMenuElement(request=self.request, name="Edit account", url="/tc_player/editPlayer/"+str(self.request.user.id)+"/"))
        # self.l[-1].addChildraen(LogedInMenuElement(request= self.request, name="Change Password", url="/tc_player/changePassword/"))

    def getMenu(self):
        return [e for e in self.l if e.visible]


def manage(request):
    return {"menuElem": MenuManager(request).getMenu()}

register = template.Library()

@register.simple_tag(takes_context=True)
def makeMenu(context):
    menu = MenuManager(context['request']).getMenu()

    out = "<ol>"
    for menuElem in menu:
        if menuElem.visible:
            out += "<li>{}</li>".format(menuElem.getLinkTag())
            if menuElem.hasChildren:
                for child in menuElem.getChildren():
                    out += '<li class="menuChild">{}</li>'.format(child.getLinkTag())
    out += "<ol>"
    return mark_safe(out)