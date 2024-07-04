"""
ASGI config for back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from .tasks import scheduler

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "KUA.settings")

application = get_asgi_application()

scheduler.start()
