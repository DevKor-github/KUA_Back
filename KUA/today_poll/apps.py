from django.apps import AppConfig
from django.db.utils import ProgrammingError
import logging

logger = logging.getLogger(__name__)


class TodayPollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'today_poll'

    def ready(self):
        logger.info("TodayPollConfig ready() 호출됨")
        import today_poll.signals
        from .scheduler import start
        print("Signals have been imported and connected.")
        try:
            # 스케줄러를 시작하는 코드 (기존 코드)
            start()
        except ProgrammingError:
            # 마이그레이션 전에는 테이블이 없으므로, 예외를 무시합니다.
            pass
