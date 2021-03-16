from django.urls import path

from . import views

urlpatterns = [
    path('list-all/', views.list_all_proc),
    path('list-active/', views.list_active_proc),
    path('status/', views.status_proc),
    path('day/', views.day_proc),
    path('order/', views.order_proc),
]
