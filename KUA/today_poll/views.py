from rest_framework import viewsets, generics, permissions
from .models import TodayPoll, Briefing
from .serializers import TodayPollSerializer, BriefingSerializer
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

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            default_user = get_object_or_404(User, pk=1)
            serializer.save(user=default_user)


class UserTodayPollListCreateView(generics.ListCreateAPIView):
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
            return TodayPoll.objects.filter(user=user)
        return TodayPoll.objects.none()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            default_user = get_object_or_404(User, pk=1)
            serializer.save(user=default_user)


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
        user_id = request.data.get('user_id')
        if user_id:
            user = get_object_or_404(User, id=user_id)
        else:
            user = request.user if request.user.is_authenticated else get_object_or_404(
                User, pk=1)

        try:
            today_poll = TodayPoll.objects.get(pk=pk, user=user)
        except TodayPoll.DoesNotExist:
            return Response({'error': 'TodayPoll not found'}, status=404)

        data = request.data
        today_poll.check_attention = data.get(
            'check_attention', today_poll.check_attention)
        today_poll.check_test = data.get('check_test', today_poll.check_test)
        today_poll.check_homework = data.get(
            'check_homework', today_poll.check_homework)
        today_poll.created_at = data.get('created_at', today_poll.created_at)
        today_poll.answered_at = timezone.now()
        today_poll.save()

        return Response(TodayPollSerializer(today_poll).data)


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
