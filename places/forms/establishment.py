from django import forms

from places.models import Establishment


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'
