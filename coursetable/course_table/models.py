from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=20)
    #year = models.IntegerField()
    course_name = models.CharField(max_length=1000)
    instructor = models.CharField(max_length=1000)
    credits = models.IntegerField()
    classification = models.CharField(max_length=1000)
    course_week = models.TextField()
    course_period = models.TextField()
    course_room = models.TextField()



    def __str__(self):
        return self.course_name