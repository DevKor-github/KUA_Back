from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('student/', include('student.urls')),
    path('course-table/', include('course_table.urls')),
    path('course/', include('course.urls')),
    path('today-poll/', include('today_poll.urls')),   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

