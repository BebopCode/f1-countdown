from rest_framework import serializers
from .models import RaceModel

class RaceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaceModel
        fields = ['id','title','race','qualifying','sprint', 'sprint_shootout']