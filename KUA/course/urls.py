from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='course')
router.register(r'tags', views.TagViewSet, basename='tag')
router.register(r'posts', views.PostViewSet, basename='post')
router.register(r'comments', views.CommentViewSet, basename='comment')
router.register(r'timetables', views.TimeTableViewSet, basename='timetable')

urlpatterns = [
    path('', include(router.urls)),
]
