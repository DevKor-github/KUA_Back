from django.db import models
from courses.models import Course

class TodayPoll(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='today_polls')
    check_attention = models.BooleanField(default=None, null=True, blank=True)
    check_test = models.BooleanField(default=None, null=True, blank=True)
    check_homework = models.BooleanField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, blank=True)
