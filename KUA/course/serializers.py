from rest_framework import serializers
from .models import Course, Tag, Post, Comment, TimeTable
from student.models import Student
from django.contrib.auth.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'course_id']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'

    def create(self, validated_data):

        student = validated_data['student']
        course_id = validated_data['courses']
        year = validated_data['year']
        semester = validated_data['semester']

        check_student = Student.objects.filter(student=student)
        check_course = Course.objects.filter(
            course_id=course_id, year=year, semester=semester).exists()

        if check_student and check_course:
            timetable = TimeTable(
                student=student,
                course_id=course_id,
                year=year,
                semester=semester,
            )
            return timetable
        elif check_student == False:
            return {'error': 'This User id is not in Student Table.'}

        elif check_course == False:
            return {'error': 'This Course is not in Course Table.'}

        else:
            return {'error': 'code error'}
        
    class Meta:
        model = TimeTable
        fields = '__all__'