from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            user_id = validated_data['user_id'],
            password = validated_data['password'],
            username = validated_data['username'],
            nickname = validated_data['nickname'],
            email = validated_data['email'],
        )
        return user
    class Meta:
        model = User
        fields = ['user_id', 'password', 'username', 'nickname', 'email']

