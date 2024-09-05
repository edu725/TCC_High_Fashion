from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('login/', CustomLoginView.as_view(), name='login'),#ok
    path('logout/', LogoutView.as_view(), name='logout'),#ok
    path('dashboard/gerente/', DashboardManagerPage.as_view(), name="manager_dashboard"),#ok
    path('adicionar/usuarios/', UserCreateView.as_view(), name='user_add'),#ok
    path('editar/usuario/<int:pk>/', UserUpdateView.as_view(), name='user_edit'),#ok
    path('deletar/ususario/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),#ok
    path('profile/', UserProfileView.as_view(), name='profile'),#ok
    path('listar/dash', UserDashView.as_view(), name='dashboard_user'),#ok
    path('register/', CustomRegisterView.as_view(), name='register'),#ok
    path('register/dash', CustomRegisterView.as_view(), name='register_dash'),#ok
]