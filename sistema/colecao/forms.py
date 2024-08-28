from django import forms
from .models import Collection

class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection       
        fields = ['name','description','image']
        labels = {
            'name': 'Nome',
            'description': 'Descrição',
            'image': 'Imagem',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da Coleção'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nome da Descrição'
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class':'form-control'
                }
            )
        }    
            
