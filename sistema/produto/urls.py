from .views import *
from django.urls import path


urlpatterns = [

    path('produto/<int:id>',ProductDetailView.as_view() , name='product_list'), #ok
    path('listar/',ProductListView.as_view() , name='product_list'), #ok
    path('criar/',ProductCreateView.as_view() , name='product_create'), #ok
    path('editar/<int:id>/',ProductUpdateView.as_view() , name='product_update'), #ok
    path('deletar/<int:id>/',ProductDeleteView.as_view() , name='product_delete'), #ok
    path('comentar/<int:id_product>',ProductCommentListView.as_view() , name='product_comment_list'),
    path('comentar_create/<int:id_product>',ProductCommentCreateView.as_view() , name='product_comment_create'), 
    path('comentar_delete/<int:id_comment>',ProductCommentDeleteView.as_view() , name='product_comment_delete'),
    path('comentar_page/<int:id_user>',PageCommentListView.as_view() , name='page_comment_list'),
    path('comentar_page_create/<int:id_user>',PageCommentCreateView.as_view() , name='page_comment_create'), 
    path('comentar_page_delete/<int:id_comment>',PageCommentDeleteView.as_view() , name='page_comment_delete'),  
]