from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views as course_views
from today_poll import views as poll_views

router = DefaultRouter()
router.register(r'courses', course_views.CourseViewSet)
router.register(r'tags', course_views.TagViewSet)
router.register(r'posts', course_views.PostViewSet)
router.register(r'comments', course_views.CommentViewSet)
router.register(r'todaypolls', poll_views.TodayPollViewSet,
                basename='todaypolls')
router.register(r'briefings', poll_views.BriefingViewSet, basename='briefings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('courses/<int:course_id>/posts/',
         course_views.CoursePostListView.as_view(), name='course-posts'),
    path('posts/<int:post_id>/comments/',
         course_views.PostCommentListView.as_view(), name='post-comments'),
    path('tp/', poll_views.UserTodayPollListCreateView.as_view(),
         name='user-todaypoll-list-create'),
    path('tp/<int:pk>/', poll_views.TodayPollDetailView.as_view(),
         name='todaypoll-detail'),
    path('tp/<int:pk>/answer/', poll_views.TodayPollAnswerView.as_view(),
         name='todaypoll-answer'),
    path('courses/<int:course_id>/briefings/',
         poll_views.CourseBriefingListView.as_view(), name='course-briefings'),
    path('courses/<int:course_id>/create-briefing/',
         poll_views.CreateBriefingView.as_view(), name='create-briefing'),
]
