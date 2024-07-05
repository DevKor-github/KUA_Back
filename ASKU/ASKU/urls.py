"""
URL configuration for ASKU project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views as course_views
from today_poll import views as poll_views

router = DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)
router.register(r'posts', course_views.PostViewSet)
router.register(r'comments', course_views.CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('tp/', poll_views.TodayPollListCreateView.as_view(), name='TodayPollList'),
    path('tp/<int:pk>/', poll_views.TodayPollDetailView.as_view(), name='TodayPollDetail'),
    path('br/', poll_views.BriefingListCreateView.as_view(), name='BriefingList'),
    path('br/<int:pk>/', poll_views.BriefingDetailView.as_view(), name='BriefingDetail'),
]
