from django.db import models


class Vulnerability(models.Model):
    title = models.CharField(max_length=255)
    generated = models.BooleanField()
    wiki_url = models.URLField(null=True, blank=True)
    avds = models.ForeignKey('AvdsVulnerability', null=True, blank=True)
    cenzic = models.ForeignKey('CenzicVulnerability', null=True, blank=True)
    qualys = models.ForeignKey('QualysVulnerability', null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        app_label = 'armored'


class AvdsVulnerability(models.Model):
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


class CenzicVulnerability(models.Model):
    cenzic_id = models.CharField(max_length=100, unique=True)  # qid
    name = models.TextField(blank=True)
    description = models.TextField(blank=True)
    how_it_works = models.TextField(blank=True)
    impact = models.TextField(blank=True)
    remediation = models.TextField(blank=True)

    class Meta:
        app_label = 'armored'


class QualysVulnerability(models.Model):
    provider_id = models.IntegerField(unique=True)  # qid
    category = models.CharField(max_length=200)
    last_update = models.DateTimeField()
    diagnosis = models.TextField(null=True, blank=True)
    consequence = models.TextField(null=True, blank=True)
    solution = models.TextField(null=True, blank=True)

    class Meta:
        app_label = 'armored'
