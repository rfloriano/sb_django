from django.db import models
from cliente.models import Client


class Device(models.Model):  # Dispositivos
    name = models.CharField(max_length=255)  # nome
    client = models.ForeignKey(Client)  # client_id
    active = models.BooleanField()  # ativo
    accept = models.BooleanField()  # aceite
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'blindado'


class IpDevice(Device):
    alias = models.CharField(max_length=255)
    number_vulns_1 = models.PositiveIntegerField()  # num_vulns_1
    number_vulns_2 = models.PositiveIntegerField()  # num_vulns_2
    number_vulns_3 = models.PositiveIntegerField()  # num_vulns_3
    number_vulns_4 = models.PositiveIntegerField()  # num_vulns_4
    number_vulns_5 = models.PositiveIntegerField()  # num_vulns_5

    class Meta:
        app_label = 'blindado'


class UrlDevice(Device):
    certified = models.BooleanField()  # certificado
    description = models.TextField()  # description
    logo = models.ImageField(upload_to='dispositivos/logos')  # dispositivo_logo_file_name dispositivo_logo_content_type, dispositivo_logo_file_size, dispositivo_logo_updated_at
    number_access = models.PositiveIntegerField()  # acessos
    number_vulns_1 = models.PositiveIntegerField()  # num_vulns_1
    number_vulns_2 = models.PositiveIntegerField()  # num_vulns_2
    number_vulns_3 = models.PositiveIntegerField()  # num_vulns_3
    number_vulns_4 = models.PositiveIntegerField()  # num_vulns_4
    number_vulns_5 = models.PositiveIntegerField()  # num_vulns_5

    class Meta:
        app_label = 'blindado'
