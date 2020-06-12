from django.contrib import admin
from .models import Place, Image


class ImageInLine(admin.StackedInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_short',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInLine, )


admin.site.register(Image)
