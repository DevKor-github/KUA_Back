from django.apps import AppConfig


class TodayPollConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'today_poll'

    def ready(self):
        import today_poll.signals
