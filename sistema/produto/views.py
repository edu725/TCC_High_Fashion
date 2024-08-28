from django.shortcuts import render,redirect
from produto.service import ProductService
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import*
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# class ProductDetailView(View):

class ProductListView(ListView): 
    template_name = 'produto/product_list.html'
    context_object_name = 'produto'
    paginate_by = 10

    def get_queryset(self):
        search_query = self.request.GET.get('search', '')
        page = self.request.GET.get('page', 1)
        
        if search_query:
            produto = ProductService.search_product(search_query, page=page, per_page=self.paginate_by)
        else:
            produto = ProductService.list_all_products(page=page, per_page=self.paginate_by)
        
        return produto

class ProductCreateView(CreateView):
    template_name = 'produto/product_register.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        name=form.cleaned_data['name']
        description=form.cleaned_data['description']
        type=form.cleaned_data['type']
        path=form.cleaned_data['path']
        ProductService.create_product(name, description, type, path)
        messages.success(self.request, "Produto criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro na criação do produto.")
        return super().form_invalid(form)

class ProductUpdateView(UpdateView):
    template_name = 'produto/product_register.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

    def get_object(self):
        product_id = self.kwargs['pk']
        return ProductService.get_product_by_id(product_id)

    def form_valid(self, form):
        ProductService.update_product(self.object.id, **form.cleaned_data)
        messages.success(self.request, "Produto atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro na atualização do produto.")
        return super().form_invalid(form)
    
class ProductDeleteView(DeleteView):
    success_url = reverse_lazy('product_list')  

    def get_object(self):
        product_id = self.kwargs['pk']
        return ProductService.get_product_by_id(product_id)

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        ProductService.delete_product(product.id)
        messages.success(request, "Produto excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
    

    
