from django.shortcuts import render

from places.models import Place, City, Establishment


def cities_list(request):
    places = Place.objects.all()
    green_cities = set([place.establishment.city for place in places if place.status == 'vacant'])
    red_cities = set([place.establishment.city for place in places if place.status != 'vacant' and place.establishment.city not in green_cities])
    context = {
        'places': places,
        'green_cities': green_cities,
        'red_cities': red_cities,
    }
    return render(request, 'cities.html', context)


def city_details(request, pk):
    city = City.objects.get(pk=pk)
    city_establishments = Establishment.objects.filter(city=city)
    context = {
        'city_establishments': city_establishments,
        'city': city,
    }
    return render(request, 'city_details.html', context)
