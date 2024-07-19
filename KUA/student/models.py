from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.core.exceptions import ValidationError
from course.models import Course
    
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

class TimeTable(models.Model):
    username = models.CharField(null = False, max_length = 20)
    course_id = models.ForeignKey(Course, null = False, on_delete=models.CASCADE)
    year = models.CharField(null = False, max_length=6)
    semester = models.CharField(null = False, max_length = 6)

    def __str__(self):
        return self.id
    
