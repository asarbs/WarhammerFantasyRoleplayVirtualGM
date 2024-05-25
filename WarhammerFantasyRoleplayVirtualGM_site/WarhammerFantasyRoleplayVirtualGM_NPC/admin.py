from django.contrib import admin

from . import models
# Register your models here.


class NPC2SkillAdmin(admin.TabularInline):
    model = models.NPC2Skill

class NPC2TalentAdmin(admin.TabularInline):
    model = models.NPC2Talent

class NPC2TrappingAdmin(admin.TabularInline):
    model = models.NPC2Trapping

class NPCAdmin(admin.ModelAdmin):
    inlines = (NPC2SkillAdmin, NPC2TalentAdmin, NPC2TrappingAdmin)


admin.site.register(models.NPC, NPCAdmin)