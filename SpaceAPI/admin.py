from django.contrib import admin
from SpaceAPI.models import destination, crew, technology
from django.utils.html import format_html

# Register your models here.

class destinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'Image', 'description']

    def Image(self, obj):
        return format_html('<img src="{}" style="max-width:90px; max-height:90px margin:0 15px;"/>'.format(obj.image.url))

admin.site.register(destination, destinationAdmin),

class crewAdmin(admin.ModelAdmin):
    list_display = ['name', 'Image', 'bio']

    def Image(self, obj):
        return format_html('<img src="{}" style="max-width:90px; max-height:90px"/>'.format(obj.image.url))

admin.site.register(crew, crewAdmin),

class technologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'Image', 'description']

    def Image(self, obj):
        return format_html('<img src="{}" style="max-width:90px; max-height:90px"/>'.format(obj.image.url))

admin.site.register(technology, technologyAdmin)
