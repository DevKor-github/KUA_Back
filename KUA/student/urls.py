from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('get-points/', views.PointGetView().as_view()),
    path('use-points/', views.PointUseView().as_view()),
    path('check-permission/', views.IsPermissionView().as_view()),
]
