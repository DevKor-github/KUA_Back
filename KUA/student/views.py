from django.shortcuts import render
from . import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from . import serializers
import string
import random
from django.core.mail import EmailMessage
from django.utils import timezone


class EmailCodeSendView(APIView):
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
            subject='KU&A Permission Code',
            body= f'KU&A 인증 번호는 {random_code}입니다.',
            to=[email],
        )
        email_message.send()
        
        if models.CertificationCode.objects.filter(email=email).exists():
            email_object = models.CertificationCode.objects.get(email=email)
        else:
            email_object = models.CertificationCode(email=email)

        email_object.certification_code = random_code

        email_object.save()

        return Response({'Permission Code Update' : True})

class EmailCodeCheckView(APIView):
    def post(self, request):
        email = request.data['email']
        code = request.data['code']
        
        if not email:
            return Response({'error': 'Invalid Email Address'})
        
        if models.CertificationCode.objects.filter(email=email).exists():
            email_object = models.CertificationCode.objects.get(email=email)
            if code == email_object.certification_code:
                email_object.certification_check = True
                return Response({'Permission': True})
            else:
                return Response({'Permission': False})
        
        else:
            return Response({'error': 'Invalid Email Address'})

class CreateGroupView(APIView):
    def post(self, request):
        group = Group.objects.create(name=request.data['group_name'])
        return Response('Success to create group')
    
class SignupView(APIView):
    def post(self, request):
        user_data = {
            'username' : request.data['username'],
            'first_name' : request.data['first_name'],
            'last_name' : request.data['last_name'],
            'email' : request.data['email'],
            'password' : request.data['password'],
            'group': request.data['group'],
            'is_staff' : False,
            'is_active' : True,
            'is_superuser' : False,
            'date_joined' : timezone.now(),
        }
        
        user_serializer = serializers.UserSerializer(data = user_data)
        if not user_serializer.is_valid():
            return Response({'Invalid User Infomation'})
        
        user = user_serializer.save()
        
        student = {
            'user': user.id,
            'nickname': 'hi',
            'points': 0,
            'permission_type':  '7',
            'permission_date': timezone.now(),
        }

        student_serializer = serializers.StudentSerializer(data = student)

        if not student_serializer.is_valid():   
            return Response(student_serializer.errors)
            
        student_serializer.save()
        token = Token.objects.create(user = user)
        return Response({"Token": token.key})
        
        
class LoginView(APIView):
    def post(self, request):
        user = authenticate(username = request.data['username'], password = request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status = 401)
        
