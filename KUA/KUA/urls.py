from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views as course_views
from today_poll import views as poll_views
from . import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)
router.register(r'tags', course_views.TagViewSet)
router.register(r'posts', course_views.PostViewSet)
router.register(r'comments', course_views.CommentViewSet)
router.register(r'todaypolls', poll_views.TodayPollViewSet,
                basename='todaypoll')
router.register(r'briefings', poll_views.BriefingViewSet, basename='briefing')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/', include('rest_framework.urls')),
    path('student/', include('student.urls')),
    path('', include('course_table.urls')),   

    # 특정 게시판 게시글
    path('courses/<int:course_id>/posts/',
         course_views.CoursePostListView.as_view(), name='course-posts'),

    # 특정 게시판의 브리핑 목록
    path('courses/<int:course_id>/briefings/',
         poll_views.CourseBriefingListView.as_view(), name='course-briefings'),

    # 특정 게시글의 댓글
    path('posts/<int:post_id>/comments/',
         course_views.PostCommentListView.as_view(), name='post-comments'),
    
    # 특정 태그의 게시글
    path('posts/<int:tag_id>/', course_views.TagListView.as_view(), name='post-tags'),

    # 특정 사용자의 오늘의 설문 목록
    path('student/<int:user_id>/todaypolls/', poll_views.UserTodayPollListCreateView.as_view(),
         name='user-todaypoll-list-create'),
    
    # 특정 설문 디테일
    path('todaypolls/<int:pk>/', poll_views.TodayPollDetailView.as_view(),
         name='todaypoll-detail'),
    
    # 특정 설문 응답
    path('todaypolls/<int:pk>/answer/', poll_views.TodayPollAnswerView.as_view(),
         name='todaypoll-answer'),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

