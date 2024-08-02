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
    
    def get_queryset(self):
        queryset = Course.objects.all()

        # 필터링 조건 추가 (예: course_id, instructor, year 등의 필터)
        course_id = self.request.query_params.get('course_id', None)
        instructor = self.request.query_params.get('instructor', None)
        year = self.request.query_params.get('year', None)

        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)

        if instructor is not None:
            queryset = queryset.filter(instructor__name__icontains=instructor)

        if year is not None:
            queryset = queryset.filter(year=year)

        return queryset
    
    @swagger_auto_schema(
        operation_summary="강의 목록 조회 기능 - 완료",
        operation_description="모든 강의 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 강의 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('course_id', openapi.IN_QUERY, description="강의 ID로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('instructor', openapi.IN_QUERY, description="강의 담당 교수로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('year', openapi.IN_QUERY, description="강의 개설 연도로 필터링", type=openapi.TYPE_INTEGER),
        ],
        responses={200: CourseSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 생성 기능 - 완료",
        operation_description="새로운 강의를 생성합니다.",
        request_body=CourseSerializer,
        responses={201: CourseSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 조회 기능 - 작업 중",
        operation_description="ID 또는 학수번호, 교수 등으로 특정 강의를 조회합니다.",
        responses={200: CourseSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 수정 기능 - 완료",
        operation_description="기존 강의 정보를 수정합니다. 강의 모델의 모든 내용이 들어있어야 합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 부분 수정 - 완료",
        operation_description="강의 정보의 일부만 수정합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 삭제 - 완료",
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
        operation_summary="태그 목록 조회 - 완료",
        operation_description="모든 태그 목록을 조회합니다.",
        responses={200: TagSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 생성 - 완료",
        operation_description="새로운 태그를 생성합니다.",
        request_body=TagSerializer,
        responses={201: TagSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 조회 - 작업 중",
        operation_description="ID 혹은 이름으로 특정 태그를 조회합니다.",
        responses={200: TagSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 수정 - 완료",
        operation_description="기존 태그 정보를 수정합니다.",
        request_body=TagSerializer,
        responses={200: TagSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 부분 수정 - 완료",
        operation_description="태그 정보의 일부를 수정합니다.",
        request_body=TagSerializer,
        responses={200: TagSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="태그 삭제 - 작업 중",
        operation_description="ID 또는 이름으로 특정 태그를 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 게시글 전체 뷰


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_summary="게시글 목록 조회 - 완료",
        operation_description="모든 게시글 목록을 조회합니다.",
        responses={200: PostSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 생성 - 작업 중",
        operation_description="현재 로그인한 유저로 특정 강의에 대해 새로운 게시글을 생성합니다.",
        request_body=PostSerializer,
        responses={201: PostSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 조회 - 작업 중",
        operation_description="ID 혹은 제목으로 특정 게시글을 조회합니다.",
        responses={200: PostSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 수정 - 완료",
        operation_description="기존 게시글 정보를 수정합니다.",
        request_body=PostSerializer,
        responses={200: PostSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 부분 수정 - 완료",
        operation_description="게시글 정보의 일부를 수정합니다.",
        request_body=PostSerializer,
        responses={200: PostSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 삭제 - 완료",
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
        operation_summary="댓글 목록 조회 - 완료",
        operation_description="모든 댓글 목록을 조회합니다.",
        responses={200: CommentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 작성 - 완료",
        operation_description="특정 게시글에 대한 새로운 댓글을 작성합니다.",
        request_body=CommentSerializer,
        responses={201: CommentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 조회 - 작업 중",
        operation_description="ID, 학생, 강의명 등으로 특정 댓글을 조회합니다.",
        responses={200: CommentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 수정 - 완료",
        operation_description="기존 댓글 정보를 수정합니다.",
        request_body=CommentSerializer,
        responses={200: CommentSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 부분 수정 - 완료",
        operation_description="댓글 정보의 일부를 수정합니다.",
        request_body=CommentSerializer,
        responses={200: CommentSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 삭제 - 완료",
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
        operation_summary="시간표 목록 조회 - 작업 중",
        operation_description="모든 시간표 목록을 조회합니다.",
        responses={200: TimeTableSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 생성 - 작업 중",
        operation_description="새로운 시간표를 생성합니다.",
        request_body=TimeTableSerializer,
        responses={201: TimeTableSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 조회 - 작업 중",
        operation_description="ID로 특정 시간표를 조회합니다.",
        responses={200: TimeTableSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 수정 - 작업 중",
        operation_description="기존 시간표 정보를 수정합니다.",
        request_body=TimeTableSerializer,
        responses={200: TimeTableSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 부분 수정 - 작업 중",
        operation_description="시간표 정보의 일부를 수정합니다.",
        request_body=TimeTableSerializer,
        responses={200: TimeTableSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 삭제 - 작업 중",
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
        operation_summary="특정 강의의 게시글 목록 조회 - 완료",
        operation_description="강의 인스턴스 ID로(학수번호 아님!) 특정 강의에 대한 모든 게시글을 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'id', openapi.IN_PATH,
                description="조회할 강의의 ID", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 게시글 목록",
                schema=PostSerializer(many=True)
            ),
            404: openapi.Response(description="강의를 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        id = self.kwargs['id']
        return Post.objects.filter(course_fk_id = id)


# 특정 게시글의 댓글을 보는 뷰


class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="특정 게시글의 댓글 목록 조회",
        operation_description="게시글 ID로 특정 게시글에 대한 모든 댓글을 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'post_id', openapi.IN_PATH,
                description="조회할 게시글의 ID", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 댓글 목록",
                schema=CommentSerializer(many=True)
            ),
            404: openapi.Response(description="게시글을 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)


# 특정 태그의 게시글 리스트를 보는 뷰

class TagPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_summary="특정 태그의 게시글 목록 조회",
        operation_description="태그 이름으로 특정 태그가 포함된 게시글을 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'tag', openapi.IN_PATH,
                description="조회할 태그의 이름", type=openapi.TYPE_STRING
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 게시글 목록",
                schema=PostSerializer(many=True)
            ),
            404: openapi.Response(description="해당 태그를 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        tag = self.kwargs['tag']
        return Post.objects.filter(tags__name=tag)


# 특정 학생이 작성한 게시글 리스트 뷰

class StudentPostListView(generics.ListAPIView):
    serializer_class = PostSerializer

    @swagger_auto_schema(
        operation_summary="특정 학생이 작성한 게시글 목록 조회",
        operation_description="학생 ID로 특정 학생이 작성한 모든 게시글을 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'student_id', openapi.IN_PATH,
                description="조회할 학생의 ID", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 게시글 목록",
                schema=PostSerializer(many=True)
            ),
            404: openapi.Response(description="해당 학생을 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return Post.objects.filter(student=student)



# 특정 학생이 작성한 댓글 리스트 뷰


class StudentCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer

    @swagger_auto_schema(
        operation_summary="특정 학생이 작성한 댓글 목록 조회",
        operation_description="학생 ID로 특정 학생이 작성한 모든 댓글을 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'student_id', openapi.IN_PATH,
                description="조회할 학생의 ID", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 댓글 목록",
                schema=CommentSerializer(many=True)
            ),
            404: openapi.Response(description="해당 학생을 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return Comment.objects.filter(student=student)

# id, 학수번호, 개설년도와 학기 정보를 통해 시간표를 등록하는 view


class SubmitTimeTableView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = TimeTableSerializer

    @swagger_auto_schema(
        operation_summary="시간표 등록",
        operation_description="사용자의 시간표를 등록하는 기능입니다. 사용자 번호, 학수 번호, 년도, 학기를 입력하면 사용자에게 시간표를 등록합니다.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['course', 'year', 'semester'],
            properties={
                'course': openapi.Schema(type=openapi.TYPE_INTEGER, description="학수 번호"),
                'year': openapi.Schema(type=openapi.TYPE_INTEGER, description="년도"),
                'semester': openapi.Schema(type=openapi.TYPE_STRING, description="학기"),
            }
        ),
        responses={
            201: openapi.Response(
                description="시간표가 성공적으로 저장되었습니다.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'response': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            ),
            400: openapi.Response(
                description="시간표 저장이 거부되었습니다.",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'response': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        }
    )
    def post(self, request):
        user = request.user
        student = get_object_or_404(Student, user=user)
        course = request.data['course']
        year = request.data['year']
        semester = request.data['semester']
        timetable = {
            'student': student.id,
            'course': course,
            'year': year,
            'semester': semester
        }
        serializer = TimeTableSerializer(data=timetable)
        if serializer.is_valid():
            serializer.save()
            return Response({'response': 'Time Table Saved'}, status=status.HTTP_201_CREATED)
        return Response({'response': 'Time Table Rejected'}, status=status.HTTP_400_BAD_REQUEST)



# 특정 학생의 id로 시간표 뷰
class StudentTimeTableView(generics.ListAPIView):
    serializer_class = TimeTableSerializer

    @swagger_auto_schema(
        operation_summary="특정 학생의 시간표 조회",
        operation_description="학생 ID로 특정 학생이 등록한 시간표를 조회합니다.",
        manual_parameters=[
            openapi.Parameter(
                'student_id', openapi.IN_PATH,
                description="조회할 학생의 ID", type=openapi.TYPE_INTEGER
            )
        ],
        responses={
            200: openapi.Response(
                description="성공적으로 조회된 시간표 목록",
                schema=TimeTableSerializer(many=True)
            ),
            404: openapi.Response(description="해당 학생을 찾을 수 없습니다.")
        }
    )
    def get_queryset(self):
        student_id = self.kwargs['student_id']
        student = get_object_or_404(Student, id=student_id)
        return TimeTable.objects.filter(student=student)
