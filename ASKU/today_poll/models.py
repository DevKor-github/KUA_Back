from django.db import models
from courses.models import Course

# Create your models here.

class today_poll(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='today_polls')
    check_attention = models.BooleanField(default= None)
    check_test = models.BooleanField(default= None)
    check_homework = models.BooleanField(default= None)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(auto_now=False)
    
    