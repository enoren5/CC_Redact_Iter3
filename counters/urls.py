
from django.urls import path, include
from . import views


urlpatterns = [
    path('counters', views.counters, name='counters'),

]