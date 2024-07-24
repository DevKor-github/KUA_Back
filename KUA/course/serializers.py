from rest_framework import serializers
from .models import Course, Tag, Post, Comment, TimeTable
from django.contrib.auth.models import User

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


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
    def create(self, validated_data):
        username = validated_data['username']
        check_username =  User.objects.filter(username=username).exists()
        course_id = validated_data['course_id']
        year = validated_data['year']
        semester = validated_data['semester']
        check_course =  Course.objects.filter(course_id = course_id, year = year, semester = semester).exists()

        if check_username and check_course: 
            timetable = TimeTable(
                username = username,
                course_id = course_id,
                year = year,
                semester = semester,
            )
            return timetable
        elif check_username == False:
            return {'error': 'This User id is not in User Table.'}
        
        elif check_course == False:
            return {'error': 'This Course is not in Course Table.'}
        
        else:
            return {'error': 'code error'}