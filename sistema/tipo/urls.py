from django.urls import path
from .views import *


urlpatterns = [ 
    path('listar/', TypeListView.as_view(), name='type_list'),
    path('criar/', TypeCreateView.as_view(), name='type_create'),
    path('editar/<int:pk>/', TypeUpdateView.as_view(), name='type_update'),
    path('deletar/<int:pk>/', TypeDeleteView.as_view(), name='type_delete'),
]