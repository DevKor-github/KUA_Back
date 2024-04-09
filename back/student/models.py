from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
# Create your models here.

class UserManager(BaseUserManager):
    #일반 유저 생성
    def create_user(self, username, password, name, nickname, email):       
        user = self.model(
            username = username,
            name = name,
            nickname = nickname,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    #관리자 user 생성
    def create_superuser(self, username, password, name, nickname, email):
        user = self.create_user(
            username = username,
            password = password,
            nickname = nickname,
            name = name,
            email = email,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user

class Student(AbstractBaseUser):
    user = models.OneToOneField(User, ondelete=models.CASCADE)
    name = models.CharField(default='', max_length=20, null = False, blank=False)
    nickname = models.CharField(default='', max_length = 10, null = False, blank = False, unique = True)
    points = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)
    role = models.BooleanField(default = False)
    permission = models.BooleanField(default = False)

    #헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.nickname

    
