from django.db import models
from django.contrib.postgres.fields import ArrayField


class Course(models.Model):
    COURSE_DAYS = [
        ('월', 'Monday'),
        ('화', 'Tuesday'),
        ('수', 'Wednesday'),
        ('목', 'Thursday'),
        ('금', 'Friday'),
        ('토', 'Saturday'),
    ]
    
    # 학수번호
    course_id = models.CharField(max_length=20, unique=True)
    course_name = models.CharField(max_length=50)
    year = models.DateField().year()
    semester = models.IntegerField()
    instructor = models.CharField(max_length=30)
    credits = models.IntegerField()
    classification = models.CharField(max_length=10)

    # 수업 요일 리스트
    course_week = ArrayField(
        models.CharField(max_length=3, choices=COURSE_DAYS),
        size=7,
        default=list
    )
    
    # 수업 교시 이차원 배열
    course_period = ArrayField(
        ArrayField(
            models.IntegerField(),
            size=7,
        ),
        size=7,
        default=list
    )
    
    # 강의실 리스트(Nullable)
    course_room = ArrayField(
        models.CharField(max_length=100),
        size=7,
        default=list,
        null=True
    )
    
    def __str__(self):  
        return f"{self.year} 년도, {self.semester}학기 {self.instructor} 교수님 {self.course_name} ({self.course_id})"

# 태그 모델


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

# 게시글 (각 강의에 대한)

class Post(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attached_file = models.FileField(
        upload_to='attachments/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return f"{self.title}, {self.content[:20]}"


# 댓글
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 채택?
    is_chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.content[:20]  # 최초 20글자만 표시
