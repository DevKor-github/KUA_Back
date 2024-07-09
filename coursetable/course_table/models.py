from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length=10)
    #year = models.IntegerField()
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    credits = models.IntegerField()
    classification = models.CharField(max_length=100)
    course_week = models.TextField()
    course_period = models.TextField()
    course_room = models.TextField()



    def __str__(self):
        return self.course_name