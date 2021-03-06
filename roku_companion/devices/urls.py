from django.contrib import admin
from django.urls import path, include , re_path
from .views import ClientDeviceView, DevicesListView, DeviceCommandsList


urlpatterns = [
    re_path(r'client-devices/(?P<user>\w+)/', ClientDeviceView.as_view()),
    path("devices/", DevicesListView.as_view()),
    re_path(r'devices/command/', DeviceCommandsList.as_view()),
]