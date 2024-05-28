from django.contrib import admin
from django.db import models as db_models

from tinymce.widgets import TinyMCE
from . import models
# Register your models here.


class NPC2SkillAdmin(admin.TabularInline):
    model = models.NPC2Skill
    extra = 0

class NPC2TalentAdmin(admin.TabularInline):
    model = models.NPC2Talent
    extra = 0

class NPC2TrappingAdmin(admin.TabularInline):
    model = models.NPC2Trapping
    extra = 0

class NPC2CreatureTraitsAdmin(admin.TabularInline):
    model = models.NPC2CreatureTraits
    extra = 0

class NPC2SpellsAdmin(admin.TabularInline):
    model = models.NPC2Spells
    extra = 0

class NPCAdmin(admin.ModelAdmin):
    inlines = (NPC2SkillAdmin, NPC2TalentAdmin, NPC2TrappingAdmin, NPC2CreatureTraitsAdmin, NPC2SpellsAdmin)


class CreatureTraitsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        db_models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }


admin.site.register(models.NPC, NPCAdmin)
admin.site.register(models.CreatureTraits, CreatureTraitsAdmin)