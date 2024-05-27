from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('signup/', views.SignupView.as_view()),
    path('login/', views.LoginView().as_view()),
    path('emailcodesend/', views.EmailCodeSendView().as_view()),
    path('emailcodecheck/', views.EmailCodeCheckView().as_view()),
    path('groupCreate/', views.CreateGroupView().as_view()),
]
