from django.urls import path, include
from . import views


urlpatterns = [
    path('converter', views.mile2km, name='mile2km'),
    path('converter', views.km2mile, name='km2mile'),
]