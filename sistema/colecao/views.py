from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages  
from .repository import CollectionRepository
from .forms import CollectionForm
from django.contrib.auth.decorators import login_required
from .service import CollectionService

class TypeListView(View):
    template_name = 'colecao/collections.html'
    paginate_by = 10

    @login_required
    def get(self, request, *args, **kwargs):
        # search_query = request.GET.get('search', '')
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        
        # if search_query:
        #     collections = CollectionService.search_collections(search_query, page=page, per_page=per_page)
        # else:
        #     collections = CollectionService.list_all_collections(page=page, per_page=per_page)
        
        form = CollectionForm()
        #return render(request, self.template_name, {'collections': collections, 'form': form, 'search_query': search_query})
        return render(request, self.template_name, {'form': form})

class TypeDetailView(View):
    @login_required
    def get(self, request, id):
        collection = CollectionRepository.get_collection_by_id(id)
        return render(request, 'colecao/collections.html', {'collection': collection})

class TypeCreateView(View):
    @login_required
    def get(self, request):
        form = CollectionForm()
        return render(request, 'colecao/collections.html', {'form': form})

    @login_required
    def post(self, request):
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            collection = form.save(commit=False)
            collection.id_user = request.user.id  
            collection.save()
            messages.success(request, 'Sua coleção foi criada com sucesso!')
            return redirect('collection_list')
        else:
            messages.error(request, 'Erro ao criar a coleção. Verifique os dados informados.')
            return render(request, 'colecao/collections.html', {'form': form})

class TypeDeleteView(View):
    @login_required
    def post(self, request, id):
        success = CollectionRepository.delete_collection(id)
        if success:
            messages.success(request, 'Coleção deletada com sucesso!')
        else:
            messages.error(request, 'Erro ao deletar a coleção.')
        return redirect('collection_list')

class TypeUpdateView(View):
    @login_required
    def post(self, request, id):
        name = request.POST.get('name')
        description = request.POST.get('description')
        success = CollectionRepository.update_collection(id, name, description)
        if success:
            messages.success(request, 'Coleção atualizada com sucesso!')
        else:
            messages.error(request, 'Erro ao atualizar a coleção.')
        return redirect('collection_detail', id=id)