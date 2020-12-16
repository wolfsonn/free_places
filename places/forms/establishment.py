from django import forms

from places.models.establishment import Establishment


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'
