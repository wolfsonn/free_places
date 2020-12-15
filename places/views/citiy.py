from django.shortcuts import render, redirect

from places.forms.city import CityForm
from places.models import Place, City


def cities_list(request):
    places = Place.objects.all()
    green_cities = set([place.establishment.city for place in places if place.status == 'vacant'])
    red_cities = set([place.establishment.city for place in places if place.status != 'vacant' and place.establishment.city not in green_cities])
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
            return redirect('cities_list.html')

        context = {
            'form': form,
        }
        return render(request, 'create_city.html', context)


def city_details(request, pk):
    city = City.objects.get(pk=pk)
    places = Place.objects.all()
    city_green_establishments = set([place.establishment for place in places if place.status == 'vacant' and place.establishment.city == city])
    city_red_establishments = set([place.establishment for place in places if place.status != 'vacant' and place.establishment.city == city and place.establishment not in city_green_establishments])

    context = {
        'city_green_establishments': city_green_establishments,
        'city_red_establishments': city_red_establishments,
        'city': city,
    }
    return render(request, 'city_details.html', context)
