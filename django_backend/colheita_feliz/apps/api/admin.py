from django.contrib import admin

from .models import (
    Endpoint,
    Device,
    Status,)

# Register your models here.
admin.site.register(Endpoint)
admin.site.register(Device)
admin.site.register(Status)
