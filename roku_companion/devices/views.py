from .models import Client, ClientDevices, DevicesModel, DeviceCommands
from django.db.models import Q

from .serializer import ClientDeviceSerializer,DevicesSerializer,CommandSerializer
from rest_framework.generics import RetrieveAPIView, ListAPIView, ListCreateAPIView

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
    model = serializer_class.Meta.model


    def get_queryset(self):
        query = self.request.GET
        if query:
            device_model = query.get('device_model')
            command = query.get('command')
            queryset = DevicesModel.objects.get(device_model=device_model).commands.all()
            if query.get('command'):
                queryset = queryset.filter(command=command)
            return queryset


class ReturnCommand(ListCreateAPIView):

    serializer_class = CommandSerializer
    model = serializer_class.Meta.model

    def get_queryset(self):
        client_id,command = self.request.GET.all()
        self.handle_something()


    def handle_something(self):
        command = self.request.data['command'].split(" ")
        client_ip = self.request.data['client_ip']

        client = Client.objects.get(client_ip = client_ip)
        device = self.get_device(client,command)

    def get_command(self,device,user_command):
        import operator
        dic_list = {}
        indexed = []
        command_list = DevicesModel.objects.get(device_model = device).client_device_list
        for word in user_command:
            for command in command_list:
                if word in command.command:
                    dic_list[command.command] += command
                    indexed.append({"command":command.command,"length":len(word)})
        max_command =
        return dic_list['max_command']


    def get_device(self,client,command):
        import operator
        dic_list = {}

        for device in client.client_device_list.all():
            for key in device.keys():
                for word in command:
                    if word in key:
                        dic_list[key] +=1

        device = max(dic_list.items(), key=operator.itemgetter(1))[0]
        return device.device_model




