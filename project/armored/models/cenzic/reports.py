from django.db import models
from core.models.reports import Report
from scans import CenzicArmoredScan


class CenzicReport(Report):
    scan = models.OneToOneField(CenzicArmoredScan)

    class Meta:
        app_label = 'armored'
