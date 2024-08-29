from .views import *
from django.urls import path


urlpatterns = [
    path('', ParameterView.as_view(), name='parameters_view')
]