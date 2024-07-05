from rest_framework import viewsets
from .models import TodayPoll, Briefing
from .serializers import TodayPollSerializer, BriefingSerializer


class TodayPollListCreateView(viewsets.ModelViewSet):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer


class BriefingListCreateView(viewsets.ModelViewSet):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
