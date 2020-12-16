from django import forms

from places.models.city import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
