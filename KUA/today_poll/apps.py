from django.apps import AppConfig
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
        start()
