from django.urls import path

from places.views.city import cities_list, city_details, create_city, edit_city
from places.views.establishment import establishments_list, create_establishment, establishment_details, \
    edit_establishment
from places.views.place import places_list, create_place, place_details, edit_place

urlpatterns = [
    path('establishments/', establishments_list, name='establishments'),
    path('establishments/create/', create_establishment, name='create establishment'),
    path('establishments/details/<int:pk>/', establishment_details, name='establishment details'),
    path('establishments/edit/<int:pk>/', edit_establishment, name='edit establishment'),
    path('cities/', cities_list, name='cities'),
    path('cities/create/', create_city, name='create city'),
    path('cities/details/<int:pk>/', city_details, name='city details'),
    path('cities/edit/<int:pk>/', edit_city, name='edit city'),
    path('places/', places_list, name='places'),
    path('places/create/', create_place, name='create place'),
    path('places/details/<int:pk>/', place_details, name='place details'),
    path('places/edit/<int:pk>/', edit_place, name='edit place'),
]
