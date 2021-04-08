from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_base),
    path('list/endpoints/', views.api_list_endpoints),
    path('list/devices/*', views.api_list_devices),
    path('status/', views.api_status),
    path('order/', views.api_order),
]
