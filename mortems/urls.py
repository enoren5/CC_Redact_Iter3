
from django.urls import path, include
from . import views


urlpatterns = [
    path('alls/landings', views.mortems, name='mortems'),
]