from django.urls import path
from .views import DeviceListView, DeviceDetailView, MetricListView, MetricCurrentView

app_name = "api"

urlpatterns = [
    path("device/list", DeviceListView.as_view(), name="list_device"),
    path("device/<str:token>",
         DeviceDetailView.as_view(), name="detail_device"),
    path("device/<str:token>/data",
         MetricListView.as_view(), name="detail_device")
]
