from django.db import models
from armored.models.scans import ArmoredScan


class CenzicArmoredScan(ArmoredScan):
    # report = models.OneToOneField(CenzicReport, null=True, blank=True)  # relatorio_cenzic

    class Meta:
        app_label = 'armored'
