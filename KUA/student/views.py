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
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics
from datetime import timedelta
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 이메일 코드 전송 기능


class EmailCodeSendView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CertificationCodeSerializer

    @swagger_auto_schema(
        operation_summary="이메일 인증 기능 코드입니다. - 완료",
        operation_description="이메일 입력 -> 인증코드 발행.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL)
            }
        ),
        responses={
            201: openapi.Response(description="Email Code Send Success"),
            500: openapi.Response(description="Email Code Send Rejected")
        }
    )
    def post(self, request):
        letters_set = string.ascii_letters
        random_code_list = random.sample(letters_set, 8)
        random_code = ''.join(random_code_list)

        email = request.data['email']

        if User.objects.filter(email=email).exists():
            return Response({'error': 'This email is already used.'}, status=400)

        email_message = EmailMessage(
            subject='KU&A Permission Code',
            body=f'KU&A 인증 번호는 {random_code}입니다.',
            to=[email],
        )
        email_message.send()

        email_object, created = models.CertificationCode.objects.get_or_create(
            email=email)
        email_object.certification_code = random_code
        email_object.certification_check = False
        email_object.save()

        return Response({'Permission Code Update': True}, status=201)

# 이메일 코드 인증 확인 기능


class EmailCodeCheckView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.CertificationCodeSerializer

    @swagger_auto_schema(
        operation_summary="이메일 인증 확인 코드입니다. - 완료",
        operation_description="email, code 입력 -> 인증코드 확인",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'code': openapi.Schema(type=openapi.TYPE_STRING)
            }
        ),
        responses={
            201: openapi.Response(description="Permission Success"),
            400: openapi.Response(description="Permission Rejected")
        }
    )
    def post(self, request):
        email = request.data['email']
        code = request.data['code']

        if not email:
            return Response({'error': 'Invalid Email Address'})

        if models.CertificationCode.objects.filter(email=email).exists():
            email_object = models.CertificationCode.objects.get(email=email)
            if code == email_object.certification_code:
                email_object.certification_check = True
                email_object.save()
                return Response(status=201)
            else:
                return Response(status=400)

        else:
            return Response({'error': 'Invalid Email Address'})

# 회원가입 기능


