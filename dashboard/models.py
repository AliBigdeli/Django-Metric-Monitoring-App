from django.db import models
from django.contrib.auth.models import User
from .utils import create_device_token

class Device(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )
    name = models.CharField(max_length=255)
    token = models.CharField(max_length=15, unique=True, blank=True)    
    descriptions = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_date"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:        
            self.token = create_device_token(self)

        super().save(*args, **kwargs)

class Metric(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()    
    time = models.DateTimeField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device.name
    
    class Meta:
        ordering = ["-created_date"]

    @property
    def latest_humidity(self,id):
        obj = self.objects.filter(device=id).latest('created_date')
        return obj.humidity 
        

    @property
    def latest_temperature(self,id):
        obj = self.objects.filter(device=id).latest('created_date')
        return obj.temperature 
        
    