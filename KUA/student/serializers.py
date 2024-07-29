from . import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.response import Response
        
class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        if len(validated_data['username']) > 20 or len(validated_data['username']) < 0 or ' ' in validated_data['username'] or models.User.objects.filter(username = validated_data['username']).exists():
            return False
        
        if len(validated_data['password']) > 20 or len(validated_data['password']) < 0 or ' ' in validated_data['password']:
            return False

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