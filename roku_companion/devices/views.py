from .models import Client, ClientDevices, DevicesModel, DeviceCommands
from django.db.models import Q

from .serializer import ClientDeviceSerializer,DevicesSerializer,CommandSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView

from django_filters.rest_framework import DjangoFilterBackend
from .filter import DeviceModelFilter


class ClientDeviceView(RetrieveAPIView):
    serializer_class = ClientDeviceSerializer
    model = serializer_class.Meta.model
    lookup_field = "client"

class DevicesListView(ListAPIView):
    serializer_class = DevicesSerializer
    model = serializer_class.Meta.model
    queryset = DevicesModel.objects.all()

class DeviceCommandsList(ListCreateAPIView):

    serializer_class = CommandSerializer
    # model = DeviceCommands
    model = serializer_class.Meta.model

    # print(DeviceCommands.objects.get(command='select'))

    # lookup_url_kwarg =

    def get_queryset(self):
        queryset_list = DeviceCommands.objects.all()
        # query = self.request.GET

                
        # if self.request.GET:
        #     queryset = queryset_list.filter(device_model="rokuTV")
        # else:
        #     queryset = queryset_list
        #
        # return queryset

