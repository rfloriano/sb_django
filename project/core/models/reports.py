from django.db import models
from vulnerabilities import Vulnerability, Reference


class Report(models.Model):  # Relatorios
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'armored'


class ReportVulnerability(models.Model):
    report = models.ForeignKey(Report)
    vulnerability = models.ForeignKey(Vulnerability)
    reference = models.ForeignKey(Reference)

    class Meta:
        app_label = 'armored'
