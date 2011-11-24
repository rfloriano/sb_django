from django.db import models
from schedules import Schedule


class Scan(models.Model):  # Scans
    scan_date = models.DateTimeField()  # data_do_scan
    schedule = models.ForeignKey(Schedule)  # agendamento_id
    scan_finished_date = models.DateTimeField(null=True, blank=True)  # data_conclusao
    error_description = models.CharField(max_length=255, null=True, blank=True)  # error_description
    number_attempts = models.IntegerField(null=True, blank=True)  # numero_tentativas
    status = models.CharField(max_length=20)
    scan_type = models.CharField(max_length=100)  # the class name to extended objects
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at
    hackalert_id = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'core'
