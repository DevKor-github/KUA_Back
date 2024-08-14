from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
router.register(r'todaypolls', views.TodayPollViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
