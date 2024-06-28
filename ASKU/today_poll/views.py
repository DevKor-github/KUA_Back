from rest_framework import generics
from .models import TodayPoll, Briefing
from .serializers import TodayPollSerializer, BriefingSerializer

class TodayPollListCreateView(generics.ListCreateAPIView):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer

class TodayPollDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodayPoll.objects.all()
    serializer_class = TodayPollSerializer

class BriefingListCreateView(generics.ListCreateAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer

class BriefingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Briefing.objects.all()
    serializer_class = BriefingSerializer
