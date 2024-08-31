from django.shortcuts import render,redirect
from produto.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import *
from colecao.service import CollectionService
from users.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404


# Create your views here.

class ProductIndex(View):
    template_name = 'produto/index.html'
    form_class = EmailLoginForm
    vorm_class = UserForm
    
    def get(self, request, *args, **kwargs):
        collections = CollectionService.get_all_collections()
        product = ProductService.get_all_products()
        form = self.form_class
        vorm = self.vorm_class
        return render(request, self.template_name,{'form':form, 'vorm':vorm, 'collections':collections, 'products':product})

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

    def get(self, request):
        product = ProductService.get_product_by_id(1)
        comment = CommentPageService.list_all_comments()
        form_comment = CommentProductForm()
        return render(request, self.template_name, {'product':product, 'form':form_comment, 'comment':comment})
    
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
    
class CreateCommentProduct(View):
    def post(self, product_id, request, *args, **kwargs):
        form = CommentProductForm(request.POST)
        if form.is_valid():
            CommentProductService.create_comment_product(product_id, form.cleaned_data['comment'])

class DeleteCommentProduct(View):
    def get(self, comment_id, request, *args, **kwargs):
        CommentProductService.delete_comment_product(comment_id)
        messages.success(request, "Comentário deletado com sucesso!")
        return redirect('product_single')
    
class CreateCommentPage(View):
    def post(self, request, user_id, *args, **kwargs):
        form = CommentPageForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, id=user_id)
            CommentPageService.create_comment_page(user, form.cleaned_data['comment'])
            messages.success(request, "Comentário criado com sucesso!")
            return redirect('mural_comment')
        else:
            messages.error(request, "Erro ao criar comentário.")
            return redirect('mural_comment')
    


class CommentPageList(View):
    template_name = 'produto/mural_comments.html'
    paginate_by = 5
    def get(self, request, *args, **kwargs):
        form = CommentPageForm()
        page = request.GET.get('page', 1)
        user = request.user
        per_page = self.paginate_by
        comments = CommentPageService.list_all_comments(page=page, per_page=per_page)
     
        return render(request, self.template_name, {'form':form,'comments':comments, 'user':user})
