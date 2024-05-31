from django.contrib import admin

from . import models
# Register your models here.

class AdventureAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Adventure, AdventureAdmin)