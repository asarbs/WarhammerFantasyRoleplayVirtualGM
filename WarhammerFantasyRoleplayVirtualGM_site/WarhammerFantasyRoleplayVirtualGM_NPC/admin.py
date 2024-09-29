from django.contrib import admin
from django.db import models as db_models
from django.contrib.admin import SimpleListFilter

from tinymce.widgets import TinyMCE
from . import models
from WarhammerFantasyRoleplayVirtualGM_app.models import RefBook
# Register your models here.

class RedBookFilter(SimpleListFilter):
    title = "Reference Book"
    parameter_name = "refBook"
    def lookups(self, request, model_admin):
        refBook = RefBook.objects.all().order_by('name')
        out = []
        for rb in refBook:
            out.append((rb.id, f"{rb.name}"))
        return out

    def queryset(self, request, queryset):
        if not 'refBook' in  request.GET:
            return queryset
        refBookId = request.GET['refBook']
        out = queryset.filter(ref__refBook__id=refBookId)
        for o in out:
            print(refBookId, f"{o.name}, {o.ref.refBook.id}, {o.ref.refBook.name}")
        return out


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
    list_display = ("name", "refBook")
    list_filter =(RedBookFilter,)


class CreatureTraitsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        db_models.TextField: {'widget': TinyMCE(mce_attrs={'width': 600})}
    }

admin.site.register(models.NPC, NPCAdmin)
admin.site.register(models.CreatureTraits, CreatureTraitsAdmin)
