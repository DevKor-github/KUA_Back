from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.SignupView().as_view()),
    path('login/', views.LoginView().as_view()),
    path('send-code/', views.EmailCodeSendView().as_view()),
    path('check-code/', views.EmailCodeCheckView().as_view()),
    path('create-group/', views.CreateGroupView().as_view()),
]
