from django.db import models
from schedules import Schedule


class ScanType(models.Model):  # TipoScan
    name = models.CharField(max_length=50)  # nome
    description = models.CharField(max_length=200)  # descricao
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'


class Scan(models.Model):  # Scans
    scan_date = models.DateTimeField()  # data_do_scan
    completed = models.BooleanField()  # concluido
    schedule = models.ForeignKey(Schedule)  # agendamento_id
    scan_finished_date = models.DateTimeField(null=True, blank=True)  # data_conclusao
    error_description = models.CharField(max_length=765, blank=True)  # error_description
    number_attempts = models.IntegerField(null=True, blank=True)  # numero_tentativas
    request_id = models.CharField(unique=True, max_length=45, null=True, blank=True)  # request_id
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'core'
