from django.shortcuts import render
from django.shortcuts import render,redirect
from parametros.service import *
from django.utils.decorators import method_decorator
from users.decorators import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from parametros.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
@method_decorator(user_is_manager, name='dispatch')
class ParameterView(View):
    template_name = 'parametros/parametros.html'
    def get(self, request, *args, **kwargs):
        parameter = ParametersService.get_id_parameter()
        form = ParametersForm()
        return render(request, self.template_name, {'form':form, 'parameter':parameter})
    
class ParameterUpdateView(View):
    def post(self, request):
        form = ParametersForm(request.POST)
        if form.is_valid():
            ParametersService.update_parameter(
                impostos=form.cleaned_data['impostos'],
                retirada=form.cleaned_data['retirada'],
                frete=form.cleaned_data['frete'],
                comissao=form.cleaned_data['comissao'],
                despesas_financeiras=form.cleaned_data['despesas_financeiras'],
                despesas_comerciais=form.cleaned_data['despesas_comerciais'],
                lucro=form.cleaned_data['lucro']
                )
            messages.success(request, "Parametros atualizados com sucesso!")
            return redirect('parameters_view')
        else:
            messages.error(request, "Erro ao atualizar o Parametro.")
        return redirect('parameters_view')