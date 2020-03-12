from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

# Create your views here.

User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = CustomLoginForm

