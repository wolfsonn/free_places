from django.shortcuts import render

from places.models import Place, Establishment


def establishment(request, pk):
    establishment = Establishment.objects.get(pk=pk)
    places = Place.objects.filter()
    green_establishments = set([place.establishment for place in places if place.status == 'vacant'])
    red_establishments = set([place.establishment for place in places if place.status != 'vacant' and place.establishment not in green_establishments])
    context = {
        'places': places,
        'establishment': establishment,
    }
    return render(request, 'overview.html', context)