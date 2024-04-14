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
from django.core.mail import EmailMessage


class PermissionCodeSendView(APIView):
    def post(self, request):
        letters_set = string.ascii_letters
        random_code_list = random.sample(letters_set,8)
        random_code = ''.join(random_code_list)

        email = request.data['email']

        if not email:
            return Response({'error': 'Not Valid Email'})
        
        if User.objects.filter(email=email).exists():
            return Response({'error': 'This email is already used.'})
        
        email_message = EmailMessage(
            subject='AKSU Permission Code',
            body= f'물어보라KU 인증 번호는 {random_code}입니다.',
            to=[email],
        )
        email_message.send()
        
        if models.Email.objects.filter(email=email).exists():
            email_obj = models.Email.objects.get(email=email)
        else:
            email_obj = models.Email(email=email)

        email_obj.permission_code = random_code

        email_obj.save()

        return Response({'Permission Code Update' : True})

class PermissionCodeCheckView(APIView):
    def post(self, request):
        email = request.data['email']
        
        if not email:
            return Response({'error': 'Invalid Email Address'})
        
        if models.Email.objects.filter(email=email).exists():
            email_obj = models.Email.objects.get(email=email)
            if request.data['permission_code'] == email_obj.permission_code:
                return Response({'Permission': True})
            else:
                return Response({'Permission': False})
        
        else:
            return Response({'error': 'Invalid Email Address'})

class SignupView(APIView):
    def post(self, request):
        username = request.data['id']
        if User.objects.filter(username = username).exists():
            return Response({'error': 'This ID is already used'})
        
        password = request.data['password']
        email = request.data['email']

        user = User.objects.create_user(
            username = username,
            password = password,
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