from django.shortcuts import render
from .serializers import UserSerializer
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class CreateView(APIView):
    def post(self, request):
        username = request.data.get('user_id')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username:
            return Response({'error': 'user_id is invalid'})
        if not password:
            return Response({'error': 'user_id is invalid'})
        if not email:
            return Response({'error': 'user_id is invalid'})

# class UserDestroy(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
class SignupView(APIView):
    def post(self, request):
        user = User.objects.create_user(
            username = request.data[id], 
            password = request.data['password'],
            email = request.data['email'],
            )
        student = models.Student(
            user = user,
            name = request.data['name'],
            nickname = request.data['nickname'],
        )
        
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})
        
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username = request.data['id'], password = request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status = 401)