from django.db import models
from schedules import Schedule

STATUS = [
    ("AGENDADO", "AGENDADO"),
    ("EXECUTANDO", "EXECUTANDO"),
    ("CONCLUIDO", "CONCLUIDO"),
    ("CANCELADO", "CANCELADO"),
    ("FALHOU", "FALHOU"),
    ("NA FILA", "NA FILA"),
]


class ScanType(models.Model):  # TipoScan
    name = models.CharField(max_length=50)  # nome
    description = models.CharField(max_length=200)  # descricao
    created_at = models.DateTimeField()  # created_at
    updated_at = models.DateTimeField()  # updated_at

    class Meta:
        app_label = 'blindado'


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
        app_label = 'blindado'


class ArmoredScan(Scan):
    status = models.CharField(max_length=20, choices=STATUS)  # status
    percentage = models.PositiveIntegerField(default=0)  # percentual

    class Meta:
        abstract = True
        app_label = 'blindado'


class CenzicArmoredScan(ArmoredScan):
    # report = models.OneToOneField(CenzicReport, null=True, blank=True)  # relatorio_cenzic

    class Meta:
        app_label = 'blindado'


class AvdsArmoredScan(ArmoredScan):
    scan_avds = models.CharField(max_length=100, blank=True)
    webscan_avds_id = models.CharField(max_length=100, blank=True)
    # report = models.OneToOneField(AvdsReport, null=True, blank=True)  # relatorio_avds

    class Meta:
        app_label = 'blindado'


class QualysArmoredScan(ArmoredScan):
    # report = models.OneToOneField(QualysReport, null=True, blank=True)  # relatorio_qualys

    class Meta:
        app_label = 'blindado'
