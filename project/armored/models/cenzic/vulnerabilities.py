from django.db import models
from core.models.vulnerabilities import Vulnerability, Reference


class CenzicVulnerability(Vulnerability):
    provider_id = models.IntegerField(unique=True)  # qid
    family = models.TextField(blank=True)
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    how_it_works = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    risk = models.IntegerField(null=True, blank=True)
    test_id = models.IntegerField(null=True, blank=True)
    service = models.CharField(max_length=255, blank=True)

    class Meta:
        app_label = 'armored'


class CenzicReference(Reference):
    mensagem = models.TextField(blank=True)
    data_criacao = models.DateTimeField(null=True, blank=True)
    http_request = models.TextField(blank=True)
    http_response = models.TextField(blank=True)

    class Meta:
        app_label = 'armored'
