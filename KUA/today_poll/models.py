from django.db import models


class TodayPoll(models.Model):
    course = models.ForeignKey(
        'course.Course', on_delete=models.CASCADE, related_name='todaypolls')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='todaypolls')
    check_attention = models.BooleanField(default=False, null=False)
    check_test = models.BooleanField(default=False, null=False)
    check_homework = models.BooleanField(default=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    answered_at = models.DateTimeField(null=True, auto_now=True)
    expired = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.course.course_name} - {self.user.username} - {self.created_at.date()}"


class Briefing(models.Model):
    course = models.ForeignKey(
        'course.Course', on_delete=models.CASCADE, related_name='briefings')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Briefing for {self.course.course_name} on {self.created_at.date()}"
