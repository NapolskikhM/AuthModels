"""
модуль views фреймворка Django
регистрация пользователей и аутентификация  через почту

Functions:
main(request) -> func
home(request) -> func
signup(request) -> func
authenticate_(request) -> func
dashboard(request) -> func

"""


from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
import secrets
from django.contrib.auth.models import User
from django.contrib.auth import login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .forms import ContactForm, MagicLinkForm, TokenLoginForm

email = None
token = None
code = None


def main(request):
    """главная страница"""
    return render(request, "main.html")


@require_http_methods(["GET", "POST"])
def home(request: HttpRequest):
    """отправка кода на mail"""

    global email, token
    context = {}

    if request.POST:
        form = MagicLinkForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]  # Получаем адрес пользователя
            users = User.objects.all()

            emails = []  # список адесов для проверки
            for i in users:
                emails.append(i.email)

            if email in emails:  # проверка наличия адреса в зарегистрированных пользователях

                token = secrets.token_urlsafe(nbytes=32)  # формируем код
                # отправляем письмо
                send_mail(
                    subject="Access Code",
                    message=f"Ваш код доступа: {token}",
                    from_email="abcde@rambler.ru",
                    recipient_list=[email],
                    fail_silently=True,
                )
                return redirect('/auth') # отправляем на страницу ввода кода
            else:  # если email не зарегистрирован, возвращаем
                context['no_user'] = f'email {email} не зарегистрирован'
                context['email'] = email

    return render(request, "magic.html", context)

#
def signup(request):
    """регистрация пользователя"""
    users = User.objects.all()
    usernames = []
    username = None
    for i in users:
        usernames.append(i.username)
    info = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            mail = form.cleaned_data['mail']
            if password == repeat_password and username not in usernames: # проверки
                user = User.objects.create_user(username=username, password=password, email=mail)
                user.save() # сохраняем в базе
            else: # возвращаем с предупреждениями
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif username in usernames:
                    info['error'] = 'Пользователь уже существует'
    context = {'error': info, 'welcome': f'Приветствуем, {username}', 'username': username,
               'error_message': info.get('error')}
    return render(request, 'signup.html', context)


def authenticate_(request):
    """login"""

    global email, token, code

    if request.POST: # получаем введенный код
        form = TokenLoginForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["code"]
        if code == token: # сравниваем с оригиналом
            user = User.objects.get(email=email)
            login(request, user)
            return redirect("/dashboard") # отправляем на страницу с ограниченным доступом
    return render(request, "login.html")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    """страница ограниченного доступа"""
    return render(request, "dashboard.html")




