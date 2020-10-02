from django.urls import path, include
from . import views


urlpatterns = [
    path('converters', views.mile2km, name='converters'),
    path('converters', views.km2mile, name='converters'),
]