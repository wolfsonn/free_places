from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from places.forms.city import CityForm
from places.models.city import City
from places.models.place import Place
from places.tables import PlaceTable


def cities_list(request):
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
    return render(request, 'cities/cities_list.html', context)


@staff_member_required
def create_city(request):
    if request.method == 'GET':
        context = {
            'form': CityForm(),
        }
        return render(request, 'cities/create_city.html', context)
    else:
        form = CityForm(request.POST)
        form.user = request.user
        if form.is_valid():
            form.save()
            return redirect('cities')

        context = {
            'form': form,
        }
        return render(request, 'cities/create_city.html', context)


@staff_member_required
def edit_city(request, pk):
    city = City.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'city': city,
            'form': CityForm(instance=city),
        }

        return render(request, 'cities/edit_city.html', context)
    else:
        form = CityForm(request.POST, instance=city)

        if form.is_valid():
            form.save()
            return redirect('cities')

        context = {
            'city': city,
            'form': form,
        }

        return render(request, 'cities/edit_city.html', context)


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
    return render(request, 'cities/city_details.html', context)
