from django.contrib import admin
from adminsortable2.admin import SortableInlineAdminMixin
from .models import Place, Image


class ImageInLine(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInLine, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'get_preview')
