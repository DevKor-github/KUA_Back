from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from course.models import Course, Tag, Post, Comment, TimeTable
from student.models import Student
from django.contrib.auth.models import User

class CourseViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
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
            'course_room': ["Room 101", "Room 102", "Room 103"]
        }
        self.course = Course.objects.create(**self.course_data)

    def test_get_courses(self):
        url = reverse('course-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.tag_data = {'name': 'Django'}
        self.tag = Tag.objects.create(**self.tag_data)

    def test_get_tags(self):
        url = reverse('tag-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tag(self):
        url = reverse('tag-list')
        response = self.client.post(url, self.tag_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class PostViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post_data = {
            'course': self.course.id,
            'student': self.student.id,
            'title': 'Test Post',
            'content': 'This is a test post.'
        }
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')

    def test_get_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('post-list')
        response = self.client.post(url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CommentViewSetTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.comment_data = {
            'post': self.post.id,
            'student': self.student.id,
            'content': 'This is a test comment.'
        }
        self.comment = Comment.objects.create(post=self.post, student=self.student, content='This is a test comment.')

    def test_get_comments(self):
        url = reverse('comment-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        url = reverse('comment-list')
        response = self.client.post(url, self.comment_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class CoursePostListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.url = reverse('course-posts', kwargs={'course_id': self.course.id})

    def test_get_course_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PostCommentListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.comment = Comment.objects.create(post=self.post, student=self.student, content='This is a test comment.')
        self.url = reverse('post-comments', kwargs={'post_id': self.post.id})

    def test_get_post_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StudentPostListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.url = reverse('student-posts', kwargs={'student_id': self.student.id})

    def test_get_student_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class StudentCommentListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.comment = Comment.objects.create(post=self.post, student=self.student, content='This is a test comment.')
        self.url = reverse('student-comments', kwargs={'student_id': self.student.id})

    def test_get_student_comments(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TagPostListViewTest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id='CS101', course_name='Introduction to Computer Science',
            year=2024, semester=1, instructor='Prof. Smith', credits=3,
            classification='Major', course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]], course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.tag = Tag.objects.create(name='Django')
        self.post = Post.objects.create(course=self.course, student=self.student, title='Test Post', content='This is a test post.')
        self.post.tags.add(self.tag)
        self.url = reverse('tag-posts', kwargs={'tag': self.tag.name})

    def test_get_tag_posts(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class TimeTableViewSetTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick')
        self.client.force_authenticate(user=self.user)
        self.course = Course.objects.create(
            course_id="CS101",
            course_name="Introduction to Computer Science",
            instructor="Prof. Smith",
            credits=3,
            classification="Major",
            course_week=['월', '수', '금'],
            course_period=[[1, 2], [1, 2], [1, 2]],
            course_room=["Room 101", "Room 102", "Room 103"]
        )
        self.timetable = TimeTable.objects.create(student=self.student, course=self.course, year='2024', semester='1')

    def test_get_timetables(self):
        self.url = reverse('student-timetable', kwargs={'student_id': self.student.id})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_submit_timetable(self):
        self.url = reverse('submit-timetable', kwargs={'student_id': self.student.id})
        data = {
            'student': self.student,
            'course': self.course,
            'year': '2024',
            'semester': '1'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)