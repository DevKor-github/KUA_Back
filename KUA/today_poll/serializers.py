from rest_framework import serializers
from .models import TodayPoll, Briefing
from django.utils import timezone

class TodayPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayPoll
        fields = '__all__'
class TodayPollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayPoll
        fields = ['id', 'course_fk', 'student']

class TodayPollAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayPoll
        fields = ['check_attention', 'check_test', 'check_homework', 'answered_at']
        read_only_fields = ['answered_at']

    def update(self, instance, validated_data):
        instance.check_attention = validated_data.get('check_attention', instance.check_attention)
        instance.check_test = validated_data.get('check_test', instance.check_test)
        instance.check_homework = validated_data.get('check_homework', instance.check_homework)
        instance.answered_at = timezone.now()
        instance.save()
        return instance

class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
        
class BriefingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = ['id', 'course_fk', 'updated_at']
