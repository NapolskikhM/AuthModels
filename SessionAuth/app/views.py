"""модуль views фреймворка Django
регистрация и аутентификация пользователя

classes:
SignUpView

Functions:
registered_(request) -> func
deleted_user(request) -> func

"""


from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUpView(generic.CreateView):
    """регистация пользователя с переходом на страницу входа"""
    form_class = UserCreationForm
    success_url = reverse_lazy('registered_')
    template_name = 'signup.html'


@api_view(['GET'])
@permission_classes([AllowAny])
def registered_(request):
    """подтверждение регистрации"""
    return render(request, 'registered.html')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    """страница ограниченного доступа"""
    return render(request, 'access_page.html')


