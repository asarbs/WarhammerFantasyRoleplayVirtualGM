from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django import template
from django.utils.safestring import mark_safe

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
        self.url = "/tc_player/addUser"
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
        ]

        # self.l.append( MenuElement("League", "/tc_league/leagueList") )
        # if module == "tc_league":
        #     self.l[-1].addChildraen(MenuElementWithPrivileges("Add a League", "/tc_league/addLeague", self.request,  ["Owners"]) )

        
        # if module == "tc2":
        #     self.l[-1].addChildraen(MenuElementWithPrivileges("Add a tournament", reverse("tc2_addNewTournament"), self.request, ["Owners"]) )
        #     self.l[-1].addChildraen(
        #         MenuElementWithPrivileges("Additional points category list", reverse("tc2_AdditionalPointsCategoryList"), self.request,
        #                                   ["Owners"]))

        # self.l.append(MenuElement("FAQ", "/news/1/"))
        # self.l.append(RegisterMenuElement(self.request) )
        # self.l.append(AuthenticationStateMenuElement(self.request))
        # self.l.append(NotLogedInMenuElement(request= self.request, name="Remind Password", url=reverse("RemindPassword")))
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
        out += "<li><a href=\"" + str(menuElem.url) + "\">" + str(menuElem.name) + "</a></li>"
        if menuElem.hasChildren:
            for child in menuElem.getChildren():
                out += "<li class=\"menuChild\"><a href=\"" + str(child.url) + "\">" + str(child.name) + "</a></li>"
    out += "<ol>"
    return mark_safe(out)