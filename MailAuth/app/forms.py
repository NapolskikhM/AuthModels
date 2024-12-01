from django import forms

# регистрация пользователя
class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Введите имя')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(label='Повторите пароль')
    mail = forms.EmailField(label='Введите email')


# email пользователя
class MagicLinkForm(forms.Form):
    email = forms.EmailField()


# код доступа из письма
class TokenLoginForm(forms.Form):
    code = forms.CharField(max_length=43, label='Введите код из Email')

