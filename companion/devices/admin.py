from django.contrib import admin
from .models import DevicesModel, DeviceCommands, Client, ClientDevices
# Register your models here.
admin.site.register(Client)
admin.site.register(ClientDevices)
admin.site.register(DevicesModel)
# admin.site.register(CommandsList)
admin.site.register(DeviceCommands)


