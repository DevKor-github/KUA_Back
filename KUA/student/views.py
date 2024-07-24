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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics



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

class PointGetView(generics.UpdateAPIView):  # 포인트 값과 user를 받아 해당 포인트 값만큼 유저가 포인트를 얻는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    point_reward = {
        'answer': 5,
        'chosen': 20,
        'survey': 10
    }

    def post(self, request):
        user = request.user
        point_type = request.data['point_type']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        reward = self.point_reward.get(point_type)

        if reward:
            student.points += reward
            student.save()
            return Response(f"Get {reward} Points")

        else:
            return Response({'error': ' invalid getting points type'})


class PointUseView(generics.UpdateAPIView):  # 포인트를 이용하여 이용권을 구매하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    point_costs = {
        '1': 80,
        '7': 160,
        '14': 240,
        '30': 300
    }

    def post(self, request):
        user = request.user
        permission_type = request.data['point_costs']
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        cost = self.point_costs.get(permission_type)

        if cost:
            if student.points < cost:
                return Response('Not Enough Points')
            student.points -= cost
            student.permission_date = timezone.now()
            student.permission_type = '1'
            student.save()
            return Response(f"Get {permission_type} day permission")

        else:
            return Response({'error': ' invalid using points type'})

class IsPermissionView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        if timezone.now() - student.permission_date > timedelta(days=int(student.permission_type)):
            return Response("You Need to Buy")
        else:
            return Response("Success")
