from rest_framework import serializers
from .models import TodayPoll, Briefing
from student.models import Student
from django.shortcuts import get_object_or_404
from django.utils import timezone

class TodayPollSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = TodayPoll
        fields = ['id', 'student', 'course', 'check_attention', 'check_test',
                  'check_homework', 'created_at', 'answered_at', 'student_id']
        read_only_fields = ['created_at', 'answered_at']

    def validate_student_id(self, value):
        if not Student.objects.filter(id=value).exists():
            raise serializers.ValidationError("Student not found.")
        return value

    def create(self, validated_data):
        student_id = validated_data.pop('student_id', None)
        if student_id:
            validated_data['student'] = get_object_or_404(Student, id=student_id)
        else:
            validated_data['student'] = self.context['request'].user.student if self.context['request'].user.is_authenticated else get_object_or_404(
                Student, user_id=1)  # 기본 학생 사용자
        return super().create(validated_data)

    def update(self, instance, validated_data):
        student_id = validated_data.pop('student_id', None)
        if student_id:
            validated_data['student'] = get_object_or_404(Student, id=student_id)
        return super().update(instance, validated_data)


class TodayPollAnswerSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = TodayPoll
        fields = ['id', 'student', 'course', 'check_attention',
                  'check_test', 'check_homework', 'answered_at', 'student_id']
        read_only_fields = ['answered_at']

    def validate_student_id(self, value):
        if not Student.objects.filter(id=value).exists():
            raise serializers.ValidationError("Student not found.")
        return value

    def validate_expired(self, data):
        if data.get('expired'):
            raise serializers.ValidationError("Already Expired.")
        return data

    def update(self, instance, validated_data):
        student_id = validated_data.pop('student_id', None)

        if student_id:
            validated_data['student'] = get_object_or_404(Student, id=student_id)

        instance.answered_at = timezone.now()
        return super().update(instance, validated_data)


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
