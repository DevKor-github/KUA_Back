from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.core.exceptions import ValidationError
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 10, null = False, blank = False)
    points = models.IntegerField(default = 0)
    permission_date = models.DateTimeField(null = True)
    permission_type = models.CharField(max_length = 10)

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.CharField(max_length = 10)
    year_semester = models.CharField(max_length = 6)
    course_name = models.CharField(max_length = 20)
    course_time = models.CharField(max_length = 20)
    instructor = models.CharField(max_length = 20)
    def __str__(self):
        return self.course_id

class TimeTable(models.Model):
    id = models.AutoField(primary_key = True)
    username = models.CharField(null = False, max_length = 20)
    course_id = models.CharField(null = False, max_length=10)
    year_semester = models.CharField(null = False, max_length=6)

    def __str__(self):
        return self.id
    
