from django.db import models


class Course(models.Model):
    # 학수번호
    course_id = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_time = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)
    class_day_first = models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'),
                                          ('Fri', 'Friday')], default= None)
    class_day_second = models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'),
                                          ('Fri', 'Friday')], default= None)
    start_time = models.IntegerField(default=None)
    end_time = models.IntegerField(default=None)

    def __str__(self):
        return f"{self.course_name} ({self.year})"



# 게시글 (각 강의에 대한)
class Post(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file_posted = models.FileField(blank=True)

    def __str__(self):
        return self.title
    
# 태그 모델
class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)
    posts = models.ManyToManyField(Post)

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
