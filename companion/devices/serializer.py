from rest_framework import routers, serializers, viewsets
from .models import ClientDevices, DevicesModel, DeviceCommands


class ClientDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ClientDevices
        fields = ['client', 'device_model', 'device_name', 'device_ip', 'device_port']

#
# class CommandListSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = CommandsList
#         fields = ['created_by', 'subscribers', 'device_brand', 'firmware']

class DevicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DevicesModel
        fields = ['device_brand', 'device_model']

class CommandSerializer(serializers.HyperlinkedModelSerializer):
    # device_model = DevicesSerializer()
    class Meta:
        model = DeviceCommands
        fields = ["command", 'endpoint', 'method', 'body']
