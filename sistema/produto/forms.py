from django import forms
from .models import *
from tipo.service import TypeService
from colecao.service import CollectionService
from parametros.repository import ParametersRepository


class ProductForm(forms.ModelForm):
    type=forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label="",
        label="Tipo de roupa",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    collection=forms.ModelChoiceField(
        queryset=None,
        required=True,
        empty_label="",
        label="Coleção",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:

        model = Product
        fields = ['name','description', 'path', 'type', 'collection']
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
        self.fields['type'].queryset = TypeService.get_all_types()
        self.fields['collection'].queryset = CollectionService.get_all_collections()

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
        # Separando dados e arquivos para os dois formulários
        product_form_data = kwargs.pop('product_form_data', None)
        product_form_files = kwargs.pop('product_form_files', None)
        product_cost_form_data = kwargs.pop('product_cost_form_data', None)
        product_cost_form_files = kwargs.pop('product_cost_form_files', None)
        product_instance = kwargs.pop('product_instance', None)
        product_cost_instance = kwargs.pop('product_cost_instance', None)
        
        super().__init__(*args, **kwargs)

        self.product_form = ProductForm(
            data=product_form_data, 
            files=product_form_files, 
            instance=product_instance
        )
        self.product_cost_form = ProductCostForm(
            data=product_cost_form_data, 
            files=product_cost_form_files, 
            instance=product_cost_instance
        )

    def is_valid(self):
        return self.product_form.is_valid() and self.product_cost_form.is_valid()

    def save(self):
        if self.is_valid():
            product = self.product_form.save()
            product_cost = self.product_cost_form.save(commit=False)
            product_cost.product = product
            product_cost.parameters = ParametersRepository.get_id_parameter()
            product_cost.save()
            return product
        return None