class SignupView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="회원가입 기능입니다. - 완료",
        operation_description="id(username), first_name, last_name, email, password, group입력 -> 회원가입 ",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'first_name': openapi.Schema(type=openapi.TYPE_STRING),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING),
                'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
                'group': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(description="Sign Up Success"),
            400: openapi.Response(description="Sign Up Rejected")
        }
    )
    def post(self, request):
        user_data = {
            'username': request.data['username'],
            'first_name': request.data['first_name'],
            'last_name': request.data['last_name'],
            'email': request.data['email'],
            'password': request.data['password'],
            'group': request.data['group'],
            'is_staff': False,
            'is_active': True,
            'is_superuser': False,
            'date_joined': timezone.now(),
        }

        user_serializer = serializers.UserSerializer(data=user_data)
        if not user_serializer.is_valid():
            return Response({'Invalid User Information'})

        user = user_serializer.save()

        student_number = models.Student.objects.count()

        nickname_animal = ['고양이', '강아지', '호랑이', '토끼', '쥐', '기린', '얼룩말', '여우']

        random_animal = random.choices(nickname_animal, k=1)

        nickname = random_animal[0] + str(student_number)

        student = {
            'user': user.id,
            'nickname': nickname,
            'nickname_change_time': timezone.now(),
            'points': 0,
            'permission_type':  '7',
            'permission_date': timezone.now(),
        }
        

        student_serializer = serializers.StudentSerializer(data=student)

        if not student_serializer.is_valid():
            return Response(student_serializer.errors)

        student_serializer.save()
        history_data = {
            'user': user.id,
            'nickname' : nickname,
            'nickname_time': timezone.now()
        }
        serializer = serializers.NicknameHistorySerializer(data=history_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            token = Token.objects.create(user=user)
            return Response({"Token": token.key})      
        else:
            return Response({'error': 'Failed to save nickname history'}, status=400)

# 로그인 기능


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(
        operation_summary="로그인 기능입니다. - 완료",
        operation_description="id(username), password입력 -> 로그인(Token return)",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING),
                'password': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(description="Login Success"),
            400: openapi.Response(description=" Login Rejected")
        }
    )
    def post(self, request):
        from datetime import datetime
        user = authenticate(
            username=request.data['username'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            user.last_login = timezone.localtime()
            user.save()
            return Response({"Token": token.key})
        else:
            return Response(status=400)

# 포인트 획득 기능
class PointGetView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StudentSerializer

    point_reward = {
        'answer': 5,
        'chosen': 20,
        'survey': 10
    }

    @swagger_auto_schema(
        operation_summary="포인트 획득 기능입니다. - 완료",
        operation_description="포인트 타입 획득 타입(answer, chosen, survey)을 입력 -> 해당 타입에 따라 포인트 획득",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_type': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(description="Point Get Success"),
            400: openapi.Response(description="Point Get Rejected")
        }
    )
    def post(self, request):  # If using UpdateAPIView, consider using put or patch
        user = request.user
        point_type = request.data.get('point_type')
        
        if not point_type or point_type not in self.point_reward:
            return Response({'error': 'Invalid point type'}, status=400)

        try:
            student = user.student
        except models.Student.DoesNotExist:
            return Response({'error': 'Student not found'}, status=400)

        reward = self.point_reward.get(point_type)
        student.points += reward
        student.save()

        history_data = {
            'user': user.id,
            'purpose': 'G',
            'point': reward,
            'point_time': timezone.now()
        }
        
        serializer = serializers.PointHistorySerializer(data=history_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(f"Get {reward} Points", status=201)
        else:
            return Response({'error': 'Failed to save point history'}, status=400)

# 포인트로 이용권 구매 기능
class PointUseView(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StudentSerializer

    point_costs = {
        '1': 80,
        '7': 160,
        '14': 240,
        '30': 300
    }

    @swagger_auto_schema(
        operation_summary="포인트로 이용권 구매하는 기능입니다. - 완료",
        operation_description="이용권 type(1, 7, 14, 30)을 입력 -> 해당 타입에 따라 포인트를 사용하여 이용권 구매 OR 실패",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'point_costs': openapi.Schema(type=openapi.TYPE_STRING),
            }
        ),
        responses={
            201: openapi.Response(description="Point Use Success"),
            400: openapi.Response(description="Point Use Rejected")
        }
    )
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
            student.permission_type = permission_type
            student.save()
            history_data = {
                'user': user.id,
                'purpose': 'U',
                'point': cost,
                'point_time': timezone.now()
            }
            
            serializer = serializers.PointHistorySerializer(data=history_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(f"Use {cost} Points", status=201)
            else:
                return Response({'error': 'Failed to save point history'}, status=400)

        else:
            return Response({'error': ' invalid using points type'})

# 사용자가 게시물 접근 권한이 있는지 확인하는 기능


class IsPermissionView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StudentSerializer

    @swagger_auto_schema(
        operation_summary="이용권 보유 여부를 확인하는 기능입니다. - 완료",
        operation_description="파라미터 없이 get 요청 -> 보유한 이용권이 타당하면 Success return",
        responses={
            201: openapi.Response(description="Success"),
            400: openapi.Response(description="You Need to Buy")
        }
    )
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

#id로 닉네임 조회하는 기능

class GetNickNameView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.NicknameSerializer

    @swagger_auto_schema(
        operation_summary="id를 parameter로 닉네임을 조회하는 기능입니다 - 완료",
        operation_description="user_id를 parameter로 입력 -> 닉네임 get",
        manual_parameters=[
            openapi.Parameter('user_id', openapi.IN_QUERY, description="user Id", type=openapi.TYPE_STRING)
        ],
        responses={
            200: openapi.Response(description='Nickname retrieved successfully'),
            404: openapi.Response(description='User not found')
        }
    )
    def get(self, request):
        user_id = request.query_params.get('user_id')

        try:
            student = models.Student.objects.get(user=user_id)
            serializer = self.serializer_class(student)
            return Response(serializer.data, status=200)
        except models.Student.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

#현재 포인트 조회하기 기능

class GetNowPointView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.StudentSerializer

    @swagger_auto_schema(
        operation_summary="현재 포인트를 조회하는 기능입니다 - 완료",
        operation_description="파라미터 없이 get 요청 -> 현재 보유한 포인트 return",
        responses={
            201: openapi.Response(description="Success"),
            400: openapi.Response(description="Not Success")
        }
    )
    def get(self, request):
        user = request.user

        try:
            student = user.student
            return Response(student.points, status = 200)
        
        except models.Student.DoesNotExist:
            return Response("Student not found", status=400)


class UserStudentInfoView(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        operation_summary="유저의 학생 정보 반환 뷰 - 완료",
        operation_description="특정 학생 ID를 쿼리 파라미터로 입력받아 해당 학생의 정보를 반환합니다. 아무 파라미터도 입력하지 않았을 때는 현재 로그인한 학생의 정보를 반환합니다.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_QUERY,
                description="학생 ID (선택적)",
                type=openapi.TYPE_INTEGER
            ),
        ],
    )
    def get(self, request):
        student_id = request.query_params.get('id')  # 쿼리 파라미터에서 'id'를 가져옴

        try:
            if student_id:
                # 특정 학생 ID로 조회
                student = models.Student.objects.get(id=student_id)
            else:
                # 현재 로그인한 유저의 학생 정보 조회
                student = models.Student.objects.get(user=request.user)
                
            student_data = {
                "user_id": student.user.id,
                "nickname": student.nickname,
                "points": student.points,
                "permission_date": student.permission_date,
                "permission_type": student.permission_type,
            }
            return Response(student_data)
        except models.Student.DoesNotExist:
            return Response({"error": "학생 정보가 없습니다."}, status=404)

#로그인 한 사용자의 포인트 사용 기록을 알 수 있는 기능
class GetPointHistoryView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PointHistorySerializer

    @swagger_auto_schema(
        operation_summary="유저의 포인트 사용 기록 반환 뷰",
        operation_description="파라미터 입력 x -> 로그인 되어 있는 사용자의 포인트 사용 기록 return",
        responses={
            201: openapi.Response(description="Success"),
            400: openapi.Response(description="Not Success")
        }
    )

    def get(self, request):
        user = request.user

        try:
            history = models.PointHistory.objects.all(user = user.id)
            return Response(history, status = 200)
        
        except:
            return Response("Student not found", status=400)
         