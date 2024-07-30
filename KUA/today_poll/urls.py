from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import urls

router = DefaultRouter()
router.register(r'todaypolls', views.TodayPollViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # 특정 게시판의 브리핑 목록
    path('courses/<int:course_id>/briefings/',
         views.CourseBriefingListView.as_view(), name='course-briefings'),
    # 특정 사용자의 오늘의 설문 목록
    path('student/<int:user_id>/todaypolls/', views.UserTodayPollListCreateView.as_view(),
         name='user-todaypoll-list-create'),
    
    # 특정 설문 디테일
    path('todaypolls/<int:pk>/', views.TodayPollDetailView.as_view(),
         name='todaypoll-detail'),
    
    # 특정 설문 응답
    path('todaypolls/<int:pk>/answer/', views.TodayPollAnswerView.as_view(),
         name='todaypoll-answer'),
]
