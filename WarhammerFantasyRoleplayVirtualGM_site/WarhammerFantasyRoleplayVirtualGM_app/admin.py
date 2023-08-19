from django.contrib import admin
from django.forms import forms, Textarea
from django.db import models
from tinymce.widgets import TinyMCE
from django.db.models import Q

from WarhammerFantasyRoleplayVirtualGM_app.forms import SpeciesForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import CareerPathForm


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
    form = SpeciesForm
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
    form = CareerPathForm
    list_display = ("careers", "name", "earning_money")
    #list_editable = (,)
    # list_filter = ("careers",)
    ordering = ("name", )
    list_max_show_all = 1500
    list_per_page = 1000

    def careers(self, obj):
        Q1 = Q(advances_level_1 = obj.id)
        Q2 = Q(advances_level_2 = obj.id)
        Q3 = Q(advances_level_3 = obj.id)
        Q4 = Q(advances_level_4 = obj.id)
        return models.CareersAdvanceScheme.objects.get(Q1 | Q2 | Q3 | Q4).career
    careers.short_description = 'careers'

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
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name", "characteristics", 'ref')
    list_editable = ("characteristics", "ref")
    ordering = ("name",)
    save_as=True
    list_max_show_all = 1500
    list_per_page = 1000

class TalenAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name", 'max', 'tests', 'ref')
    list_editable = ("ref",)
    ordering = ("name",)
    save_as=True
    list_max_show_all = 1500
    list_per_page = 1000

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

class CareersAdvanceSchemeAdmin(admin.ModelAdmin):
    pass

class TrappingAdmin(admin.ModelAdmin):
    ordering = ("name",)

class RandomTalentsTableAdmin(admin.ModelAdmin):
    list_display = ("talent", "any","random_interal_start", "random_interal_end")
    list_editable = ("random_interal_start", "random_interal_end", "any")
    ordering = ("random_interal_start",)
    list_max_show_all = 1500
    list_per_page = 1000


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
admin.site.register(models.CareersAdvanceScheme, CareersAdvanceSchemeAdmin)
admin.site.register(models.Trapping, TrappingAdmin)
admin.site.register(models.RandomTalentsTable, RandomTalentsTableAdmin)