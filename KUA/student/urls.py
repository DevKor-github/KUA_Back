from django.urls import path, include
from . import views
from rest_framework import urls

urlpatterns = [
    path('submit-timetable/', views.SubmitTimeTableView().as_view()),
]