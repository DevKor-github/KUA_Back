from .models import TodayPoll, Briefing
from django.utils import timezone
from course.models import Course


def create_briefing(course_id, target_date):
    try:
        course = Course.objects.get(id=course_id)
        polls = TodayPoll.objects.filter(course=course)

        if not polls.exists():
            return None

        total_polls = polls.count()
        attendance_count = polls.filter(check_attention=True).count()
        assignment_count = polls.filter(check_homework=True).count()
        exam_count = polls.filter(check_test=True).count()

        attendance_percentage = (attendance_count / total_polls) * 100
        assignment_percentage = (assignment_count / total_polls) * 100
        exam_percentage = (exam_count / total_polls) * 100

        content = (
            f"Attendance: {attendance_percentage:.2f}%\n"
            f"Assignment: {assignment_percentage:.2f}%\n"
            f"Exam: {exam_percentage:.2f}%\n"
        )

        # 기존 브리핑이 있는지 확인
        briefing, created = Briefing.objects.get_or_create(
            course=course,
            created_at__date=target_date,
            defaults={'content': content, 'created_at': timezone.now()}
        )

        if not created:
            # 기존 브리핑이 있으면 업데이트
            briefing.content = content
            briefing.save()

        return briefing

    except Course.DoesNotExist:
        print(f"No course found with id={course_id}")
        return None
    except Exception as e:
        print(f"Error updating or creating briefing: {e}")
        raise
