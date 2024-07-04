from django.urls import path
from .views import LeaderBoardCreateView,RaceModelCreateView

urlpatterns = [
    path('race_data/', RaceModelCreateView.as_view(), name='race-data-create'),
    path('leaderboard_data/', LeaderBoardCreateView.as_view(), name='leaderboard-data-create'),
]
