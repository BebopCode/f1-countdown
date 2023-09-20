from django.urls import path
from . import views
from django.views.generic import TemplateView

#will register tha app namespace
app_name = 'scrap'
urlpatterns = [
    path('countdown/', views.show_countdown, name='countdown'),
    path('drivers/', views.show_drivers, name='driver'),
    path('404/', TemplateView.as_view(template_name='404.html'), name='404'),

]