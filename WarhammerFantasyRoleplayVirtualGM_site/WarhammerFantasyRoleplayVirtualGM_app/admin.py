from django.contrib import admin

# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("user", "getLastLogin")

    def getLastLogin(self, obj):
        return obj.user.last_login

    getLastLogin.short_description = 'Last Login'
    getLastLogin.admin_order_field = 'user__last_login'

class CampaignAdmin(admin.ModelAdmin):
    pass

class CharacterAdmin(admin.ModelAdmin):
    pass

class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "random_interal_start", "random_interal_end")
    list_editable = ("random_interal_start", "random_interal_end")
    ordering = ("random_interal_start", )


class CharacterClassAdmin(admin.ModelAdmin):
    pass

class CareerPathAdmin(admin.ModelAdmin):
    pass

class CareerAdmin(admin.ModelAdmin):
    pass

class StatusAdmin(admin.ModelAdmin):
    pass

class HairAdmin(admin.ModelAdmin):
    pass

class EyesAdmin(admin.ModelAdmin):
    pass

class SkillsAdmin(admin.ModelAdmin):
    list_display = ("name", "characteristics", "description")
    ordering = ("name",)

class TalenAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    ordering = ("name",)

class Campaign2PlayerAdmin(admin.ModelAdmin):
    pass

class ExampleNameAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "sex")
    list_filter = ("species", "sex")



from . import models
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.Species ,SpeciesAdmin)
admin.site.register(models.ExampleName ,ExampleNameAdmin)
admin.site.register(models.CharacterClass ,CharacterClassAdmin)
admin.site.register(models.CareerPath ,CareerPathAdmin)
admin.site.register(models.Career ,CareerAdmin)
admin.site.register(models.Status ,StatusAdmin)
admin.site.register(models.Hair ,HairAdmin)
admin.site.register(models.Eyes ,EyesAdmin)
admin.site.register(models.Skils ,SkillsAdmin)
admin.site.register(models.Talent ,TalenAdmin)
admin.site.register(models.Campaign2Player, Campaign2PlayerAdmin)