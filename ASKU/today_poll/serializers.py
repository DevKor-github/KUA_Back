from rest_framework import serializers
from .models import Today_Poll, Briefing


class Today_PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Today_Poll
        fields = '__all__'


class BriefingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Briefing
        fields = '__all__'
