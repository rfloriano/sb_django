from django.db import models
from core.models.vulnerabilities import Vulnerability, Reference


class QualysVulnerability(Vulnerability):
    provider_id = models.IntegerField(unique=True)  # qid
    category = models.CharField(max_length=200)
    last_update = models.DateTimeField()
    diagnosis = models.TextField(null=True, blank=True)
    consequence = models.TextField(null=True, blank=True)
    solution = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'armored'


class QualysReference(Reference):  # Referencias
    rid = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    section = models.CharField(max_length=765, blank=True)
    compliance_type = models.CharField(max_length=765, blank=True)
    info = models.CharField(max_length=765, blank=True)

    class Meta:
        app_label = 'armored'
