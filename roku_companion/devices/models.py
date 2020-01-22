from django.db import models
from django.contrib.auth.models import User
from rest_framework_api_key.models import AbstractAPIKey


# save database space by extending user class or nah to sep diff users or maybe groups?
class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="Client")
    client_id = models.GenericIPAddressField()


class ComClient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="ComClient")


class ComClientAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        ComClient,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )


class ClientAPIKey(AbstractAPIKey):
    organization = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name="api_keys",
    )


class DevicesModel(models.Model):
    device_brand = models.CharField(max_length=20)
    device_model = models.CharField(max_length=15, unique=True)


class DeviceCommands(models.Model):
    methods = [("POST", "POST"),
               ("PUT", "PUT"),
               ("GET", "GET"),
               ("DELETE", "DELETE"),
               ("UPDATE", "UPDATE")]

    device_model = models.ForeignKey(DevicesModel, unique=False, on_delete=models.CASCADE, related_name='commands')
    command = models.CharField(max_length=15)
    endpoint = models.CharField(max_length=100, unique=True)
    method = models.CharField(max_length=10, choices=methods)
    body = models.CharField(max_length=200, blank=True)


class ClientDevices(models.Model):  ## add user to below after extending user
    user = models.ManyToManyField(Client, related_name="client_device_list")  # now you can lookup client devices using client
    device_name = models.CharField(max_length=15)
    device_model = models.ManyToManyField(DevicesModel, related_name="device_model_list", related_query_name="client_device")
    device_ip = models.GenericIPAddressField()
    device_port = models.IntegerField()


