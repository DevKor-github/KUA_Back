import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from today_poll.models import TodayPoll
from course.models import TimeTable
from django.utils import timezone

logger = logging.getLogger(__name__)
def create_today_poll():
    try:
        logger.info("create_today_poll 작업 시작")
        timetables = TimeTable.objects.all()
        
        for timetable in timetables:
            student = timetable.student
            courses = timetable.courses.all()
            for course in courses:
                TodayPoll.objects.create(student=student, course_fk=course)
                logger.info(f"{student.nickname}의 TodayPoll 생성: {course.course_name}")

        logger.info("create_today_poll 작업 완료")
    except Exception as e:
        logger.error(f"create_today_poll 작업 중 예외 발생: {str(e)}")


def delete_old_today_poll():
    # 현재 시각에서 하루를 뺀 시간 계산
    threshold = timezone.now() - timezone.timedelta(days=1)
    # 해당 시간 이전에 생성된 TodayPoll 인스턴스 삭제
    old_polls = TodayPoll.objects.filter(created_at__lt=threshold)
    count, _ = old_polls.delete()
    logger.info(f"{count}개의 TodayPoll 인스턴스가 삭제되었습니다.")

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    scheduler.add_job(create_today_poll, 'cron', hour=0, minute=0, id='create_today_poll', replace_existing=True)
    scheduler.add_job(delete_old_today_poll, 'cron', hour=0, minute=0, id='delete_old_today_poll', replace_existing=True)

    register_events(scheduler)
    scheduler.start()
    logger.info("Scheduler started")
