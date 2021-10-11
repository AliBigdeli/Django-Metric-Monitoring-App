from django.contrib import admin

from .models import Device,Metric

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "token","user", "created_date"]
    search_fields = ["name", "token"]
    list_filter = ("user",)

class MetricAdmin(admin.ModelAdmin):
    list_display = ["device","temperature", "humidity", "created_date"]
    search_fields = ["device"]
    list_filter = ("device",)

admin.site.register(Device, DeviceAdmin)
admin.site.register(Metric, MetricAdmin)
