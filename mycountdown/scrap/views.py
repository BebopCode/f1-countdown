from django.shortcuts import render
from rest_framework import generics
from .models import RaceModel
from .serializers import RaceModelSerializer

# Create your views here.
class RaceDataCreateView(generics.ListCreateAPIView):
    #queryset = RaceModel.objects.all()
    serializer_class = RaceModelSerializer
    def get_queryset(self):
        # Sort by the 'race' column and return only the first entry
        return RaceModel.objects.order_by('-race')[:1]
