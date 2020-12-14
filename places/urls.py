from django.urls import path

from places.views.cities import cities_list, city_details
from places.views.overview import overview

urlpatterns = [
    path('overview/', overview, name='overview'),
    path('cities/', cities_list, name='cities'),
    path('cities/details/<int:pk>', city_details, name='city details'),
]
