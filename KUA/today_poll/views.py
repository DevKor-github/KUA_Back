from rest_framework import viewsets, generics, permissions
from .models import TodayPoll, Briefing
from .serializers import TodayPollSerializer, BriefingSerializer, TodayPollAnswerSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404


class TodayPollViewSet(viewsets.ModelViewSet):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            return TodayPoll.objects.filter(user=user)
        return TodayPoll.objects.none()


class UserTodayPollListCreateView(generics.ListCreateAPIView):
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            return TodayPoll.objects.filter(user=user)
        return TodayPoll.objects.none()


class TodayPollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            return TodayPoll.objects.filter(user=user)
        return TodayPoll.objects.none()


class TodayPollAnswerView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, pk):
        today_poll = get_object_or_404(TodayPoll, pk=pk)
        serializer = TodayPollAnswerSerializer(
            today_poll, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
    permission_classes = [permissions.AllowAny]


class CourseBriefingListView(generics.ListAPIView):
    serializer_class = BriefingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Briefing.objects.filter(course_id=course_id)
