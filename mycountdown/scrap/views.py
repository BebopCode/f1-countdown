from django.shortcuts import render
from rest_framework import generics
from .models import LeaderBoard, RaceModel, TeamLeaderBoard
from .serializers import LeaderBoardSerializer, RaceModelSerializer, TeamLeaderBoardSerializer
from datetime import datetime
import pytz
# Create your views here.
class LeaderBoardCreateView(generics.ListCreateAPIView):
    #queryset = RaceModel.objects.all()
    serializer_class = LeaderBoardSerializer
    def get_queryset(self):
        return LeaderBoard.objects.all()

class TeamLeaderBoardCreateView(generics.ListCreateAPIView):
    serializer_class = TeamLeaderBoardSerializer
    def get_queryset(self):
        return TeamLeaderBoard.objects.all()
    
class RaceModelCreateView(generics.ListCreateAPIView):
    queryset = RaceModel.objects.all()
    serializer_class = RaceModelSerializer
    
    def get_current_time_as_string(self):
        current_time = datetime.now(pytz.UTC)
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        return formatted_time
    
    def get_queryset(self):
        time_now = self.get_current_time_as_string()
        #queryset = super().get_queryset()
        sorted_filtered = self.queryset.filter(race__gt=time_now).order_by('race')
        if sorted_filtered.exists():
            print(type(sorted_filtered))
            return sorted_filtered[:1]
