from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from produto.service import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from produto.forms import*
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.

# class ProductList(View):
#     template_name = 'produto/tela_tcc.html'
#     paginate_by = 10
#     def get(self, request, *args, **kwargs):
#         page = request.GET.get('page', 1)
#         per_page = self.paginate_by
#         products = ProductService.list_all_products(page=page, per_page=per_page)
#         form = ProductForm()
#         return render(request, self.template_name, {'products':products,'form':form})