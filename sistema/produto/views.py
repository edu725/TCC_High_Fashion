from django.shortcuts import render,redirect
from produto.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import*
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.


def ProductDetailView(request):
    return render(request, 'produto/product_single.html')
    

class ProductListView(ListView): 
    template_name = 'produto/product_single.html'
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
    success_url = reverse_lazy('product_single')

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
    success_url = reverse_lazy('product_single')


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
    success_url = reverse_lazy('product_single')  

    def get_object(self):
        product_id = self.kwargs['pk']
        return ProductService.get_product_by_id(product_id)

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        ProductService.delete_product(product.id)
        messages.success(request, "Produto excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
    

class ProductCommentCreateView(CreateView):
    template_name = 'produto/product_register.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_single')

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        user_id = self.kwargs['pk']
        comment=form.cleaned_data['comment']
        CommentProductService.create_product(product_id, user_id, comment)
        messages.success(self.request, "Comentário adicionado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro na criação do comentario.")
        return super().form_invalid(form)

class ProductCommentDeleteView(DeleteView):
    success_url = reverse_lazy('product_single')  

    def get_object(self):
        comment_id = self.kwargs['pk']
        return CommentProductService.get_product_by_id(comment_id)

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        CommentProductService.delete_comment_product(comment.id)
        messages.success(request, "Comentario excluído com sucesso!")
        return super().delete(request, *args, **kwargs)

