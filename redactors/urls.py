
from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('alls/results', views.results, name='results'),
]