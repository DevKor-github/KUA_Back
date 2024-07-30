# course/utils.py

from .models import Course

from django.conf import settings

def get_class_time(period):
    return settings.CLASS_TIMES.get(period, "Invalid period number")