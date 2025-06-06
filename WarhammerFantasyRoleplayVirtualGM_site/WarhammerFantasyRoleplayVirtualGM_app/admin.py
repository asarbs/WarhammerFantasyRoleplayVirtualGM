from django.contrib import admin
from django.forms import forms, Textarea
from django.db import models
from tinymce.widgets import TinyMCE
from django.db.models import Q

from WarhammerFantasyRoleplayVirtualGM_app.forms import SpeciesForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import CareerPathForm
from WarhammerFantasyRoleplayVirtualGM_app.forms import ClassTrappingsForm
from WarhammerFantasyRoleplayVirtualGM_app.models import Character2Weapon


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
#    inlines = [Character2WeaponInline]
    list_display = ("name", "player", "campaign", "hash_id", "deleted")

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
    list_display = ("careers", "name", "status")
    #list_editable = (,)
    list_filter = ("status",)
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

class HairAdmin(admin.ModelAdmin):
    list_display = ("species", "random_table_start", "random_table_end", "name")
    list_filter = ("species",)
    list_editable = ("name",)
    ordering = ("species",'random_table_start','name')

class EyesAdmin(admin.ModelAdmin):
    list_display = ("species", "random_table_start", "random_table_end", "name")
    list_filter = ("species",)
    list_editable = ("name",)
    ordering = ("species",'random_table_start','name')

class SkillsAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name", "characteristics", 'ref', 'skils_parent')
    list_editable = ("characteristics", "ref", 'skils_parent')
    ordering = ("name",)
    save_as=True
    list_max_show_all = 1500
    list_per_page = 1000

class TalenAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name", 'max', 'tests', 'ref', 'talent_parent')
    list_editable = ("ref", 'talent_parent')
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
    list_display = ("characters", "skills", "adv", "is_basic_skill", "is_species_skill", "is_career_skill")
    list_filter = ("characters",)
    ordering = ("characters", "skills")
    list_editable = ("adv", "is_basic_skill", "is_species_skill", "is_career_skill")
    save_as = True

class RefBookAdmin(admin.ModelAdmin):
    ordering = ("name",)

class ReferenceAdmin(admin.ModelAdmin):
    list_display = ("refBook","page")
    list_filter = ("refBook",)

class CareersAdvanceSchemeAdmin(admin.ModelAdmin):
    list_display = ('career', 'characteristics_ws_initial', 'characteristics_bs_initial', 'characteristics_s_initial', 'characteristics_t_initial', 'characteristics_i_initial', 'characteristics_ag_initial', 'characteristics_dex_initial', 'characteristics_int_initial', 'characteristics_wp_initial', 'characteristics_fel_initial', 'advances_level_1', 'advances_level_2', 'advances_level_3', 'advances_level_4')
    list_editable = ('characteristics_ws_initial', 'characteristics_bs_initial', 'characteristics_s_initial', 'characteristics_t_initial', 'characteristics_i_initial', 'characteristics_ag_initial', 'characteristics_dex_initial', 'characteristics_int_initial', 'characteristics_wp_initial', 'characteristics_fel_initial', 'advances_level_1', 'advances_level_2', 'advances_level_3', 'advances_level_4')

class TrappingAdmin(admin.ModelAdmin):
    list_display = ("name","encumbrance", "price", "availability", "to_view")
    list_editable = ("availability", "to_view")
    ordering = ("name",)
    list_max_show_all = 1500
    list_per_page = 20

class RandomTalentsTableAdmin(admin.ModelAdmin):
    list_display = ("talent", "any","random_interal_start", "random_interal_end")
    list_editable = ("random_interal_start", "random_interal_end", "any")
    ordering = ("random_interal_start",)
    list_max_show_all = 1500
    list_per_page = 1000


class ClassTrappingsAdmin(admin.ModelAdmin):
    form = ClassTrappingsForm
    list_display = ("ch_class", "trapping")
    ordering = ("ch_class",)
    list_filter = ("ch_class",)
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class StatusAdmin(admin.ModelAdmin):
    form = ClassTrappingsForm
    list_display = ("tier", "level")
    ordering = ("tier", "level")
    list_filter = ("tier",)
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class ArmourLocationsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class ArmourAdmin(admin.ModelAdmin):
    list_display = ("name", "armour_type", "price_formated", "encumbrance", "availability", "penalty", "armour_locations", "armour_points", "qualities_and_flaws")
    list_filter = ("armour_type", "availability")
    ordering = ("armour_type", "name")
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class WeaponQualitiesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name",'type',"ref")
    list_editable = ("type",)
    ordering = ('type', "name",)
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class MeleeWeaponsAdmin(admin.ModelAdmin):
    list_display = ("name", "weapon_group", "price", "encumbrance", "availability", "reach", "damage", "qualities_and_flaws", )
    list_filter = ("weapon_group", "availability")
    ordering = ("weapon_group", "name")
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class RangedWeaponAdmin(admin.ModelAdmin):
    list_display = ("name", "weapon_group", "price", "encumbrance", "range", "availability", "damage", "qualities_and_flaws")
    list_filter = ("weapon_group", "availability")
    ordering = ("weapon_group", "name")
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class ImprovementXPCostsAdmin(admin.ModelAdmin):
    list_display = ("advances_interval_start", "advances_interval_end", "characteristics_xp_cost", "skills_xp_cost")
    ordering = ("advances_interval_start", "advances_interval_end")
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class SpellsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("name", "cn", "range", "target", "duration", "effect")
    list_filter = ("spellLists",)
    ordering = ("spellLists", "name")
    save_as = True
    list_max_show_all = 1500
    list_per_page = 1000

