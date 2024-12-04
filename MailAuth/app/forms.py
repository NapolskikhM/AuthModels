"""
модуль forms фреймворка Django

classes:
ContactForm
MagicLinkForm
TokenLoginForm

"""

from django import forms


class ContactForm(forms.Form):
    """форма регистрации пользователя"""
    username = forms.CharField(max_length=30, label='Введите имя')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(label='Повторите пароль')
    mail = forms.EmailField(label='Введите email')


class MagicLinkForm(forms.Form):
    """форма email пользователя"""
    email = forms.EmailField()


class TokenLoginForm(forms.Form):
    """форма кода доступа из письма"""
    code = forms.CharField(max_length=43, label='Введите код из Email')

