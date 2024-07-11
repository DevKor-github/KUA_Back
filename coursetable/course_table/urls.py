from django.urls import path
# from . import views
from .views import upload_file, home
from django.shortcuts import render

urlpatterns = [
    path('', home, name='home'),  # 루트 URL에 대한 뷰 연결
    path('upload/', upload_file, name='upload_file'),
    path('upload_success/', lambda request: render(request, 'course_table/upload_success.html'), name='upload_success'),

]
