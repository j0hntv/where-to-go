from django.contrib import admin
from django.utils.html import format_html
from .models import Place, Image


class ImageInLine(admin.TabularInline):
    model = Image
    readonly_fields = ('get_preview',)
    list_display = ('image', 'get_preview')
    
    def get_preview(self, obj):
        url = obj.image.url
        return format_html(f'<img src="{url}" width="150" />')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_short',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInLine, )


admin.site.register(Image)
