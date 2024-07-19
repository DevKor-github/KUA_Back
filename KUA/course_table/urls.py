# -*- coding: utf-8 -*-

from django.urls import path
# from . import views
from .views import upload_file, home
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),  # 루트 URL???�??�??�결
    path('upload/', upload_file, name='upload_file'), # ?�로??url
    path('upload-success/', lambda request: render(request, 'course_table/upload_success.html'), name='upload_success'), # ?�로???�공 url

]
