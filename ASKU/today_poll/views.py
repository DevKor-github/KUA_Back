from rest_framework import viewsets, generics, permissions
from .models import TodayPoll, Briefing
from .serializers import TodayPollSerializer, BriefingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone
from django.shortcuts import get_object_or_404


class TodayPollViewSet(viewsets.ModelViewSet):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodayPoll.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserTodayPollListCreateView(generics.ListCreateAPIView):
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodayPoll.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodayPollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TodayPoll.objects.filter(user=self.request.user)


class TodayPollAnswerView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            today_poll = TodayPoll.objects.get(pk=pk, user=request.user)
        except TodayPoll.DoesNotExist:
            return Response({'error': 'TodayPoll not found'}, status=404)

        data = request.data
        today_poll.check_attention = data.get(
            'check_attention', today_poll.check_attention)
        today_poll.check_test = data.get('check_test', today_poll.check_test)
        today_poll.check_homework = data.get(
            'check_homework', today_poll.check_homework)
        today_poll.answered_at = timezone.now()
        today_poll.save()

        return Response(TodayPollSerializer(today_poll).data)


class BriefingViewSet(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
    permission_classes = [permissions.IsAuthenticated]


class CourseBriefingListView(generics.ListAPIView):
    serializer_class = BriefingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Briefing.objects.filter(course_id=course_id)


class CreateBriefingView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_id):
        course = get_object_or_404(Course, id=course_id)
        polls = TodayPoll.objects.filter(
            course=course, answered_at__isnull=False)

        if not polls.exists():
            return Response({'error': 'No answered polls found for this course'}, status=404)

        content = self.generate_summary(polls)
        briefing = Briefing.objects.create(course=course, content=content)
        return Response(BriefingSerializer(briefing).data)

    def generate_summary(self, polls):
        total_polls = polls.count()
        attention_count = polls.filter(check_attention=True).count()
        test_count = polls.filter(check_test=True).count()
        homework_count = polls.filter(check_homework=True).count()

        attention_percentage = (attention_count / total_polls) * 100
        test_percentage = (test_count / total_polls) * 100
        homework_percentage = (homework_count / total_polls) * 100

        summary = (
            f"Total polls: {total_polls}\n"
            f"Attention: {attention_percentage:.2f}%\n"
            f"Tests: {test_percentage:.2f}%\n"
            f"Homework: {homework_percentage:.2f}%"
        )
        return summary
