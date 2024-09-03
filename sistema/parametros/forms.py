from django import forms
from .models import Parameters


class ParametersForm(forms.ModelForm):
    class Meta:

        model = Parameters
        fields = ['impostos','retirada', 'frete', 'comissao', 'despesas_financeiras', 'despesas_comerciais', 'lucro']
        labels = {
            "impostos": "Impostos",
            "retirada": "Retirada",
            "frete": "Frete",
            "comissao": "Comissao",
            "despesas_financeiras": "Despesas Financeiras",
            "despesas_comerciais": "Despesas Comerciais",
            "lucro": "Lucro",
        }
        widgets = {
            'impostos': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Impostos'}),
            'retirada': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Retirada'}),
            'frete': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Frete'}),
            'comissao': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Comissao'}),
            'despesas_financeiras': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desp. financeira'}),
            'despesas_comerciais': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Desp. comercias'}),
            'lucro': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Lucro'}),
        }