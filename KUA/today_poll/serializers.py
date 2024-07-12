from rest_framework import serializers
from .models import TodayPoll, Briefing


class TodayPollSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayPoll
        fields = '__all__'


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
