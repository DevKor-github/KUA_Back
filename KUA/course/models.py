from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


class Course(models.Model):
    def default_course_period():
        return [[], [], [], [], [], [], []]

    COURSE_DAYS = [
        ('월', 'Monday'),
        ('화', 'Tuesday'),
        ('수', 'Wednesday'),
        ('목', 'Thursday'),
        ('금', 'Friday'),
        ('토', 'Saturday'),
    ]

    course_id = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=50)
    year = models.IntegerField()
    semester = models.IntegerField()
    instructor = models.CharField(max_length=30)
    credits = models.IntegerField()
    classification = models.CharField(max_length=10)

    course_week = ArrayField(
        models.CharField(max_length=3, choices=COURSE_DAYS),
        size=7,
        default=list
    )

    course_period = ArrayField(
        ArrayField(
            models.IntegerField(),
            size=7,
        ),
        size=7,
        null=True,  # 초기값 설정을 피하기 위해 null=True 설정
        blank=True  # 필드가 비어 있어도 무시되도록 설정
    )

    course_room = ArrayField(
        models.CharField(max_length=100),
        size=7,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.id:  # 객체가 처음 생성될 때만 설정
            now = timezone.now()
            self.year = now.year
            self.semester = 1 if now.month < 6 else 2

            # course_period가 비어 있을 때만 기본값 설정
            if not self.course_period:
                self.course_period = [[], [], [], [], [], [], []]

        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.year} 년도, {self.semester}학기 {self.instructor} 교수님 {self.course_name} ({self.course_id})"


# 태그 모델


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

# 게시글 (각 강의에 대한)


class Post(models.Model):
    course_fk = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='posts')
    student = models.ForeignKey(
        'student.Student', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attached_file = models.FileField(
        upload_to='attachments/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True,  related_name='posts')

    def __str__(self):
        return f"{self.title}, {self.content[:20]}"


# 댓글
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    student = models.ForeignKey(
        'student.Student', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 채택?
    is_chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:20]  # 최초 20글자만 표시


class TimeTable(models.Model):
    student = models.OneToOneField(
        'student.Student', on_delete=models.CASCADE, related_name='timetables')
    course_fk = models.ManyToManyField(
        Course, related_name='timetables', blank=True)
    year = models.CharField(null=False, max_length=6)
    semester = models.CharField(null=False, max_length=6)

    def __str__(self):
        return f"{self.year}년도 {self.semester} 학기 {self.student}의 시간표"
