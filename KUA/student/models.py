from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from django.core.exceptions import ValidationError
from django.utils import timezone
    
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 10, null = False, blank = False)
    nickname_change_time = models.DateTimeField(null = True, default='2024-07-01 12:22:44.398477+09')
    points = models.IntegerField(default = 0)
    #permission_date = models.DateTimeField(null = True, default='7')
    permission_date = models.DateTimeField(null = True, default=timezone.now)
    permission_type = models.CharField(max_length = 10)


    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.nickname

class CertificationCode(models.Model):
    email = models.CharField(max_length = 30, null = False, blank=False, unique=True)
    certification_code = models.CharField(default='', max_length = 8, null = False, blank = False)
    certification_check = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
class NicknameHistory(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, null = False, blank = False)
    nickname_time = models.DateTimeField(null = False)

    def __str__(self):
        return self.user