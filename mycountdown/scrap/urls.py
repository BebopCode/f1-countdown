from django.urls import path
from .views import RaceDataCreateView

urlpatterns = [
    path('race_data/', RaceDataCreateView.as_view(), name='race-data-create'),
]
