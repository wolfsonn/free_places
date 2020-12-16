from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from places.forms.place import PlaceForm
from places.models.place import Place
from places.tables import PlaceTable


def places_list(request):
    table = PlaceTable(Place.objects.all())
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request).configure(table)
    context = {
        'table': table,
    }
    return render(request, 'places_list.html', context)


def create_place(request):
    if request.method == 'GET':
        context = {
            'form': PlaceForm(),
        }
        return render(request, 'create_place.html', context)
    else:
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('places')

        context = {
            'form': form,
        }
        return render(request, 'create_place.html', context)


def place_details(request, pk):
    place = Place.objects.get(pk=pk)
    context = {
        'place': place,
    }
    return render(request, 'place_details.html', context)
