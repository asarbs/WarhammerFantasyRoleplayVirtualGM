from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models

from . import models as cmd_models

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    pass


class News2TagAdmin(admin.TabularInline):
    model = cmd_models.News2Tag
    extra = 0

class NewsAdmin(admin.ModelAdmin):
    formfield_overrides = {
          models.TextField: {'widget': TinyMCE(mce_attrs={'width': 800})}
    }
    inlines = [News2TagAdmin]
    list_display = ("title", "author", "datetime_create", "datetime_update", "id","is_deleted", "is_yt", "internal_id")
    list_filter = ("author","tagss")
    list_editable = ("is_deleted",)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super(NewsAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user
        return form


admin.site.register(cmd_models.Tag, TagAdmin)
admin.site.register(cmd_models.News, NewsAdmin)