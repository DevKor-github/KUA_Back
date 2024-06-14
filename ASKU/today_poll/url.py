from django.urls import path
from .views import Today_PollListCreateView, Today_PollDetailView, BriefingListCreateView, BriefingDetailView

urlpatterns = [
    path('polls/', Today_PollListCreateView.as_view(),
         name='todaypoll-list-create'),
    path('polls/<int:pk>/', Today_PollDetailView.as_view(), name='todaypoll-detail'),
    path('briefings/', BriefingListCreateView.as_view(),
         name='briefing-list-create'),
    path('briefings/<int:pk>/', BriefingDetailView.as_view(), name='briefing-detail'),
]
