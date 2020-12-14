from django.shortcuts import render

from places.models import Place


def overview(request):
    places = Place.objects.all()
    green_establishments = set([place.establishment for place in places if place.status == 'vacant'])
    red_establishments = set([place.establishment for place in places if place.status != 'vacant' and place.establishment not in green_establishments])
    context = {
        'places': places,
        'green_establishments': green_establishments,
        'red_establishments': red_establishments,
    }
    return render(request, 'overview.html', context)
