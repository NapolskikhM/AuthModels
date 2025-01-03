"""модуль views фреймворка Django

classes:
RestrictedView

Functions:
main_page(request) -> func

"""

from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class RestrictedView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(data={"message": "You have access to this restricted content."})


def main_page(request):
    return render(request, 'mainpage.html')


