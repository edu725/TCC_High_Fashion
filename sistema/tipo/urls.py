from django.urls import path
from .views import *


urlpatterns = [ 
    path('listar/', TypeListView.as_view(), name='type_list'),
    path('criar/', TypeCreateView.as_view(), name='type_create'),
    path('editar/', TypeUpdateView.as_view(), name='type_update'),
    path('deletar/', TypeDeleteView.as_view(), name='type_delete'),
]