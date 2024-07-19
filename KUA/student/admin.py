from django.contrib import admin
from . import models
#  Register your models here.
admin.site.register(models.Student)
admin.site.register(models.TimeTable)
admin.site.register(models.CertificationCode)
admin.site.register(models.NicknameHistory)