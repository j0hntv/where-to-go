from django.contrib import admin
from .models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_short',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInLine, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'get_preview')
