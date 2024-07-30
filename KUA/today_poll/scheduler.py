import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from apscheduler.triggers.cron import CronTrigger
from django.utils import timezone
import sys

logger = logging.getLogger(__name__)


def test_scheduler():
    dt_now = timezone.now()
    logger.debug(f'dt_now: {dt_now}')


def start():
    try:
        job_id = 'job_1'
        sched = BackgroundScheduler(timezone='Asia/Seoul')
        sched.add_jobstore(DjangoJobStore(), "default")
        register_events(sched)
        sched.start()
        logger.info("Scheduler started...")

        sched.add_job(test_scheduler, 'cron', second='*/5',
                      id=job_id, jobstore='default', replace_existing=True)
        logger.info(f"Job {job_id} added.")
    except Exception as ex:
        logger.error(ex)
        sched.shutdown()


# from apscheduler.schedulers.background import BackgroundScheduler
# from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# from today_poll.models import TodayPoll
# from django.contrib.auth.models import User
# from course.models import Course


# def create_today_poll():
#     default_user = User.objects.get(pk=1)
#     courses = Course.objects.all()
#     for course in courses:
#         TodayPoll.objects.create(user=default_user, course=course)


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_jobstore(DjangoJobStore(), 'default')

#     # 매일 자정에 실행되도록 스케줄러 설정
#     register_job(scheduler, 'cron', create_today_poll, hour=0, minute=0)

#     register_events(scheduler)
#     scheduler.start()
#     print("Scheduler started")
