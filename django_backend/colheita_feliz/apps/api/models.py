import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Endpoint(models.Model):
    endpoint_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    creation_time = models.DateField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    last_seen = models.DateTimeField(blank=True,
                                     null=True)

    def is_active(self):
        if last_seen:
            return self.last_seen >= timezone.now() - datetime.timedelta(hours=1)
        else:
            return False

    def __str__(self):
        return 'Endpoint '+str(self.endpoint_id)+': '+self.name


class Device(models.Model):
    class Meta:
        unique_together = (('name', 'endpoint_id'))

    device_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256,
                                   blank=True,
                                   default='')
    endpoint_id = models.ForeignKey(Endpoint,
                                    on_delete=models.CASCADE,
                                    db_column='endpoint_id')
    DEV_TYPE_CHOICES = [
        ('A', 'Actuator'),
        ('S', 'Sensor'),
    ]
    device_type = models.CharField(max_length=1,
                                   choices=DEV_TYPE_CHOICES)

    DATA_TYPE_CHOICES = [
        ('b', 'Bool'),
        ('n', 'Number'),
        ('s', 'String'),
    ]
    data_type = models.CharField(max_length=1,
                                 choices=DATA_TYPE_CHOICES)
    unit = models.CharField(max_length=8,
                            blank=True,
                            default='')
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Device '+str(self.device_id)+': '+self.name


class Status(models.Model):
    class Meta:
        verbose_name_plural = "Status"

    status_id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=16)
    device_id = models.ForeignKey(Device,
                                  on_delete=models.CASCADE,
                                  db_column='device_id')
    send_time = models.DateTimeField()
    recept_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Status '+str(self.status_id)+': '+self.value
