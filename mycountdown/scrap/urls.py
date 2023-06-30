from django.urls import path
from . import views

#will register tha app namespace
app_name = 'scrap'
urlpatterns = [
    path('countdown/', views.show_countdown, name='countdown'),
]