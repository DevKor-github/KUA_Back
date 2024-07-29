from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course, Tag, Post, Comment
from student.models import Student
from .serializers import CourseSerializer, TagSerializer, PostSerializer, CommentSerializer, TimeTableSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 강의 전체 뷰(CRUD 포함)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 태그 전체 뷰


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

# 게시글 전체 뷰


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 댓글 전체 뷰


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# 특정 강의에 대한 게시글을 보는 뷰


class CoursePostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('param_name', openapi.IN_QUERY,
                              description="기능 테스트 중입니다.", type=openapi.TYPE_STRING)
        ]
    )
    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Post.objects.filter(course_id=course_id)

# 특정 게시글의 댓글을 보는 뷰


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

# 특정 태그의 게시글 리스트를 보는 뷰


class TagPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__name=tag)

# 특정 학생이 작성한 게시글 리스트 뷰


class StudentPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return Post.objects.filter(student=student)

# 특정 학생이 작성한 댓글 리스트 뷰


class StudentCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return Comment.objects.filter(student=student)
# id, 학수번호, 개설년도와 학기 정보를 통해 시간표를 등록하는 view


class SubmitTimeTableView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TimeTableSerializer  # 추가

    @swagger_auto_schema(
        operation_summary="사용자의 시간표를 등록하는 기능입니다.",
        operation_description="사용자 번호, 학수 번호, 년도, 학기를 입력하면 사용자에게 시간표를 등록합니다.",
        request_body=TimeTableSerializer,
        responses={
            201: openapi.Response(description="Time Table Saved"),
            400: openapi.Response(description="Time Table Rejected")
        }

    )
    def post(self, request):
        user = request.user
        student = get_object_or_404(Student, user=user)
        course_id = request.data['course_id']
        year = request.data['year']
        semester = request.data['semester']
        timetable = {
            'student': student,
            'course_id': course_id,
            'year': year,
            'semester': semester
        }
        serializer = TimeTableSerializer(data=timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'})
        return Response({'response': 'Time Table Rejected'})
