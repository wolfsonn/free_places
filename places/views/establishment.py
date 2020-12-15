from django.shortcuts import render, redirect

from places.forms.establishment import EstablishmentForm
from places.models import Place, Establishment


def establishments_list(request):
    places = Place.objects.all()
    green_establishments = set([place.establishment for place in places if place.status == 'vacant'])
    red_establishments = set([place.establishment for place in places if place.status != 'vacant' and place.establishment not in green_establishments])
    context = {
        # 'places': places,
        'green_establishments': green_establishments,
        'red_establishments': red_establishments,
    }
    return render(request, 'establishments_list.html', context)


def create_establishment(request):
    if request.method == 'GET':
        context = {
            'form': EstablishmentForm(),
        }
        return render(request, 'create_establishment.html', context)
    else:
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('establishments_list.html')

        context = {
            'form': form,
        }
        return render(request, 'create_establishment.html', context)


def establishment_details(request, pk):
    establishment = Establishment.objects.get(pk=pk)
    places = Place.objects.filter()
    green_establishments = set([place.establishment for place in places if place.status == 'vacant'])
    red_establishments = set([place.establishment for place in places if place.status != 'vacant' and place.establishment not in green_establishments])
    context = {
        'places': places,
        'establishment': establishment,
    }
    return render(request, 'establishment_details.html', context)

