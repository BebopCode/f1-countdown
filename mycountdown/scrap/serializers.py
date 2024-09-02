from rest_framework import serializers
from .models import RaceModel, LeaderBoard, TeamLeaderBoard

class RaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceModel
        fields = ['id', 'title', 'location', 'race', 'qualifying', 'sprint', 'sprint_shootout']

class LeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaderBoard
        fields = ['id', 'position', 'driver', 'car', 'points']

class TeamLeaderBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeaderBoard
        fields = ['id','position', 'team', 'points']