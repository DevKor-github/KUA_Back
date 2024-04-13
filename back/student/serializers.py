from . import models
from django.contrib.auth.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        student = models.Student(
            user = validated_data['user'],
            name = validated_data['name'],
        )
        return student
    
    class Meta:
        model = models.Student
        fields = ['user', 'name']

class EmailSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        email = models.Email(
            email = validated_data['email'],
            permission_code = validated_data['permission_code'],
        )
        return email
    
    class Meta:
        model = models.Email
        fields = ['email', 'permission_code']