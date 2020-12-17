from itertools import count

from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from places.forms.city import CityForm
from places.models.city import City
from places.models.place import Place
from places.tables import PlaceTable


def cities_list(request):
    # city_places = count(city.place_set)
    places = Place.objects.all()
    green_cities = sorted(list(set([place.establishment.city for place in places if place.status == 'vacant'])),
                          key=lambda city: city.name)
    red_cities = sorted(list(set([place.establishment.city for place in places if
                                  place.status != 'vacant' and place.establishment.city not in green_cities])),
                        key=lambda city: city.name)

    context = {
        'places': places,
        'green_cities': green_cities,
        'red_cities': red_cities,
    }
    return render(request, 'cities_list.html', context)


def create_city(request):
    if request.method == 'GET':
        context = {
            'form': CityForm(),
        }
        return render(request, 'create_city.html', context)
    else:
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cities')

        context = {
            'form': form,
        }
        return render(request, 'create_city.html', context)


def city_details(request, pk):
    city = City.objects.get(pk=pk)
    places = Place.objects.all()
    city_green_establishments = set(
        [place.establishment for place in places if place.status == 'vacant' and place.establishment.city == city])
    city_red_establishments = set([place.establishment for place in places if
                                   place.status != 'vacant' and place.establishment.city == city and place.establishment not in city_green_establishments])
    table = PlaceTable(Place.objects.filter(city_id=city))
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request).configure(table)
    context = {
        'city_green_establishments': sorted(list(city_green_establishments)),
        'city_red_establishments': city_red_establishments,
        'city': city,
        'table': table,
    }
    return render(request, 'city_details.html', context)
