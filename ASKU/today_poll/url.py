from django.urls import path
from .views import TodayPollListCreateView, TodayPollDetailView, BriefingListCreateView, BriefingDetailView

urlpatterns = [
    path('polls/', TodayPollListCreateView.as_view(), name='todaypoll-list-create'),
    path('polls/<int:pk>/', TodayPollDetailView.as_view(), name='todaypoll-detail'),
    path('briefings/', BriefingListCreateView.as_view(), name='briefing-list-create'),
    path('briefings/<int:pk>/', BriefingDetailView.as_view(), name='briefing-detail'),
]
