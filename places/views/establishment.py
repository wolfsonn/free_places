from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from places.forms.establishment import EstablishmentForm
from places.models.establishment import Establishment
from places.models.place import Place
from places.tables import PlaceTable


def establishments_list(request):
    places = Place.objects.all()
    green_establishments = sorted(list(set([place.establishment for place in places if place.status == 'vacant'])),
                                  key=lambda establishment: establishment.name)
    red_establishments = sorted(list(set([place.establishment for place in places if
                                          place.status != 'vacant' and place.establishment not in green_establishments])),
                                key=lambda establishment: establishment.name)
    context = {
        'green_establishments': green_establishments,
        'red_establishments': red_establishments,
        'places': places,
    }
    return render(request, 'establishments/establishments_list.html', context)


@staff_member_required
def create_establishment(request):
    if request.method == 'GET':
        context = {
            'form': EstablishmentForm(),
        }
        return render(request, 'establishments/create_establishment.html', context)
    else:
        form = EstablishmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('establishments')

        context = {
            'form': form,
        }
        return render(request, 'establishments/create_establishment.html', context)


@staff_member_required()
def edit_establishment(request, pk):
    establishment = Establishment.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'establishment': establishment,
            'form': EstablishmentForm(instance=establishment),
        }

        return render(request, 'establishments/edit_establishment.html', context)
    else:
        form = EstablishmentForm(request.POST, instance=establishment)

        if form.is_valid():
            form.save()
            return redirect('establishments')

        context = {
            'establishment': establishment,
            'form': form,
        }

        return render(request, 'establishments/edit_establishment.html', context)


def establishment_details(request, pk):
    establishment = Establishment.objects.get(pk=pk)
    table = PlaceTable(Place.objects.filter(establishment_id=establishment))
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request).configure(table)
    context = {
        'table': table,
        'establishment': establishment,
    }
    return render(request, 'establishments/establishment_details.html', context)
