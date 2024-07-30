from django.test import TestCase
from django.contrib.auth.models import User
from student.models import Student
from course.models import Course, Tag, Post, Comment, TimeTable
from django.utils import timezone

class CourseModelTest(TestCase):
    def setUp(self):
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

    def test_course_creation(self):
        self.assertEqual(self.course.course_name, "Introduction to Computer Science")
        self.assertEqual(self.course.year, 2024)
        self.assertEqual(self.course.instructor, "Prof. Smith")

class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Django")

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, "Django")

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick')
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
        self.post = Post.objects.create(
            course=self.course,
            student=self.student,
            title="Test Post",
            content="This is a test post."
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.content, "This is a test post.")
        self.assertEqual(self.post.student.nickname, "testnick")

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick')
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

    def test_comment_creation(self):
        self.assertEqual(self.comment.content, "This is a test comment.")
        self.assertEqual(self.comment.student.nickname, "testnick")

class TimeTableModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.student = Student.objects.create(user=self.user, nickname='testnick')
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

    def test_timetable_creation(self):
        self.assertEqual(self.timetable.year, '2024')
        self.assertEqual(self.timetable.semester, '1')
        self.assertEqual(self.timetable.student.nickname, 'testnick')
        self.assertEqual(str(self.timetable), '2024년도 1 학기 testnick의 시간표')