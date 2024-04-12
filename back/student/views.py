from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import serializers


class SignupView(APIView):
    def post(self, request):
        username = request.data['id']
        password = request.data['password']
        email = request.data['email']

        user = User.objects.create_user(
            username = request.data['id'], 
            password = request.data['password'],
            email = email,
        )
    
        student = models.Student(
            user = user,
            name = request.data['name'],
        )
        user.save()
        
        serializer = serializers.StudentSerializer(data = student)
        if serializer.is_valid():
            serializer.save()

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