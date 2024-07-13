from rest_framework import serializers
from .models import TodayPoll, Briefing
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone


class TodayPollSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = TodayPoll
        fields = ['id', 'user', 'course', 'check_attention', 'check_test',
                  'check_homework', 'created_at', 'answered_at', 'user_id']
        read_only_fields = ['created_at', 'answered_at']

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User not found.")
        return value

    def create(self, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            validated_data['user'] = get_object_or_404(User, id=user_id)
        else:
            validated_data['user'] = self.context['request'].user if self.context['request'].user.is_authenticated else get_object_or_404(
                User, pk=1)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        if user_id:
            validated_data['user'] = get_object_or_404(User, id=user_id)
        return super().update(instance, validated_data)


class TodayPollAnswerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = TodayPoll
        fields = ['id', 'user', 'course', 'check_attention',
                  'check_test', 'check_homework', 'answered_at', 'user_id']
        read_only_fields = ['answered_at']

    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User not found.")
        return value
    
    def validate_todayPoll(self, value):
    
    def update(self, instance, validated_data):
        user_id = validated_data.pop('user_id', None)
        expired = validated_data.get('expired')
        if user_id:
            validated_data['user'] = get_object_or_404(User, id=user_id)

        instance.answered_at = timezone.now()
        return super().update(instance, validated_data)


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
