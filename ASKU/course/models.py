from django.db import models


class Course(models.Model):
    course_id = models.CharField(max_length=20, unique=True)
    year = models.IntegerField()
    course_name = models.CharField(max_length=100)
    course_time = models.CharField(max_length=50)
    instructor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_name} ({self.year})"


class Post(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:20]  # 최초 20글자만 표시
