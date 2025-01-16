from . import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
        
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        email = validated_data['email']
        first_name = validated_data.get('first_name', '')
        last_name = validated_data.get('last_name', '')
        group_name = validated_data.get('group', None)
        is_staff = validated_data.get('is_staff', False)
        is_active = validated_data.get('is_active', True)
        is_superuser = validated_data.get('is_superuser', False)
        
        if len(username) > 20 or len(username) < 1 or ' ' in username:
            raise serializers.ValidationError({"username": "사용자 이름은 1~20자 사이여야 하며, 공백이 포함될 수 없습니다."})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "이미 사용 중인 사용자 이름입니다."})

        if len(password) > 20 or len(password) < 1 or ' ' in password:
            raise serializers.ValidationError({"password": "비밀번호는 1~20자 사이여야 하며, 공백이 포함될 수 없습니다."})

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "이미 사용 중인 이메일입니다."})
        
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=is_staff,
            is_active=is_active,
            is_superuser=is_superuser,
            date_joined=validated_data['date_joined'],
        )
        
        group_name = validated_data.get('group')
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