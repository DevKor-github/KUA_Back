from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from .models import TodayPoll, Briefing
from .scheduler import *
import json

@receiver(post_migrate)
def restart_scheduler(sender, **kwargs):
    start()


@receiver(post_save, sender=TodayPoll)
def update_briefing(sender, instance, created, **kwargs):
    if instance.answered_at:
        # 설문이 응답되었을 때 브리핑 업데이트
        target_date = instance.created_at.date()
        
        total_polls = TodayPoll.objects.filter(
            course_fk=instance.course_fk,
            created_at__date=target_date
        ).count()

        # 응답된 설문들만 가져옴
        answered_polls = TodayPoll.objects.filter(
            course_fk=instance.course_fk,
            created_at__date=target_date,
            answered_at__isnull=False
        ).count()
        
        attendance_true = TodayPoll.objects.filter(
            course_fk=instance.course_fk,
            created_at__date=target_date,
            check_attention=True
        ).count()

        assignment_true = TodayPoll.objects.filter(
            course_fk=instance.course_fk,
            created_at__date=target_date,
            check_homework=True
        ).count()

        exam_true = TodayPoll.objects.filter(
            course_fk=instance.course_fk,
            created_at__date=target_date,
            check_test=True
        ).count()

        response_percentage = (answered_polls / total_polls) * 100 if total_polls > 0 else 0
        attendance_percentage = (attendance_true / answered_polls) * 100 if total_polls > 0 else 0
        assignment_percentage = (assignment_true / answered_polls) * 100 if total_polls > 0 else 0
        exam_percentage = (exam_true / answered_polls) * 100 if total_polls > 0 else 0
        
        briefing, created = Briefing.objects.get_or_create(
            course_fk=instance.course_fk,
            created_at__date=target_date,
            defaults={'content': ''}
        )
        briefing_content = {
            "briefing_data":{
                "date": target_date.isoformat(),
                "course_fk": instance.course_fk.id,
                "course_name": instance.course_fk.course_name,
            },
            "responses":{
                "total": total_polls,
                "answered": answered_polls,
                "attendance_true": attendance_true,
                "assignment_true": assignment_true,
                "exam_true": exam_true,
            },
            "summary":{
                "response_percentage": response_percentage,
                "attendance_percentage": attendance_percentage,
                "assignment_percentage": assignment_percentage,
                "exam_percentage": exam_percentage,
            }
        }
        logger.info(f"Briefing created: {created}, ID: {briefing.id}")
        
        briefing.content = json.dumps(briefing_content)
        briefing.updated_at = timezone.now()
        briefing.save()
        
        logger.info(f"Briefing saved with content: {briefing.content}")