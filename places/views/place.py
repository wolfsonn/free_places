from django.shortcuts import render, redirect

from places.forms.place import PlaceForm
from places.models import Place


def places_list(request):
    places = Place.objects.all()
    context = {
        'places': places,
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
            return redirect('places_list.html')

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
