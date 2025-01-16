from . import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.validator import UniqueValidator
        
class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="이미 사용 중인 사용자 이름입니다."),
        ]
    )
    
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="이미 사용 중인 이메일입니다."),
        ]
    )
    
    password = serializers.CharField(
        max_length=20,
        min_length=1,
        write_only=True,
    )
        
    def create(self, validated_data):
        group_name = validated_data.get('group')
        user = User.objects.create_user(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            password = validated_data['password'],
            is_staff = validated_data['is_staff'],
            is_active = validated_data['is_active'],
            is_superuser = validated_data['is_superuser'],
            date_joined = validated_data['date_joined'],
        )
        
        if group_name:
            group = Group.objects.filter(name=group_name).first()
            if group:
                user.groups.add(group)

        return user
    
    class Meta:
        model = User
        fields = '__all__'
        
class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student = models.Student.objects.create(
            user = validated_data['user'],
            nickname = validated_data['nickname'],
            points = 0,
            permission_date = validated_data['permission_date'],
            permission_type = validated_data['permission_type'],
        )
        return student
    
    class Meta:
        model = models.Student
        fields = '__all__'

class CertificationCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

class NicknameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class PointHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PointHistory
        fields = '__all__'

class NicknameHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NicknameHistory
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ['name', 'tag', 'image']