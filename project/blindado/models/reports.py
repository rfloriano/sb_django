from django.db import models
from scans import CenzicArmoredScan, AvdsArmoredScan, QualysArmoredScan


class Report(models.Model):  # Relatorios
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class CenzicReport(Report):
    scan = models.OneToOneField(CenzicArmoredScan)

    class Meta:
        app_label = 'blindado'


class AvdsReport(Report):
    scan = models.OneToOneField(AvdsArmoredScan)

    class Meta:
        app_label = 'blindado'


class QualysReport(Report):
    scan = models.OneToOneField(QualysArmoredScan)

    class Meta:
        app_label = 'blindado'
