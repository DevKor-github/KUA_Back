"""
WSGI config for KUA project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

from today_poll.scheduler import start
from student.scheduler import start as start2
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'KUA.settings')

application = get_wsgi_application()

start()
start2()
