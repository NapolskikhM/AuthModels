"""модуль views фреймворка Django

classes:
SignUpView
PasswordChange

Functions:
delete_user(request) -> func
deleted_user(request) -> func
access_page(request) -> func

"""

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required


class SignUpView(CreateView):
    """Регистрация пользователя и перенаправление его на страницу входа"""
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PasswordChange(UpdateView):
    """Изменение пароля зарегистрированного пользователя"""
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")


@login_required
def delete_user(request):
    """Функция подтверждения удаления учетной записи пользователя"""
    return render(request, 'delete_user.html')


@login_required
def deleted_user(request):
    """Функция удаления учетной записи пользователя"""
    user = request.user
    user.delete()
    return render(request, 'deleted_user.html')


@login_required
def access_page(request):
    """Функция представления страницы ограниченного доступа"""
    return render(request, 'access_page.html')
