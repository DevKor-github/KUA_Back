from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
# Create your models here.

# class StudentManager(BaseUserManager):
#     #일반 유저 생성
#     def create_student(self, username, password, name, nickname, email):       
#         user = self.model(
#             username = username,
#             email = self.normalize_email(email),
#         )
#         user.set_password(password)
#         student = self.model(
#             user = user,
#             name = name, 
#             nickname = nickname,
#         )
#         student.save(using=self.db)
#         return student

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(default='', max_length=20, null = False, blank=False, unique=False)
    # nickname = models.CharField(default='', max_length = 10, null = False, blank = False, unique = True)
    points = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    role = models.BooleanField(default = False)
    permission = models.BooleanField(default = False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.nickname

    
