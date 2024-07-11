from django.db import models

# Create your models here.
class Course(models.Model):
    # 학수번호
    course_id = models.CharField(max_length=20)
    #year = models.IntegerField()
    # 강의명
    course_name = models.CharField(max_length=1000)
    # 교수명
    instructor = models.CharField(max_length=1000)
    # 학점
    credits = models.IntegerField()
    # 이수구분
    classification = models.CharField(max_length=1000)
    # 요일
    course_week = models.TextField()
    # 교시
    course_period = models.TextField()
    # 강의실
    course_room = models.TextField()



    def __str__(self):
        return self.course_name