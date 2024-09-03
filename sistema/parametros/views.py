from django.shortcuts import render
from django.shortcuts import render,redirect
from parametros.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from parametros.forms import *
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class ParameterView(View):
    template_name = 'parametros/parametros.html'
    def get(self, request, *args, **kwargs):
        parameters = ParametersService.get_id_parameter()
        form = ParametersForm()
        return render(request, self.template_name, {'form':form, 'parameters':parameters})
    
class ParameterUpdateView(View):
    def post(self, request):
        id = request.POST['parameter_id']
        form = ParameterView(request.POST)
        if form.is_valid():
            ParametersService.update_parameter(id, form.cleaned_data['name'])
            messages.success(request, "Parametros atualizados com sucesso!")
        else:
            messages.error(request, "Erro ao atualizar o Parametro.")
        return redirect('parameters_view')