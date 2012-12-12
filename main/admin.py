from django.contrib import admin
from placeignatius.main.models import PlaceImage

class PlaceImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(PlaceImage, PlaceImageAdmin)
