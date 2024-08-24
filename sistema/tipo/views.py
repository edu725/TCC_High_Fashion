from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View  
from tipo.models import Type
from tipo.forms import TypeForm
from django.contrib.auth.decorators import login_required
from tipo.service import TypeService

# Create your views here.

