from rest_framework import viewsets, generics, permissions
from .models import TodayPoll, Briefing, Student
from .serializers import TodayPollSerializer, BriefingSerializer, TodayPollAnswerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# 모든 오늘의 설문 전체 뷰


class TodayPollViewSet(viewsets.ModelViewSet):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer

# 특정 유저의 오늘의 설문 뷰


class UserTodayPollListCreateView(generics.ListCreateAPIView):
    serializer_class = TodayPollSerializer

    def get_queryset(self):
        student_id = self.kwargs.get('student_id')
        if student_id:
            student_id = get_object_or_404(Student, id=student_id)
            return TodayPoll.objects.filter(id=student_id)
        return TodayPoll.objects.none()

# 오늘의 설문 상세 뷰


class TodayPollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer

    def get_queryset(self):
        id = self.kwargs.get('id')
        if id:
            id = get_object_or_404(TodayPoll, id=id)
            return TodayPoll.objects.filter(id=id)
        return TodayPoll.objects.none()

# 오늘의 설문 응답을 위한 뷰


class TodayPollAnswerView(APIView):

    def post(self, request, pk):
        today_poll = get_object_or_404(TodayPoll, pk=pk)
        serializer = TodayPollAnswerSerializer(
            today_poll, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

# 브리핑 전체 뷰


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

# 특정 강의의 브리핑 뷰


class CourseBriefingListView(generics.ListAPIView):
    serializer_class = BriefingSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Briefing.objects.filter(course_id=course_id)
