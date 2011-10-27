from django.db import models
from clients import Client


class Device(models.Model):  # Dispositivos
    name = models.CharField(max_length=255)  # nome
    client = models.ForeignKey(Client)  # client_id
    active = models.BooleanField()  # ativo
    accept = models.BooleanField()  # aceite
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
