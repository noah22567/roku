from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# save database space by extending user class
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="testUser")
    client_ip = models.GenericIPAddressField()
    # command_preferences = models.ManyToManyField(CommandsList)


class DevicesModel(models.Model):
    device_brand = models.CharField(max_length=20)
    device_model = models.CharField(max_length=15,unique=True)


# class CommandsList(models.Model):
    # created_by = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    # subscribers = models.ManyToManyField(User, related_name="Sublist", blank=True)
    # device_model = models.ManyToManyField(DevicesModel, unique=False)
    # firmware = models.CharField(max_length=15, blank=True)


class DeviceCommands(models.Model):
    # device_model = models.ForeignKey(devices_model,on_delete=models.CASCADE)
    methods = [("POST", "POST"),
               ("PUT", "PUT"),
               ("GET", "GET"),
               ("DELETE", "DELETE"),
               ("UPDATE", "UPDATE")]

    device_model = models.ManyToManyField(DevicesModel, related_name='commands')
    command = models.CharField(max_length=15)
    endpoint = models.CharField(max_length=100, unique=True)
    method = models.CharField(max_length=10, choices=methods)
    body = models.CharField(max_length=200, blank=True)


# may be able to use something other than many to many to protect from mixing of user data
class ClientDevices(models.Model):  # devices connected to client_
    user = models.ManyToManyField(User, related_name="find_client")  # now you can lookup client devices using client
    device_name = models.CharField(max_length=15)
    device_model = models.ManyToManyField(DevicesModel)
    device_ip = models.GenericIPAddressField()
    device_port = models.IntegerField()
