from django.db import models
from roku import Roku

# Create your models here.
import requests

class device(models.Model):

    device_ip = models.CharField( max_length=15)

    power_state = 'ON'
    current_app = None

