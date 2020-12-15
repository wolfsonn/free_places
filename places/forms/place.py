from django import forms

from places.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
