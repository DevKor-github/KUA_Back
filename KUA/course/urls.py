from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course import views

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'posts', views.PostViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'timetables', views.TimeTableViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('courses/<int:course_id>/posts/', views.CoursePostListView.as_view(), name='course-posts'),
    path('posts/<int:post_id>/comments/', views.PostCommentListView.as_view(), name='post-comments'),
    path('tags/<str:tag>/posts/', views.TagPostListView.as_view(), name='tag-posts'),
    path('student/<int:student_id>/posts/', views.StudentPostListView.as_view(), name='student-posts'),
    path('student/<int:student_id>/comments/', views.StudentCommentListView.as_view(), name='student-comments'),
    
    path('student/<int:student_id>/submit-timetable/', views.SubmitTimeTableView().as_view(), name='submit-timetable'),
    
    # 특정 게시판 게시글
    path('courses/<int:course_id>/posts/',
         views.CoursePostListView.as_view(), name='course-posts'),
    # 특정 게시글의 댓글
    path('posts/<int:post_id>/comments/',
         views.PostCommentListView.as_view(), name='post-comments'),
    # 특정 태그의 게시글
    path('posts/<int:tag_id>/', views.TagPostListView.as_view(), name='post-tags'),
    
    # 특정 학생의 시간표
    path('student/<int:student_id>/timetable/', views.StudentTimeTableView.as_view(), name='student-timetable'),
    
    

]
