from django.shortcuts import render,redirect
from produto.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import *
from colecao.service import CollectionService
from users.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from notifications.service import EmailService

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
    template_name = 'produto/product_list.html'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        products = ProductService.list_all_products(page=page, per_page=per_page)
        form = ProductForm()
        return render(request, self.template_name, {'products':products,'form':form})


class Product_Single(View):
    template_name = 'produto/product_single.html'

    def get(self, request, product_id, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Usuario precisa estar logado.")
            return redirect('index')
        product = ProductService.get_product_by_id(product_id)
        comment = CommentProductService.list_all_comments(product_id)
        form_comment = CommentProductForm()
        total_comments = len(comment)
        user = request.user
        return render(request, self.template_name, {'product':product, 'form':form_comment, 'comments':comment, 'total_comments':total_comments, 'user':user})
    
class CreateProduct(View):
    template_name = 'produto/create.html'
    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            ProductService.create_product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                path=form.cleaned_data['path'],
                type=form.cleaned_data['type_name'],
                collection=form.cleaned_data['collection_name']
            )
            messages.success(request, "Produto criado com sucesso!")
            produto = ProductService.get_last_product()
            EmailService.send_email_with_attachment(
                subject="Novo produto adicionado",
                message=f"Confira as Novidades do nosso site como o novo lançamento da/o {produto.name}",
                recipient_list=EmailService.list_all_email_users,
                attachment_path=produto.path,
            )
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
        product = get_object_or_404(Product, id=product_id)
        ProductService.delete_product(product)
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('all_products')
    
class CreateCommentProduct(View):
    def post(self, request, product_id, user_id ,*args, **kwargs):
        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(User, id=user_id)
        form = CommentProductForm(request.POST)
        if form.is_valid():
            CommentProductService.create_comment_product(product,user, form.cleaned_data['comment'])
        return redirect('index')

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
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        user = request.user
        comment = CommentPageService.list_all_comments_page(page=page, per_page=self.paginate_by)
        form = CommentPageForm()
        return render(request, self.template_name, {'comments':comment,'form':form, 'user':user})
    
    
class HomeView(View):
    template_name = 'produto/home.html'

    def get(self, request):
        products = ProductService.list_all_products()
        # price = ProductCostService.get_price_sell()
        return render(request, self.template_name, {'products':products})
