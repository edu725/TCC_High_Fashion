from .views import *
from django.urls import path


urlpatterns = [
    path('', ParameterView.as_view(), name='parameters_view'),
    path('editar/', ParameterUpdateView.as_view(), name='update_parameters')
]