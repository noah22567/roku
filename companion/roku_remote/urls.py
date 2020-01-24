from django.urls import path
from .views import remote

urlpatterns = [
    path('remote/', remote),
]