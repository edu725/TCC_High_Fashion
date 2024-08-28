from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages  
from .repository import CollectionRepository

class TypeListView(View):
    def get(self, request):
        collections = CollectionRepository.get_all_collections()
        return render(request, 'collections/collection_list.html', {'collections': collections})

class TypeDetailView(View):
    def get(self, request, id):
        collection = CollectionRepository.get_collection_by_id(id)
        return render(request, 'collections/collection_detail.html', {'collection': collection})

class TypeCreateView(View):
    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        id_user = request.user.id  
        CollectionRepository.create_collection(name, description, id_user)
        messages.success(request, 'Sua coleção foi criada com sucesso!')
        return redirect('collection_list')

class TypeDeleteView(View):
    def post(self, request, id):
        success = CollectionRepository.delete_collection(id)
        if success:
            messages.success(request, 'Coleção deletada com sucesso!')
        else:
            messages.error(request, 'Erro ao deletar a coleção.')
        return redirect('collection_list')

class TypeUpdateView(View):
    def post(self, request, id):
        name = request.POST.get('name')
        description = request.POST.get('description')
        success = CollectionRepository.update_collection(id, name, description)
        if success:
            messages.success(request, 'Coleção atualizada com sucesso!')
        else:
            messages.error(request, 'Erro ao atualizar a coleção.')
        return redirect('collection_detail', id=id)
