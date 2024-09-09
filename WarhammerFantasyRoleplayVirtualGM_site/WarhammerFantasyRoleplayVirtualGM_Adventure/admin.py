from django.contrib import admin

from . import models
# Register your models here.


class Adventure2NPCAdmin(admin.TabularInline):
    model = models.Adventure2NPC
    extra = 0

class AdventureAdmin(admin.ModelAdmin):
    inlines= (Adventure2NPCAdmin,)


admin.site.register(models.Adventure, AdventureAdmin)