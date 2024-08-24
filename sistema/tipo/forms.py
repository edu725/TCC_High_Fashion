from django import forms
from .models import Type


class TypeForm(forms.ModelForm):
    class Meta:

        model = Type
        fields = ['name']
        labels = {
            "name": "Nome",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do Tipo de Roupa"
                }
            )
        }