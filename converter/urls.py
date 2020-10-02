from django.urls import path, include
from . import views


urlpatterns = [
    path('converter', views.mile2km, name='converter'),
    path('converter', views.km2mile, name='converter'),
]