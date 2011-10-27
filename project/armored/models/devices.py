from django.db import models
from core.models.devices import Device


class IpDevice(Device):
    alias = models.CharField(max_length=255)
    number_vulns_1 = models.PositiveIntegerField()  # num_vulns_1
    number_vulns_2 = models.PositiveIntegerField()  # num_vulns_2
    number_vulns_3 = models.PositiveIntegerField()  # num_vulns_3
    number_vulns_4 = models.PositiveIntegerField()  # num_vulns_4
    number_vulns_5 = models.PositiveIntegerField()  # num_vulns_5

    class Meta:
        app_label = 'armored'


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
        app_label = 'armored'
