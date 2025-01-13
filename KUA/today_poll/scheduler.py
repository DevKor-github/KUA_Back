import logging
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from today_poll.models import TodayPoll, Briefing
from student.models import Student
from course.models import TimeTable, Post, Tag
from django.utils import timezone
import json

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

def create_briefing_to_post():
    try:
        logger.info("create_briefing_to_post 작업 시작")
        
        # 1일 이전의 브리핑 데이터를 가져옴
        threshold = timezone.now() - timezone.timedelta(days=1)
        old_brifs = Briefing.objects.filter(created_at__lt=threshold)
        
        # `Student`와 `Tag` 확인
        student_instance = Student.objects.first()
        if not student_instance:
            logger.warning("학생 데이터가 없습니다.")
            return
        
        tags = Tag.objects.filter(name='브리핑')
        if not tags.exists():
            logger.warning("브리핑 태그가 없습니다.")
            return
        
        # 브리핑 데이터를 Post로 변환
        for briefing in old_brifs:
            # 이미 처리된 브리핑인지 확인
            if Post.objects.filter(title=f"{briefing.created_at.strftime('%Y년-%m월-%d일')} 브리핑").exists():
                logger.info(f"이미 처리된 브리핑: {briefing.id}")
                continue  # 처리된 경우 다음 브리핑으로 넘어감
            
            try:
                # 게시글 생성
                post = Post.objects.create(
                    title=f"{briefing.created_at.strftime('%Y년-%m월-%d일')} 브리핑",
                    content=json.loads(briefing.content),
                    student=student_instance,
                    course_fk=briefing.course_fk,
                )
                post.tags.set(tags)
                logger.info(f"게시글 생성됨: {post.title}")
                
                # 브리핑 삭제
                briefing.delete()
                logger.info(f"브리핑 삭제됨: {briefing.id}")
            except Exception as e:
                logger.error(f"브리핑 처리 중 오류 발생: {str(e)}")
        
        logger.info("create_briefing_to_post 작업 완료")
    except Exception as e:
        logger.error(f"create_briefing_to_post 작업 중 예외 발생: {str(e)}")



def start():
    scheduler = BackgroundScheduler()
    scheduler.remove_all_jobs()
    scheduler.add_jobstore(DjangoJobStore(), 'default')

    scheduler.add_job(create_today_poll, 'cron', hour=0, minute=0, id='create_today_poll', replace_existing=True)
    scheduler.add_job(delete_old_today_poll, 'cron', hour=0, minute=0, id='delete_old_today_poll', replace_existing=True)
    scheduler.add_job(create_briefing_to_post, 'cron', hour=0, minute=0, id='create_briefing_to_post', replace_existing=True)
    
    register_events(scheduler)
    scheduler.start()
    logger.info("Scheduler started")
