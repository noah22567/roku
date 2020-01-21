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
        # client_ip = self.request.GET.get('client_ip')#### correctly grab values
        # command = self.request.Get.get('command')
        command = self.request.data['command']
        client_ip = self.request.data['client_ip']
        client = Client.objects.get(client_ip=client_ip)
        device = self.get_device_model(client, command)
        device_command = self.get_command(device, command)

        return device_command


    ## some day you can use synonyms to teat for this =)
    def get_command(self,device,user_command):
        import operator
        dic_list = {}
        indexed = {}
        device = DevicesModel.objects.get(device_model = device)
        command_list = device.objects
        print(command_list)
        for word in user_command.split(" "):
            for command in command_list:
                if word in command.command:
                    dic_list[command.command] = command
                    indexed[command.command] += len(word)
        max_command = max(indexed.items(), key=operator.itemgetter(1))[0]
        return dic_list[max_command]

## some day you can use synonyms to teat for this =)
    def get_device_model(self,client,command):
        import operator

        possible_devices = {}

        for word in command.split(" "):
            for client_device in client.client_device_list.all():
                dev = DevicesModel.objects.get(client_device=client_device)
                if word in dev.device_model:
                    if (dev.device_model in possible_devices.keys()):
                        possible_devices[dev.device_model] += 1
                    else:
                        possible_devices[dev.device_model] = 1

                elif word in client_device.device_name:
                    if (dev.device_model in possible_devices.keys()):
                        possible_devices[dev.device_model] += 1
                    else:
                        possible_devices[dev.device_model] = 1

        return max(possible_devices.items(), key=operator.itemgetter(1))[0]





