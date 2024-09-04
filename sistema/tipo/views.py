from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from users.decorators import *
from django.utils.decorators import method_decorator
from django.views import View  
from tipo.models import Type
from tipo.forms import TypeForm
from django.contrib.auth.decorators import login_required
from tipo.service import TypeRepository
from tipo.service import TypeService

@method_decorator(user_is_manager_or_common, name='dispatch')
class TypeListView(View):
    template_name = 'tipo/types.html'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        form = TypeForm()
        types = TypeService.list_all_types(page=page, per_page=per_page)
        return render(request, self.template_name, {'form_type': form, 'types':types})

@method_decorator(user_is_manager, name='dispatch')
class TypeCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TypeForm(request.POST)
        if form.is_valid():
            TypeService.create_new_type(form.cleaned_data['name'])
            messages.success(request, 'Tipo de roupa criado com sucesso!')
            return redirect('type_list')
        else:
            messages.error(request, 'Erro ao cadastrar tipo de roupa.')
        return redirect('type_list')

@method_decorator(user_is_manager, name='dispatch')
class TypeUpdateView(View):
    def post(self, request):
        id = request.POST['type_id']
        form = TypeForm(request.POST)
        if form.is_valid():
            TypeService.update_existing_type(id, form.cleaned_data['name'])
            messages.success(request, "Tipo de roupa atualizado com sucesso!")
        else:
            messages.error(request, "Erro ao atualizar o tipo.")
        return redirect('type_list')

@method_decorator(user_is_manager, name='dispatch')
class TypeDeleteView(View):  
    def post(self, request):
        id = request.POST['type_id']
        TypeService.delete_type(id)
        messages.success(request, 'Tipo de roupa deletado com sucesso!')
        return redirect('type_list')