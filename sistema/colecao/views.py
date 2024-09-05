from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  
from .repository import CollectionRepository
from .forms import CollectionForm
from django.utils.decorators import method_decorator
from users.decorators import *
from django.contrib.auth.decorators import login_required
from .service import CollectionService
from produto.service import ProductService
from users.forms import *


class CollectionListView(View):
    template_name = 'colecao/collections.html'
    paginate_by = 10
    form_login = EmailLoginForm
    form_register = UserForm

 
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        
        collections = CollectionService.list_all_collections(page=page, per_page=per_page)
        
        return render(request, self.template_name, {'collections': collections, 'form_login': self.form_login, 'form_register': self.form_register})
       

class CollectionDetailView(View):
    template_name = 'colecao/collection_single.html'
    form_login = EmailLoginForm
    form_register = UserForm

    def get(self, request, id, *args, **kwargs):
    
        collection = CollectionService.get_collection_by_id(id)
        products = ProductService.get_products_by_collection(id_collection=id)
        return render(request, self.template_name, {'collection':collection, 'products':products, 'form_login': self.form_login, 'form_register': self.form_register})


@method_decorator(user_is_manager, name='dispatch')
class CollectionCreateView(View):

    def get(self, request):
        form_collection = CollectionForm()
        return render(request, 'colecao/criar_colecao.html', {'form_collection': form_collection})

    def post(self, request, *args, **kwargs):
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            # Chamando o serviço com os dados corretos
            CollectionService.create_collection(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                image=form.cleaned_data['image']
            )
            messages.success(request, "Coleção criada com sucesso!")
            return redirect('collection_list')
        else:
            messages.error(request, "Erro ao criar a coleção.")
            return redirect('collection_list')


@method_decorator(user_is_manager, name='dispatch')
class CollectionDeleteView(View):
   
    def post(self, request, id, *args, **kwargs):
        success = CollectionService.delete_collection(id)
        if success:
            messages.success(request, 'Coleção deletada com sucesso!')
        else:
            messages.error(request, 'Erro ao deletar a coleção.')
        return redirect('collection_dash')
    

@method_decorator(user_is_manager, name='dispatch')
class CollectionUpdateView(View):

    def post(self, request, id, *args, **kwargs):
        name = request.POST.get('name')
        description = request.POST.get('description')
        success = CollectionRepository.update_collection(id, name, description, request.FILES.get('image'))
        if success:
            messages.success(request, 'Coleção atualizada com sucesso!')
        else:
            messages.error(request, 'Erro ao atualizar a coleção.')
        return redirect('collection_dash')
    
    def get(self, request, id):
        collection = CollectionService.get_collection_by_id(id)
        form_collection = CollectionForm(collection)
        return

@method_decorator(user_is_manager, name='dispatch')
class CollectionListDashView(View):

    def get(self, request):
        form_collection = CollectionForm
        collections = CollectionService.list_all_collections()
        return render(request, 'colecao/collections_dash.html', {'collections': collections, 'form_collection': form_collection})