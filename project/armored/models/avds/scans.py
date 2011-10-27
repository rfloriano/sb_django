from django.db import models
from armored.models.scans import ArmoredScan


class AvdsArmoredScan(ArmoredScan):
    scan_avds = models.CharField(max_length=100, blank=True)
    webscan_avds_id = models.CharField(max_length=100, blank=True)
    # report = models.OneToOneField(AvdsReport, null=True, blank=True)  # relatorio_avds

    class Meta:
        app_label = 'armored'
