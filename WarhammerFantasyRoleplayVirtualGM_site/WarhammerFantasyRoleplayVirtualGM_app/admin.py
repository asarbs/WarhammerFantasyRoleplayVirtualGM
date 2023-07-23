from django.contrib import admin

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("user", "getLastLogin")

    def getLastLogin(self, obj):
        return obj.user.last_login

    getLastLogin.short_description = 'Last Login'
    getLastLogin.admin_order_field = 'user__last_login'

from . import models
admin.site.register(models.Player, PlayerAdmin)