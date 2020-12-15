from django.urls import path

from places.views.citiy import cities_list, city_details, create_city
from places.views.establishment import establishments_list, create_establishment, establishment_details
from places.views.place import places_list, create_place, place_details

urlpatterns = [
    path('establishments/', establishments_list, name='establishments'),
    path('establishments/create', create_establishment, name='create establishment'),
    path('establishments/details/<int:pk>', establishment_details, name='establishment details'),
    path('cities/', cities_list, name='cities'),
    path('cities/create', create_city, name='create city'),
    path('cities/details/<int:pk>', city_details, name='city details'),
    path('places/', places_list, name='places'),
    path('palces/create', create_place, name='create place'),
    path('palces/details/<int:pk>', place_details, name='place details'),
]
