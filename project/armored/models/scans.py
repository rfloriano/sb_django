from django.db import models
from core.models.scans import Scan


class AvdsScan(Scan):
    scan_avds_id = models.CharField(max_length=100, blank=True)
    webscan_avds_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        app_label = 'armored'


# class CenzicScan(Scan):
#     request_id = models.CharField(unique=True, max_length=45, null=True, blank=True)  # request_id
#     client_id = models.CharField(unique=True, max_length=45, null=True, blank=True)  # client_id

#     class Meta:
#         app_label = 'armored'


class QualysScan(Scan):
    scan_ref = models.CharField(max_length=100, blank=True)

    class Meta:
        app_label = 'armored'
