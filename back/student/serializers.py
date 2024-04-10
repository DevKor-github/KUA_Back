from . import models
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            password = validated_data['password'],
            
            email = validated_data['email'],
        )
        student = models.Student(
            user = user,
            name = validated_data['name'],
        )
        return student
    
    class Meta:
        model = models.Student
        fields = ['username', 'password', 'name', 'nickname', 'email']