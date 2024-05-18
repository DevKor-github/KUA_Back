import json
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
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone


class PermissionCodeSendView(APIView): #이메일 인증을 위해 제출한 이메일에 인증 코드를 내보내는 view
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

class PermissionCodeCheckView(APIView): #입력한 메일 인증 번호가 맞는지 틀린지 체크하는 view
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

class SignupView(APIView): #아이디, 비밀번호, 이메일을 통해 회원가입 하는 view
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
        student.save()
        
        serializer = serializers.StudentSerializer(data = student)
        if serializer.is_valid():
            serializer.save()

        token = Token.objects.create(user=user)

        return Response({"Token": token.key})
        
class LoginView(APIView): #id, 비밀번호를 통해 로그인하는 view
    def post(self, request):
        user = authenticate(username = request.data['id'], password = request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status = 401)
        
class SubmitTimeTableView(APIView): #id, 학수번호, 개설년도와 학기 정보를 통해 시간표를 등록하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        print(user.username)
        course_id = request.data['course_id']
        year_semester = request.data['year_semester']
        timetable = {
            'username': user.username,
            'course_id': course_id,
            'year_semester': year_semester,
        }
        serializer = serializers.TimeTableSerializer(data = timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'})
        return Response({'response': 'Time Table Rejected'})
    
class PointGetView(APIView): #포인트 값과 user를 받아 해당 포인트 값만큼 유저가 포인트를 얻는 view
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)

        student.points += int(request.data['points'])
        student.save()

        return Response("Point added successfully")
    
class PointUseView(APIView): #포인트를 이용하여 이용권을 구매하는 view
    authentication_classes = [TokenAuthentication]
    permission_classes =[IsAuthenticated]
    
    def post(self, request):
        user = request.user
        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response("Student not found", status = 400)
        
        if student.points < 40: #이용권 구매 값 40 포인트로 가정함
            return Response("Cannot Get Permission")
        student.points -= 40

        student.permission_date = timezone.now()
        student.save()

        return Response("Success For Getting Permission")

