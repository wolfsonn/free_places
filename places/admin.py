from django.contrib import admin

from places.models.place import Place
from places.models.establishment import Establishment
from places.models.city import City


class PostInline(admin.StackedInline):
    model = Place


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'establishment', 'city', 'user')
    inlines = (PostInline,)


admin.site.register(Place)
admin.site.register(Establishment)
admin.site.register(City)
