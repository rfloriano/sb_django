from django.db import models
from core.models.reports import Report
from scans import QualysArmoredScan


class QualysReport(Report):
    scan = models.OneToOneField(QualysArmoredScan)

    class Meta:
        app_label = 'armored'
