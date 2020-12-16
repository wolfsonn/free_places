from django.contrib import admin

from places.models.place import Place
from places.models.establishment import Establishment
from places.models.city import City

admin.site.register(Place)
admin.site.register(Establishment)
admin.site.register(City)
