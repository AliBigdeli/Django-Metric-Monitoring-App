from rest_framework import serializers
from dashboard.models import Device,Metric


class DeviceSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Device
        fields = "__all__"    


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = "__all__"
