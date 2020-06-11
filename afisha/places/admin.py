from django.contrib import admin
from .models import Place, Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description_short',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Image)
