
from django.urls import path, include
from . import views


urlpatterns = [
    path('posts', views.home, name='posts'),
    path('results', views.results, name='results'),
]