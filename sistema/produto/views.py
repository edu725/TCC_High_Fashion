from django.shortcuts import render,redirect
from produto.service import *
from django.views import View
from produto.forms import *
from colecao.service import CollectionService
from users.forms import *
from users.service import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from users.decorators import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from notifications.service import EmailService

# Create your views here.

class ProductIndex(View):
    template_name = 'produto/index2.html'
    form_login = EmailLoginForm
    form_register = UserForm
    
    def get(self, request, *args, **kwargs):
        collections = CollectionService.get_all_collections()
        product = ProductService.get_all_products()
        form_login = self.form_login
        form_register = self.form_register
        return render(request, self.template_name,{'form_login':form_login, 'form_register':form_register, 'collections':collections, 'products':product})

@method_decorator(user_is_manager, name='dispatch')
class ProductListDash(View):
    template_name = 'produto/product_list_dash.html'
    paginate_by = 10
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        products = ProductService.list_all_products(page=page, per_page=per_page)
        form_product = ProductForm
        return render(request, self.template_name, {'products':products,'form_product':form_product})

class ProductList(View):
    template_name = 'produto/product_list.html'
    paginate_by = 10
    form_login = EmailLoginForm
    form_register = UserForm
    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        per_page = self.paginate_by
        products = ProductService.list_all_products(page=page, per_page=per_page)
        return render(request, self.template_name, {'products':products,'form_login':self.form_login, 'form_register':self.form_register})

@method_decorator(user_is_manager_or_common, name='dispatch')
class Product_Single(View):
    template_name = 'produto/product_single.html'

    def get(self, request, product_id, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Usuario precisa estar logado.")
            return redirect('index')
        product = ProductService.get_product_by_id(product_id)
        comment = CommentProductService.list_all_comments(product_id)
        form_comment_product = CommentProductForm()
        total_comments = len(comment)
        user = request.user
        return render(request, self.template_name, {'product':product, 'form_comment_product':form_comment_product, 'comments':comment, 'total_comments':total_comments, 'user':user})
    
@method_decorator(user_is_manager, name='dispatch')
class CreateProduct(View):
    template_name = 'produto/create.html'
    def get(self, request):
        form_product = ProductForm()
        return render(request, self.template_name, {'form_product':form_product})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            ProductService.create_product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                type=form.cleaned_data['type_name'],
                path=form.cleaned_data['path'],
                collection=form.cleaned_data['collection_name']
            )
            messages.success(request, "Produto criado com sucesso!")
            # produto = ProductService.get_last_product()
            # EmailService.send_email_with_attachment(
            #     subject="Novo produto adicionado",
            #     message=f"Confira as Novidades do nosso site como o novo lançamento da/o {produto.name}",
            #     recipient_list=EmailService.list_all_email_users,
            #     attachment_path=produto.path,
            # )
            return redirect('all_products')
        else:
            messages.error(request, "Erro ao criar produto.")
        return render(request, self.template_name, {'form':form})

@method_decorator(user_is_manager, name='dispatch')
class UpdateProduct(View):
    template_name = 'produto/edit_product.html'
    
    def get(self, request, product_id, *args, **kwargs):
        product = ProductService.get_product_by_id(product_id)
        form = ProductForm(instance=product)
        return render(request, self.template_name, {'forms':form})

    def post(self, request, product_id,  *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            ProductService.update_product(
                 product_id,
                 name=form.cleaned_data['name'],
                 description=form.cleaned_data['description'],
                 type=form.cleaned_data['type_name'],
                 collection=form.cleaned_data['collection_name'],
                 path=form.cleaned_data['path']
             )
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('all_products')
        else:
            messages.error(request,'Erro ao atualizar produto.')
            return render(request, self.template_name, {'form':form})

@method_decorator(user_is_manager, name='dispatch')
class DeleteProduct(View):
    def post(self, request):
        id = request.POST['product_id']
        ProductService.delete_product(id)
        messages.success(request, "Produto deletado com sucesso!")
        return redirect('all_products')

@method_decorator(user_is_manager_or_common, name='dispatch')
class CreateCommentProduct(View):
    def post(self, request, product_id, user_id ,*args, **kwargs):
        product = get_object_or_404(Product, id=product_id)
        user = get_object_or_404(User, id=user_id)
        form = CommentProductForm(request.POST)
        if form.is_valid():
            CommentProductService.create_comment_product(product,user, form.cleaned_data['comment'])
        return redirect('all_products')

@method_decorator(user_is_manager_or_common, name='dispatch')
class DeleteCommentProduct(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        CommentProductService.delete_comment_product(comment_id)
        messages.success(request, "Comentário deletado com sucesso!")
        return redirect('index')
    
@method_decorator(user_is_manager_or_common, name='dispatch')
class UpdateCommentProduct(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        content = request.POST.get('comment')
        user_id = request.user.id
        product_id = request.POST.get('product_id')

        # Busca as instâncias necessárias
        user = get_object_or_404(User, id=user_id)
        product = get_object_or_404(Product, id=product_id)

        # Se o comentário já existir, atualize; caso contrário, crie um novo
        if comment_id:
            comment_product = get_object_or_404(CommentProduct, id=comment_id)
        else:
            comment_product = CommentProduct(id_user=user, id_product=product)

        comment_product.comment = content  # Define o conteúdo do comentário
        comment_product.save()  # Salva ou atualiza o comentário

        messages.success(request, "Comentário salvo com sucesso!")
        return redirect('index')
    
       
    
@method_decorator(user_is_manager_or_common, name='dispatch')
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

@method_decorator(user_is_manager_or_common, name='dispatch')
class CommentPageList(View):
    template_name = 'produto/mural_comments.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        user = request.user
        comment = CommentPageService.list_all_comments_page(page=page, per_page=self.paginate_by)
        form_comment_page = CommentPageForm()
        return render(request, self.template_name, {'comments':comment,'form_comment_page':form_comment_page, 'user':user})


class DeleteCommentPage(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        CommentPageService.delete_comment_page(comment_id)
        messages.success(request, "Comentário deletado com sucesso!")
        return redirect('mural_comment')
    
class UpdateCommentPage(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        content = request.POST.get('comment')
        user_id = request.user.id

        # Busca as instâncias necessárias
        user = get_object_or_404(User, id=user_id)

        # Se o comentário já existir, atualize; caso contrário, crie um novo
        if comment_id:
            comment_page = get_object_or_404(CommentPage, id=comment_id)
        else:
            comment_page = CommentPage(id_user=user)

        comment_page.comment = content  # Define o conteúdo do comentário
        comment_page.save()  # Salva ou atualiza o comentário

        messages.success(request, "Comentário salvo com sucesso!")
        return redirect('mural_comment')
    

class HomeView(View):
    template_name = 'produto/home.html'

    def get(self, request):
        products = ProductService.list_all_products()
        user = UserService.get_all_users()
        comment = CommentPageService.get_all_comments()
        collections = CollectionService.get_all_collections()
        # price = ProductCostService.get_price_sell()
        return render(request, self.template_name, {'products':products, 'collections':collections, 'comments':comment, 'user':user})
