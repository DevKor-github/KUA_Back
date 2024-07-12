import math
from course_table.models import Course

# 모든 Course 객체 가져오기
courses = Course.objects.all()

for course in courses:
    changed = False
    
    # NaN 검사 및 변환
    if isinstance(course.course_id, float) and math.isnan(course.credits):
        course.credits = None
        changed = True
    if isinstance(course.course_week, str) and course.course_week == 'nan':
        course.course_week = None
        changed = True
    if isinstance(course.course_period, str) and course.course_period == 'nan':
        course.course_period = None
        changed = True
    if isinstance(course.credits, float) and math.isnan(course.credits):
        course.credits = None
        changed = True
    if isinstance(course.course_week, str) and course.course_week == 'nan':
        course.course_week = None
        changed = True
    if isinstance(course.course_period, str) and course.course_period == 'nan':
        course.course_period = None
        changed = True

    
    if changed:
        course.save()
