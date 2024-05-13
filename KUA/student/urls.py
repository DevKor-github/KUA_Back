from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView().as_view()),
    path('permissioncodesend/', views.PermissionCodeSendView().as_view()),
    path('permissioncheck/', views.PermissionCodeCheckView().as_view()),
    path('submit_timetable/', views.SubmitTimeTableView().as_view()),
]
