from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TodayPoll, Briefing
from .service import create_briefing


@receiver(post_save, sender=TodayPoll)
def update_briefing(sender, instance, created, **kwargs):
    if created:
        # 설문이 새로 생성되었을 때 브리핑 업데이트
        target_date = instance.create_at.date()
        create_briefing(instance.course.id, target_date)
