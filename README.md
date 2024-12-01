Предлагается работа по реализации на базе фреймворка Django методов  аутентификации пользователя на веб-ресурсе. 
Аутентификация и авторизация пользователя имеет важное значение для защиты  данных пользователей, предотвращения мошенничества и обеспечения безопасности в онлайн-транзакциях. Методов аутентификации множество, различные методы применяются в различных ситуациях.

В данной работе использованы следующие распространенные методы:

    Base authentication
    Session-based authentication
    JWT authentication
    Email authentication

Каждый метод реализован в качестве отдельного  Django проекта в целях упрощения и исключения конфликтов между различными методами внутри одного проекта/приложения.
Методы используют различные классы аутентификации в составе Django REST framework. Для регистрации пользователя используется стандартная модель User.
Реализована возможность пользователя зарегистрироваться, зайти на ресурс и покинуть его.
Имеются страница входа и страница, закрытая для несанкционированного доступа. Также предусмотрена работа сайта администратора.

            ​ 	Base authentication
Базовая аутентификация — один из самых простых способов реализации аутентификации. Во фреймворке Django REST (DRF) базовая аутентификация использует заголовки HTTP, в которых учетные данные пользователя отправляются в виде строк в кодировке base64. Используется класс BasicAuthentication DRF. Используется стандартная форма регистрации.

            ​ Session-based authentication
Этот метод аутентификации использует встроенную структуру сессий Django для аутентификации пользователей. Он требует использования файлов cookie для поддержания состояния сеанса. Применяется класс SessionAuthentication DRF. 

            ​ 	JWT authentication
JWT (JSON Web Tokens) - это закодированная строка JSON, которая передается в заголовках для аутентификации запросов. 
Для реализации метода использован пакет Simple JWT.
Для отладки и проверки приложения использовано приложение Postman.

            ​ 	Email authentication
Реализована возможность пользователя залогиниться, используя электронную почту, не вспоминая свои username и password. Для формирования и отправки письма использована функция Django send_mail. Создана кастомная страница регистрации с проверкой наличия username в базе. Для организации ограниченного доступа использован класс  IsAuthenticated. Для отладки приложения использована настройка в settings: EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'.
