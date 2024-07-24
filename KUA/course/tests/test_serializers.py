from django.test import TestCase
from course.models import Course, Tag, Post, Comment
from course.serializers import CourseSerializer, TagSerializer, PostSerializer, CommentSerializer
from student.models import Student
from django.contrib.auth.models import User
from django.utils import timezone

class CourseSerializerTest(TestCase):
    def setUp(self):
        self.course_data = {
            'course_id': 'CS101',
            'course_name': 'Introduction to Computer Science',
            'year': 2024,
            'semester': 2,
            'instructor': 'Prof. Smith',
            'credits': 3,
            'classification': 'Major',
            'course_week': ['월', '수', '금'],
            'course_period': [[1, 2], [1, 2], [1, 2]],
            'course_room': ['Room 101', 'Room 102', 'Room 103']
        }
        self.course = Course.objects.create(**self.course_data)

    def test_course_serializer(self):
        serializer_data = CourseSerializer(self.course).data
        serializer_data.pop('id')
        self.assertEqual(serializer_data, self.course_data)

class TagSerializerTest(TestCase):
    def setUp(self):
        self.tag_data = {'name': 'Django'}
        self.tag = Tag.objects.create(**self.tag_data)

    def test_tag_serializer(self):
        serializer_data = TagSerializer(self.tag).data
        serializer_data.pop('id')
        self.assertEqual(serializer_data, self.tag_data)

class PostSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick', permission_date=timezone.now())
        self.course = Course.objects.create(
            course_id="CS101",
            course_name="Introduction to Computer Science",
            year=2024,
            semester=1,
            instructor="Prof. Smith",
            credits=3,
            classification="Major",
            course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]],
            course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.post_data = {
            'course': self.course,
            'student': self.student,
            'title': 'Test Post',
            'content': 'This is a test post.'
        }
        self.post = Post.objects.create(**self.post_data)

    def test_post_serializer(self):
        serializer = PostSerializer(self.post)
        self.assertEqual(serializer.data['title'], self.post_data['title'])
        self.assertEqual(serializer.data['content'], self.post_data['content'])

class CommentSerializerTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick', permission_date=timezone.now())
        self.course = Course.objects.create(
            course_id="CS101",
            course_name="Introduction to Computer Science",
            year=2024,
            semester=1,
            instructor="Prof. Smith",
            credits=3,
            classification="Major",
            course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]],
            course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.post = Post.objects.create(
            course=self.course,
            student=self.student,
            title="Test Post",
            content="This is a test post."
        )
        self.comment_data = {
            'post': self.post,
            'student': self.student,
            'content': 'This is a test comment.'
        }
        self.comment = Comment.objects.create(**self.comment_data)

    def test_comment_serializer(self):
        serializer = CommentSerializer(self.comment)
        self.assertEqual(serializer.data['content'], self.comment_data['content'])
