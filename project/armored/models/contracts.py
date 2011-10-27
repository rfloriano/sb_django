from django.db import models
from core.models.contracts import PlanRange, PlanContract
from core.models.devices import Device


class ArmoredPlanRange(PlanRange):
    ips_quantity = models.PositiveIntegerField()  # num_ips
    urls_quantity = models.PositiveIntegerField()  # num_urls
    pci_quantity = models.PositiveIntegerField()  # num_ips_pci

    class Meta:
        app_label = 'armored'


class ArmoredPlanContract(PlanContract):
    device = models.ForeignKey(Device)  # dipositivo_id

    class Meta:
        app_label = 'armored'
