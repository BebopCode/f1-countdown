from django.urls import path
from .views import LeaderBoardCreateView, RaceModelCreateView, TeamLeaderBoardCreateView

urlpatterns = [
    path('race_data/', RaceModelCreateView.as_view(), name='race-data-create'),
    path('leaderboard_data/', LeaderBoardCreateView.as_view(), name='leaderboard-data-create'),
    path('team_leaderboard_data/', TeamLeaderBoardCreateView.as_view(), name='team-leaderboard-data-create')
]
