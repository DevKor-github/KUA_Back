

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from .models import Course, Tag, Post, Comment, TimeTable
from .serializers import *
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.parsers import MultiPartParser, FormParser
import mimetypes
from django.db.models import F
import requests

# 강의 전체 뷰(CRUD 포함)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all().order_by('id')

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
            openapi.Parameter('course_id', openapi.IN_QUERY,
                              description="학수번호로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('course_name', openapi.IN_QUERY,
                              description="강의명으로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('instructor', openapi.IN_QUERY,
                              description="교수로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('year', openapi.IN_QUERY,
                              description="강의 개설 연도로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('semester', openapi.IN_QUERY,
                              description="학기별로 필터링", type=openapi.TYPE_INTEGER),
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
    queryset = Tag.objects.all().order_by('id')
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
            openapi.Parameter('name', openapi.IN_QUERY,
                              description="태그 이름으로 필터링", type=openapi.TYPE_STRING),
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
        operation_summary="태그 삭제 - 완료",
        operation_description="ID로 특정 태그를 삭제합니다.",
        responses={204: 'Deleted'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 게시글 전체 뷰

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')

        # 필터링 조건 추가
        course_index = self.request.query_params.get('course_index', None)
        course_id = self.request.query_params.get('course_id', None)
        student_id = self.request.query_params.get('student_id', None)
        title = self.request.query_params.get('title', None)
        content = self.request.query_params.get('content', None)
        order_by = self.request.query_params.get('order_by', None)

        if course_index is not None:
            queryset = queryset.filter(course_fk_id=course_index)

        if course_id is not None:
            queryset = queryset.filter(
                course_fk__course_id__icontains=course_id)

        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        if content is not None:
            queryset = queryset.filter(content__icontains=content)

        # 정렬 조건 추가
        if order_by:
            if order_by == 'likes_asc':
                queryset = queryset.order_by('likes')
            elif order_by == 'likes_desc':
                queryset = queryset.order_by('-likes')
            elif order_by == 'views_asc':
                queryset = queryset.order_by('views')
            elif order_by == 'views_desc':
                queryset = queryset.order_by('-views')

        return queryset

    @swagger_auto_schema(
        operation_summary="게시글 목록 조회 기능 - 완료",
        operation_description="모든 게시글 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 게시글 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('course_index', openapi.IN_QUERY,
                              description="강의 인덱스로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('course_id', openapi.IN_QUERY,
                              description="학수번호로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('student_id', openapi.IN_QUERY,
                              description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('title', openapi.IN_QUERY,
                              description="게시글 제목으로 필터링합니다. 일부 포함된 게시글도 보여줍니다.", type=openapi.TYPE_STRING),
            openapi.Parameter('content', openapi.IN_QUERY,
                              description="게시글 내용으로 필터링합니다. 일부 포함된 게시글도 보여줍니다.", type=openapi.TYPE_STRING),
            openapi.Parameter('order_by', openapi.IN_QUERY,
                              description="정렬 기준 (likes_asc, likes_desc, views_asc, views_desc 중 하나)", type=openapi.TYPE_STRING),
        ],
        responses={200: PostMinimalSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostMinimalSerializer(queryset, many=True)
        results = serializer.data

        query_params = request.query_params.dict()

        for result in results:
            post_instance = Post.objects.get(id=result['id'])
            if 'content' in query_params:
                result['content'] = post_instance.content
            if 'course_id' in query_params:
                result['course_id'] = post_instance.course_fk.course_id

        return Response(results)

    @swagger_auto_schema(
        operation_summary="게시글 생성 기능 - 완료",
        operation_description="새로운 게시글을 생성합니다.",
        manual_parameters=[
            openapi.Parameter('title', openapi.IN_FORM,
                              type=openapi.TYPE_STRING, description='게시글 제목'),
            openapi.Parameter('content', openapi.IN_FORM,
                              type=openapi.TYPE_STRING, description='게시글 내용'),
            openapi.Parameter('course_fk', openapi.IN_FORM,
                              type=openapi.TYPE_INTEGER, description='강의 ID'),
            openapi.Parameter('student', openapi.IN_FORM,
                              type=openapi.TYPE_INTEGER, description='학생 ID'),
            openapi.Parameter('image_uploads', openapi.IN_FORM,
                              type=openapi.TYPE_FILE, description='이미지 파일 업로드', multiple=True),
            openapi.Parameter(
                'tags', openapi.IN_FORM, type=openapi.TYPE_STRING, description='태그 목록 (쉼표로 구분)'),
        ],
        consumes=['multipart/form-data'],
        responses={201: PostSerializer}
    )
    def create(self, request, *args, **kwargs):
        tags = request.data.get('tags', None)

        if tags:
            try:
                if isinstance(tags, str):
                    tags = [int(tag) for tag in tags.split(',')]
                else:
                    tags = [int(tag) for tag in tags]
            except ValueError:
                return Response({"tags": "태그는 정수형 값이어야 합니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            tags = []

        image_uploads = request.FILES.getlist('image_uploads', [])

        post_data = {
            "title": request.data.get("title"),
            "content": request.data.get("content"),
            "course_fk": request.data.get("course_fk"),
            "student": request.data.get("student"),
        }

        serializer = self.get_serializer(data=post_data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()

        # 이미지가 있을 경우 처리
        if image_uploads:
            for image in image_uploads[:10]:  # 최대 10개의 이미지 처리
                PostImage.objects.create(post=post, image=image)

        # 태그 설정
        if tags:
            post.tags.set(tags)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @swagger_auto_schema(
        operation_summary="게시글 조회 기능 - 완료",
        operation_description="게시글 인덱스로 특정 게시글의 세부 내용을 조회합니다. 조회 수가 오릅니다.",
        responses={200: PostSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = Post.objects.get(id=post_id)
        tags_data = post.tags.values('id', 'name')

        attachments = []
        post_images = PostImage.objects.filter(post=post)
        
        profile_image_url = f"http://3.37.163.236:8000/media/attachments/6789563.png"
        try:
            api_url = f"http://3.37.163.236:8000/student/image/?name={post.student.nickname}&tag=N"
            
            auth_token = request.auth
            header = {
                "Authorization": f"Token {auth_token.key}"
            }
            response = requests.get(api_url, headers=header)

            if response.status_code == 200:
                image_data = response.json()
                if isinstance(image_data, list) and len(image_data) > 0:
                    first_item = image_data[0]
                    if "image" in first_item:
                        profile_image_url = f"http://3.37.163.236:8000/{first_item['image']}"
            
        except requests.exceptions.RequestException as e:
            print(f"Request exception: {e}")
        

        for post_image in post_images:
            file_path = post_image.image.path
            content_type, _ = mimetypes.guess_type(file_path)
            attachment = {
                "uri": post_image.image.url,
                "name": post_image.image.name,
                "type": content_type or "application/octet-stream"
            }
            attachments.append(attachment)

        post.views = F('views') + 1
        post.save(update_fields=['views'])
        post.refresh_from_db()

        post_data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "course_id": post.course_fk.course_id,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
            "attachment": attachments,
            "tags": list(tags_data),
            "author": {
                "id": post.student.id,
                "nickname": post.student.nickname,
                "profileImage": profile_image_url,
            },
            "likes": post.likes,
            "views": post.views,
            "reports": post.reported,
        }

        return Response(post_data)

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
        queryset = Comment.objects.all().order_by('-created_at')

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
            openapi.Parameter('post_id', openapi.IN_QUERY,
                              description="게시글 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('student_id', openapi.IN_QUERY,
                              description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
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
        comment_id = kwargs.get('pk', None)
        comment = Comment.objects.get(pk=comment_id)
        parent_post = Post.objects.get(pk=comment.post_id)
        parent_comment = comment.parent_comment
        parent_comment_data = {
            "id": parent_comment.id,
            "content": parent_comment.content[:50]
        } if parent_comment else None

        comment_data = {
            "id": comment.id,
            "content": comment.content,
            "parent_post": {
                "id": parent_post.id,
                "title": parent_post.title,
            },
            "parent_comment": parent_comment_data,
            "created_at": comment.created_at,
            "updated_at": comment.updated_at,
            "is_chosen": comment.is_chosen,
            "author": {
                "id": comment.student.id,
                "nickname": comment.student.nickname,
            },
            "likes": comment.likes,
            "reports": comment.reported,
        }

        return Response(comment_data)

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
        queryset = TimeTable.objects.all().order_by('id')

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
            openapi.Parameter('student_id', openapi.IN_QUERY,
                              description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('year', openapi.IN_QUERY,
                              description="년도별로 필터링", type=openapi.TYPE_STRING),
            openapi.Parameter('semester', openapi.IN_QUERY,
                              description="학기별로 필터링", type=openapi.TYPE_STRING),
        ],
        responses={200: TimeTableSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 생성 기능 - 완료",
        operation_description="새로운 시간표를 생성합니다.",
        responses={201: TimeTableSerializer},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'student': openapi.Schema(type=openapi.TYPE_INTEGER, description='학생 ID'),
                'year': openapi.Schema(type=openapi.TYPE_STRING, description='년도'),
                'semester': openapi.Schema(type=openapi.TYPE_STRING, description='학기'),
                'course_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='강의 ID 리스트')
            },
            required=['student', 'year', 'semester', 'course_ids']
        )
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save()

    @swagger_auto_schema(
        operation_summary="시간표 조회 기능 - 완료",
        operation_description="ID로 특정 시간표를 조회합니다.",
        responses={200: TimeTableSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 수정 기능 - 완료",
        operation_description="기존 시간표 정보를 수정합니다.",
        responses={200: TimeTableSerializer},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'student': openapi.Schema(type=openapi.TYPE_INTEGER, description='학생 ID'),
                'year': openapi.Schema(type=openapi.TYPE_STRING, description='년도'),
                'semester': openapi.Schema(type=openapi.TYPE_STRING, description='학기'),
                'course_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='강의 ID 리스트')
            },
            required=['student', 'year', 'semester', 'course_ids']
        )
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 부분 수정 - 완료",
        operation_description="시간표 정보의 일부를 수정합니다.",
        request_body=TimeTableSerializer,
        responses={200: TimeTableSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="시간표 삭제 - 완료",
        operation_description="ID로 특정 시간표를 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
