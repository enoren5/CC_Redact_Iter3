
from django.urls import path, include
from . import views


urlpatterns = [
    path('wordcounters', views.wordcounters, name='wordcounters'),
]