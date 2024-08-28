from .views import *
from django.urls import path


urlpatterns = [

    path('produto/<int:id>',ProductDetailView.as_view() , name='product_list'),
    path('listar/',ProductListView.as_view() , name='product_list'), #ok
    path('criar/',ProductCreateView.as_view() , name='product_create'), #ok
    path('editar/<int:id>/',ProductUpdateView.as_view() , name='product_update'), #ok
    path('deletar/<int:id>/',ProductDeleteView.as_view() , name='product_delete'), #ok
    path('comentar/<int:id_product>',ProductCommentView.as_view() , name='product_comment'), #ok
]