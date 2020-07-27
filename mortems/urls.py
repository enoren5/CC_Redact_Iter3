
from django.urls import path, include
from . import views


urlpatterns = [
    path('mortems', views.mortems, name='mortems'),
]