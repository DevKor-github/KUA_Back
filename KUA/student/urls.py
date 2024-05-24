from django.urls import path, include
from . import views
from rest_framework import urls
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('pointGet/', views.PointGetView().as_view()),
    path('pointUse/', views.PointUseView().as_view()),
]
