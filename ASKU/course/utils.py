# course/utils.py

from .models import Course


def create_course_boards(crawled_data):
    for course_data in crawled_data:
        course, created = Course.objects.get_or_create(
            code=course_data['code'],
            defaults={
                'name': course_data['name'],
                'description': course_data.get('description', '')
            }
        )
        if created:
            print(f"Created course board for {course.name}")
        else:
            print(f"Course board for {course.name} already exists")
