# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class Course(models.Model):
    # ?�수번호
    course_id = models.CharField(max_length=20)
    # 강의�?
    course_name = models.CharField(max_length=1000)
    # 교수�?
    instructor = models.CharField(max_length=1000)
    # ?�점
    credits = models.IntegerField()
    # ?�수구분
    classification = models.CharField(max_length=1000)
    # ?�일
    course_week = models.TextField()
    # 교시
    course_period = models.TextField()
    # 강의??
    course_room = models.TextField()

    def __str__(self):
        return self.course_name
