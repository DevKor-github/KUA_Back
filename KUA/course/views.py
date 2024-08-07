
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Course, Tag, Post, Comment, TimeTable
from student.models import Student
from .serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# 강의 전체 뷰(CRUD 포함)
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    
    def get_queryset(self):
        queryset = Course.objects.all()

        # 필터링 조건 추가
        course_id = self.request.query_params.get('course_id', None)
        course_name = self.request.query_params.get('course_name', None)
        instructor = self.request.query_params.get('instructor', None)
        year = self.request.query_params.get('year', None)
        semester = self.request.query_params.get('semester', None)

        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)

        if course_name is not None:
            queryset = queryset.filter(course_name__icontains=course_name)

        if instructor is not None:
            queryset = queryset.filter(instructor__icontains=instructor)

        if year is not None:
            queryset = queryset.filter(year=year)

        if semester is not None:
            queryset = queryset.filter(semester=semester)

        return queryset
    
    @swagger_auto_schema(
        operation_summary="강의 목록 조회 기능 - 완료",
        operation_description="모든 강의 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 강의 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('course_id', openapi.IN_QUERY, description="학수번호로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('course_name', openapi.IN_QUERY, description="강의명으로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('instructor', openapi.IN_QUERY, description="교수로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('year', openapi.IN_QUERY, description="강의 개설 연도로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('semester', openapi.IN_QUERY, description="학기별로 필터링", type=openapi.TYPE_INTEGER),
        ],
        responses={200: CourseMinimalSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CourseMinimalSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="강의 생성 기능 - 완료",
        operation_description="새로운 강의를 생성합니다.",
        request_body=CourseSerializer,
        responses={201: CourseMinimalSerializer}
    )
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        minimal_serializer = CourseMinimalSerializer(serializer.instance)
        return Response(minimal_serializer.data, status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(
        operation_summary="강의 조회 기능 - 완료",
        operation_description="겅의 인덱스로 특정 강의의 세부 정보를 조회합니다.",
        responses={200: CourseSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 수정 기능 - 완료",
        operation_description="기존 강의 정보를 수정합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 부분 수정 - 완료",
        operation_description="강의 정보의 일부를 수정합니다.",
        request_body=CourseSerializer,
        responses={200: CourseSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="강의 삭제 - 완료",
        operation_description="ID로 특정 강의를 삭제합니다.",
        responses={204: 'Deleted'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 태그 전체 뷰
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_queryset(self):
        queryset = Tag.objects.all()

        # 필터링 조건 추가
        name = self.request.query_params.get('name', None)

        if name is not None:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    @swagger_auto_schema(
        operation_summary="태그 목록 조회 - 완료",
        operation_description="모든 태그 목록을 조회하거나, 이름으로 필터링된 태그 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('name', openapi.IN_QUERY, description="태그 이름으로 필터링", type=openapi.TYPE_STRING),
        ],
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
        operation_summary="태그 조회 - 완료",
        operation_description="이름으로 특정 태그를 조회합니다.\n 대충 포함되는 단어로도 검색이 됩니다.",
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
        responses={204: 'Deleted'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 게시글 전체 뷰


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    
    def get_queryset(self):
        queryset = Post.objects.all()

        # 필터링 조건 추가
        course_index = self.request.query_params.get('course_index',None)
        course_id = self.request.query_params.get('course_id', None)
        student_id = self.request.query_params.get('student_id', None)
        title = self.request.query_params.get('title', None)

        
        if course_index is not None:
            queryset = queryset.filter(course_fk_id=course_index)
            
        if course_id is not None:
            queryset = queryset.filter(course_fk__course_id=course_id)

        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        return queryset

    @swagger_auto_schema(
        operation_summary="게시글 목록 조회 기능 - 완료",
        operation_description="모든 게시글 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 게시글 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('course_index', openapi.IN_QUERY,description="강의 인덱스로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('course_id', openapi.IN_QUERY, description="학수번호로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('student_id', openapi.IN_QUERY, description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('title', openapi.IN_QUERY, description="게시글 제목으로 필터링", type=openapi.TYPE_STRING),
        ],
        responses={200: PostMinimalSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostMinimalSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="게시글 생성 기능 - 완료",
        operation_description="새로운 게시글을 생성합니다.",
        request_body=PostSerializer,
        responses={201: PostSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 조회 기능 - 완료",
        operation_description="게시글 인덱스로 특정 게시글을 조회합니다.",
        responses={200: PostSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="게시글 수정 기능 - 완료",
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
        responses={204: 'Deleted'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

# 댓글 전체 뷰

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        queryset = Comment.objects.all()

        # 필터링 조건 추가
        post_id = self.request.query_params.get('post_id', None)
        student_id = self.request.query_params.get('student_id', None)

        if post_id is not None:
            queryset = queryset.filter(post_id=post_id)

        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)

        return queryset

    @swagger_auto_schema(
        operation_summary="댓글 목록 조회 기능 - 완료",
        operation_description="모든 댓글 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 댓글 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('post_id', openapi.IN_QUERY, description="게시글 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('student_id', openapi.IN_QUERY, description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
        ],
        responses={200: CommentMinimalSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = CommentMinimalSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="댓글 생성 기능 - 완료",
        operation_description="새로운 댓글을 작성합니다.",
        request_body=CommentSerializer,
        responses={201: CommentSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 조회 기능 - 완료",
        operation_description="댓글 인덱스로 특정 댓글을 조회합니다.",
        responses={200: CommentSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="댓글 수정 기능 - 완료",
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
        responses={204: 'Deleted'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 시간표 뷰
class TimeTableViewSet(viewsets.ModelViewSet):
    serializer_class = TimeTableSerializer
    
    def get_queryset(self):
        queryset = TimeTable.objects.all()

        # 필터링 조건 추가
        student_id = self.request.query_params.get('student_id', None)
        year = self.request.query_params.get('year', None)
        semester = self.request.query_params.get('semester', None)

        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)

        if year is not None:
            queryset = queryset.filter(year=year)

        if semester is not None:
            queryset = queryset.filter(semester=semester)

        return queryset

    @swagger_auto_schema(
        operation_summary="시간표 목록 조회 기능 - 완료",
        operation_description="모든 시간표 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 시간표 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('student_id', openapi.IN_QUERY, description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('year', openapi.IN_QUERY, description="년도별로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('semester', openapi.IN_QUERY, description="학기별로 필터링", type=openapi.TYPE_STRING),
        ],
        responses={200: TimeTableSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 생성 기능",
        operation_description="새로운 시간표를 생성합니다.",
        request_body=TimeTableSerializer,
        responses={201: TimeTableSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 조회 기능",
        operation_description="ID로 특정 시간표를 조회합니다.",
        responses={200: TimeTableSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 수정 기능",
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


