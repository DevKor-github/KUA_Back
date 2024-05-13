from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=20, null = False, blank=False, unique=False)
    nickname = models.CharField(default='', max_length = 10, null = False, blank = False, unique = True)
    points = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    role = models.BooleanField(default = False)
    permission = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.nickname

class Email(models.Model):
    email = models.CharField(max_length = 30, null = False, blank = False, unique = True)
    permission_code = models.CharField(default='', max_length = 8, null = False, blank = False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['permission_code']

    def __str__(self):
        return self.email

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
    
