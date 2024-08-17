from rest_framework import serializers
from .models import *
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

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id', 'image']

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'course_fk', 'student', 'likes', 'views', 'reported', 'tags']

    def create(self, validated_data):
        image_uploads = validated_data.pop('image_uploads', [])
        post = Post.objects.create(**validated_data)
        
        for image in image_uploads[:10]:  # 최대 10개의 이미지 처리
            PostImage.objects.create(post=post, image=image)
        
        return post

class PostMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'likes']

class CommentSerializer(serializers.ModelSerializer):
    parent_comment = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(), allow_null=True, required=False
    )

    class Meta:
        model = Comment
        fields = '__all__'

class CommentMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post_id', 'student_id']

class TimeTableSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    courses = CourseSerializer(many=True, read_only=True)
    course_ids = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all(), write_only=True
    )

    class Meta:
        model = TimeTable
        fields = ['id', 'student', 'year', 'semester', 'courses', 'course_ids']

    def create(self, validated_data):
        course_ids = validated_data.pop('course_ids')
        timetable = TimeTable.objects.create(**validated_data)
        timetable.courses.set(course_ids)
        return timetable

    def update(self, instance, validated_data):
        course_ids = validated_data.pop('course_ids', None)
        instance.student = validated_data.get('student', instance.student)
        instance.year = validated_data.get('year', instance.year)
        instance.semester = validated_data.get('semester', instance.semester)

        if course_ids:
            instance.courses.set(course_ids)

        instance.save()
        return instance