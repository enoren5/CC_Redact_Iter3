
from django.urls import path, include
from . import views


urlpatterns = [
    path('mortems', views.home, name='mortems'),
    path('results', views.results, name='results'),
]