class AmbitionsAdmin(admin.ModelAdmin):
    list_display = ("description", "achieved",)
    list_editable = ("achieved",)
    save_as = True

class Character2TalentAdmin(admin.ModelAdmin):
    list_display = ("characters", "talent", "taken")
    list_filter = ("characters",)
    ordering = ("characters", "talent")
    save_as = True


class Character2TrappingAdmin(admin.ModelAdmin):
    list_display = ("characters", "trapping", "quantity", "container")
    list_editable = ("quantity",)
    list_filter = ("characters",)
    ordering = ("characters", "trapping")
    save_as = True

class NoteAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("datetime_create", "datetime_update", "author", "note_text")
    ordering = ("datetime_update", "datetime_create")
    save_as = True

class CharacterChangeLogAdmin(admin.ModelAdmin):
    list_display = ("datetime_create", "user", "character", 'log')
    list_filter = ("character", "datetime_create","user")
    ordering = ("character", "datetime_create")

class ContainersAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "encumbrance", "carries", 'price', 'availability', 'trapping')
    ordering = ("name",)
    # list_editable

class Character2ContainerAdmin(admin.ModelAdmin):
    list_display = ("id", "character", "container")

class ConditionAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }
    list_display = ("id", "name", "description")
    ordering = ("name",)
    save_as = True

class Condition2CharacterAdmin(admin.ModelAdmin):
    list_display = ("id", "characters", "condition", "occurrence")
    list_filter = ("characters",)
    list_editable = ("occurrence",)

class Character2CareerPathAdmin(admin.ModelAdmin):
    list_display = ("id", "character", "career_path")
    list_filter = ("character",)

from . import models
admin.site.register(models.Ambitions, AmbitionsAdmin)
admin.site.register(models.Armour, ArmourAdmin)
admin.site.register(models.ArmourLocations, ArmourLocationsAdmin)
admin.site.register(models.Campaign, CampaignAdmin)
admin.site.register(models.Campaign2Player, Campaign2PlayerAdmin)
admin.site.register(models.Career ,CareerAdmin)
admin.site.register(models.CareerPath ,CareerPathAdmin)
admin.site.register(models.CareersAdvanceScheme, CareersAdvanceSchemeAdmin)
admin.site.register(models.Character, CharacterAdmin)
admin.site.register(models.Character2CareerPath, Character2CareerPathAdmin)
admin.site.register(models.Character2Container, Character2ContainerAdmin)
admin.site.register(models.Character2Skill, Character2SkillAdmin)
admin.site.register(models.Character2Talent, Character2TalentAdmin)
admin.site.register(models.Character2Trapping, Character2TrappingAdmin)
admin.site.register(models.CharacterChangeLog, CharacterChangeLogAdmin)
admin.site.register(models.Class , ClassAdmin)
admin.site.register(models.ClassTrappings, ClassTrappingsAdmin)
admin.site.register(models.Condition, ConditionAdmin)
admin.site.register(models.Condition2Character, Condition2CharacterAdmin)
admin.site.register(models.Containers, ContainersAdmin)
admin.site.register(models.ExampleName ,ExampleNameAdmin)
admin.site.register(models.Eyes ,EyesAdmin)
admin.site.register(models.Hair ,HairAdmin)
admin.site.register(models.ImprovementXPCosts, ImprovementXPCostsAdmin)
admin.site.register(models.MeleeWeapons, MeleeWeaponsAdmin)
admin.site.register(models.Note, NoteAdmin)
admin.site.register(models.Player, PlayerAdmin)
admin.site.register(models.RandomAttributesTable, RandomAttributesTableAdmin)
admin.site.register(models.RandomTalentsTable, RandomTalentsTableAdmin)
admin.site.register(models.RangedWeapon, RangedWeaponAdmin)
admin.site.register(models.RefBook, RefBookAdmin)
admin.site.register(models.Reference, ReferenceAdmin)
admin.site.register(models.Skils ,SkillsAdmin)
admin.site.register(models.Species ,SpeciesAdmin)
admin.site.register(models.Spells, SpellsAdmin)
admin.site.register(models.Status ,StatusAdmin)
admin.site.register(models.Talent ,TalenAdmin)
admin.site.register(models.Trapping, TrappingAdmin)
admin.site.register(models.WeaponQualities, WeaponQualitiesAdmin)