from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('signup/', views.SignupView().as_view()),
    path('login/', views.LoginView().as_view()),
    path('send-code/', views.EmailCodeSendView().as_view()),
    path('check-code/', views.EmailCodeCheckView().as_view()),
    path('get-points/', views.PointGetView().as_view()),
    path('use-points/', views.PointUseView().as_view()),
    path('check-permission/', views.IsPermissionView().as_view()),
    path('get-nickname/', views.GetNickNameView().as_view()),
    path('get-now-points/', views.GetNowPointView().as_view()),
    path('user-info/', views.UserStudentInfoView.as_view()),
    path('get-point-history/', views.GetPointHistoryView.as_view()),
    path('image/', views.ImageView().as_view()),
]