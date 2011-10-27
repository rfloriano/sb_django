from django.db import models


class Vulnerability(models.Model):
    title = models.CharField(max_length=255)
    vuln_type = models.CharField(max_length=255)
    severity_level = models.PositiveIntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'core'


class Reference(models.Model):
    url_reference = models.URLField()  # url
    vulnerability = models.ForeignKey(Vulnerability)  # vulnerabilidade_id, ataque_id
    vulnerability_type = models.CharField(max_length=150)  # tipo

    class Meta:
        app_label = 'core'
