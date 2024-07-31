from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course, Tag, Post, Comment, TimeTable
from student.models import Student
from .serializers import CourseSerializer, TagSerializer, PostSerializer, CommentSerializer, TimeTableSerializer
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 강의 전체 뷰(CRUD 포함)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @swagger_auto_schema(
        operation_summary="강의 목록 조회",
        operation_description="모든 강의 목록을 조회합니다.",
        responses={200: CourseSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 생성",
        operation_description="새로운 강의를 생성합니다.",
        request_body=CourseSerializer,
        responses={201: CourseSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 조회",
        operation_description="ID로 특정 강의를 조회합니다.",
        responses={200: CourseSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 수정",
        operation_description="기존 강의 정보를 수정합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 부분 수정",
        operation_description="강의 정보의 일부를 수정합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 삭제",
        operation_description="ID로 특정 강의를 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 태그 전체 뷰


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    @swagger_auto_schema(
        operation_summary="태그 목록 조회",
        operation_description="모든 태그 목록을 조회합니다.",
        responses={200: TagSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 생성",
        operation_description="새로운 태그를 생성합니다.",
        request_body=TagSerializer,
        responses={201: TagSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 조회",
        operation_description="ID로 특정 태그를 조회합니다.",
        responses={200: TagSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 수정",
        operation_description="기존 태그 정보를 수정합니다.",
        request_body=TagSerializer,
        responses={200: TagSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 부분 수정",
        operation_description="태그 정보의 일부를 수정합니다.",
        request_body=TagSerializer,
        responses={200: TagSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 삭제",
        operation_description="ID로 특정 태그를 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 게시글 전체 뷰


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_summary="게시글 목록 조회",
        operation_description="모든 게시글 목록을 조회합니다.",
        responses={200: PostSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 생성",
        operation_description="새로운 게시글을 생성합니다.",
        request_body=PostSerializer,
        responses={201: PostSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 조회",
        operation_description="ID로 특정 게시글을 조회합니다.",
        responses={200: PostSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 수정",
        operation_description="기존 게시글 정보를 수정합니다.",
        request_body=PostSerializer,
        responses={200: PostSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 부분 수정",
        operation_description="게시글 정보의 일부를 수정합니다.",
        request_body=PostSerializer,
        responses={200: PostSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 삭제",
        operation_description="ID로 특정 게시글을 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 댓글 전체 뷰

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        operation_summary="댓글 목록 조회",
        operation_description="모든 댓글 목록을 조회합니다.",
        responses={200: CommentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 생성",
        operation_description="새로운 댓글을 생성합니다.",
        request_body=CommentSerializer,
        responses={201: CommentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 조회",
        operation_description="ID로 특정 댓글을 조회합니다.",
        responses={200: CommentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 수정",
        operation_description="기존 댓글 정보를 수정합니다.",
        request_body=CommentSerializer,
        responses={200: CommentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 부분 수정",
        operation_description="댓글 정보의 일부를 수정합니다.",
        request_body=CommentSerializer,
        responses={200: CommentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 삭제",
        operation_description="ID로 특정 댓글을 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 시간표 뷰
class TimeTableViewSet(viewsets.ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer

    @swagger_auto_schema(
        operation_summary="시간표 목록 조회",
        operation_description="모든 시간표 목록을 조회합니다.",
        responses={200: TimeTableSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 생성",
        operation_description="새로운 시간표를 생성합니다.",
        request_body=TimeTableSerializer,
        responses={201: TimeTableSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 조회",
        operation_description="ID로 특정 시간표를 조회합니다.",
        responses={200: TimeTableSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 수정",
        operation_description="기존 시간표 정보를 수정합니다.",
        request_body=TimeTableSerializer,
        responses={200: TimeTableSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 부분 수정",
        operation_description="시간표 정보의 일부를 수정합니다.",
        request_body=TimeTableSerializer,
        responses={200: TimeTableSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 삭제",
        operation_description="ID로 특정 시간표를 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

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
        timetable= {
            'student': student,
            'course' : course,
            'year': year,
            'semester': semester
        }
        serializer = TimeTableSerializer(data=timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'}, status=status.HTTP_201_CREATED)
        return Response({'response': 'Time Table Rejected'}, status=status.HTTP_201_CREATED)


# 특정 학생의 id로 시간표 뷰
class StudentTimeTableView(generics.ListAPIView):
    serializer_class = TimeTableSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return TimeTable.objects.filter(student=student)