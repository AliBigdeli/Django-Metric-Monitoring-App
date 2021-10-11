from rest_framework import serializers
from dashboard.models import Device, Metric


class DeviceSerializer(serializers.ModelSerializer):
    temperature = serializers.SerializerMethodField()
    humidity = serializers.SerializerMethodField()

    class Meta:
        model = Device
        fields = "__all__"
        read_only_fields = (
            'temperature', 'humidity'
        )

    def get_temperature(self, obj):
        data = None
        try:
            data = Metric.objects.filter(device=obj).latest('created_date')
        except Metric.DoesNotExist:
            return 0
        return data.temperature

    def get_humidity(self, obj):
        data = None
        try:
            data = Metric.objects.filter(device=obj).latest('created_date')
        except Metric.DoesNotExist:
            return 0
        return data.humidity


class MetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metric
        fields = "__all__"
