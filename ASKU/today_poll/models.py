from django.db import models
from course.models import Course


class TodayPoll(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='today_poll')
    check_attention = models.BooleanField(default=None, blank=True)
    check_test = models.BooleanField(default=None, blank=True)
    check_homework = models.BooleanField(default=None,  blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, blank=True)


class Briefing(models.Model):
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name='briefing')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Briefing for {self.course.course_name} on {self.created_at.date()}"
