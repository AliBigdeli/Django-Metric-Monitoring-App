from django.urls import path, include
from . import views

app_name = "dashboard"

urlpatterns = [
    path("", views.indexView, name="index"),    
    path("device/<str:token>", views.deviceDetailView, name="device_detail"),
    path("api/", include("dashboard.api.urls")),
]
