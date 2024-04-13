from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . import serializers
import string
import random

class PermissionCodeSendView(APIView):
    def post(self, request):
        letters_set = string.ascii_letters
        random_code_list = random.sample(letters_set,8)
        random_code = ''.join(random_code_list)

        email = request.data['email']

        if not email:
            return Response({'error': 'Not Valid Email'})
        
        if email not in models.Email:
        else:
            email_db = models.Email.objects.get(email=email)
            permission_code_db = random_code


class PermissionCodeCheckView(APIView):
    def post(self, request):
        if

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