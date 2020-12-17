from django import forms
from django.forms import TextInput

from places.models.establishment import Establishment


class EstablishmentForm(forms.ModelForm):
    class Meta:
        model = Establishment
        fields = '__all__'
        # widgets = {
        #     'name': TextInput(attrs={'placeholder': 'name'}),
        #     'address': TextInput(attrs={'placeholder': 'address'}),
        #     'phone': TextInput(attrs={'placeholder': 'phone'}),
        #     'email': TextInput(attrs={'placeholder': 'e-mail'}),
        # }
