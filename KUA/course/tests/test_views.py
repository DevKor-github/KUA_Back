from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from course.models import Course, Tag, Post, Comment
from student.models import Student
from django.contrib.auth.models import User
from django.utils import timezone

class CourseViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.course_data = {
            'course_id': 'CS101',
            'course_name': 'Introduction to Computer Science',
            'year': 2024,
            'semester': 1,
            'instructor': 'Prof. Smith',
            'credits': 3,
            'classification': 'Major',
            'course_week': ['월', '수', '금'],
            'course_period': [[1, 2], [1, 2], [1, 2]],
            'course_room': ['Room 101', 'Room 102', 'Room 103']
        }
        self.course = Course.objects.create(**self.course_data)
        self.url = reverse('course-list')

    def test_get_courses(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_course(self):
        new_course_data = self.course_data.copy()
        new_course_data['course_id'] = 'CS102'
        response = self.client.post(self.url, new_course_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TagViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag_data = {'name': 'Django'}
        self.tag = Tag.objects.create(**self.tag_data)
        self.url = reverse('tag-list')

    def test_get_tags(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tag(self):
        new_tag_data = {'name': 'Python'}
        response = self.client.post(self.url, new_tag_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PostViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
            'course': self.course.id,
            'student': self.student.id,
            'title': 'Test Post',
            'content': 'This is a test post.'
        }
        self.post = Post.objects.create(**self.post_data)
        self.url = reverse('post-list')

    def test_get_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        new_post_data = self.post_data.copy()
        new_post_data['title'] = 'New Post'
        response = self.client.post(self.url, new_post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CommentViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
            'post': self.post.id,
            'student': self.student.id,
            'content': 'This is a test comment.'
        }
        self.comment = Comment.objects.create(**self.comment_data)
        self.url = reverse('comment-list')

    def test_get_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        new_comment_data = self.comment_data.copy()
        new_comment_data['content'] = 'New Comment'
        response = self.client.post(self.url, new_comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CoursePostListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.url = reverse('course-posts', kwargs={'course_id': self.course.id})

    def test_get_course_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostCommentListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.comment = Comment.objects.create(
            post=self.post,
            student=self.student,
            content="This is a test comment."
        )
        self.url = reverse('post-comments', kwargs={'post_id': self.post.id})

    def test_get_post_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TagPostListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.tag = Tag.objects.create(name='Django')
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
            title="Test Post",
            content="This is a test post."
        )
        self.post.tags.add(self.tag)
        self.url = reverse('tag-posts', kwargs={'tag': self.tag.name})

    def test_get_tag_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StudentPostListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.url = reverse('student-posts', kwargs={'student_id': self.student.id})

    def test_get_student_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StudentCommentListViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
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
        self.comment = Comment.objects.create(
            post=self.post,
            student=self.student,
            content="This is a test comment."
        )
        self.url = reverse('student-comments', kwargs={'student_id': self.student.id})

    def test_get_student_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
