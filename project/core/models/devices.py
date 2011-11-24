from django.db import models
# from clients import Client
from old.models import Clientes


class Device(models.Model):  # Dispositivos
    name = models.CharField(max_length=255)  # nome
    # client = models.ForeignKey(Client)  # client_id
    client = models.ForeignKey(Clientes)  # client_id
    active = models.BooleanField()  # ativo
    accept = models.BooleanField()  # aceite
    object_type = models.CharField(max_length=100)  # the class name to extended objects
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
