from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "student"
    
    def ready(self):
        from .scheduler import start_scheduler  # 스케줄러 초기화
        start_scheduler()