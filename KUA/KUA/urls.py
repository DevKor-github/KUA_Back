from django.contrib import admin
from django.urls import path, include, re_path
from . import settings
from django.conf.urls.static import static
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi
from django.views.generic import RedirectView

schema_view = get_schema_view(
    openapi.Info(
        title="KU&A",
        default_version='0.1a',
        description="""
            <h2>KU&A API 문서입니다</h2>
            <p>이 문서는 KU&A API의 사용법을 설명합니다.</p>
            <ul>
                <li>버전: 0.1a</li>
                <li>용어 및 서비스 약관: <a href="https://www.google.com/policies/terms/">여기</a>를 참조하세요.</li>
                <li>문의: <a href="mailto:dlrkd1122@korea.ac.kr">dlrkd1122@korea.ac.kr</a></li>
                <li>라이선스: DevKor</li>
                <li>참고 사항: Token 사용 방식: 자물쇠 버튼 클릭 -> 'token <해당 유저의 token>'형식으로 입력</li>
            </ul>
            <p><strong>참고사항:</strong> KU&A API는 현재 개발 중입니다. 기능이 추가되거나 변경될 수 있습니다.</p>
        """,
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kuna.devkor@gmail.com"), # 부가정보
        license=openapi.License(name="DevKor"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    re_path(r'^swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-v1'),
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', RedirectView.as_view(url='/swagger', permanent=True)),
    
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('student/', include('student.urls')),
    path('course-table/', include('course_table.urls')),
    path('course/', include('course.urls')),
    path('today-poll/', include('today_poll.urls')),   
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

