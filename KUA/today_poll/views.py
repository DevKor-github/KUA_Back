from rest_framework import viewsets, status
from .models import TodayPoll, Briefing
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
import json


# 오늘의 설문 전체 뷰 (CRUD 포함)
class TodayPollViewSet(viewsets.ModelViewSet):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer

    def get_queryset(self):
        queryset = TodayPoll.objects.all().order_by('-created_at')

        # 필터링 조건 추가
        student_id = self.request.query_params.get('student_id', None)
        course_fk = self.request.query_params.get('course_fk', None)
        expired = self.request.query_params.get('expired', None)
        created_at_start = self.request.query_params.get('created_at_start', None)
        created_at_end = self.request.query_params.get('created_at_end', None)

        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)

        if course_fk is not None:
            queryset = queryset.filter(course_fk_id=course_fk)

        if expired is not None:
            expired = expired.capitalize()
            queryset = queryset.filter(expired=expired)

        if created_at_start and created_at_end:
            queryset = queryset.filter(created_at__range=[created_at_start, created_at_end])
        elif created_at_start:
            queryset = queryset.filter(created_at__gte=created_at_start)
        elif created_at_end:
            queryset = queryset.filter(created_at__lte=created_at_end)

        return queryset

    @swagger_auto_schema(
        operation_summary="오늘의 설문 목록 조회 - 완료",
        operation_description="모든 설문 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 설문 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('student_id', openapi.IN_QUERY,
                              description="학생 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('course_fk', openapi.IN_QUERY,
                              description="강의 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('expired', openapi.IN_QUERY,
                              description="만료 여부로 필터링 (true 또는 false)", type=openapi.TYPE_BOOLEAN),
            openapi.Parameter('created_at_start', openapi.IN_QUERY,
                              description="시작 날짜 및 시간으로 필터링 (YYYY-MM-DDTHH:MM 형식)", type=openapi.TYPE_STRING),
            openapi.Parameter('created_at_end', openapi.IN_QUERY,
                              description="종료 날짜 및 시간으로 필터링 (YYYY-MM-DDTHH:MM 형식)", type=openapi.TYPE_STRING),
        ],
        responses={200: TodayPollListSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = TodayPollListSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="오늘의 설문 생성 기능 - 완료",
        operation_description="새로운 설문을 생성합니다.",
        request_body=TodayPollSerializer,
        responses={201: TodayPollSerializer}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="설문 조회 기능 - 완료",
        operation_description="설문 인덱스로 특정 설문의 세부 내용을 조회합니다.",
        responses={200: TodayPollSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="설문 수정 기능 - 완료",
        operation_description="기존 설문 정보를 수정합니다.",
        request_body=TodayPollSerializer,
        responses={200: TodayPollSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="설문 부분 수정 - 완료",
        operation_description="설문 정보의 일부를 수정합니다.",
        request_body=TodayPollSerializer,
        responses={200: TodayPollSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="설문 삭제 - 완료",
        operation_description="ID로 특정 설문을 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class TodayPollAnswerView(APIView):

    @swagger_auto_schema(
        operation_summary="설문 응답 기능 - 완료",
        operation_description="특정 설문에 대한 응답을 등록합니다.",
        request_body=TodayPollAnswerSerializer,
        responses={200: TodayPollAnswerSerializer}
    )
    def post(self, request, pk):
        today_poll = get_object_or_404(TodayPoll, pk=pk)
        serializer = TodayPollAnswerSerializer(today_poll, data=request.data, partial=True)
        if serializer.is_valid():
            updated_poll = serializer.save()

            # Convert date to ISO format and return as dict
            response_data = {
                'check_attention': updated_poll.check_attention,
                'check_test': updated_poll.check_test,
                'check_homework': updated_poll.check_homework,
                'answered_at': updated_poll.answered_at.isoformat() if updated_poll.answered_at else None,
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 브리핑 전체 뷰 (CRUD 포함)
class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

    def get_queryset(self):
        queryset = Briefing.objects.all().order_by('-created_at')

        # 필터링 조건 추가
        course_fk = self.request.query_params.get('course_fk', None)
        created_at_start = self.request.query_params.get('created_at_start', None)
        created_at_end = self.request.query_params.get('created_at_end', None)

        if course_fk is not None:
            queryset = queryset.filter(course_fk_id=course_fk)

        if created_at_start is not None and created_at_end is not None:
            queryset = queryset.filter(created_at__date__range=[created_at_start, created_at_end])
        elif created_at_start is not None:
            queryset = queryset.filter(created_at__date__gte=created_at_start)
        elif created_at_end is not None:
            queryset = queryset.filter(created_at__date__lte=created_at_end)

        return queryset

    @swagger_auto_schema(
        operation_summary="브리핑 목록 조회 - 완료",
        operation_description="모든 브리핑 목록을 조회하거나, 쿼리 파라미터에 따라 필터링된 브리핑 목록을 조회합니다.",
        manual_parameters=[
            openapi.Parameter('course_fk', openapi.IN_QUERY,
                              description="강의 ID로 필터링", type=openapi.TYPE_INTEGER),
            openapi.Parameter('created_at_start', openapi.IN_QUERY,
                              description="시작 날짜로 필터링 (YYYY-MM-DD 형식)", type=openapi.TYPE_STRING),
            openapi.Parameter('created_at_end', openapi.IN_QUERY,
                              description="종료 날짜로 필터링 (YYYY-MM-DD 형식)", type=openapi.TYPE_STRING),
        ],
        responses={200: BriefingListSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = BriefingListSerializer(queryset, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="브리핑 생성 기능 - 완료",
        operation_description="새로운 브리핑을 생성합니다.",
        request_body=BriefingSerializer,
        responses={201: BriefingSerializer}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="브리핑 조회 - 완료",
        operation_description="ID로 특정 브리핑을 조회합니다.",
        responses={200: BriefingSerializer}
    )
    def retrieve(self, request, *args, **kwargs):
        briefing_id = kwargs.get('pk', None)
        briefing = Briefing.objects.get(id = briefing_id)
        response_data = {
            "id" : briefing_id,
            "course_fk": briefing.course_fk.id,
            "content": json.loads(briefing.content),
            "created_at": briefing.created_at.isoformat(),
            "updated_at": briefing.updated_at.isoformat() if briefing.updated_at else None,  # None check
        }
        return Response(response_data)

    @swagger_auto_schema(
        operation_summary="브리핑 수정 기능 - 완료",
        operation_description="기존 브리핑 정보를 수정합니다.",
        request_body=BriefingSerializer,
        responses={200: BriefingSerializer}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="브리핑 부분 수정 - 완료",
        operation_description="브리핑 정보의 일부를 수정합니다.",
        request_body=BriefingSerializer,
        responses={200: BriefingSerializer}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="브리핑 삭제 - 완료",
        operation_description="ID로 특정 브리핑을 삭제합니다.",
        responses={204: 'No Content'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
