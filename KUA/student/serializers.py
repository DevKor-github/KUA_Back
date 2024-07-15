from . import models
from django.contrib.auth.models import User
from rest_framework import serializers

class TimeTableSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        username = validated_data['username']
        check_username =  models.User.objects.filter(username=username).exists()
        course_id = validated_data['course_id']
        year = validated_data['year']
        semester = validated_data['semester']
        check_course =  models.Course.objects.filter(course_id = course_id, year = year, semester = semester).exists()

        if check_username and check_course: 
            timetable = models.TimeTable(
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
