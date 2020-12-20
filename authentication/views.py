from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig

from authentication.forms import UserProfileForm
from authentication.models import UserProfile
from places.models.place import Place
from places.tables import PlaceTable


def user_profile(request, pk=None):
    user = request.user if pk is None else User.objects.get(pk=pk)
    table = PlaceTable(Place.objects.filter(user=user.id))
    table.paginate(page=request.GET.get("page", 1), per_page=25)
    RequestConfig(request).configure(table)
    if request.method == 'GET':
        context = {
            'profile_user': user,
            'profile': user.userprofile,
            'establishments': user.establishment_set.all(),
            'places': user.place_set.all(),
            'form': UserProfileForm(),
            'table': table,
        }

        return render(request, 'accounts/user_profile.html', context)
    else:
        form = UserProfileForm(request.POST, request.FILES, instance=user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('current user profile')

        return redirect('current user profile')


def signup(request):
    if request.method == 'GET':
        context = {
            'form': UserCreationForm(),
        }

        return render(request, 'accounts/signup.html', context)
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user,
            )
            profile.save()

            login(request, user)
            return redirect('current user profile')

        context = {
            'form': form,
        }

        return render(request, 'accounts/signup.html', context)


def signout(request):
    logout(request)
    return redirect('index')
