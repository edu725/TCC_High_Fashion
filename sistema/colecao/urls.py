from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/',TypeDetailView.as_view() , name='collection_detail'),
    path('criar/',TypeCreateView.as_view() , name='collection_create'),#ok
    path('deletar/',TypeDeleteView.as_view() , name='collection_delete'),#ok
    path('update/',TypeUpdateView.as_view() , name='collection_update'),#ok
    path('listar/',TypeListView.as_view() , name='collection_list'),#ok
    
]