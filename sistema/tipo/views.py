from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View  
from tipo.models import Type
from tipo.forms import TypeForm
from django.contrib.auth.decorators import login_required
from tipo.service import TypeRepository
from tipo.service import TypeService

class TypeListView(View):
    template_name = 'tipo/types.html'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        form = TypeForm()
        types = TypeService.list_all_types(page=page, per_page=per_page)
        return render(request, self.template_name, {'form': form, 'types':types})

class TypeCreateView(View):
    def post(self, request, *args, **kwargs):
        form = TypeForm(request.POST)
        if form.is_valid():
            TypeService.create_new_type(form.cleaned_data['name'])
            messages.success(request, 'Tipo de roupa criado com sucesso!')
        else:
            messages.error(request, 'Erro ao cadastrar tipo de roupa.')
        return redirect('type_list')

    # @login_required
    # def post(self, request, *args, **kwargs):
    #     form = TypeForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Tipo criado com sucesso!')
    #         return redirect('type_list')
    #     else:
    #         messages.error(request, 'Erro ao criar o tipo. Verifique os dados informados.')
    #         return render(request, 'tipos/types.html', {'form': form})

class TypeUpdateView(View):
    @login_required
    def get(self, request, pk, *args, **kwargs):
        type_instance = get_object_or_404(Type, pk=pk)
        form = TypeForm(instance=type_instance)
        return render(request, 'tipos/types.html', {'form': form})

    @login_required
    def post(self, request, pk, *args, **kwargs):
        type_instance = get_object_or_404(Type, pk=pk)
        form = TypeForm(request.POST, instance=type_instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo atualizado com sucesso!')
            return redirect('type_list')
        else:
            messages.error(request, 'Erro ao atualizar o tipo. Verifique os dados informados.')
            return render(request, 'tipos/types.html', {'form': form})

class TypeDeleteView(View):  
    def post(self, request):
        id = request.POST['type_id']
        TypeService.delete_type(id)
        messages.success(request, 'Tipo de roupa deletado com sucesso!')
        return redirect('type_list')