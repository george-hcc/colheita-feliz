from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_base),
    path('get/endpoints/', views.api_get_endpoints),
    path('get/devices/<int:endpoint_id>/', views.api_get_devices),
    path('get/status/<int:device_id>/', views.api_get_status),
    path('get/status/<int:device_id>/hour/', views.api_get_status_hour),
    path('get/status/<int:device_id>/day/', views.api_get_status_day),
    path('get/status/<int:device_id>/week/', views.api_get_status_week),
    path('post/status/', views.api_post_status),
]
