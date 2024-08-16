from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
router.register(r'todaypolls', views.TodayPollViewSet)
router.register(r'briefings', views.BriefingViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('todaypolls/<int:pk>/answer/', views.TodayPollAnswerView.as_view(), name='todaypoll-answer'),
]
