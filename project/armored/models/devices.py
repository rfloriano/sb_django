from django.db import models
from core.models.devices import Device


class IpDevice(Device):
    alias = models.CharField(max_length=255, null=True, blank=True)
    number_vulns_1 = models.PositiveIntegerField(default=0)  # num_vulns_1
    number_vulns_2 = models.PositiveIntegerField(default=0)  # num_vulns_2
    number_vulns_3 = models.PositiveIntegerField(default=0)  # num_vulns_3
    number_vulns_4 = models.PositiveIntegerField(default=0)  # num_vulns_4
    number_vulns_5 = models.PositiveIntegerField(default=0)  # num_vulns_5

    class Meta:
        app_label = 'armored'


class UrlDevice(Device):
    certified = models.BooleanField()  # certificado
    description = models.TextField(null=True, blank=True)  # description
    logo_file_name = models.CharField(max_length=255, blank=True, null=True)
    logo_content_type = models.CharField(max_length=255, blank=True, null=True)
    logo_file_size = models.IntegerField(null=True, blank=True)
    logo_updated_at = models.DateTimeField(null=True, blank=True)
    number_access = models.PositiveIntegerField(default=0)  # acessos
    number_vulns_1 = models.PositiveIntegerField(default=0)  # num_vulns_1
    number_vulns_2 = models.PositiveIntegerField(default=0)  # num_vulns_2
    number_vulns_3 = models.PositiveIntegerField(default=0)  # num_vulns_3
    number_vulns_4 = models.PositiveIntegerField(default=0)  # num_vulns_4
    number_vulns_5 = models.PositiveIntegerField(default=0)  # num_vulns_5

    class Meta:
        app_label = 'armored'
