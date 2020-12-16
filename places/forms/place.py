from django import forms

from places.models.place import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'
