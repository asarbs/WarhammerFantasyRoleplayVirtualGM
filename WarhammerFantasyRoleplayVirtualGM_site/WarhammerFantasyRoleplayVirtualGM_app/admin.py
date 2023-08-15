from django.contrib import admin
from django.forms import forms, Textarea
from django.db import models
from tinymce.widgets import TinyMCE


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
    list_display = ("player", "name",)


class SpeciesAdmin(admin.ModelAdmin):
    list_display = ("name", "random_interal_start", "random_interal_end")
    list_editable = ("random_interal_start", "random_interal_end")
    ordering = ("random_interal_start", )


class RandomAttributesTableAdmin(admin.ModelAdmin):
    list_display = ("species", "weapon_skill", "ballistic_skill", "strength", "toughness", "initiative", "agility", "dexterity", "intelligence", "willpower", "fellowship", "fate", "resilience", "extra_points", "movement")
    list_editable = ("weapon_skill", "ballistic_skill", "strength", "toughness", "initiative", "agility", "dexterity", "intelligence", "willpower", "fellowship", "fate", "resilience", "extra_points", "movement")
    ordering = ("species", )

class ClassAdmin(admin.ModelAdmin):
    pass

class CareerPathAdmin(admin.ModelAdmin):
    pass

class CareerAdmin(admin.ModelAdmin):
    list_display = ("ch_class", "name", "random_table_human_start", "random_table_human_end","random_table_dwarf_start","random_table_dwarf_end","random_table_halfling_start","random_table_halfling_end","random_table_high_elf_start","random_table_high_elf_end","random_table_wood_elf_start","random_table_wood_elf_end")
    ordering = ("name", )
    list_filter = ("ch_class",)

class StatusAdmin(admin.ModelAdmin):
    pass

class HairAdmin(admin.ModelAdmin):
    list_display = ("species", "random_table_start", "random_table_end", "name")
    list_filter = ("species",)
    list_editable = ("name",)
    ordering = ("species",'random_table_start')

class EyesAdmin(admin.ModelAdmin):
    list_display = ("species", "random_table_start", "random_table_end", "name")
    list_filter = ("species",)
    list_editable = ("name",)
    ordering = ("species",'random_table_start')

class SkillsAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE()}
    }
    list_display = ("name", "characteristics", "description", 'ref')
    list_editable = ("characteristics", 'description', "ref")
    ordering = ("name",)

class TalenAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    ordering = ("name",)

class Campaign2PlayerAdmin(admin.ModelAdmin):
    pass

class ExampleNameAdmin(admin.ModelAdmin):
    list_display = ("name", "species", "sex")
    list_filter = ("species", "sex")

class Character2SkillAdmin(admin.ModelAdmin):
    pass

class RefBookAdmin(admin.ModelAdmin):
    ordering = ("name",)

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("refBook","page")
    list_filter = ("refBook",)

from . import models
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.Species ,SpeciesAdmin)
admin.site.register(models.ExampleName ,ExampleNameAdmin)
admin.site.register(models.Class , ClassAdmin)
admin.site.register(models.CareerPath ,CareerPathAdmin)
admin.site.register(models.Career ,CareerAdmin)
admin.site.register(models.Status ,StatusAdmin)
admin.site.register(models.Hair ,HairAdmin)
admin.site.register(models.Eyes ,EyesAdmin)
admin.site.register(models.Skils ,SkillsAdmin)
admin.site.register(models.Talent ,TalenAdmin)
admin.site.register(models.Campaign2Player, Campaign2PlayerAdmin)
admin.site.register(models.Character2Skill, Character2SkillAdmin)
admin.site.register(models.RefBook, RefBookAdmin)
admin.site.register(models.Reference, ReferenceAdmin)
admin.site.register(models.RandomAttributesTable, RandomAttributesTableAdmin)