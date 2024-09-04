from django import forms
from .models import *
from tipo.service import TypeService
from colecao.service import CollectionService


class ProductForm(forms.ModelForm):
    type_name=forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label="",
        label="Tipo de roupa",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    collection_name=forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label="",
        label="Coleção",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:

        model = Product
        fields = ['name','description', 'path']
        labels = {
            "name": "Nome",
            "description": "Descrição",
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
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    }
            ),
        }

    def __init__(self ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_name'].queryset = TypeService.get_all_types()
        self.fields['collection_name'].queryset = CollectionService.get_all_collections()

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
            'raw_materials': "Preço da matéria-prima",
            'labor': "Preço da mão de obra",
            'indirect': "Preço indireto"
        }
        widgets = {
            'raw_materials': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da Matéria-Prima'}),
            'labor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor da Mão de obra'}),
            'indirect': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Preço indireto'}),
        }


class ProductAndCostForm(forms.Form):
    product_form = ProductForm()
    product_cost_form = ProductCostForm()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_form'] = self.product_form
        self.fields['product_cost_form'] = self.product_cost_form

    def save(self):
        product_form = self.product_form
        product_cost_form = self.product_cost_form

        if product_form.is_valid() and product_cost_form.is_valid():
            # Save Product
            product = product_form.save()

            # Save ProductCost
            product_cost = product_cost_form.save(commit=False)
            product_cost.product = product
            product_cost.save()

            return product
        return None