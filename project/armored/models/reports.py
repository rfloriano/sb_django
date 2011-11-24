from django.db import models
from core.models.scans import Scan
from vulnerabilities import Vulnerability


class Report(models.Model):  # Relatorios
    scan = models.ForeignKey(Scan, related_name='armored_report')
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'armored'


class SpecificReport(models.Model):
    text = models.TextField()

    class Meta:
        app_label = 'armored'


class ReportVulnerability(models.Model):
    report = models.ForeignKey(Report)
    vulnerability = models.ForeignKey(Vulnerability)
    specific_report = models.ForeignKey(SpecificReport)
    severity_level = models.CharField(max_length=50)
    path = models.CharField(max_length=255)
    vulnerability_type = models.CharField(max_length=255)

    class Meta:
        app_label = 'armored'
