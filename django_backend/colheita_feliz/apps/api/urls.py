from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_base),
    path('endpoints/', views.api_endpoints),
    path('devices/<int:endpoint_id>/', views.api_devices),
    path('status/<int:device_id>/', views.api_status),
    path('status/<int:device_id>/hour/', views.api_status_hour),
    path('status/<int:device_id>/day/', views.api_status_day),
    path('status/<int:device_id>/week/', views.api_status_week),
]
