from django.urls import path, include
from . import views


urlpatterns = [
    path('mile2km', views.mile2km, name='mile2km'),
]