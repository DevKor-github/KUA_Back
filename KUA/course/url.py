from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses/<int:course_id>/posts/', views.CoursePostListView.as_view(), name='course-posts'),
    path('posts/<int:post_id>/comments/', views.PostCommentListView.as_view(), name='post-comments'),
    path('tags/<str:tag>/posts/', views.TagPostListView.as_view(), name='tag-posts'),
    path('students/<int:student_id>/posts/', views.StudentPostListView.as_view(), name='student-posts'),
    path('students/<int:student_id>/comments/', views.StudentCommentListView.as_view(), name='student-comments'),
    
        # 특정 게시판 게시글
    path('courses/<int:course_id>/posts/',
         views.CoursePostListView.as_view(), name='course-posts'),

    # 특정 게시판의 브리핑 목록
    path('courses/<int:course_id>/briefings/',
         views.CourseBriefingListView.as_view(), name='course-briefings'),

    # 특정 게시글의 댓글
    path('posts/<int:post_id>/comments/',
         views.PostCommentListView.as_view(), name='post-comments'),
    
    # 특정 태그의 게시글
    path('posts/<int:tag_id>/', views.TagPostListView.as_view(), name='post-tags'),

    # 특정 사용자의 오늘의 설문 목록
    path('student/<int:user_id>/todaypolls/', views.UserTodayPollListCreateView.as_view(),
         name='user-todaypoll-list-create'),
    
    # 특정 설문 디테일
    path('todaypolls/<int:pk>/', views.TodayPollDetailView.as_view(),
         name='todaypoll-detail'),
    
    # 특정 설문 응답
    path('todaypolls/<int:pk>/answer/', views.TodayPollAnswerView.as_view(),
         name='todaypoll-answer'),
]
