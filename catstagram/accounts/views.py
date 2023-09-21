from django import views
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy

from catstagram.accounts.forms import UserCreateForm

CatstagramUserModel = get_user_model()


class SignUpView(views.generic.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')
