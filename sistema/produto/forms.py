from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = ['name','description', 'type', 'colection', 'path']
        labels = {
            "name": "Nome",
            "description": "Descrição",
            "type": "Tipo",
            "colection": "Coleção",
            "path": "Fotografia",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do Produto"
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Descrição do Produto"
                }
            ),
            'type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'colection': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
        }


class CommentProductForm(forms.ModelForm):
    class Meta:
        model = CommentProduct
        fields = ['comment']
        labels = {
            'comment': "Comentário:",
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }


class CommentPageForm(forms.ModelForm):
    class Meta:
        model = CommentPage
        fields = ['comment']
        labels = {
            'comment': "Comentário:",
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your comment here...'}),
        }
