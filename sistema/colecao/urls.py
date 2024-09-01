from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>/',CollectionDetailView.as_view() , name='collection_detail'),
    path('criar/',CollectionCreateView.as_view() , name='collection_create'),#ok
    path('deletar/<int:id>/',CollectionDeleteView.as_view() , name='collection_delete'),#ok
    path('update/<int:id>/',CollectionUpdateView.as_view() , name='collection_update'),#ok
    path('listar/',CollectionListView.as_view() , name='collection_list'),#ok
    path('listar/dash',CollectionListDashView.as_view() , name='collection_dash'),#ok
    
]