from django.db import models

# Create your models here.

class IphoneModels(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="pics")
    network = models.CharField(max_length=100, default="Network")
    network_description = models.TextField()
    display = models.CharField(max_length=100, default="Display")
    display_description = models.TextField()
    memory = models.CharField(max_length=100, default="Memory")
    memory_description = models.TextField()
    camera = models.CharField(max_length=100, default="Camera")
    camera_description = models.TextField()
    battery = models.CharField(max_length=100, default="Battery")
    battery_description = models.TextField()



class IphoneFeatures(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="pics")

