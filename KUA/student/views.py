from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import render
from . import models
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from . import serializers
import string
import random
from django.core.mail import EmailMessage
from django.utils import timezone
from datetime import timedelta

class SubmitTimeTableView(generics.CreateAPIView): #id, 학수번호, 개설년도와 학기 정보를 통해 시간표를 등록하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(user.username)
        course_id = request.data['course_id']
        year = request.data['year']
        semester = request.data['semester']
        timetable = {
            'username': user.username,
            'course_id': course_id,
            'year': year,
            'semester': semester
        }
        serializer = serializers.TimeTableSerializer(data = timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'})
        return Response({'response': 'Time Table Rejected'})
    
class EmailCodeSendView(generics.CreateAPIView):
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
        
class SubmitTimeTableView(APIView):
    def post(self, request):
        username = request.data['id']
        course_id = request.data['course_id']
        year_semester = request.data['year_semester']
        timetable = models.TimeTable(
            username = username,
            course_id = course_id,
            year_semester = year_semester,
        )
        serializer = serializers.TimeTableSerializer(data = timetable)
        if serializer.is_valid():
            serializer.save()
            return {'response': 'Time Table Saved'}
        return {'response': 'Time Table Rejected'}
    
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
