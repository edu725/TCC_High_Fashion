from django.shortcuts import render,redirect
from produto.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import*
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

class ProductList(View):
    template_name = 'produto/tela_tcc.html'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        products = ProductService.list_all_products(page=page, per_page=per_page)
        form = ProductForm()
        return render(request, self.template_name, {'products':products,'form':form})
    
class Product_Single(View):
    template_name = 'produto/product_single.html'

    def get(self, product_id, request, *args, **kwargs):
        product = ProductService.get_product_by_id(product_id)
        return render(request, self.template_name, {'product':product})
    
class CreateProduct(View):
    template_name = 'produto/create.html'
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
                ProductService.create_product(form.cleaned_data['name', 'description', 'type', 'path'])
                messages.success(request, "Produto criado com sucesso!")
                return redirect('all_products')
        else:
            messages.error(request, "Erro ao criar produto.")
        return render(request, self.template_name, {'form':form})
    
class UpdateProduct(View):
    def post(self, request, product_id, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            ProductService.update_product(product_id, form.cleaned_data['name', 'description', 'type', 'path'])
            messages.success(request, 'Produto editado com sucesso!')
        else:
            messages.error(request,'Erro ao editar produto.')
        return redirect('all_products')

class DeleteProduct(View):
    def get(self, product_id, request, *args, **kwargs):
        ProductService.delete_product(product_id)
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('all_products')