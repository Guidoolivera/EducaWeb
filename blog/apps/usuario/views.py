from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse

# Create your views here.

class RegistrarUsuario(CreateView):
    template_name = 'register/register.html'
    form_class = RegistrarUsuarioForm

    def form_valid(self, form):
        messages.success(self.request, 'Registro exitoso. Por favor, Inicia Sesion.')
        form.save()

        return redirect('apps.usuario:registrar')

class LoginUsuario(LoginView):
    template_name = 'register/login.html'

    def get_success_url(self):
        messages.success(self.request, 'Login Exitoso')

        return reverse('apps.usuario:login')


class LogoutUsuario(LogoutView):
    template_name = 'register/logout.html'

    def get_success_url(self):
        messages.success(self.request, 'Logout Exitoso')

        return reverse ('apps.usuario:logout')