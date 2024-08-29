from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:

        model = Product
        fields = ['name','description', 'type', 'collection', 'path']
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
            'collection': forms.Select(
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
            'comment': "Comentário",
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva seu comentário aqui...'}),
        }


class CommentPageForm(forms.ModelForm):
    class Meta:
        model = CommentPage
        fields = ['comment']
        labels = {
            'comment': "Comentário",
        }
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escreva seu comentário aqui...'}),
        }

class ProductCostForm(forms.ModelForm):
    class Meta:
        model = ProductCost
        fields = ['raw_materials','labor','indirect']
        labels = {
            'raw_materials': "Matéria-prima",
            'labor': "Mão de obra",
            'indirect': "Preço indireto"
        }
        widgets = {
            'raw_materials': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da Matéria-Prima'}),
            'labor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da Mão de obra'}),
            'indirect': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço indireto'}),
        }
