from django.urls import path
# from . import views
from .views import upload_file

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),
    path('upload_success/', lambda request: render(request, 'course_table/upload_success.html'), name='success'),

]
