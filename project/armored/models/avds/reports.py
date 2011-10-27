from django.db import models
from core.models.reports import Report
from scans import AvdsArmoredScan


class AvdsReport(Report):
    scan = models.OneToOneField(AvdsArmoredScan)

    class Meta:
        app_label = 'armored'
