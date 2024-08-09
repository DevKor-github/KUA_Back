from rest_framework import serializers
from .models import Course, Tag, Post, Comment, TimeTable
from student.models import Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseMinimalSerializer(serializers.ModelSerializer):
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

class PostMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'student_id']

class TimeTableSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), many=True)

    class Meta:
        model = TimeTable
        fields = ['student', 'year', 'semester', 'courses']

def create(self, validated_data):
    courses = validated_data.pop('courses', [])
    print(f"Creating timetable with courses: {courses}")  # 디버깅용 출력

    # 시간표 객체 생성
    timetable = TimeTable.objects.create(**validated_data)

    if courses:
        timetable.courses.set(courses)  # ManyToMany 관계 설정
        print(f"Successfully added courses to timetable: {timetable.id}")  # 디버깅용 출력
    else:
        print(f"No courses were provided for timetable: {timetable.id}")  # 디버깅용 출력

    return timetable