from django.shortcuts import redirect, render
from django.contrib import messages
from django.utils.decorators import method_decorator
from .decorators import *
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .service import UserService
from .forms import *

    

class CustomLoginView(View):
    form_class = EmailLoginForm
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index')  
            else:
                messages.error(request, "Email ou senha incorretos")
        return redirect('index')
    

class CustomRegisterView(View):
    template_name = 'produto/index.html'
    form_register = UserForm
    def post(self, request, *args, **kwargs):
        form = self.form_register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Ocorreu um erro ao criar a conta.")
            return redirect('index')
        
        
@method_decorator(user_is_manager, name='dispatch')
class CustomRegisterDashView(View):
    template_name = 'produto/index.html'
    form_register = UserDashForm
    def post(self, request, *args, **kwargs):
        form = self.form_register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Conta criada com sucesso!")
            return redirect('index')
        else:
            messages.error(request, "Ocorreu um erro ao criar a conta.")
            return render(request, self.template_name, {'form_register_dash': form})


@method_decorator(user_is_manager, name='dispatch')
class UserCreateView(CreateView):
    form_login = UserForm

    def post(self, request, *args, **kwargs):
        vorm = self.form_class(request.POST)
        if vorm.is_valid():
            
            email = vorm.cleaned_data.get('email')
            password = vorm.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login realizado com sucesso!")
                return redirect('index')  
            else:
                messages.error(request, "Email ou senha incorretos")
        return redirect('index')

    def form_valid(self, form):
        messages.success(self.request, "Usuário criado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro ao criar o usuário.")
        return super().form_invalid(form)


@method_decorator(user_is_manager, name='dispatch')
class UserUpdateView(UpdateView):
    template_name = 'users/user_register.html'
    form_class = UserForm
    success_url = reverse_lazy('dashboard_user')
    erro_url = reverse_lazy('dashboard_user')    

    def get_object(self):
        user_id = self.kwargs['pk']
        return UserService.get_user_details(user_id)

    def form_valid(self, form):
        UserService.update_existing_user(self.object.id, **form.cleaned_data)
        messages.success(self.request, "Usuário atualizado com sucesso!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Ocorreu um erro ao atualizar o usuário.")
        return super().form_invalid(form)


@method_decorator(user_is_manager, name='dispatch')    
class UserDeleteView(DeleteView):
    success_url = reverse_lazy('dashboard_user')  # Redirecionar após exclusão

    def get_object(self):
        user_id = self.kwargs['pk']
        return UserService.get_user_details(user_id)

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        UserService.delete_user(user.id)
        messages.success(request, "Usuário excluído com sucesso!")
        return super().delete(request, *args, **kwargs)
    


@method_decorator(user_is_manager, name='dispatch')
class DashboardManagerPage(View):
    template_name = 'users/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



@method_decorator(user_is_manager_or_common, name='dispatch')
class UserProfileView(View):
    template_name = 'users/profile.html'

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect('profile')
        else:
            messages.error(request, "Ocorreu um erro ao atualizar o perfil.")
            return render(request, self.template_name, {'form': form})
 

@method_decorator(user_is_manager, name='dispatch')
class UserDashView(View):
    template_name = 'users/user_list.html'
    paginate_by = 10
    form_register = UserDashForm

    def get(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)
        users = UserService.list_all_users(page=page, per_page=self.paginate_by)
        vorm = self.form_register()

        return render(request, self.template_name, {'users': users, 'form_register': vorm})